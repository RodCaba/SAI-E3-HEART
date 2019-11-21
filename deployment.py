import urllib3, requests, json
from watson_machine_learning_client import WatsonMachineLearningAPIClient
import requests

all_credentials = {
  "apikey": "",
  "iam_apikey_description": "Auto-generated for key 34ccb1c6-4061-43fd-becc-d3e30bdfa96b",
  "iam_apikey_name": "wdp-writer",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/eb0a6c22e42b4b90b7380e5dc9f9ef47::serviceid:ServiceId-d1a7fa33-0871-4cde-bc91-83c8c4d48f0b",
  "instance_id": "f0072c5c-eb70-42e3-9e65-eb0525dee1a6",
  "url": "https://us-south.ml.cloud.ibm.com"
}

wml_credentials = {
    "apikey": "",
    "instance_id": "f0072c5c-eb70-42e3-9e65-eb0525dee1a6",
    "url": "https://us-south.ml.cloud.ibm.com"
}

apikey = ""

# Get an IAM token from IBM Cloud
url     = "https://iam.bluemix.net/oidc/token"
headers = { "Content-Type" : "application/x-www-form-urlencoded" }
data    = "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
IBM_cloud_IAM_uid = "bx"
IBM_cloud_IAM_pwd = "bx"
response  = requests.post( url, headers=headers, data=data, auth=( IBM_cloud_IAM_uid, IBM_cloud_IAM_pwd ) )
iam_token = response.json()["access_token"]

client = WatsonMachineLearningAPIClient(wml_credentials)
# NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation	
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': "f0072c5c-eb70-42e3-9e65-eb0525dee1a6"}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
dat = [[58,0,4,80,95],[62,1,2,120,200],[72,0,2,100,145]]
payload_scoring = {"input_data": [{"fields": ["age", "sex", "cp", "trestbps", "chol"], "values": dat}]}


response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v4/deployments/88901ff5-9852-42b6-8c12-8bd78056e5a2/predictions', json=payload_scoring, headers=header)
print("Scoring response")
print(json.loads(response_scoring.text))

