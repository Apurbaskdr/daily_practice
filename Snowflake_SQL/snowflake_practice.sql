create table my_table (id number(38,0));

select * from my_table;

SELECT CURRENT_ACCOUNT(), CURRENT_REGION(), current_role();

SELECT CURRENT_ORGANIZATION_NAME() || '-' || CURRENT_ACCOUNT_NAME() AS org_account;


show databases;

show users;

show warehouses;

show schemas;

select current_account(), current_region();

SELECT CURRENT_USER();


show parameters like 'account_locator';



CREATE TABLE Employees (
    emp_id         INT PRIMARY KEY,
    first_name     VARCHAR(50),
    last_name      VARCHAR(50),
    department     VARCHAR(50),
    salary         DECIMAL(10,2),
    hire_date      DATE,
    manager_id     INT NULL
);


INSERT INTO Employees (emp_id, first_name, last_name, department, salary, hire_date, manager_id) VALUES
(101, 'Amit',       'Sharma',    'IT',           75000.00, '2018-03-12', NULL),
(102, 'Neha',       'Patel',     'Finance',      68000.00, '2019-07-15', NULL),
(103, 'Rahul',      'Verma',     'HR',           62000.00, '2020-01-10', NULL),
(104, 'Sneha',      'Iyer',      'IT',           55000.00, '2021-05-21', 101),
(105, 'Vikram',     'Singh',     'Sales',        58000.00, '2022-02-14', 108),
(106, 'Priya',      'Menon',     'Finance',      49000.00, '2021-08-05', 102),
(107, 'Karan',      'Bhatia',    'Marketing',    45000.00, '2023-01-12', 110),
(108, 'Meera',      'Ghosh',     'Sales',        82000.00, '2017-11-30', NULL),
(109, 'Arjun',      'Rao',       'IT',           60000.00, '2022-09-18', 101),
(110, 'Pooja',      'Nair',      'Marketing',    70000.00, '2018-06-01', NULL),
(111, 'Ravi',       'Kumar',     'IT',           56000.00, '2020-10-25', 101),
(112, 'Anita',      'Das',       'Finance',      72000.00, '2018-12-17', 102),
(113, 'Deepak',     'Gupta',     'Sales',        54000.00, '2021-03-09', 108),
(114, 'Shweta',     'Banerjee',  'HR',           64000.00, '2019-09-23', 103),
(115, 'Sanjay',     'Mishra',    'Marketing',    47000.00, '2023-06-15', 110),
(116, 'Ritika',     'Chopra',    'IT',           59000.00, '2021-01-30', 101),
(117, 'Gaurav',     'Tiwari',    'Finance',      53000.00, '2022-07-05', 102),
(118, 'Kavita',     'Joshi',     'Sales',        61000.00, '2020-04-18', 108),
(119, 'Manish',     'Pillai',    'IT',           52000.00, '2023-03-25', 101),
(120, 'Aisha',      'Sheikh',    'HR',           58000.00, '2022-11-11', 103);



select * from employees;


select department, salary from employees order by 1,2;

select * exclude(rnk) from (select 
    department, 
    salary, 
    rank() over(partition by department order by salary desc) as rnk 
from employees
group by 1,2) where rnk in (1,2,3);


with dept_avg as(
select 
    department
    ,avg(salary) as avg_s
from employees group by 1)
select em.*, da.avg_s from employees em join dept_avg da on em.department=da.department
and em.salary>da.avg_s
order by department;

CREATE TABLE Customers (
    customer_id     INT PRIMARY KEY,
    first_name      VARCHAR(50),
    last_name       VARCHAR(50),
    email           VARCHAR(100),
    city            VARCHAR(50),
    purchase_amount DECIMAL(10,2),
    purchase_date   DATE
);


INSERT INTO Customers (customer_id, first_name, last_name, email, city, purchase_amount, purchase_date) VALUES
(1,  'Rohit',   'Sharma',   'rohit.sharma@example.com',   'Mumbai',     1500.00, '2023-01-15'),
(2,  'Sneha',   'Patel',    'sneha.patel@example.com',    'Delhi',      3200.50, '2023-03-10'),
(3,  'Amit',    'Verma',    'amit.verma@example.com',     'Bangalore',  2750.75, '2023-05-22'),
(4,  'Pooja',   'Iyer',     'pooja.iyer@example.com',     'Pune',       1800.00, '2023-07-09'),
(5,  'Vikram',  'Singh',    'vikram.singh@example.com',   'Chennai',    4500.00, '2023-08-30'),
(6,  'Neha',    'Ghosh',    'neha.ghosh@example.com',     'Kolkata',    2200.00, '2023-09-12'),
(7,  'Karan',   'Rao',      'karan.rao@example.com',      'Mumbai',     3900.00, '2024-01-03'),
(8,  'Meera',   'Menon',    'meera.menon@example.com',    'Hyderabad',  3100.00, '2024-02-18'),
(9,  'Arjun',   'Nair',     'arjun.nair@example.com',     'Delhi',      2600.00, '2024-03-27'),
(10, 'Anita',   'Bhatia',   'anita.bhatia@example.com',   'Pune',       1400.00, '2024-04-15'),
(11, 'Ravi',    'Kumar',    'ravi.kumar@example.com',     'Mumbai',     5100.00, '2024-05-20'),
(12, 'Shweta',  'Das',      'shweta.das@example.com',     'Kolkata',    1950.00, '2024-07-02'),
(13, 'Gaurav',  'Mishra',   'gaurav.mishra@example.com',  'Bangalore',  3300.00, '2024-08-09'),
(14, 'Kavita',  'Joshi',    'kavita.joshi@example.com',   'Chennai',    2800.00, '2024-09-16'),
(15, 'Deepak',  'Chopra',   'deepak.chopra@example.com',  'Hyderabad',  1700.00, '2024-10-21'),
(16, 'Ritika',  'Banerjee', 'ritika.banerjee@example.com','Delhi',      4400.00, '2025-01-11'),
(17, 'Sanjay',  'Tiwari',   'sanjay.tiwari@example.com',  'Pune',       1200.00, '2025-02-07'),
(18, 'Aisha',   'Sheikh',   'aisha.sheikh@example.com',   'Kolkata',    2950.00, '2025-04-13'),
(19, 'Manish',  'Pillai',   'manish.pillai@example.com',  'Bangalore',  3750.00, '2025-06-29'),
(20, 'Priya',   'Reddy',    'priya.reddy@example.com',    'Mumbai',     4100.00, '2025-08-22');




select * from information_schema.tables;


select * from CUSTOMERS;

select get_ddl('table','CUSTOMERS');


create or replace TABLE RAW_CUSTOMERS (
	CUSTOMER_ID NUMBER(38,0) NOT NULL,
	FIRST_NAME VARCHAR(50),
	LAST_NAME VARCHAR(50),
	EMAIL VARCHAR(100),
	CITY VARCHAR(50),
	PURCHASE_AMOUNT NUMBER(10,2),
	PURCHASE_DATE DATE,
	primary key (CUSTOMER_ID)
);


select * from customers;



create or replace stage customer_stage
file_format=(type='CSV', field_optionally_enclosed_by='"', skip_header=1);


truncate table customers;

select * from customers;

SELECT CURRENT_ACCOUNT();  --MA90931
SELECT CURRENT_REGION();  --AWS_AP_SOUTHEAST_1
SELECT CURRENT_USER(); --APURBASKDR6

MA90931.AWS_AP_SOUTHEAST_1

select * from CUSTOMER_RAW;



put file://D:\Practice\Files\customer_data.csv @customer_stage;

CREATE or replace pipe customer_pipe
auto_ingest= TRUE
as
copy into raw_customers
from @customer_stage
file_format=(type='CSV' field_optionally_enclosed_by='"' skip_header=1) on_error='continue';

create or replace table CUSTOMER_LOAD_LOG (
    LOG_TIMESTAMP TIMESTAMP_NTZ,
    STATUS        STRING,
    ERROR_MESSAGE STRING
);

select * from customers;

select get_ddl('table','customers');


create or replace procedure customer_sp()
returns STRING
language sql
execute as owner
as
$$
declare
    v_rows_count number :=0;
begin
    merge into customers t
        using(
            select distinct CUSTOMER_ID,FIRST_NAME,LAST_NAME,EMAIL,CITY,PURCHASE_AMOUNT,PURCHASE_DATE from raw_customers
        ) s on t.customer_id = s.customer_id
        when matched then
            update set
                t.first_name=s.first_name,
                t.last_name=s.last_name,
                t.email=s.email,
                t.city=s.city,
                t.purchase_amount=s.purchase_amount,
                t.purchase_date=s.purchase_date
        when not matched then
            insert (CUSTOMER_ID,FIRST_NAME,LAST_NAME,EMAIL,CITY,PURCHASE_AMOUNT,PURCHASE_DATE)
            values (s.CUSTOMER_ID,s.FIRST_NAME,s.LAST_NAME,s.EMAIL,CITY,s.PURCHASE_AMOUNT,s.PURCHASE_DATE);

    v_rows_count := SQLROWCOUNT;
    insert into customer_load_log (LOG_TIMESTAMP, STATUS, ERROR_MESSAGE) values (current_timestamp(), 'SUCCESS -' || :v_rows_merged || ' rows merged', NULL);

    return 'Upsert completed successfully: '|| v_rows_merged ||' rows merged';

exception
    when other then
        insert into CUSTOMER_LOAD_LOG (LOG_TIMESTAMP, STATUS, ERROR_MESSAGE) values (current_timestamp(), 'FAILED', :SQLERRM);
        return 'Failed ' || SQLERRM;

end;
$$ 
        
