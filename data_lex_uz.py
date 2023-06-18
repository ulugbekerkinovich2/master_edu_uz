import json
import time
with open('jsons/new1_cleaned_masters_data.json', 'r', encoding='utf-8-sig') as file:
    data_magistr_latest = json.load(file)
university_name_ = None
array = []
for object in data_magistr_latest:
    id_number = object['university_name']
    university_name = object['direction_name']
    grand_quota = object['grant_quota']
    kontrakt_quota = object['kontrakt_quota']
    if grand_quota == '':
        grand_quota = 0
    if kontrakt_quota == '':
        kontrakt_quota = 0
    # print(id_number, university_name, grand_quota, kontrakt_quota)
    # time.sleep(0.1)
    if len(id_number) < 3:
        university_name_ = university_name
    if len(id_number) == 8:
        obj = {
            'university_name': university_name_,
            'id_number': id_number,
            'direction_name': object['university_name'],
            'grand_quota': grand_quota,
            'kontrakt_quota': kontrakt_quota
        }
        array.append(obj)
print(array)
with open('new_cleaned_data_lex_uz_masters.json', 'w', encoding='utf-8-sig') as file:
    json.dump(array, file, indent=4, ensure_ascii=False)
