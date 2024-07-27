import unittest
import pandas as pd
from app.orders_analysis import compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, get_top_customers

#import unittest module for writing and running tests
#import pandas library
#Import functions from orders_analysis.py for the test

class TestOrdersAnalysis(unittest.TestCase): #A test class that contains the test methods
    def setUp(self):
        data = { #dictionary conatining sample data for testing. Includes the required columns
            'order_id': [1, 2, 3],
            'customer_id': [101, 102, 101],
            'order_date': ['2023-01-01', '2023-01-02', '2023-02-01'],
            'product_id': [1001, 1002, 1001],
            'product_name': ['Product A', 'Product B', 'Product A'],
            'product_price': [10.0, 20.0, 10.0],
            'quantity': [1, 2, 3]
        }
        self.orders = pd.DataFrame(data) #Create a pandas DataFrame from the dictionary and assign to orders
        self.orders['order_date'] = pd.to_datetime(self.orders['order_date']) #Create to datetime format
        self.orders['total_revenue'] = self.orders['product_price'] * self.orders['quantity'] #Computes total revenue for each order and store in a new column

    def test_compute_monthly_revenue(self): #test method for monthly revenue
        result = compute_monthly_revenue(self.orders) #Calculate using the compute_monthly_revenue method
        expected = pd.DataFrame({
            'Month': pd.to_datetime(['2023-01', '2023-02']).to_period('M'), 'Total Revenue': [50.0, 30.0]
        }) #Create DataFrame with expected result for the monthly revenue
        pd.testing.assert_frame_equal(result, expected) #Assert that the result from the function matches expected DataFrame

#Similarly for product revenue
    def test_compute_product_revenue(self):
        result = compute_product_revenue(self.orders)
        expected = pd.DataFrame({'Product ID': [1001, 1002], 'Total Revenue': [40.0, 40.0]})
        pd.testing.assert_frame_equal(result, expected)

#Similarly for customer revenue
    def test_compute_customer_revenue(self):
        result = compute_customer_revenue(self.orders)
        expected = pd.DataFrame({'Customer ID': [101, 102], 'Total Revenue': [40.0, 40.0]})
        pd.testing.assert_frame_equal(result, expected)

#Similarly for customer revenue
    def test_get_top_customers(self):
        result = get_top_customers(self.orders, top_n=2) #To get the top 2 customers by revenue
        expected = pd.DataFrame({'Customer ID': [101, 102], 'Total Revenue': [40.0, 40.0]})
        pd.testing.assert_frame_equal(result, expected)

#Main script for running the tests
if __name__ == '__main__':
    unittest.main() #Run all the test methods defined in the class
