from random import randint, sample, uniform
from acme import Product
# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        name = (sample(ADJECTIVES) + ' ' + sample(NOUNS))
        price = randint(5, 101)
        weight = randint(5, 101)
        flammability = uniform(0, 2.5)
        products.append(Product(name=name, price=price, weight=weight,
                                flammability=flammability))
    return products


def inventory_report(products):
    unique_names = []
    total_price, total_weight, total_flammability = 0, 0, 0
    products_count = len(products)

    for product in products:
        unique_names.append(product.name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names:', len(set(unique_names)))
    print('Average price:', total_price/products_count)
    print('Average weight:', total_weight/products_count)
    print('Average flammability:', total_flammability/products_count)


if __name__ == '__main__':
    inventory_report(generate_products())