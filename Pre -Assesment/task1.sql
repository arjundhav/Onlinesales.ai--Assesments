-- Our database name is company which has data imported from worksheet 1 & worksheet 2
use company;

SELECT D.NAME, AVG(S.SALARY) AS avg_salary
FROM employees E
LEFT JOIN departments D on D.ID = E.DEPT_ID
LEFT JOIN salaries S on S.EMP_ID = E.ID
GROUP BY D.NAME
ORDER BY avg_salary DESC
LIMIT 3;