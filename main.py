import requests

TOKEN = '5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4'

def get_updates(TOKEN):
    updates = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    updates = updates.json()
    return updates

def dog(chat_id):
    Dog = requests.get('https://random.dog/woof.json')
    dog_data = Dog.json()['url']
    data = {
            'chat_id':chat_id,
            'photo':dog_data
            }
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',json=data)

def cat(chat_id):    
    Cat = requests.get('https://aws.random.cat/meow')
    url= Cat.json()['file']
    data1 = {
                'chat_id':chat_id,
                'photo':url,
            }
        
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',json=data1)
def get_button(chat_id):
        
    button1 = {'text':'😺CAT'}
    button2 = {'text':'🐶DOG'}

    keyboard = [[button1,button2]]
    
    reply_markup = {'keyboard':keyboard,'resize_keyboard':True}
    data = {
            'chat_id':chat_id,
            'text':text,
            'reply_markup':reply_markup
        }
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',json=data)
        
    return reply_markup 
def get_lastupdate(updates):
    last_update = updates['result'][-1]
    chat_id = last_update['message']['chat']['id']
    text = last_update['message']['text']
    message_id = last_update['message']['message_id']
    return chat_id,message_id,text

def send_alternative(chat_id):
    data2 = {
        'chat_id':chat_id,
        'text':'Iltimos dog yoki cat so`zini kiriting!'
        }
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',json=data2)
        


new_message = -1
while True:
    updates = get_updates(TOKEN)
    lastupdate = get_lastupdate(updates)
    chat_id,last_message_id,text= lastupdate

    if new_message != last_message_id:
        if text.lower()=='😺cat' or 'cat':
            cat(chat_id)
            get_button(chat_id)
        elif text.lower()=='🐶dog' or 'dog':
            dog(chat_id)
            get_button(chat_id)
        elif text.lower() != 'cat' or 'dog':
            send_alternative(chat_id)
            get_button(chat_id)
        
        new_message = last_message_id