from channels import Group
#connect
def connet(message):
	message.reply_channel.send({"accept":True})
	Group('chat').add(message.reply_channel)


def receive_message(message):
	Group('chat').send({'text':message.content['text']})

def disconnect(message):
	Group('chat').discard(message.reply_channel)