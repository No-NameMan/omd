"""Task 4: analyze a store's daily statistics."""


def main():
    days = [
        {'day': 'пн', 'orders': 20, 'revenue': 40_000, 'returns': 2},
        {'day': 'вт', 'orders': 16, 'revenue': 19_200, 'returns': 4},
        {'day': 'ср', 'orders': 25, 'revenue': 55_000, 'returns': 1},
        {'day': 'чт', 'orders': 10, 'revenue': 12_000, 'returns': 3},
        {'day': 'пт', 'orders': 30, 'revenue': 48_000, 'returns': 3},
    ]

    total_revenue = sum(day['revenue'] for day in days)
    best_day = max(days, key=lambda day: day['revenue'])
    high_return_days = [
        day['day']
        for day in days
        if day['returns'] / day['orders'] > 0.2
    ]

    print('Общая выручка:', total_revenue)
    print('День с наибольшей выручкой:', best_day['day'])
    print('Средняя выручка на заказ по дням:')
    for day in days:
        average_revenue = day['revenue'] / day['orders']
        print(f"  {day['day']}: {average_revenue:.2f}")
    print('Дни с долей возвратов выше 20%:', high_return_days)


if __name__ == '__main__':
    main()
