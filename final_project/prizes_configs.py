from json_dict_processing import create_processor


def process_award_year(year):
    if year is None:
        return None
    year_text = str(year)
    return int(year_text) if year_text.isdigit() else None


CONFIG_PRIZE = {
    'prize_amount': ['prizeAmount'],
    'prize_amount_adjusted': ['prizeAmountAdjusted'],
    'award_year': (['awardYear'], process_award_year),
    'category_en': ['category', 'en'],
    'prize_status': ['prizeStatus'],
    'motivation_en': ['motivation', 'en'],
}


prize_processor = create_processor(CONFIG_PRIZE, list_processor=True)
