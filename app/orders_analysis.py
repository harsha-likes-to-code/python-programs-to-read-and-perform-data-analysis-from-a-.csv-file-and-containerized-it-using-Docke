import pandas as pd

#for monthly revenue
def compute_monthly_revenue(orders):
    orders['order_date'] = pd.to_datetime(orders['order_date']) #converts to datetime format
    orders['total_revenue'] = orders['product_price'] * orders['quantity'] #Total revenue for each order
    monthly_revenue = orders.groupby(orders['order_date'].dt.to_period('M'))['total_revenue'].sum().reset_index()#Total sum of revenue grouped by months
    monthly_revenue.columns = ['Month', 'Total Revenue'] #Rename column for clarity
    return monthly_revenue

#For product revenue
def compute_product_revenue(orders):
    orders['total_revenue'] = orders['product_price'] * orders['quantity']#Calculate total revenue for each order
    product_revenue = orders.groupby('product_id')['total_revenue'].sum().reset_index() #Group by the data by productid and sum all the total revenue for each product
    product_revenue.columns = ['Product ID', 'Total Revenue'] #Rename for clarity
    return product_revenue

#For customer revenue
def compute_customer_revenue(orders):
    orders['total_revenue'] = orders['product_price'] * orders['quantity'] #Calculate total revenue for each order
    customer_revenue = orders.groupby('customer_id')['total_revenue'].sum().reset_index() #Sum of the total revenue after grouping by customer_id
    customer_revenue.columns = ['Customer ID', 'Total Revenue'] #Rename columns for clarity
    return customer_revenue

#For top customers
def get_top_customers(orders, top_n=10): #For the top customers, default is 10
    customer_revenue = compute_customer_revenue(orders) #Calculate total revenue
    top_customers = customer_revenue.sort_values(by='Total Revenue', ascending=False).head(top_n) #Sort the custumers by the total revenue in descending order to select top 'n' customers
    return top_customers #Return top customers DataFrame

#Main script
if __name__ == "__main__":
    orders = pd.read_csv('orders.csv') #read csv file orders.csv into a DataFrame called 'orders'

    print("Monthly Revenue:")
    print(compute_monthly_revenue(orders)) #Print computed monthly revenue

    print("\nProduct Revenue:")
    print(compute_product_revenue(orders))#Print computed product revenue

    print("\nCustomer Revenue:")
    print(compute_customer_revenue(orders))#Print computed customer revenue

    print("\nTop 10 Customers:")
    print(get_top_customers(orders)) #print the top 10 customers




