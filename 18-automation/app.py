import requests
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': '+353 (00) 000 0000',
        'message': 'Good afternoon. This is python automated message.',
        'key': 'textbelt'
    })
    print(resp.json())

# schedule.every().day.at('07:35').do(send_message)
schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)