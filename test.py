import pymsteams

# You must create the connectorcard object with the Microsoft Webhook URL
myTeamsMessage = pymsteams.connectorcard(
    "https://outlook.office.com/webhook/93e6d77e-78e8-49cc-b406-963c72a3ac37@83f3a6e1-0470-4e13-984f-16a25372914c/IncomingWebhook/1784b62b5d5d4b508c5ca0db45367540/e1f661e7-f295-4368-8b14-1c0237cdac11")

# Add text to the message.
myTeamsMessage.title("Title of message")
myTeamsMessage.text("message")

# send the message.
myTeamsMessage.send()
