from decimal                                    import Decimal

from kapshop.common.rounding                     import KapsRounding


def exec_binary_search(countries, country):

    left, right = 0, len(countries) - 1

    while left <= right:

        middle = left + (right - left) // 2

        # Check if country is present at mid
        if countries[middle] == country:
            return middle

        # If country is greater, ignore left half
        elif countries[middle] < country:
            left = middle + 1

        # If country is smaller, ignore right half
        else:
            right = middle - 1

    return False


def process_discount_prices(price, discount_price):

    discount_amount = Decimal(0.00)

    if Decimal(discount_price) > 0.00:
        discount_amount = Decimal(price) - Decimal(discount_price)

    discount_amount = KapsRounding(discount_amount).round_2_places()

    return discount_amount
