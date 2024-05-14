#Source: https://stackoverflow.com/questions/75889310/attributeerror-testorders-object-has-no-attribute-token
from API_project.Requests.api_clients import *
import unittest

class TestOrders(unittest.TestCase):   

    def setup_method(self):
        self.token = get_token()

    def test_add_order_book_out_of_stock(self):
        response = add_order(self.token, 2, '100 years in prison - fiction')
        assert response.status_code == 404, 'Status code is not correct'
        assert response.json()['error'] == 'This book is not in stock. Try again later.'

    def test_add_valid_order(self):
        response = add_order(self.token, 1, '1% rule')
        assert response.status_code == 201, 'Status code is not correct'
        assert response.json()['created'] is True, 'Order not created'
        # cleanup
        delete_order(self.token, response.json()['orderId'])