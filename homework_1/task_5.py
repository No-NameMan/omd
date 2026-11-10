"""Task 5: summarize normalized product reviews."""


def main():
    reviews = [
        {'id': 1, 'product': 'Чехол', 'stars': 5},
        {'id': 1, 'product': 'Чехол', 'stars': 3},
        {'id': 1, 'product': 'Чехол', 'stars': 4},
        {'id': 2, 'product': 'Наушники', 'stars': 2},
        {'id': 2, 'product': 'наушники', 'stars': 2},
        {'id': 2, 'product': 'НАУШНИКИ', 'stars': 5},
        {'id': 3, 'product': 'Планшет', 'stars': 5},
        {'id': 4, 'product': 'Колонка', 'stars': 4},
        {'id': 4, 'product': 'Колонка', 'stars': 4},
        {'id': 5, 'product': 'Кабель', 'stars': 1},
    ]

    product_names = {}
    product_ratings = {}

    for review in reviews:
        product_id = review['id']
        product_names[product_id] = review['product'].strip().capitalize()
        if product_id not in product_ratings:
            product_ratings[product_id] = []
        product_ratings[product_id].append(review['stars'])

    average_ratings = {
        product_id: sum(ratings) / len(ratings)
        for product_id, ratings in product_ratings.items()
    }
    rated_multiple_times = [
        product_id
        for product_id, ratings in product_ratings.items()
        if len(ratings) >= 2
    ]
    worst_product_id = min(
        rated_multiple_times, key=average_ratings.get
    )
    low_rating_count = sum(
        review['stars'] in (1, 2) for review in reviews
    )
    low_rating_share = low_rating_count / len(reviews)

    print('Средняя оценка каждого товара:')
    for product_id, average in average_ratings.items():
        print(f'  {product_names[product_id]}: {average:.2f}')
    print('Худший товар с двумя и более отзывами:',
          product_names[worst_product_id])
    print('Количество отзывов на 1 или 2 звезды:', low_rating_count)
    print(f'Доля низких оценок: {low_rating_share:.2%}')


if __name__ == '__main__':
    main()
