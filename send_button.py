import requests


TOKEN = '5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4'
while True:
    def get_updates():
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
        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',data=data)
        
    def cat(chat_id):
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
        return chat_id,text,message_id
    def button(chat_id,TOKEN):
        
        button1 = {'text':'aCAT'}
        button2 = {'text':'🐶DOG'}
        keyboard = [[button1,button2]]
        reply_markup = {'keyboard':keyboard,'resize_keyboard':True}
        data = {
            'chat_id':chat_id,
            'text':text,
            'reply_markup':reply_markup
        }
        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',json=data)
        
    new_message = -1

    updates = get_updates(TOKEN)
    lastupdate = get_lastupdate(updates)
    chat_id,last_message_id,text= lastupdate

    
    updates = (TOKEN)
    lastupdate = (updates)
    text=lastupdate
    if text.lower()=='cat':
        cat(chat_id)
    if text.lower()=='dog':
        dog(chat_id)
            