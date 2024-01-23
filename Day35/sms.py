import os
from twilio.rest import Client

# https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1

account_sid = "insira account sid"
auth_token = "insira auth token"

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Teste de disparo de sms.",
                     from_='+12676338514',
                     to='+5511999995979'
                 )

print(message.sid)