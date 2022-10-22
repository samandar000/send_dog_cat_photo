import requests

TOKEN = '5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4'

def get_updates(TOKEN):
    updates = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    updates = updates.json()
    return updates

def send_dog(chat_id):
    Dog = requests.get('https://random.dog/woof.json')
    dog_data = Dog.json()['url']
    data = {
        'chat_id':chat_id,
        'photo':dog_data

        }
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',data=data)
    



def send_cat(chat_id):
    Cat = requests.get('https://aws.random.cat/meow')
    url= Cat.json()['file']
    data1 = {
            'chat_id':chat_id,
            'photo':url,
        }
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',data=data1)

def send_cat_and_dog(chat_id):
    img_url = 'https://storage.googleapis.com/petbacker/images/blog/2017/dog-and-cat-cover.jpg'
    data = {
        'chat_id':chat_id,
        'photo':img_url
        
        }
    
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',data=data)
    




def send_alternative(chat_id,text):
    data2 = {
        'chat_id':chat_id,
        'text':'Iltimos dog yoki cat so`zini kiriting!'
        }
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',data=data2)
    





def get_lastupdate(updates):
    last_update = updates['result'][-1]
    chat_id = last_update['message']['chat']['id']
    text = last_update['message']['text']
    message_id = last_update['message']['message_id']
    return chat_id,message_id,text


new_message=-1





while True:
    updates = get_updates(TOKEN)
    lastupdate = get_lastupdate(updates)
    chat_id,last_message_id,text= lastupdate

    if new_message != last_message_id:
        if text.lower()=='cat and dog':
            send_cat_and_dog(chat_id)
        if text.lower()=='cat':
            send_cat(chat_id)
        elif text.lower()=='dog':
            send_dog(chat_id)
        elif text.lower() != 'cat' or 'dog':
            send_alternative(chat_id,text)
        
        new_message = last_message_id
