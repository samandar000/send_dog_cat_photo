import requests

TOKEN = '5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4'

def get_updates(TOKEN):
    updates = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    updates = updates.json()
    return updates

def paramet_dog(Dog):
    Dog = requests.get('https://random.dog/woof.json')
    dog_data = Dog.json()
    return dog_data 
def send_cat(chat_id):
    Cat = requests.get('https://aws.random.cat/meow')
    url= Cat.json()['file']
    data1 = {
            'chat_id':chat_id,
            'photo':url,
        }
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',data=data1)
def get_lastupdate(updates):
    last_update = updates['result'][-1]
    chat_id = last_update['message']['chat']['id']
    text = last_update['message']['text']
    message_id = last_update['message']['message_id']
    return chat_id,message_id,text

# def urls(TOKEN,cat_data,dog_data,text,chat_id):
#     url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
#     dog = 'dog' or 'DOG' or 'Dog'
#     cat = 'cat' or 'CAT' or 'Cat'
#     cat_url = cat_data.get('file')
    
#     if text in dog:
#         img_url = dog_data.get('url')
#     if text in cat:
#         cat_url = cat_data.get('file')
#     if text not in dog or cat:
#         text = 'Iltimos Dog yoki Cat yozing'
    

#     data = {
#             'chat_id':chat_id,
#             'photo':img_url,
#             'text':text
#         }
#     data1 = {
#             'chat_id':chat_id,
#             'photo':cat_url,
#             'text':text
#         }
    
#     Dog = requests.post(url,data=data)
#     Cat = requests.post(url,data=data1)
new_message=-1
while True:
    updates = get_updates(TOKEN)
    lastupdate = get_lastupdate(updates)
    chat_id,last_message_id,text= lastupdate

    if new_message != last_message_id:
        if text.lower()=='cat':
            send_cat(chat_id)
        new_message = last_message_id
