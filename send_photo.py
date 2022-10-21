import requests

TOKEN = '5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4'
# while True:
Dog = requests.get('https://random.dog/woof.json')
dog_data = Dog.json()

Cat = requests.get('https://aws.random.cat/meow')
cat_data = Cat.json()

updates = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
updates = updates.json()

chat_id = updates['result'][-1]['message']['chat']['id']
text = updates['result'][-1]['message']['text']

url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
dog = 'dog' or 'DOG' or 'Dog'
cat = 'cat' or 'CAT' or 'Cat'
if text in dog:
    img_url = dog_data.get('url')
if text in cat:
    img_url = cat_data.get('url')
data = {
        'chat_id':chat_id,
        'photo':img_url,
        'text':text
    }
Dog = requests.post(url,data=data)
Cat = requests.post(url,data=data)
print(Dog.status_code)
print(Cat.status_code)