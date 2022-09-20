from imap_tools import MailBox,A , AND, OR
import schedule
import telnyx
import requests

user="enter email"
password="enter password"
imap_url = 'imap.gmail.com'
import time as t





def send_sms(text):
  profile_secret = "enter secret telnyx"

  headers = {
      "X-Profile-Secret": profile_secret,
  }
  url = "https://sms.telnyx.com/messages"
  payload = {
    "from": "",
    "to": "",
    "body": text,
  }

  response = requests.post(
      url,
      headers=headers,
      json=payload
  )
  print(response)
  print(response.json())






def mailChecker(mailbox): 
      responses = mailbox.idle.wait(timeout=1)
      for msg in mailbox.fetch(AND(seen=False)):
        if msg.from_ == "":
          print("=============")
          print("Message id:", msg.uid)
          print("Message Subject:",msg.subject)
          print("Message Date:", msg.date)
          print("message text" , msg.text)
          try:
            send_sms(text=msg.text)
          except:
            print("error")




mailbox = MailBox(imap_url).login(user, password, "INBOX")

schedule.every(1).seconds.do(mailChecker,mailbox)


while True:
    schedule.run_pending()
    t.sleep(1)


