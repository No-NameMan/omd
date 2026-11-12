def add_attribute(records, name, calculate):
    result = []
    for record in records:
        updated = record.copy()
        updated[name] = calculate(record)
        result.append(updated)
    return result
