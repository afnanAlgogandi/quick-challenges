
import requests
token = '6052800085:AAEjNPlYLKTW8FNA6Rgb91BMHfiQS14zEN4'
groupId = 'fullizaag'
msg = 'صعبه صعبه ذي ههههههههههه'
def sendMsg(message):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=@{groupId}&text={message}'
    res = requests.get(url)
    if res.status_code==200:
        print('Successfully sent')
    else:
        print('ERROR: Could not send Message')
sendMsg(msg)
