from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC3ffa171859af9e7371347e63a1988cf5"
auth_token  = "2cda6e1bea5533239519fe20028a0754"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Siddhanth you're the best",
    to="+918755240637",    # Replace with your phone number
    from_="+12282830238") # Replace with your Twilio number
print message.sid