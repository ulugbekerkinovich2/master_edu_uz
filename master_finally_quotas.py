import json

from master_for_mentalaba import return_university_id, return_university_name

with open('jsons/magistrature_latest_without_ascii.json', 'r', encoding='utf-8-sig') as file:
    data_magistr_latest = json.load(file)

with open('jsons/master-with_tution_fee.json', 'r', encoding='utf-8-sig') as file:
    data_master_with_tuion_fee = json.load(file)

with open('jsons/masters_by_category_id2.json', 'r', encoding='utf-8-sig') as file:
    data_masters_by_category_id2 = json.load(file)

with open('jsons/uni_id_direction_id.json', 'r', encoding='utf-8-sig') as file:
    data_uni_id_direction_id = json.load(file)


def get_tuion_fee(university_id, code):
    for obj in data_master_with_tuion_fee:
        university_name = return_university_name(university_id)
        if obj['university'] == university_name and obj['code'] == code:
            return obj['tution_fee']

    # No matching data found
    return None


# arr = []
# for object in data_uni_id_direction_id:
#     univresity_name = object['full_name_uz']
#     arr.append(univresity_name)
# data = []
#
# for object in data_magistr_latest:
#     university_name = object['university']
#     if university_name not in arr:
#         university = object['university']
#         code = object['name'].split('-')[0].strip()
#         direction_name = object['name'].split('-')[1].strip()
#         grand = object['grand']
#         kontrakt = object['kontrakt']
#         obj = {
#             'university': university,
#             'code': code,
#             'direction_name': direction_name,
#             'grand': grand,
#             'kontrakt': kontrakt
#         }
#         data.append(obj)
# with open('jsons/new_magistrature_latest_without_ascii.json', 'w', encoding='utf-8-sig') as file:
#     data = json.dump(data, file, indent=4, ensure_ascii=False)


def get_masters_quota(university_name, code, direction_name):
    for obj in data_magistr_latest:
        shifr_code = obj['name'].split('-')[0].strip()
        direction_name_ = obj['name'].split('-')[1].strip()
        if str(obj['university']) == str(university_name) and str(shifr_code) == str(
                code) and direction_name_ == direction_name:
            grand = obj['grand']
            kontrakt = obj['kontrakt']
            # print(grand, kontrakt)
            return grand, kontrakt

    # No matching data found 65180
    return None, None


array = []
for obj in data_masters_by_category_id2:
    direction_id = obj['direction_id']
    id_number = obj['id_number']
    education_language_id = 1
    education_type_id = 1
    degrees = 2
    direction_name = obj['name_uz']
    university_id = str(obj['university_id'])
    code = str(obj['id_number'])
    local_tuition_fee = get_tuion_fee(university_id, code)
    grand, kontrakt = get_masters_quota(return_university_name(university_id), code, direction_name)

    #     # if grand or kontrakt is None:
    #     #
    #     print(university_id)
    print(university_id, direction_name,
          direction_id, grand, kontrakt)
    obj = {
        "direction_id": direction_id,
        "id_number": id_number,
        "education_language_id": education_language_id,
        "education_type_id": education_type_id,
        "degrees": degrees,
        "local_tuition_fee": local_tuition_fee,
        "grant": grand,
        "contract": kontrakt
    }
    array.append(obj)
with open('master_finally_2.json', 'w', encoding='utf-8-sig') as file:
    json.dump(array, file, indent=4, ensure_ascii=False)
print(len(array))
