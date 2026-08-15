import json
from pathlib import Path
from dotenv import load_dotenv
import os
import requests
from datetime import datetime, timezone
from urllib.parse import quote
from zoneinfo import ZoneInfo
import time
import httpx
import asyncio

folder = Path('Curriculum_Map')
folder.mkdir(exist_ok=True)


def milli_start():
    utc_current_time = int(datetime.now(timezone.utc).timestamp() * 1000)
    return utc_current_time

def format_gmp_date_seconds(time):
    eastern = ZoneInfo('America/New_York')
    date_format = datetime.fromtimestamp(
    time / 1000,
    tz=eastern).strftime("%d%b%Y %I:%M:%S%p").upper()
    return date_format

def format_gmp_date_now():
    eastern = ZoneInfo('America/New_York')
    date_format = datetime.now(eastern).strftime("%d%b%Y_%I:%M:%S%p").upper()
    return date_format

def format_gmp_date_now_file():
    eastern = ZoneInfo('America/New_York')
    date_format = datetime.now(eastern).strftime("%d%b%Y__%I_%M_%S%p").upper()
    return date_format

def todoitems(userID):
    endpoint = f"/learning/odatav4/public/user/learningplan-service/v1/UserTodoLearningItems?$filter=criteria/targetUserID eq '{userID}'&$select=title,componentTypeID,componentID,qualificationID,rootQualificationID,qualTitle,assignedDate&$orderby=assignedDate"
    link = base_url + endpoint
    call = requests.get(link, headers=headers)
    reply = call.json()
    inner = reply.get('value', [])
    return inner


def find_curriculums(curriculum_partial_ID):
    endpoint = f"/learning/odatav4/searchCurriculum/v1/Curricula?$filter=contains(criteria/curriculumID,'{curriculum_partial_ID}') and criteria/active eq true"
    link = base_url + endpoint
    call = requests.get(link, headers=headers)
    reply = call.json()
    inner = reply.get('value', [])
    return inner

def curriculum_count(curriculum_partial_ID):
    endpoint = f"/learning/odatav4/searchCurriculum/v1/Curricula?$filter=contains(criteria/curriculumID,'{curriculum_partial_ID}') and criteria/active eq true&$count=true&$top=1"
    link = base_url + endpoint
    call = requests.get(link, headers=headers)
    reply = call.json()
    curriculum_number = reply['@odata.count']
    print('Curriculum count - ' + str(curriculum_number))
    return curriculum_number

# Get token
load_dotenv('Hidden.env')
client_id = os.getenv('CLIENT_ID')
secret_key = os.getenv('SECRET_KEY')
companyId = os.getenv('COMPANY_ID')
base_url = os.getenv('BASE_URL')
token_path = os.getenv('TOKEN_PATH')
admin_id = os.getenv('ADMIN_ID')

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
print('Value:   ', token_json)
token = token_response.json()['access_token']
headers = {"Authorization": "Bearer " + token, 
           'Accept': 'application/json',
           'Content-Type': 'application/json'
           }

date = format_gmp_date_now_file()
now = milli_start()

user_ID = '0000000' # user ID

# Find curriculums from a partial ID 
partial_curriculum_ID = 'CUR-LSG-BED-'
count_curriculums = curriculum_count(partial_curriculum_ID)
curriculum_payload_loop_setup = find_curriculums(partial_curriculum_ID)

async def assign_curriculums(partial_curriculum_ID):
    async with httpx.AsyncClient(timeout=30.0) as client:
        total_items = 0
        each_payload = 0
        for item in curriculum_payload_loop_setup:
            payload = {
                'primaryKey': user_ID,
                'curricula': [
                ]
            }
            while each_payload < 10:
                for item in curriculum_payload_loop_setup:
                    total_items += 1
                    each_curriculum = {
                            'studentID': user_ID,
                            'assignmentDate': now,
                            'priority': 1
                        }
                    curriculum = item['qualID']
                    each_curriculum['qualificationID'] = curriculum
                    payload['curricula'].append(each_curriculum)
                    time.sleep(0.5)
                    break

                # Assigning Curriculums
                endpoint_path = f"/learning/odatav4/public/admin/curriculum-service/v1/Curricula?$filter=contains(criteria/curriculumID,'{partial_curriculum_ID}') and active eq true&$select=qualID,totalCount"
                link = f'{base_url}{endpoint_path}'
                call = await client.post(link, headers=headers, json=payload)
                reply = call.json()
                await asyncio.sleep(0.5)
                print(json.dumps(reply, indent=2))
                print('Item count - ' + str(total_items))
                print()
