def filter_records(records, predicate):
    return [record for record in records if predicate(record)]


def group_by_attributes(records, attributes):
    groups = {}
    for record in records:
        group_key = tuple(record.get(name) for name in attributes)
        groups.setdefault(group_key, []).append(record)
    return groups


def aggregate_groups(groups, aggregation):
    return {
        group_key: aggregation(records)
        for group_key, records in groups.items()
    }
