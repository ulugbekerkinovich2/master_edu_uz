import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time
import time

# driver.execute_script("window.open()")


# def translate_text(text):
#     driver.switch_to.window(driver.window_handles[-1])
#
#     url = "https://translate.google.com/"
#     driver.get(url)
#     input = driver.find_element(By.XPATH,
#                                 '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span')
#     time.sleep(0.02)
#     input.send_keys(text)
#     time.sleep(0.09)
#     translated_text = driver.find_element(By.XPATH,
#                                           '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[9]/div/div[1]').text
#     time.sleep(0.05)
#     return translated_text


# {
#     "id_number": 12345678,
#     "university_id": 18,
#     "name_uz": "Mahalla va suv xo‘jaligida texnik",
#     "name_ru": "Qishloq va suv xo‘jaligida texnik servis1",
# }

# "direction_id": 117,
# "id_number": "60230101",
# "education_type_id": 1,
# "education_language_id": 1,
# "grant": 175.1,
# "contract": 154.9,
# "grant_quota": 10,
# "contract_quota": 40

with open('jsons/master_latest_.json', 'r', encoding='utf-8-sig') as file:
    data_master = json.load(file)

with open('jsons/master-with_tution_fee.json', 'r', encoding='utf-8-sig') as file:
    data_tutiton_fee = json.load(file)

with open('jsons/uni_id_direction_id.json', 'r', encoding='utf-8-sig') as file:
    data_uni_id_direction_id = json.load(file)

with open('jsons/category_by_id.json', 'r', encoding='utf-8-sig') as file:
    data_category_by_id = json.load(file)


def get_data(university_name, code_):
    for obj in data_master:
        university = obj.get('university', 'university_name_yoq')
        direction_name = obj.get('name', 'direction_name_yoq').split('-')[1].strip()
        code = obj.get('name', 'code_yoq').split('-')[0].strip()
        grand_quota = obj.get('grand', 0).strip()
        kontrakt = obj.get('kontrakt', 0).strip()
        print(university, direction_name, code, grand_quota, kontrakt)
        # time.sleep(0.01)
        if university_name == university and code == code_:
            return grand_quota, kontrakt


def collet_data():
    for obj in data_tutiton_fee:
        pass


def return_university_id(university_name):
    for obj in data_uni_id_direction_id:
        # print(obj)
        university = obj['full_name_uz']
        # print(university)
        if university_name == university:
            university_id = obj['uni_id']
            # print(university_id)
            #     time.sleep(0.05)
            return university_id
        # else:
        #     return None


def return_university_name(university_id):
    for obj in data_uni_id_direction_id:
        university__id = obj['uni_id']
        if university_id == university__id:
            university_name = obj['full_name_uz']
            return university_name


def return_category_id(category_name):
    for obj in data_category_by_id:
        name_uz = obj['name_uz']
        obj_id = int(obj['id'])
        if category_name == name_uz:
            return obj_id

# todo Qoraqalpog'iston tibbiyot instituti
# todo Qarshi muhandislik - iqtisodiyot instituti
# todo Urganch davlat pedagogika instituti
# todo Botir Zokirov nomidagi Milliy estrada san'ati instituti
# todo O‘zbekiston davlat san’at va madaniyat instituti

# array = []
# #
# for obj in data_master:
#     id_number = obj['name'].split('-')[0].strip()
#     univer = obj['university']
#     university_id = return_university_id(univer)
#     if university_id is None:
#         continue
#     name_uz = obj['name'].split('-')[1].strip()
#     print(id_number, university_id, '----')
#     # time.sleep(1)
#     objects = {
#         "id_number": id_number,
#         "university_id": university_id,
#         "name_uz": name_uz.replace('\u02bb', "'").replace('\u02bc', "'").replace('\u2018', "'"),
#         "name_ru": name_uz.replace('\u02bb', "'").replace('\u02bc', "'").replace('\u2018', "'")
#     }
#     array.append(objects)
#
# with open('sirojiddinga1.json', 'w') as file:
#     json.dump(array, file, indent=4, ensure_ascii=False)
