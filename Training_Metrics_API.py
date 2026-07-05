from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import quote
import json
import os
import requests
from datetime import datetime, timezone
import httpx
import time

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
print(token)

# This is a list of User IDs I pulled from the SuccessFactors user interface. There is currently no API query property that allows me to call users by job location.
users = ["00467512","00306082","00500774","00413977","00167081","00350114","00329293","00413555","00544856","00356652","00457099","00319820","00423389","00345360","00146262","00341328","00424542","00434373","00110434","00409574","00328319","00418355","00345388","00415807","00525324","00346608","00335585","00220223","00344887","00254405","00445662","00433227","00403936","00447897","00336991","00344941","00428470","00337399","00279294","00465955","00350530","00505708","00407182","00309068","00512305","00505592","00526251","00406541","00412388","00344885","00413483","00418039","00339431","00414209","00421427","00342456","00345800","00105213","00488278","00352966","00419806","00201600","00340755","00195392","00433981","00504009","00471953","00342972","00327772","00143814","00538252","00423850","00449106","00533581","00357982","00445672","00534515","00338621","00320196","00429726","00533689","00286859","00142703","00494905","00251412","00408217","00147792","00410011","00167178","00507988","00450636","00432535","00320421","00340149","00457548","00341502","00347513","00329968","00537492","00284051","00150737","00529212","00255748","00110820"]   

overdue_items = 0
on_time_items = 0
total_item_count = 0
late_user_count = 0
total_user_count = 0

user = "Chelmsford_Loop_compliance_June_2026.json"
with open(user, 'w', encoding='utf-8') as f:
    for user in users:
        endpoint = f"/learning/odatav4/public/user/learningplan-service/v1/UserTodoLearningItems?$filter=criteria/targetUserID eq '{user}'&$select=userID,title,componentTypeID,componentID,daysRemaining,requirementTypeId"
        link = f"{base_url}{endpoint}"
        call = requests.get(link, headers=headers)
        response = call.json()
        list_item = response.get('value', [])

        user_is_late = False
        total_user_count += 1
        for item in list_item:
            user_items = 0
            days_remaining = item.get('daysRemaining')
            if days_remaining is None:
                continue
            total_item_count += 1
            if days_remaining < 0:
                overdue_items += 1
                user_is_late = True
                f.write(json.dumps(item, indent=2))
            else:
                on_time_items += 1
                f.write(json.dumps(item, indent=2))
        if user_is_late:
            late_user_count += 1 
        time.sleep(2)
        print(f'{user}')

item_compliance = on_time_items / total_item_count
print('Past due items - ' + str(overdue_items))
print('On time items - ' + str(on_time_items))
print('Total items - ' + str(total_item_count))
print('Item Compliance = ' + str(item_compliance))


on_time_users = total_user_count - late_user_count
user_compliance = on_time_users / total_user_count
print('On time user count - ' + str(on_time_users))
print('Total user count - ' + str(total_user_count))
print('User compliance % - ' + str(user_compliance))


'''
with gaynor 

Past due items - 1
On time items - 29
Total items - 30
Late user count - 1
Total user count - 3

without gaynor

'''