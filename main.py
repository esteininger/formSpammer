import requests
import random
import names
import threading

base_url = ''

def random_phone():
    n = '0000000000'
    while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==n[9]:
        n = str(random.randint(10**9, 10**10-1))
    return n[:3] + '-' + n[3:6] + '-' + n[6:]

def main():
    domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]

    for i in range(25):
        name = names.get_first_name()
        email_index = random.randint(0, len(domains) - 1)

        payload = {
            'name': name,
            'phone': random_phone(),
            'email': '{}@{}'.format(name, domains[email_index]),
            'comments': '{} says hi!'.format(name)
        }
        try:
            r = requests.post(base_url, data=payload)
            print ('ok')

        except Exception as e:
            print(e)

if __name__ == '__main__':
    for i in range(10):
        threading.Thread(target=main).start()
