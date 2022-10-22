import requests

cat_and_dog = requests.get('https://storage.googleapis.com/petbacker/images/blog/2017/dog-and-cat-cover.jpg')
url =cat_and_dog.json()
print(cat_and_dog.json())

# TOKEN = '5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4'

# def get_updates(TOKEN):
#     updates = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
#     updates = updates.json()
#     r = requests.get('https://dog.ceo/api/breeds/image/random')
#     data = r.json()
#     return updates,data

# def get_lastupdate(updates,data):
#     last_update = updates['result'][-1]
#     chat_id = last_update['message']['chat']['id']
#     text = last_update['message']['text']
#     message_id = last_update['message']['message_id']
#     img_url = data.get('message')
#     return chat_id,message_id,img_url

# def send_message(TOKEN,chat_id,img_url):
#     url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
#     data = {
#             'chat_id':chat_id,
#             'photo':img_url
#             # 'text':text
#         }

#     r = requests.post(url,data=data)    
    
# # print(r.status_code)




# new_message = -1

# while True:
#     updates = get_updates(TOKEN)
#     lastupdate = get_lastupdate(updates)
#     chat_id,text,last_message_id = lastupdate

#     if new_message != last_message_id:
#         send_message(TOKEN,chat_id=chat_id,text=text)
#         new_message = last_message_id