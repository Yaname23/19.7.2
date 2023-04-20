import requests
import json

from api import url_get, url_put, headers_dn, url_del, data_putn,data_putn1,data_putn2, headers_putn,headers_put,data_put, data_postn, data_npost1, headers_npost,data_npost,nname, nage, headers_n1,headers_n2,headers_n3, base_url, url_pet_list, url_create_pet, headers_post, data_post

#Positive
for url in [base_url]:
    reo = requests.options(base_url)
    if reo.status_code == 200:
        print('OPTIONS.Статус код: 200.', 'API-ключ: ', reo.headers)
    else:
        print('OPTIONS.Код ошибки: ', reo.status_code, ', данные не были изменены')

for url in [base_url]:
    rp = response = requests.head(base_url)
    if rp.status_code == 200:
        print('HEAD.Статус код: 200.', 'API-ключ: ', rp.headers)
    else:
        print('HEAD.Код ошибки: ', rp.status_code, ', данные не были изменены')

#Negative

for url in [url_get]: #укажем неверный email
    res = requests.get(url_get, headers= headers_n1)
    if res.status_code == 200:
        print('GET.Статус код: 200.', 'API-ключ: ', res.json())
    else:
        print('GET(неверно указан email).Код ошибки:',res.status_code)

for url in [url_get]: #неверный пароль
    res = requests.get(url_get, headers= headers_n2)
    if res.status_code == 200:
        print('GET.Статус код: 200.', 'API-ключ: ', res.json())
    else:
        print('GET(неверно указан пароль).Код ошибки:',res.status_code)

for url in [url_pet_list]:
    r = requests.get(url_pet_list, headers=headers_n3)
    if r.status_code == 200:
        print('GET.Статус код: 200.', 'Список моих животных: ', r.json())
    else:
        print('GET(неверно указан API-ключ).Код ошибки:',r.status_code)
        #4
for url in [url_create_pet]:#API
    a = requests.post(url_create_pet, headers=headers_npost, data=json.dumps(data_post))
    if a.status_code == 200:
        print('POST.Статус код: 200.','Добавлены данные:', data_post)
    else:
        print('POST(неверно указан API-ключ).Код ошибки:',a.status_code)
#5
for url in [url_create_pet]:#
    a = requests.post(url_create_pet, headers=headers_post, data=json.dumps(data_npost))
    if a.status_code == 200:
        print('POST(недопустимые знаки в имени).НО!!! Статус код: 200.','Добавлены данные:', data_npost)
    else:
        print('POST(неверно указано имя)', nname,'Код ошибки:',a.status_code)
#6
for url in [url_create_pet]:#
    a = requests.post(url_create_pet, headers=headers_post, data=json.dumps(data_npost1))
    if a.status_code == 200:
        print('POST(недопустимые знаки в возрасте).НО!!! Статус код: 200.','Добавлены данные:', data_npost1)
    else:
        print('POST(недопустимые знаки в возрасте)', nage,'Код ошибки:',a.status_code)
#7
for url in [url_create_pet]:#
    a = requests.post(url_create_pet, headers=headers_post, data=json.dumps(data_postn))
    if a.status_code == 200:
        print('POST(недопустимые знаки в animal_type).НО!!! Статус код: 200.','Добавлены данные:', data_postn)
    else:
        print('POST(недопустимые знаки в animal_type)', nage,'Код ошибки:',a.status_code)
#8
for url in [url_put]:
    pu = requests.put(url, headers=headers_putn, data=json.dumps(data_put))
    if pu.status_code == 200:
        print('PUT.Статус код: 200.','Изменен возраст Турбо, обновленные данные:',pu.text )
    else:
        print('PUT(неверно указан API-ключ).Код ошибки: ', pu.status_code, ', данные не были изменены')

#9
for url in [url_put]:
    pu = requests.put(url, headers=headers_put, data=json.dumps(data_putn))
    if pu.status_code == 200:
        print('PUT(недопустимые знаки в имени).НО!!! Статус код: 200.','Добавлены данные:', data_putn)
    else:
        print('PUT(недопустимые знаки в имени).Код ошибки: ', pu.status_code, ', данные не были изменены')
#10
for url in [url_put]:
    pu = requests.put(url, headers=headers_put, data=json.dumps(data_putn1))
    if pu.status_code == 200:
        print('PUT(недопустимые знаки в animal_type).НО!!! Статус код: 200.','Добавлены данные:', data_putn1)
    else:
        print('PUT(недопустимые знаки в animal_type).Код ошибки: ', pu.status_code, ', данные не были изменены')
#11
for url in [url_put]:
    pu = requests.put(url, headers=headers_put, data=json.dumps(data_putn2))
    if pu.status_code == 200:
        print('PUT(недопустимые знаки в возрасте).НО!!! Статус код: 200.','Добавлены данные:', data_putn2)
    else:
        print('PUT(недопустимые знаки в возрасте).Код ошибки: ', pu.status_code, ', данные не были изменены')
#12
for url in [url_del]:
    re = requests.delete(url_del, headers=headers_dn)
    if re.status_code == 200:
        print('DELETE.Статус код: 200.','Удаление питомца прошло успешно')
    else:
        print('DELETE(неверно указан API-ключ).Код ошибки: ', re.status_code, ', удаление питомца не было произведено')
