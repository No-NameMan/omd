"""Task 2: count and analyze search queries."""


def main():
    queries = [
        'чехол',
        'iphone',
        'чехол',
        'наушники',
        'iphone',
        'iphone',
        'кабель',
        'чехол',
        'iphone',
    ]

    total_queries = len(queries)
    query_counts = {}

    for query in queries:
        query_counts[query] = query_counts.get(query, 0) + 1

    most_common_query = max(query_counts, key=query_counts.get)
    most_common_share = query_counts[most_common_query] / total_queries
    single_queries = [
        query for query, count in query_counts.items() if count == 1
    ]

    print('Всего запросов:', total_queries)
    print('Частота каждого запроса:', query_counts)
    print('Самый частый запрос:', most_common_query)
    print(f'Доля самого частого запроса: {most_common_share:.2%}')
    print('Запросы, встретившиеся один раз:', single_queries)


if __name__ == '__main__':
    main()
