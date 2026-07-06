# SFLMS API Documentation

This documentation outlines the set of the available API GET calls I can access with Admin rights from the SAP SuccessFactors Learning Management System, which follows the OData standard. As I explored the schema, I realized my company developed a smaller set of endpoints. All code has been written and tested by me. The purpose of this document as a portfolio piece is to demonstrate my proficiency in Python and Markdown.

## Standard SFLMS API Call

This script calls the SFLMS API. The value in `resource_path` and `query_expression` will change with each endpoint. The rest wil remain the same. 

```python
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import quote
import json
import os
import requests

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
           }

resource_path = "modified with each endpoint"
query_expression = "modified with each endpoint"

link = f"{base_url}{resource_path}"
response = requests.get(link, headers=headers)
data = response.json()
```


#### Query Options 
- $filter
- $select
- $top
- $count
- $skip

### Supported functions and operators

- `contains()` with `and`
- `eq`



## Service Path `/learning/odatav4/searchCurriculum/v1/`

<table>

### Endpoint `Curricula`

<tr>

<!--Left column-->

<td valign="top">

**Query Expression**
```python
$filter=contains(criteria/curriculumID,'cur-lsg-bed-pilo-5')&$count=true&$top=1
```

Parameters
- criteria/curriculumID
- criteria/curriculumIDOperator
- criteria/curriculumTitle
- criteria/curriculumTitleOperator
- criteria/active
- criteria/activeOperator
- criteria/domainIDs
- criteria/domainIDsOperator

</td>


<!--Right column-->

<td valign="top">

**Response**
```powershell
[
  {
    "qualID": "CUR-LSG-BED-PILO-5001",
    "qualTitle": "Pilot Plant Team Intro Curriculum (Bedford Pilot Plant)",
    "domainID": "BED",
    "active": true,
    "qualTypeID": "",
    "basisDate": null,
    "forceIncomp": "No",
    "qualDesc": "Curriculum covers Pilot Plant basic trainings all department employees will need to take following onboarding training completion.",
    "criteria": null,
    "totalCount": 5
  }
]
```
</td>
</tr>
</table>

## Service Path - `/learning/odatav4/searchStudent/v1/`


<table>

### Endpoint - Students
<tr><td valign="top">

**Query Expression**
```python
$filter=criteria/learnerID eq '00342456'"
```

### Parameters
- criteria/studentID
- criteria/personGUID
- criteria/firstName
- criteria/lastName
- criteria/isActive
- criteria/domainIDs

</td><td valign="top">

**Response**

```powershell
[
  {
    "studentID": "00342456",
    "personGUID": "1D15754763FE41F4AFDD35BF80ACF531",
    "personExternalID": "00342456",
    "empStatID": "Active",
    "empTypID": "Regular",
    "regularTempID": "",
    "fulltime": "Yes",
    "jobLocID": "508",
    "jobPosID": "",
    "domainID": "LSG",
    "orgID": "",
    "compID": null,
    "lastName": "MacGown",
    "firstName": "Andrea",
    "middleName": "Lee",
    "notActive": "no",
    "addr": "",
    "city": "",
    "state": "",
    "postal": "",
    "cntry": "",
    "superField": "00279294",
    "hireDate": 1630281600000,
    "termDate": null,
    "emailAddr": "andrea.macgown@thermofisher.com",
    "hasAccess": "Yes",
    "selfReg": "N",
    "locked": "No",
    "regionID": "",
    "roleID": "LSG_Learner",
    "profileStatus": "ACTIVE",
    "accountID": null,
    "posNumID": "",
    "nativeDeeplinkUser": "Yes",
    "criteria": null,
    "totalCount": null
  }
]
```
</td></tr>
</table>

## Service Path - `/learning/odatav4/public/user/userlearning-service/v1/`

<table>

### Endpoint - LearningHistories
<tr><td valign="top">

**Query Expression**

```python
$filter=criteria/targetUserID eq '00342456'
```

Parameters 
- criteria/maxNumberToRetrieve
- criteria/itemID
- criteria/itemTypeID
- criteria/targetUserID
- criteria/personGUID
- criteria/fromDate 
- criteria/toDate
- criteria/itemRevisionDate 
- criteria/includeDeepLink

</td>
<td>

**Response**

```powershell
[
  {
    "componentTypeID": "DOC",
    "componentID": "LSG-BED-BED3308",
    "revisionDate": 1781064000000,
    "title": "BED3308 MATERIAL DISPOSITION & LABELING (PPA MA Sites)",
    "revisionNumber": "R1",
    "completionStatusID": "DOC-C",
    "provideCredit": true,
    "studentComponentID": 35523770,
    "instructorName": null,
    "grade": "100",
    "totalHours": null,
    "creditHours": null,
    "contactHours": null,
    "cpeHours": null,
    "comments": null,
    "esigUsername": "User - 00342456",
    "lastUpdateTimestamp": 1781704730293,
    "esigMeaningCode": "USER-RECORD",
    "scheduleID": null,
    "componentKey": "1646379",
    "reviewContentAllowed": true,
    "rating": null,
    "seqNum": null,
    "enableRating": false,
    "formattedRevisionDate": "10/Jun/2026",
    "completionDate": 1781704713000,
    "status": "Document - Complete",
    "ratingDate": null,
    "ratingPending": null,
    "lastCompletionDate": 1781704713000,
    "certificateLink": null,
    "onlineContentLink": null,
    "criteria": null,
    "embeddableDeeplink": null
  }
]
```
</td>
</tr>
</table>


<!--New Row-->


<!---New row-->
## Service Path - `/learning/odatav4/public/user/learningplan-service/v1/`

<table>

### UserTodoLearningItems
<tr>

<!--Left column-->
<td valign="top">

**Query Expression**
```python
$filter=criteria/targetUserID eq '00342456'
```

Parameters
- criteria/minRowNum
- criteria/maxRowNum
- criteria/qualItemsAndReqThresholdDays
- criteria/targetUserID
- criteria/targetPersonGUID
- criteria/retrieveLinkedSchedules
- criteria/includeDeepLink
- criteria/includeVLSlink
- criteria/includeSurveys
- criteria/includeLearnerActions
- criteria/sourceID
- criteria/cpntTypeID


</td>

<!--Right column-->
<td valign="top">

**Response**
```powershell
[
  {
    "sku": "SKU-1674339",
    "cpnt_classification": "BLENDED",
    "isUserRequestsEnabled": true,
    "title": "Line Clearance (Bedford and Chelmsford MA Sites)",
    "description": null,
    "status": "Y,N,N,N,-1,-6,-1,33198808,N,N,N,N,N,Y,N,Y,Y",
    "userID": "00342456",
    "personGUID": "1D15754763FE41F4AFDD35BF80ACF531",
    "personExternalID": "00342456",
    "componentTypeID": "OJT",
    "componentTypeDesc": "On the Job Training",
    "componentID": "LSG-BED-QA-OJT-0010",
    "componentKey": 1570218,
    "componentLength": 1.0,
    "contactHours": null,
    "creditHours": null,
    "cpeHours": null,
    "revisionDate": 1739545200000,
    "assignedDate": 1767744000000,
    "availableNewRevision": false,
    "revisionNumber": "1",
    "requiredDate": 1770267599000,
    "daysRemaining": -135,
    "addUser": "S",
    "addUserName": "00279294",
    "addUserTypeLabelID": "Manager",
    "orderItemID": null,
    "usedOrderTicketNumber": null,
    "usedOrderTicketSequence": null,
    "onlineLaunched": true,
    "origin": "Curriculum",
    "cdpGoalID": null,
    "seqNumber": null,
    "scheduleID": null,
    "qualificationID": "CUR-LSG-BED-QA-0041",
    "rootQualificationID": "CUR-LSG-BED-QA-5001",
    "qualTitle": "Line Clearance (Bedford QA)",
    "isRequired": true,
    "orderItemStatusTypeID": null,
    "showInCatalog": true,
    "requirementTypeDescription": "Required",
    "requirementTypeId": "REQ",
    "hasOnlinePart": true,
    "itemDetailsDeeplink": null,
    "courseDeeplink": null,
    "criteria": null,
    "linkedSchedules": [],
    "programType": null,
    "programEndDate": null,
    "programStartDate": null,
    "programDuration": null,
    "programDurationType": null,
    "programDeeplink": null,
    "vlsLink": null,
    "studentSurveyID": null,
    "itemSurveyID": null,
    "surveyID": null,
    "surveyLevel": null,
    "surveydesc": null,
    "surveyStatusID": null,
    "surveyDeepLink": null,
    "learnerActions": [],
    "embeddableDeeplink": null
  }
]
  ```

<td>
</tr>
</table>

<!--New row-->
## Service Path - `/learning/odatav4/public/admin/curriculum-service/v1/`

<table>

### Endpoint - CurriculumItemDetails

<tr>
<!---Left column-->
<td valign="top">

#### **Query Expression**
```python
$filter=cisCriteria/targetUserID eq '00142180' and cisCriteria/curriculumID eq 'CUR-LSG-BED-QA-0058' and cisCriteria/rootCurriculumID eq 'CUR-LSG-BED-QA-5010'
```

Parameters
- cisCriteria/userID
- cisCriteria/personGUID
- cisCriteria/curriculumID
- cisCriteria/rootCurriculumID

</td>

<!---Right column-->
<td valign>

#### **Response**

```powershell
[
  {
    "totalCount": null,
    "userID": "00142180",
    "personGUID": "2907D1DFB36C4AA6ABCE70F8F44AB4FD",
    "requirementGroupID": null,
    "requirementGroupDesc": null,
    "curriculumRequirementItems": [],
    "nextActionDate": 1778544000000,
    "curriculaID": "CUR-LSG-BED-QA-0058",
    "curriculaDesc": "The logic, terminology, and processes in PCP. \r\n",
    "htmlCurriculaDesc": null,
    "rootCurriculaID": "CUR-LSG-BED-QA-5010",
    "itemTypeID": "DOC",
    "itemID": "LSG-BED-BED1103",
    "revDate": 1744585200000,
    "itemTitle": "BED1103 QSP, DESIGN CONTROL (PPA MA Sites)",
    "assignmentType": "REQ",
    "displayOrder": 3,
    "requiredDate": 1797137999000,
    "expiryDate": 1797137999000,
    "requirementID": null,
    "requirementTypeID": null,
    "requirementDesc": null,
    "requirementSequenceNumber": null,
    "assignedDate": 1762473600000,
    "numberOfHours": null,
    "numberOfComponents": null,
    "globalDisplayOrder": "000003",
    "hourTypeID": null,
    "cisCriteria": null
  }
]
```
</td>
</tr>
</table>

<table>

### Endpoint - UserCurriculumStatuses

<tr>
<td valign="top">

#### Query Expression
```python
$filter=criteria/userID eq '00342456'&$top=1"
```

Parameters
- criteria/userID
- criteria/personGUID
- criteria/curriculumID
- criteria/rootCurriculumID

</td>

<td valign="top">

#### Response
```powershell
[
  {
    "userID": "00342456",
    "personGUID": "1D15754763FE41F4AFDD35BF80ACF531",
    "curriculumID": "CUR-GBL-OCPLM-0001",
    "curriculumStatus": "Y",
    "assignmentDate": 1763442000000,
    "expirationDate": null,
    "nextActionDate": null,
    "remainingDays": null,
    "totalCount": null,
    "rootCurriculaID": "CUR-GBL-OCPLM-0001"
  }
]
```
</tr>
</table>

<table>

### Endpoint - Items  

<tr>

<!--Left column-->
<td valign="top">

**Query Expression**
```python
$filter=icriteria/itemID eq 'LSG-GBL-50376028'&$top=1&$count=true
```

Parameters 
- icriteria/itemID
- icriteria/itemTypeIDs
- icriteria/revisionDate
- icriteria/itemTitle
- icriteria/classificationIDs
- icriteria/sourceIDs
- icriteria/deliveryMethodIDs
- icriteria/domainIDs
- icriteria/active


</td>

<!--Right column-->
<td valign="top">

**Response**
```powershell
[
  {
    "icriteria": null,
    "itemID": "LSG-GBL-50376028",
    "itemTypeID": "DOC",
    "revisionDate": 1530273600000,
    "itemTitle": "SOP0008877 - Product Risk Management (Global)",
    "classificationID": "CONTINUOUS ONLINE ACCESS",
    "sourceID": "",
    "deliveryMethodID": "",
    "domainID": "GBL",
    "active": false,
    "criteria": null,
    "totalCount": 7
  }
]
```
</td>
</tr>
</table>

<table>

### Students  

<tr>

<!--Left column-->
<td valign="top">

**Query Expression**
```python
$filter=scriteria/learnerID eq '00342456'&$count=true
```

Parameters 
- scriteria/learnerID
- scriteria/personGUID
- scriteria/personExternalID
- scriteria/lastName
- scriteria/firstName
- scriteria/middleInit
- scriteria/isActive
- scriteria/domainIDs
- scriteria/organizationIDs
- scriteria/jobPositionIDs 

</td>

<!--Right column-->
<td valign="top">

**Response**
```powershell
[
  {
    "scriteria": null,
    "studentID": "00342456",
    "personGUID": "1D15754763FE41F4AFDD35BF80ACF531",
    "personExternalID": "00342456",
    "empStatID": "Active",
    "empTypID": "Regular",
    "regularTempID": "",
    "fulltime": "Yes",
    "jobLocID": "508",
    "jobPosID": "",
    "domainID": "LSG",
    "orgID": "",
    "compID": null,
    "lastName": "MacGown",
    "firstName": "Andrea",
    "middleName": "Lee",
    "notActive": "no",
    "addr": "",
    "city": "",
    "state": "",
    "postal": "",
    "cntry": "",
    "superField": "00279294",
    "hireDate": 1630281600000,
    "termDate": null,
    "emailAddr": "andrea.macgown@thermofisher.com",
    "hasAccess": "Yes",
    "selfReg": "N",
    "locked": "No",
    "regionID": "",
    "roleID": "LSG_Learner",
    "profileStatus": "ACTIVE",
    "accountID": null,
    "posNumID": "",
    "nativeDeeplinkUser": "Yes",
    "criteria": null,
    "totalCount": 1
  }
]
```
</td>
</tr>
</table>


### Markdown Column Structure

````Markdown
## Resource path

<table>

## Endpoint

<tr>
<!--Left Column -->
<td valign="top">

**Query Expression**

```python
$filter=
```

</td>

<!--Right Column-->
<td valign="top">

**Query Expression**

```powershell
{ 
  [
    "Response Property": "Response Value",
  ]
}
```

</td>
</tr>
</table>

````