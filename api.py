base_url = 'https://petfriends.skillfactory.ru'
new_admin = 'yaname.test@gmail.com'
new_pass = 'test2023'
patch_params = {'user': new_admin, 'password': new_pass}
url_get = 'https://petfriends.skillfactory.ru/api/key'
password = 'test2022'
email = 'yaname.test@gmail.com'

#Негативные параметры
headers_n1 = {'email': email + 'jhff','password': password,'accept': 'application/json'}
headers_n2 = {'email': email,'password': password+ 'jhff','accept': 'application/json'}
headers_n3 = {'auth_key': '7aaf89817fcebb6a9d441ca2e29b97b4b8142bc78a852bb18b16d65ajhff','accept': 'application/json'}
headers_npost = {'accept': 'application/json','auth_key': '7aaf89817fcebb6a9d441ca2e29b97b4b8142bc78', 'Content-Type': 'application/json'}
nname = 'Dand876tyuf5erdt45wers47889vj!@!%^y'

data_npost  = {
    'name': nname,
    'animal_type': 'crokodile',
    'age': '3'
}
nage = 'j8gu6utf3@$534$#@@$%*&*Yghjgtew'
data_npost1  = {
    'name': 'Dandy',
    'animal_type': 'crokodile',
    'age': nage
}



url_pet_list= 'https://petfriends.skillfactory.ru/api/pets?filter=my_pets'
url_create_pet= 'https://petfriends.skillfactory.ru/api/create_pet_simple'
url_put = 'https://petfriends.skillfactory.ru/api/pets/1431cce9-878f-4586-aa79-e04179c631c4'
url_del = 'https://petfriends.skillfactory.ru/api/pets/149fb392-eaff-429d-a740-9aa6cd9efe04'
key = '7aaf89817fcebb6a9d441ca2e29b97b4b8142bc78a852bb18b16d65a'

data_postn = {
    'name': 'Dandy',
    'animal_type': nage,
    'age': '3'
}


data_h = {'email': email,
    'password': password,
    'Content-Type': 'application/json'
}
headers_put = {
    'accept': 'application/json',
    'auth_key': '7aaf89817fcebb6a9d441ca2e29b97b4b8142bc78a852bb18b16d65a',
    'Content-Type': 'application/json'
}
headers_putn = {
    'accept': 'application/json',
    'auth_key': '7aaf89817fcebb6a9d441ca2e29b97b4b8142bc78a',
    'Content-Type': 'application/json'
}

data_put  = {
    'name': 'Turbo',
    'animal_type': 'ulitka',
    'age': '5'
}
data_putn  = {
    'name': nage,
    'animal_type': 'ulitka',
    'age': '5'
}

data_putn1  = {
    'name': 'Turbo',
    'animal_type': nage,
    'age': '5'
}
data_putn2  = {
    'name': 'Turbo',
    'animal_type': 'ulitka',
    'age': nage
}
headers_3 = {'auth_key': '7aaf89817fcebb6a9d441ca2e29b97b4b8142bc78a852bb18b16d65a','accept': 'application/json'}
headers_dn = {'auth_key': '7aaf89817fcebb6a9d441ca2e29b97b4b814','accept': 'application/json'}
headers_post = {
    'accept': 'application/json',
    'auth_key': '7aaf89817fcebb6a9d441ca2e29b97b4b8142bc78a852bb18b16d65a',
    'Content-Type': 'application/json'
}

data_post  = {
    'name': 'Dandy',
    'animal_type': 'crokodile',
    'age': '3'
}

data_head  = {
    'name': 'Turbo',
}
headers_head = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

