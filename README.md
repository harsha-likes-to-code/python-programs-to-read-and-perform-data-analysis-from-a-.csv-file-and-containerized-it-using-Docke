# (Please refer master branch for code)


# Online Store Revenue Analysis

## Problem Statement

You have been given a dataset of customer orders from an online store. The data is in a CSV file `orders.csv` with the following columns:
- `order_id`: unique identifier for each order
- `customer_id`: unique identifier for each customer
- `order_date`: date when the order was placed
- `product_id`: unique identifier for each product
- `product_name`: name of the product
- `product_price`: price of the product
- `quantity`: quantity of the product ordered

Your task is to write a Python program that reads the data from the CSV file and performs the following tasks:
1. Compute the total revenue generated by the online store for each month in the dataset.
2. Compute the total revenue generated by each product in the dataset.
3. Compute the total revenue generated by each customer in the dataset.
4. Identify the top 10 customers by revenue generated.

## Instructions

1. **Write a Python Program**: Create a Python program that reads the data from the `orders.csv` file and performs the tasks outlined above.
2. **Write Tests**: Implement tests to ensure your code works correctly.
3. **Commit Changes**: Commit your changes to your branch.
4. **Dockerize Your Application**: Create two separate services:
   - One for the main task.
   - One for running the tests.


## Structure and Architecture

1. app/
This directory contains the main application code.

`orders_analysis.py`: The Python script that performs the data analysis tasks.

`requirements.txt`: Lists the Python dependencies required for the application.

`Dockerfile`: Dockerfile to containerize the main application.

`orders.csv`: The CSV file containing the customer orders data.

3. Testing/
This directory contains the test code.

`test_orders_analysis.py`: The Python script containing the test cases for the application.

`requirements.txt`: Lists the Python dependencies required for running the tests.

`Dockerfile`: Dockerfile to containerize the test environment.

3. docker-compose.yml
This file defines the services for Docker Compose to manage the application and test environments.

## DOCKERIZING STEPS:
1. In the app/Dockerfile write the code with appropriate directories to copy the files into a docker file.
2. Similarly, do the same for the Testing/Dockerfile
3. Now, write the docker-compose.yml to define and manage multicontainer docker applications
4. Detailed explanations are given as comments in the Docker files and the  docker-compose.yml file.

After these files have been made, we can proceed to test our orders_analysis.py using the test suite using the terminal:

1. Build and Run the Task Service:
'docker-compose up --build app'
This command will build the Docker image for the application and run the orders_analysis.py script.

2. Build and Run the Testing Service:
'docker-compose up --build test'
This command will build the Docker image for the Testing and run the test_orders_analysis.py script.

3. Build and Run the Test Service:
'docker-compose run --rm test'
This command will build the Docker image for testing and run the tests defined in 'test_orders_analysis.py'.

