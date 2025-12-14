create warehouse my_first_project;
create database raw_db;
create database analytics;
create schema first_schema;
drop schema first_schema;
create schema raw_db.raw_first_schema;
create schema analytics.first_schema;


CREATE TABLE department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    location VARCHAR(50)
);


INSERT INTO department (dept_id, dept_name, location) VALUES
(10, 'HR', 'Kolkata'),
(20, 'IT', 'Hyderabad'),
(30, 'Finance', 'Chennai');


CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_name VARCHAR(50),
    manager_id INT,
    salary INT,
    hire_date DATE
);



INSERT INTO employee VALUES
(1, 'Amit', 'IT', NULL, 120000, '2018-01-10'),
(2, 'Neha', 'IT', 1, 90000, '2019-03-15'),
(3, 'Rahul', 'HR', 5, 70000, '2020-07-20'),
(4, 'Sneha', 'HR', 5, 75000, '2019-11-01'),
(5, 'Vikram', 'HR', NULL, 150000, '2017-05-05'),
(6, 'Kiran', 'Finance', 7, 80000, '2021-02-12'),
(7, 'Pooja', 'Finance', NULL, 140000, '2016-09-25');



CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50)
);


INSERT INTO customer VALUES
(1, 'Rahul', 'Bangalore'),
(2, 'Sneha', 'Mumbai'),
(3, 'Amit', 'Delhi');


CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);


INSERT INTO orders VALUES
(1001, 1, '2024-01-10', 15000),
(1002, 2, '2024-01-15', 22000),
(1003, 1, '2024-02-01', 18000),
(1004, 3, '2024-02-05', 12000);


CREATE TABLE attendance (
    emp_id INT,
    attendance_date DATE,
    status VARCHAR(10),
    PRIMARY KEY (emp_id, attendance_date)
);


INSERT INTO attendance VALUES
(101, '2024-12-01', 'Present'),
(101, '2024-12-02', 'Absent'),
(102, '2024-12-01', 'Present'),
(103, '2024-12-01', 'Present');


CREATE TABLE product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(30),
    price DECIMAL(8,2)
);


INSERT INTO product VALUES
(1, 'Laptop', 'Electronics', 65000),
(2, 'Mobile', 'Electronics', 25000),
(3, 'Chair', 'Furniture', 5000);


CREATE TABLE emp_dept (
    emp_id INT,
    dept_id INT
);


INSERT INTO emp_dept VALUES
(1, 10),
(2, 10),
(3, 20),
(4, 20),
(5, 20),
(6, 30),
(7, 30);


CREATE TABLE salary_history (
    emp_id INT,
    salary INT,
    effective_date DATE
);


INSERT INTO salary_history VALUES
(1, 90000, '2018-01-10'),
(1, 110000, '2020-01-01'),
(1, 120000, '2022-01-01'),
(2, 70000, '2019-03-15'),
(2, 90000, '2021-04-01'),
(3, 60000, '2020-07-20'),
(3, 70000, '2022-08-01');


CREATE TABLE login_activity (
    user_id INT,
    login_date DATE
);


INSERT INTO login_activity VALUES
(1, '2024-01-01'),
(1, '2024-01-02'),
(1, '2024-01-03'),
(2, '2024-01-01'),
(2, '2024-01-03'),
(3, '2024-01-01'),
(3, '2024-01-02');




