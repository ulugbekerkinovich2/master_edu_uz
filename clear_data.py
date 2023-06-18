import json

with open('jsons/new_all_data.json', 'r', encoding='utf-8-sig') as file:
    data_abt = json.load(file)

with open('jsons/new_datas.json', 'r', encoding='utf-8-sig') as files:
    new_data = json.load(files)

with open('jsons/new_datas-with_code.json', encoding='utf-8-sig') as files_:
    data = json.load(files_)


def get_objects(univer_id):
    for obj in data_abt:
        university_id = int(obj['Universities'])
        id_number = int(obj["Yo'nalish kodi"])
        kunduzgi_uzb = obj["Kunduzgi o'zbek ta'lim"]
        kunduzgi_rus = obj["Kunduzgi rus ta'lim"]
        kunduzgi_turkman = obj["Kunduzgi turkman ta'lim"]
        kunduzgi_qozoq = obj["Kunduzgi qozoq ta'lim"]
        kunduzgi_qoraqalpoq = obj["Kunduzgi qoraqalpoq ta'lim"]
        kunduzgi_qirgiz = obj["Kunduzgi qirg'iz ta'lim"]
        kunduzgi_tojik = obj["Kunduzgi tojik ta'lim"]
        sirtqi_uzb = obj["Sirtqi o'zbek ta'lim"]
        sirtqi_rus = obj["Sirtqi rus ta'lim"]
        sirtqi_turkman = obj["Sirtqi turkman ta'lim"]
        sirtqi_qozoq = obj["Sirtqi qozoq ta'lim"]
        sirtqi_qoraqalpoq = obj["Sirtqi qoraqalpoq ta'lim"]
        sirtqi_tojik = obj["Sirtqi tojik ta'lim"]
        kechki_uzb = obj["Kechki o'zbek ta'lim"]
        kechki_rus = obj["Kechki rus ta'lim"]
        kechki_qoraqalpoq = obj["Kechki qoraqalpoq ta'lim"]
        kechki_tojik = obj["Kechki tojik ta'lim"]
        masof_uzb = obj["Masofaviy o'zbek ta'lim"]
        masof_rus = obj["Masofaviy rus ta'lim"]
        masofaviy_qoraqalpoq = obj["Masofaviy qoraqalpoq ta'lim"]
        kunduzgi_uzb_qabul = obj["Kunduzgi o'zbek qabul"]
        kunduzgi_rus_qabul = obj["Kunduzgi rus qabul"]
        kunduzgi_turkman_qabul = obj["Kunduzgi turkman qabul"]
        kunduzgi_qozoq_qabul = obj["Kunduzgi qozoq qabul"]
        kunduzgi_qirgiz_qabul = obj["Kunduzgi qirg'iz qabul"]
        kunduzgi_qoraqalpoq_qabul = obj["Kunduzgi qoraqalpoq qabul"]
        kunduzgi_tojik_qabul = obj["Kunduzgi tojik qabul"]
        sirtqi_uzb_qabul = obj["Sirtqi o'zbek qabul"]
        sirtqi_rus_qabul = obj["Sirtqi rus qabul"]
        sirtqi_turkman_qabul = obj["Sirtqi turkman qabul"]
        sirtqi_qozoq_qabul = obj["Sirtqi qozoq qabul"]
        sirtqi_qoraqalpoq_qabul = obj["Sirtqi qoraqalpoq qabul"]
        sirtqi_tojik_qabul = obj["Sirtqi tojik qabul"]
        kechki_uzb_qabul = obj["Kechki o'zbek qabul"]
        kechki_rus_qabul = obj["Kechki rus qabul"]
        kechki_qoraqalpoq_qabul = obj["Kechki qoraqalpoq qabul"]
        kechki_tojik_qabul = obj["Kechki tojik qabul"]
        masof_uzb_qabul = obj["Masofaviy o'zbek qabul"]
        masof_rus_qabul = obj["Masofaviy rus qabul"]
        masofaviy_qoraqalpoq_qabul = obj["Masofaviy qoraqalpoq qabul"]
        kunduzgi_uzb_grand = obj["Kunduzgi o'zbek grand"]
        kunduzgi_rus_grand = obj["Kunduzgi rus grand"]
        kunduzgi_turkman_grand = obj["Kunduzgi turkman grand"]
        kunduzgi_qozoq_grand = obj["Kunduzgi qozoq grand"]
        kunduzgi_qirgiz_grand = obj["Kunduzgi qirg'iz grand"]
        kunduzgi_qoraqalpoq_grand = obj["Kunduzgi qoraqalpoq grand"]
        kunduzgi_tojik_grand = obj["Kunduzgi tojik grand"]
        sirtqi_uzb_kontrakt = obj["Sirtqi o'zbek kontrakt"]
        sirtqi_rus_kontrakt = obj["Sirtqi rus kontrakt"]
        sirtqi_qozoq_kontrakt = obj["Sirtqi qozoq kontrakt"]
        sirtqi_qoraqalpoq_kontrakt = obj["Sirtqi qoraqalpoq kontrakt"]
        sirtqi_tojik_kontrakt = obj["Sirtqi tojik kontrakt"]
        kechki_uzb_kontrakt = obj["Kechki o'zbek kontrakt"]
        kechki_rus_kontrakt = obj["Kechki rus kontrakt"]
        kechki_turkman_kontrakt = obj["Kechki turkman kontrakt"]
        kechki_tojik_kontrakt = obj["Kechki tojik kontrakt"]
        masof_uzb_kontrakt = obj["Masofaviy o'zbek kontrakt"]
        masof_rus_kontrakt = obj["Masofaviy rus kontrakt"]
        masof_qoraqalpoq_kontrakt = obj["Masofaviy qoraqalpoq kontrakt"]
        if kunduzgi_uzb is not None:
            k_uzb = kunduzgi_uzb.split(',')
            k_uzb = [int(i) for i in k_uzb]


get_objects()


# def get_direction_object(**kwargs):
#     for objects in data:
#         if objects['uni_id'] == int(kwargs['universities_id']) and \
#                 objects["Yo'nalish kodi"] == int(kwargs['direction_code']):
