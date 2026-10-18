"""Task 1: compare product availability across two warehouses."""


def main():
    moscow = {201, 202, 203, 204}
    kazan = {203, 204, 205, 206}

    available_in_both = moscow & kazan
    moscow_only = moscow - kazan
    kazan_only = kazan - moscow
    distinct_products = len(moscow | kazan)

    print('Товары в обоих городах:', sorted(available_in_both))
    print('Товары только в Москве:', sorted(moscow_only))
    print('Товары только в Казани:', sorted(kazan_only))
    print('Всего разных товаров:', distinct_products)


if __name__ == '__main__':
    main()
