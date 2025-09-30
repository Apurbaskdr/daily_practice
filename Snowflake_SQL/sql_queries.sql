1. Find the 2nd highest salary in each department without using LIMIT or TOP.

	select * exclude(rnk) from (select 
		department, 
		salary, 
		rank() over(partition by department order by salary desc) as rnk 
	from employees
	group by 1,2) where rnk=2;


2. Rank employees by their salary within each department and select only the top 3 per department.

	select 
		* exclude(rnk) 
		from 
			(select 
				department, 
				salary, 
				rank() over(partition by department order by salary desc) as rnk 
			from employees
			group by 1,2) 
		where rnk in (1,2,3);
		

3. Get employees whose salary is greater than the department’s average salary.

	with dept_avg as(
		select 
			department
			,avg(salary) as avg_s
		from employees group by 1)
	select 
		em.*, 
		da.avg_s 
	from employees em join dept_avg da 
		on em.department=da.department
		and em.salary>da.avg_s
	order by department;