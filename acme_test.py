import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):

    def test_default_product_price(self):
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)


class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        products = generate_products()

        for product in products:
            adjective = product.name.split()[0]
            noun = product.name.split()[1]
            self.assertIn(adjective, ADJECTIVES)
            self.assertIn(noun, NOUNS)

if __name__ == '__main__':
    unittest.main()