1.Basic Data Retrieval & Filtering
    --How do you retrieve all records from a table named Employees?
        select * from Employees;
    --Write a query to find all students whose first name starts with the letter 'K'.
        select * from students where first_name like 'K%';
    --How do you select only unique values from a column named City in a Customers table?
        select distinct named_city from customers;
    --Write a SQL statement to retrieve the top 5 highest-priced products from a Products table.
        select * from products product_price desc limit 5;
    --How do you filter records where a specific column's value is between 10 and 50?
        select * from abc where age between 10 to 50;
    --Write a query to find records where the Email column is NULL. 
        select * from employees where email is null;
2. Joins & Data Relationships
--What is the difference between an INNER JOIN and a LEFT JOIN?
--Write a query to join an Orders table with a Customers table on CustomerID.
    select a.* from customer a join Order b on a.CustomerID=b.CustomerID;
How would you perform a SELF JOIN to find employees and their respective managers in the same table?
Explain the result of a CROSS JOIN between two tables.
How do you handle NULL values when performing a join? 
3. Aggregation & Grouping
How do you find the total number of rows in a table?
Write a query to calculate the average salary of employees grouped by their department.
What is the difference between the WHERE clause and the HAVING clause?
Write a query to find departments that have more than 10 employees.
How do you find the maximum and minimum values in a specific numeric column? 
4. Intermediate Coding Challenges
Write a SQL query to find the second highest salary from an Employees table.
How do you find duplicate records in a table based on a specific column?
Write a query to delete all duplicate rows while keeping only one unique entry.
How would you select the last 10 records inserted into a table?
Explain the difference between UNION and UNION ALL. 
5. Advanced Concepts & Optimization
What is a Common Table Expression (CTE) and how is it used?
Explain the difference between RANK(), DENSE_RANK(), and ROW_NUMBER().
How do you write a Recursive CTE to traverse hierarchical data?
What is an index, and how does a Clustered Index differ from a Non-Clustered Index?
How would you optimize a slow-running query that involves multiple joins and large datasets?
What is a Stored Procedure, and how does it differ from a User-Defined Function? 
6. Database Design & DDL
What is the difference between DELETE, TRUNCATE, and DROP?
How do you create a new table with a Primary Key and a Foreign Key?
Explain the concept of Database Normalization (1NF, 2NF, 3NF).
What are the ACID properties of a database transaction?
How do you add a new column to an existing table using the ALTER command? 



--How do you find the nth highest value in a column of a table?
Q2. Highest Paid Employee(s) per Department

'''Return all employees who earn the maximum salary in their department.'''
select emp_id,emp_name,salary, rank() over(order by salary desc) as flag from employee qualify flag=1;


with cte1 as(
    select distinct dept_name,salary, rank() over(partition by dept_name order by salary desc) as flag from employee qualify flag=1
)
select a.* from employee a join cte1 b on a.dept_name=b.dept_name and a.salary=b.salary;


Q1. Nth Highest Salary per Department

'''Find the 2nd highest salary in each department.
If a department has less than 2 employees, exclude it.'''

select emp_id,emp_name,dept_name,salary, rank() over(partition by dept_name order by salary desc) as flag from employee qualify flag=2;



Q3. Employees Earning More Than Department Average

'''List employees whose salary is greater than the average salary of their department.

Concepts: AVG() OVER(), filtering on window results'''

with avg_emp as(
    select distinct dept_name,avg(salary) over(partition by dept_name) as avg_sal from employee
)
select a.* from employee a join avg_emp b on a.dept_name=b.dept_name and salary> avg_sal
;