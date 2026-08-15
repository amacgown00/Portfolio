from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import quote
import json
import os
import requests
import pandas as pd
from datetime import datetime, timezone
from docxtpl import DocxTemplate
import win32com.client as win32
import time
import re
import httpx
import pywintypes
import asyncio

load_dotenv('Hidden.env')
client_id = os.getenv('CLIENT_ID')
secret_key = os.getenv('SECRET_KEY')
companyId = os.getenv('COMPANY_ID')
base_url = os.getenv('BASE_URL')
token_path = os.getenv('TOKEN_PATH')
admin_id = os.getenv('ADMIN_ID')

def any_call(endpoint):
    link = f'{base_url}{endpoint}'
    call = requests.get(link, headers=headers)
    reply = call.json()
    inner = reply.get('value', [])        
    return inner

def student_call_ID(student_ID):
    endpoint = f"/learning/odatav4/public/admin/search-service/v1/Students?$filter=scriteria/learnerID eq '{student_ID}'"
    link = f'{base_url}{endpoint}'
    response = requests.get(link, headers=headers)
    data = response.json()
    inner = data.get('value', [])
    return inner

def format_last_name(last_name):
    if last_name.isupper():
        return last_name.title()

    return last_name[0].upper() + last_name[1:]

def name():
    first_name = input("First Name: ")
    while True:
        last_name = input("Last Name: ")
        if last_name.lower() == "retry":
            first_name = input("First Name: ")
            continue
        while True:
            department = input("Department: ")
            if department.lower() == "retry":
                break  # goes back to Last Name
            if department.lower() == "retype":
                continue  # asks Department again
            department = department.title()
            last_name = format_last_name(last_name)
            if 'msat' in department.lower():
                department = re.sub(r"\bmsat\b", "MSAT", department, flags=re.IGNORECASE)
            elif 'poros' in department.lower():
                department = re.sub(r"\bporos\b", "POROS", department, flags=re.IGNORECASE)
            first_name = first_name.title()
            return first_name, last_name, department

def student_call_name(first_name, last_name):
    endpoint = f"/learning/odatav4/public/admin/search-service/v1/Students?$filter=contains(scriteria/firstName,'{first_name}') and contains(scriteria/lastName,'{last_name}')"
    link = f'{base_url}{endpoint}'
    response = requests.get(link, headers=headers)
    data = response.json()
    inner = data.get('value', [])
    if len(inner) > 1:
        for student in inner:
            if '508' in student['jobLocID'] or 'BED' in student['jobLocID']:
                student_ID = student['studentID']
                manager_ID = student['superField']
                user_email = student['emailAddr']
                print('\nThere is more than one person with this name')
                print(student_ID)
                print(f"\t- {student['firstName']} {student['lastName']}")
                print('\t- Supervisor - ' + student['superField'])
                print('\t' + student['jobLocID'])
    else:
        student_ID = inner[0]['studentID']
        manager_ID = inner[0]['superField']
        user_email = inner[0]['emailAddr']
        print('This is the only person in the company with this name')
        print('\n\t' + student_ID + '\n')
        print('\t- ' + inner[0]['firstName'] + ' ' + inner[0]['lastName'])
        print('\t- Supervisor - ' + inner[0]['superField'])
    return student_ID, manager_ID, user_email

def skip_call(first_name, last_name):
    endpoint = f"/learning/odatav4/public/admin/search-service/v1/Students?$filter=contains(scriteria/firstName,'{first_name}') and contains(scriteria/lastName,'{last_name}')&$select=studentID,lastName,firstName,superField,jobLocID,emailAddr,totalCount&$top=100&$count=true&$skip="
    link = base_url + endpoint
    offset = 0
    alm = True
    inner = []
    while alm:
        with httpx.Client(timeout=30.0) as client:
            call = client.get(link + str(offset), headers=headers)
            reply = call.json()
            all_users = reply.get('value', [])
            for user in all_users:
                inner.append(user)
                if(len(all_users) == 0):
                    alm = False
                    break
        offset = 100
        return inner

def send_outlook_email(user_email, manager_email, user_fullname, first_name, attachment_path):
    outlook = win32.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)

    mail.To = user_email
    mail.CC = manager_email
    mail.Subject = f"Training Change and Verification Form - {user_fullname}"

    # Force Outlook to open the email editor and load your default signature
    mail.GetInspector
    mail.Display()
    time.sleep(1)

    # Display first so Outlook inserts your normal signature
    mail.Display()
    message = f"""
    <p>Hi {first_name},<br><br><br>

   
    I am attaching a form with all your open training items. Please review and follow these steps:

    <ul>
        <li>Notes column - write extend/remove/unlock/etc. for training changes.</li>
        <li>Send a Word copy to me.</li>
    </ul>

    <br>

    After I receive the changes, I will send it in DocuSign for e-signature. <br>
    Leave the notes column blank if no changes are needed. Required trainings (like GDP refreshers) can remain blank.<br><br>

    Best,</p>

    <p style="font-family:Aptos; font-size:13pt;">
    <strong>Andrea MacGown (“An-drEE-uh  Mac-Gown”)</strong>
    </p>

    <p style="font-family:Aptos; font-size:12pt;">
    Quality Engineer II, Training System<br>
    Purification and Pharma Analytics<br>
    BioProduction Group<br><br>

    <a href="https://maps.app.goo.gl/XtECZFBv1bGTQckc6">220 Mill Road Chelmsford, MA 01824<br>
    <a href="mailto:andrea.macgown@thermofisher.com">andrea.macgown@thermofisher.com</a> | <a href="http://www.thermofisher.com/">Thermo Fisher Scientific</a>

    </p>

    """
    mail.HTMLBody = message
    mail.Attachments.Add(str(Path(attachment_path).resolve()))
    mail.Display()

def multi_user(first_n, last_n):
    inner = skip_call(first_n, last_n)
    if len(inner) == 1:
        user_student_ID = inner[0]['studentID']
        user_email = inner[0]['emailAddr']
        user_fullname = inner[0]['firstName'] + ' ' + inner[0]['lastName']
        manager_ID = inner[0]['superField']
        manager_endpoint = f"/learning/odatav4/public/admin/search-service/v1/Students?$filter=scriteria/learnerID eq '{manager_ID}'"
        manager = any_call(manager_endpoint)
        manager_email = manager[0]['emailAddr']
        manager_name = manager[0]['firstName'] + ' ' + manager[0]['lastName']
        print(inner[0]['firstName'] + ' ' + inner[0]['lastName'])
        print('\n\t' + user_student_ID)
        print('\n\t' + inner[0]['jobLocID'])
        print('\n\t' + inner[0]['emailAddr'])            
    else:
        print('\n' + 'There are multiple users with this name. Choose from this list: \n')
        manager_index_dictionary = []
        for index, user in enumerate(inner):
            manager_dictionary = {}
            manager_ID = user['superField']
            manager_endpoint = f"/learning/odatav4/public/admin/search-service/v1/Students?$filter=scriteria/learnerID eq '{manager_ID}'"
            managers = any_call(manager_endpoint)
            for manager in managers:
                manager_dictionary['manager_email'] = manager['emailAddr']
                manager_name = manager['firstName'] + ' ' + manager['lastName']
                manager_dictionary['full_name'] = manager_name.title()
            number = str(index + 1)
            manager_index_dictionary.append(manager_dictionary)
            print(f"[{number}] {user['firstName']} {user['lastName']}")
            print(user['jobLocID'])
            print('Manager - ' + manager_name + '\n')
        answer = input('    ')
        index = int(answer) - 1
        user_fullname = inner[index]['firstName'] + ' ' + inner[index]['lastName']
        user_student_ID = inner[index]['studentID']
        manager_email = manager_index_dictionary[index]['manager_email']
        user_email = inner[index]['emailAddr']
        manager_name = manager_index_dictionary[index]['full_name']
    return user_student_ID, user_email, manager_email, manager_name, user_fullname

def time_start():
    return datetime.now(timezone.utc).strftime("%d%b%Y").title()
todays_date = time_start()

def user_to_do_items(userID):
    endpoint = f"/learning/odatav4/public/user/learningplan-service/v1/UserTodoLearningItems?$filter=criteria/targetUserID eq '{userID}'&$select=title,componentTypeID,componentID,qualificationID,rootQualificationID,daysRemaining,userID,qualTitle"
    link = f'{base_url}{endpoint}'
    response = requests.get(link, headers=headers)
    data = response.json()
    inner = data.get('value', [])
    return inner

token_response = requests.post(
    token_path, 
    json={
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': secret_key,
        'scope': {
            'userId': admin_id,
            'companyId': companyId,
            'userType': 'admin',
            'resourceType': 'learning_public_api'},
    })
token_json = token_response.json()
token = token_response.json()['access_token']
headers = {"Authorization": "Bearer " + token, 
           'Accept': 'application/json',
           }

user_dictionary = {}
site = 'Damascus'

todays_date = time_start()
user_dictionary['date'] = todays_date
first_name, last_name, department = name()
user_ID, user_email, manager_email, manager_name, user_fullname = multi_user(first_name, last_name)

ojt_items = []
elearn_items = []
other_items = []
on_time = []

user_open_items = user_to_do_items(user_ID)
print(f'\n# of learning items assigned - {str(len(user_open_items))}')

for item in user_open_items:
    single_item = {
        'componentID': item['componentID'],
        'componentTypeID': item['componentTypeID'],
        'title': item['title'],
        'qualificationID': item['qualificationID'],
        'qualTitle': item['qualTitle'],
        'rootQualificationID': item['rootQualificationID'],
        'daysRemaining': item['daysRemaining']
    }
    if item['daysRemaining'] is not None and item['daysRemaining'] < 100 and item['componentTypeID'] == 'OJT':
        ojt_items.append(single_item)
    elif item['daysRemaining'] is not None and item['daysRemaining'] < 100 and item['componentTypeID'] == 'ELEARN':
        elearn_items.append(single_item)
    # elif item['daysRemaining'] is not None and item['daysRemaining'] < 100:
    elif item['daysRemaining'] is not None:
        other_items.append(single_item)
    else:
        continue
manager_name = manager_name.title()
user_dictionary['open_items'] = ojt_items + elearn_items + other_items + on_time
user_dictionary['full_name'] = user_fullname
user_dictionary['supervisor_email'] = manager_email
user_dictionary['supervisor_name'] = manager_name
user_dictionary['site'] = site
user_dictionary['user_ID'] = user_ID
user_dictionary['department'] = department

automated_training_verification_folder_path = Path(rf"C:\Users\andrea.macgown\dev\sflms-purification\Training-Study-Hall\Automated_Training_Verification_Forms")
new_file = rf'{user_fullname} Training Change and Verification Form {todays_date}.docx'
output_path = automated_training_verification_folder_path / new_file
document_template = 'AUTOMATE_TRAINING_CHANGE_VERIFICATION_FORM.docx'
    
read_template = DocxTemplate(document_template)
read_template.render(user_dictionary)
read_template.save(output_path)

os.startfile(output_path)

active = True
while active:
    try:
        send_outlook_email(
            user_email=user_email,
            manager_email=manager_email,
            user_fullname=user_fullname,
            first_name=first_name,
            attachment_path=output_path
        )
        break
    except pywintypes.com_error:
        wait = input('An Outlook dialog box is open. Close and press ENTER')
        continue