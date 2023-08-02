# import requests

# Number = "+966501788450"

# text = "Hi"
# url = 'https://textflow-sms-api.p.rapidapi.com/send-sms'


# payload = {
#     "phone_number":Number,
#     "text":text
    
#     }
# headers= {
#     'content-type': 'application/json',
#     'X-RapidAPI-Key': 'c079281311mshac22dc556aea06cp194ce8jsn3e19f9446e00',
#     'X-RapidAPI-Host': 'textflow-sms-api.p.rapidapi.com'
#   }


# response = requests.post(url,json=payload,headers=headers)
# print(response.json())



import requests

url = "https://textflow-sms-api.p.rapidapi.com/send-sms"

payload = {
	"phone_number": "+966501788450",
	"text": "Test message from TextFlow"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "c079281311mshac22dc556aea06cp194ce8jsn3e19f9446e00",
	"X-RapidAPI-Host": "textflow-sms-api.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())