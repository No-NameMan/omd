"""Task 3: summarize delivered and returned orders."""


def main():
    orders = [
        {'id': 1, 'buyer': 'anya', 'status': 'delivered', 'amount': 900},
        {'id': 2, 'buyer': 'boris', 'status': 'returned', 'amount': 4_500},
        {'id': 3, 'buyer': 'anya', 'status': 'delivered', 'amount': 1_500},
        {'id': 4, 'buyer': 'vera', 'status': 'delivered', 'amount': 3_200},
        {'id': 5, 'buyer': 'boris', 'status': 'delivered', 'amount': 700},
        {'id': 6, 'buyer': 'gleb', 'status': 'returned', 'amount': 2_100},
    ]

    returned_orders = [
        order for order in orders if order['status'] == 'returned'
    ]
    delivered_orders = [
        order for order in orders if order['status'] == 'delivered'
    ]

    returned_amount = sum(order['amount'] for order in returned_orders)
    buyers_with_returns = {order['buyer'] for order in returned_orders}
    delivered_count = len(delivered_orders)
    average_delivered_amount = (
        sum(order['amount'] for order in delivered_orders) / delivered_count
    )

    print('Сумма возвратов:', returned_amount)
    print('Покупатели с возвратами:', sorted(buyers_with_returns))
    print('Количество доставленных заказов:', delivered_count)
    print(f'Средний чек доставленных заказов: {average_delivered_amount:.2f}')


if __name__ == '__main__':
    main()
