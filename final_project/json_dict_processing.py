def extract_nested_value(obj, keys):
    value = obj
    for key in keys:
        if isinstance(value, dict):
            value = value.get(key)
        elif isinstance(value, list) and isinstance(key, int):
            value = value[key] if 0 <= key < len(value) else None
        else:
            return None
    return value


def process_dictionary_with_config(dictionary, config):
    result = {}
    for attribute, rule in config.items():
        if isinstance(rule, tuple):
            path, converter = rule
        else:
            path, converter = rule, None
        value = extract_nested_value(dictionary, path)
        result[attribute] = converter(value) if converter else value
    return result


def process_list_of_dicts_with_config(list_of_dicts, config):
    if list_of_dicts is None:
        return []
    return [
        process_dictionary_with_config(item, config)
        for item in list_of_dicts
    ]


def create_processor(config, list_processor=False):
    processor = (
        process_list_of_dicts_with_config
        if list_processor else process_dictionary_with_config
    )

    def process(data):
        return processor(data, config)

    return process
