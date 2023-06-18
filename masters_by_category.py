import json
from master_for_mentalaba import return_university_id, return_category_id

with open('jsons/masters_by_category.json', 'r', encoding='utf-8-sig') as file:
    data_master = json.load(file)

with open('jsons/bachelor_by_category.json', 'r', encoding='utf-8-sig') as file:
    data_bachelor = json.load(file)
data = []
for object in data_bachelor:
    kategoriya = object['Kategoriyalar']
    if kategoriya not in data:
        data.append(kategoriya)
print(data)

array = []
i = 2762
k = 629
for obj in data_master:
    # print(json.dumps(obj, indent=4, ensure_ascii=False))
    university = obj['Universities']
    university_id = return_university_id(university)
    if university_id is not None:
        university_id = int(university_id)
    if university_id is None:
        continue
    yonalish_id = obj["Yo'nalish ID"]
    yonalish = obj["Tal'lim yo'nalishi"]
    category_name = obj['Category']
    return_category = return_category_id(category_name)
    if return_category is None:
        continue
    object = {
        'id': k,
        'direction_id': i,
        "id_number": int(yonalish_id),
        "university_id": university_id,
        "name_uz": yonalish,
        "name_ru": yonalish,
        "category_id": return_category
    }
    array.append(object)
    i += 1
    k += 1
with open('jsons/masters_by_category_id2.json', 'w', encoding='utf-8-sig') as file:
    json.dump(array, file, indent=4, ensure_ascii=False)


    # "direction_id": 117,
    # "id_number": "60230101",
    # "education_type_id": 1,
    # "education_language_id": 1,
    # "grant_quota": 10,
    # "contract_quota": 40
    # local_tuion_fee:
    # degree: 2