-- Alex the Analyst wrote this code for Microst Server.
-- See README.md notes for PostgreSQL.
CREATE TABLE #temp_employee2 (
EmployeeID int,
JobTitle varchar(100),
Salary int
)

SELECT * FROM #temp_employee2

INSERT INTO #temp_employee2 VALUES (
'1001', 'HR', '45000'
)

-- Insert values from another table
INSERT INTO #temp_employee2 
SELECT * FROM SQLTutorial..EmployeeSalary

Select * FROM #temp_employee2




DROP TABLE IF EXISTS #temp_employee3
CREATE TABLE #temp_employee3 (
JobTitle varchar(100),
EmployeesPerJob int ,
AvgAge int,
AvgSalary int
)

INSERT INTO #temp_employee3
SELECT JobTitle, Count(JobTitle), Avg(Age), AVG(salary)
FROM SQLTutorial..EmployeeDemographics emp
JOIN SQLTutorial..EmployeeSalary sal
	ON emp.EmployeeID = sal.EmployeeID
group by JobTitle

SELECT * 
FROM #temp_employee3

SELECT AvgAge * AvgSalary
FROM #temp_employee3