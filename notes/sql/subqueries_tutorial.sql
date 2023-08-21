/*

Today's Topic: Subqueries (in the SELECT, FROM, and Where Statement)

*/

SELECT EmployeeID, JobTitle, Salary
FROM EmployeeSalary

-- Subquery in SELECT

SELECT EmployeeID, Salary, (SELECT AVG(Salary) FROM EmployeeSalary) AS AllAvgSalary
FROM EmployeeSalary

-- How to do it with Partition By
SELECT EmployeeID, Salary, AVG(Salary) OVER () AS AllAvgSalary
FROM EmployeeSalary

-- Why GROUP BY doesn't work
SELECT EmployeeID, Salary, AVG(Salary) AS AllAvgSalary
FROM EmployeeSalary
GROUP BY EmployeeID, Salary
ORDER BY EmployeeID


-- Subquery in FROM

SELECT a.EmployeeID, AllAvgSalary
FROM 
	(SELECT EmployeeID, Salary, AVG(Salary) OVER () AS AllAvgSalary
	 FROM EmployeeSalary) a
Order by a.EmployeeID


-- Subquery in Where


SELECT EmployeeID, JobTitle, Salary
FROM EmployeeSalary
where EmployeeID in (
	SELECT EmployeeID 
	FROM EmployeeDemographics
	where Age > 30)