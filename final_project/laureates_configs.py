from json_dict_processing import create_processor
from prizes_configs import prize_processor


def process_id(value):
    return int(value) if value is not None else None


def process_year(date_string):
    if date_string is None:
        return None
    year_text = str(date_string).split('-')[0]
    if len(year_text) != 4 or not year_text.isdigit():
        return None
    year = int(year_text)
    return year if year > 0 else None


CONFIG_PERSON = {
    'id': (['id'], process_id),
    'name': ['knownName', 'en'],
    'gender': ['gender'],
    'birth_year': (['birth', 'date'], process_year),
    'country_birth': ['birth', 'place', 'country', 'en'],
    'country_now': ['birth', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], prize_processor),
}

CONFIG_ORG = {
    'id': (['id'], process_id),
    'name': ['orgName', 'en'],
    'founded_year': (['founded', 'date'], process_year),
    'country_founded': ['founded', 'place', 'country', 'en'],
    'country_now': ['founded', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], prize_processor),
}


process_persons = create_processor(CONFIG_PERSON)
process_orgs = create_processor(CONFIG_ORG)
