
-- table with fields :

        -- id name dept salary 

        -- give highest salary id name for each department


SELECT dept,id,name,salary  
FROM employees
WHERE (dept,salary) IN (
    SELECT department,MAX(salary)
    from employees
    Group by dept
);