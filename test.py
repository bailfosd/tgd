import requests
import json

# Define the URL and the data payload
url = "https://e-pul.az/epay/az/guest_payment/check_client_info/1457"
data = {
    "mode": "56",
    "IAMAS": "52CLL99",
    "selectedGroupId": "56",
    "frameModel": "1",
    "hdnserid": "1457",
}

# Send the POST request
response = requests.post(url, data=data)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON content of the response
    response_data = json.loads(response.text)
 full_name = response_data["fullName"]
    
    # Assuming there is only one subService and you want to extract its "amount"
    sub_service_amount = response_data["subServices"][0]["amount"]
    
    print("Full Name:", full_name)
    print("Sub Service Amount:", sub_service_amount)
    # Print the "code" and "message" values
    if(response_data["code"]=="Error"):
        print('aaaaaaaaaaaaaaaah')
    print("Message:", response_data["message"])
else:
    print(f"Request failed with status code: {response.status_code}")
