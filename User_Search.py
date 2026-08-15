from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import quote
import json
import os
import requests
import httpx
import asyncio
import time
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

load_dotenv('Hidden.env')
client_id = os.getenv('CLIENT_ID')
secret_key = os.getenv('SECRET_KEY')
companyId = os.getenv('COMPANY_ID')
base_url = os.getenv('BASE_URL')
token_path = os.getenv('TOKEN_PATH')
admin_id = os.getenv('ADMIN_ID')
mdf_base_url=os.getenv('MDF_BASE_URL')

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

def gmp_date(milli_time):
    # Accepts Unix time and returns  
    eastern = ZoneInfo('America/New_York')
    formatted_date = datetime.fromtimestamp(milli_time, eastern).strftime("%d%b%Y %I:%M:%S%p").upper()
    return formatted_date

def ddMMMYYYY_now():
    # Returns current time in GMP format (15Aug2026)
    eastern = ZoneInfo('America/New_York')
    date_format = datetime.now(eastern).strftime("%d%b%Y").upper()
    return date_format

def unix_time():
    print(int(time.time()))

# Call any endpoint and return a standard response. Good for quick queries and tests 
def any_call(endpoint):
    link = f'{base_url}{endpoint}'
    call = requests.get(link, headers=headers)
    reply = call.json()
    inner = reply.get('value', [])        
    return inner

# Search for user information via terminal input and returns a dictionary to be used in other programs.
def multi_user():
    active = True
    user_student_ID = []
    user_information = {}
    while active:
        first_n = input('First name:    ')
        first_n = first_n.title()
        last_n = input('Last name:  ')
        last_n = last_n.title()
        endpoint = f"/learning/odatav4/public/admin/search-service/v1/Students?$filter=contains(scriteria/firstName,'{first_n}') and contains(scriteria/lastName,'{last_n}')"
        link = base_url + endpoint
        call = requests.get(link, headers=headers)
        reply = call.json()
        inner = reply.get('value', [])
        if len(inner) == 1:
            learner_ID = inner[0]['studentID']
            print('\t' + inner[0]['firstName'] + ' ' + inner[0]['lastName'] + ' ' + inner[0]['jobLocID'])
            print('\n\t' + learner_ID + '\n')
            print(inner[0]['emailAddr'])
            user_student_ID.append(learner_ID)
            user_information['name'] = inner[0]['firstName'] + ' ' + inner[0]['lastName']
            user_information['user_ID'] = inner[0]['studentID']
            break
        else:
            for user in inner:
                if user['jobLocID'] == '508' or user['jobLocID'] == 'BEDF':
                    user_information['user_ID'] = user['studentID']
                    user_information['name'] = user['firstName'] + ' ' + user['lastName']
                    break
                else:
                    continue
        active = False
        print(user_information['user_ID'])
        print(f"Accessing {user_information['name']}'s open training items")
        break
    return user_information

# Returns standard API response 
def view_open_items(user_information):
    user_ID = user_information['user_ID']
    endpoint = f"/learning/odatav4/public/user/learningplan-service/v1/UserTodoLearningItems?$filter=criteria/targetUserID eq '{user_ID}'&$select=userID,title,componentTypeID,componentID,assignedDate,requiredDate,daysRemaining,origin,qualificationID,rootQualificationID,qualTitle,isRequired"
    link = f'{base_url}{endpoint}'
    call = requests.get(link, headers=headers)
    reply = call.json()
    inner = reply.get('value', [])        
    return inner

# Writes response from view_open_items() method to a text file
def late_items_first(inner):
    user_ID = inner[0]['userID']
    text = f"{user_ID}.txt"
    item_number = 0
    with open(text, 'w', encoding='utf-8') as f:
        for item in sorted(inner, key=lambda item: item['daysRemaining']):
            item_number += 1
            date_assigned = gmp_date(item['assignedDate'])
            f.write('\nUser ID - ' + item['userID'] + '\n\n')
            f.write(f'[{str(item_number)}] \n\n')
            f.write(item['componentID'] + '\n\n')
            f.write(f"Days remaining [{item['daysRemaining']}]\n")
            f.write(item['componentTypeID'] + ' - ' + item['title'] + '\n\n')
            f.write(f"Origin - {item['origin']} [assigned {date_assigned}]\n")
            f.write(item['qualificationID'] + '\n')
            f.write(item['qualTitle'] + '\n\n')
            f.write('Root Curriculum\n')
            f.write(item['rootQualificationID'] + '\n_____________________________\n')
    os.startfile(text)

def find_item():
    item_title = input('Item title: ')
    endpoint = f"/learning/odatav4/public/admin/search-service/v1/Items?$filter=contains(icriteria/itemTitle,'{item_title}') and icriteria/domainIDs eq 'BED'"
    inner = any_call(endpoint)
    now = ddMMMYYYY_now()
    file = now + '.txt'
    with open(file, 'w', encoding='utf-8') as f:
        for item in inner:
            f.write(json.dumps(item, indent=2))
    os.startfile(file)
            
def terminal_item():
    item_title = input('Item title: ')
    endpoint = f"/learning/odatav4/public/admin/search-service/v1/Items?$filter=contains(icriteria/itemTitle,'{item_title}') and icriteria/domainIDs eq 'BED'"
    inner = any_call(endpoint)
    now = ddMMMYYYY_now()
    for item in inner:
        print(item['itemID'])
        print(item['itemTypeID'])
        print(item['itemTitle'])
        print()

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

def user_history():
    user = multi_user()
    date_time_right_now = format_gmp_date()
    endpoint = f"/learning/odatav4/public/user/userlearning-service/v1/LearningHistories?$filter=criteria/targetUserID eq '{user['user_ID']}'"
    file = f'Completed_{user['name']}.txt'
    user_items = any_call(endpoint)
    file = f'{user['name']}.txt'
    with open(file, 'w', encoding='utf-8') as f:
        f.write(date_time_right_now + '\n\n')
        for item in user_items:
            date_completed = gmp_date(item['completionDate'])
            revision_date = gmp_date(item['revisionDate'])
            f.write(f"[{item['componentTypeID']}]\n")
            f.write(f"{item['componentID']}\n")
            f.write(f"{item['title']}\n")
            f.write(f"\tRev {item['revisionNumber']} - {revision_date}\n")
            f.write('\tCompleted - ' + date_completed + '\n\n')
    os.startfile(file)

# Important 
def user_todoitems():
    root_curriculums = {}
    user = multi_user()
    date_time_right_now = format_gmp_date()

    page_limit = 500
    min_row = 0
    max_row = 500
    item_number = 0
    file = f'Open_Items_{user['name']}_4.txt'
    with open(file, 'a', encoding='utf-8') as f:
        os.startfile(file)
    curriculum_count = []
    while True:
        endpoint = f"/learning/odatav4/public/user/learningplan-service/v1/UserTodoLearningItems?$filter=criteria/targetUserID eq '{user['user_ID']}' and criteria/minRowNum eq {min_row} and criteria/maxRowNum eq {max_row}"

        user_items = any_call(endpoint)
        for item in user_items:
            root_qualification_id = item['rootQualificationID']
            qualification_id = item['qualificationID']
            qual_title = item['qualTitle']
            component_id = item['componentID']
            item_title = item['title']
            days_remaining = item['daysRemaining']
            componentTypeID = item['componentTypeID']
            assignedDate = item['assignedDate']

            curriculum_count.append(qualification_id)

            if root_qualification_id not in root_curriculums:
                root_curriculums[root_qualification_id] = {}

            if qualification_id not in root_curriculums[root_qualification_id]:
                root_curriculums[root_qualification_id][qualification_id] = {
                    'qualTitle': qual_title,
                    'items': []
                }

            root_curriculums[root_qualification_id][qualification_id]['items'].append({
                'componentID': component_id,
                'title': item_title,
                'daysRemaining': days_remaining,
                'componentTypeID': componentTypeID,
                'assignedDate': assignedDate
            })

        print('Number of items open - ' + str(len(user_items)))
        if len(user_items) < 500:
            break
        min_row += page_limit - 1 
        max_row += page_limit + 1
        time.sleep(1)
    
    with open(file, 'a', encoding='utf-8') as f:
        f.write(date_time_right_now + '\n\n')

        for root_qualification_id, qualifications in sorted(
            root_curriculums.items(),
            key=lambda x: (
                '-'.join(x[0].split('-')[:-1]),
                -int(x[0].split('-')[-1])
            )
        ):
            f.write(f"{root_qualification_id}\n")
            f.write('\t|\n')
            for qualification_id, qualification_info in qualifications.items():
                f.write(f"  {qualification_id} - {qualification_info['qualTitle']}\n")

                for item_info in qualification_info['items']:
                    item_number += 1
                    f.write(
                        f'\t ↳  {'Item ' + str(item_number)}\n\n'
                        f"\t\tDays remaining - [{item_info['daysRemaining']}] - [{item_info['componentTypeID']}]\n"
                        f"\t\t{item_info['componentID']}\n"
                        f"\t\t{item_info['title']}\n\n"
                    )
                f.write('\n\n')

            f.write("\n")
    print('Number of curriculums: ' + str(len(set(curriculum_count))))
