from statistics import mean, median


def count_records(records):
    return len(records)


def metric_values(records, attribute):
    return [
        record[attribute] for record in records
        if isinstance(record.get(attribute), (int, float))
        and not isinstance(record[attribute], bool)
    ]


def mean_metric(records, attribute):
    values = metric_values(records, attribute)
    return mean(values) if values else None


def median_metric(records, attribute):
    values = metric_values(records, attribute)
    return median(values) if values else None


def max_metric(records, attribute):
    values = metric_values(records, attribute)
    return max(values) if values else None


def top_n_records(records, attribute, n=5):
    return sorted(
        (record for record in records if record.get(attribute) is not None),
        key=lambda record: record[attribute],
        reverse=True,
    )[:n]
