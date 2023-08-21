I'm using __PostgreSQL__ in implementing the solutions.

# Basics

## Creating a Table
General Idea:
```sql
CREATE TABLE table_name
(
    first_column type,
    ...,
    last_column type
)
```

Examples:
```sql
CREATE TABLE EmployeeDemographics
(EmployeeID int,
FirstName varchar(50),
LastName varchar(50),
Age int,
Gender varchar(50)
)
```

> [!NOTE]
> You can read about data types in PostgreSQL [here](https://www.postgresql.org/docs/current/datatype.html).

## Inserting Data
General Idea:
```sql
INSERT INTO table_name VALUES
(field1, field2, field3),
...
(field1, field2, field3)
```

```sql
INSERT INTO EmployeeSalary VALUES
(1001, 'Salesman', 45000),
(1002, 'Receptionist', 36000),
(1003, 'Salesman', 63000),
```

> [!NOTE]
> You can also view the [related SQL File](sql/create_table_and_insert_data.sql) for more examples on Create Tables and Inserting Data.

## SELECT + FROM
Syntax:
```sql
SELECT * FROM table_name;
SELECT TOP 5 * FROM table_name;
SELECT column1, column..., columnn FROM table_name;

SELECT DISTINCT(column_name) FROM table_name;

SELECT COUNT(column_name) AS column_name from table_name;
SELECT MAX(column_name) AS column_name from table_name;
SELECT MIN(column_name) AS column_name from table_name;
SELECT AVG(column_name) AS column_name from table_name;
```

## WHERE Statement

Syntax:
```sql
SELECT * FROM table_name WHERE condition;
```

Operators: 
| Operator | Description |
| --- | --- |
| = | Equal |
| > | Greater than |
| > | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |
| <> or != | Not equal to |
| AND | Logical Operator AND |
| OR | Logical Operator OR |
| IN | Return true if a value matches any value in a list (or tuples) |
| BETWEEN | Return true if a value is between a range of values |
| LIKE | Return true if a value matches a pattern. Read more [here](https://www.postgresql.org/docs/current/functions-matching.html) |
| IS NULL | Return true if a value is null |
| NOT | Negate the result of other operators |

## Group By + Order By
Group By Syntax:
```sql
SELECT * FROM table_name GROUP BY column1, column..., columnn;
```
> [!NOTE]
> ```DISTINCT``` returns the unique values based on the defined column, while ```GROUP BY``` returns the unique values and counts them as a group based on the defined column.

Order By Syntax:
```sql
SELECT * FROM table_name ORDER BY column1 [ASC | DESC], column... [ASC | DESC], columnn [ASC | DESC];
```

Example:
```sql
SELECT Gender, COUNT(Gender) AS CountGender
FROM EmployeeDemographics
WHERE Age > 31
GROUP BY Gender
ORDER BY CountGender;
```

> [!NOTE]
> SQL uses ```ASC``` as default for ```ORDER BY```.
# Intermediate
## Inner/Outer Joins
Syntax:
```sql
SELECT * FROM table_name1
JOIN table_name2
ON table_name1.id = table_name2.id
```

Types:
1. Inner Join - A intersection B
2. Left Outer Join - A ^ A intersection B
3. Right Outer Join - B ^ A intersection B
4. Full Outer Join - A union B

> [!NOTE]
> You can access columns from both tables when using ```JOIN```.

## Unions
Syntax:
```sql
SELECT * FROM table_name1
[UNION | UNION ALL]
SELECT * FROM table_name2;
```

> [!NOTE]
> Use ```UNION``` only if the columns are the same. You can use ```UNION ALL``` to view rows with ```NULL``` values.

> [!WARNING]
> Beware of using ```UNION``` on columns with similar data types. SQL will not be able to catch errors. So, it will lead to misleading rows.

## Case Statement
Use Case Statements if certain conditions return specific values.

Example:
```sql
SELECT FirstName, LastName, Age
CASE
    When Age > 30 THEN 'Old'
    WHEN Age > 13 THEN 'Teenager'
    When Age BETWEEN 5 AND 13 THEN 'Toddler'
    ELSE 'Baby'
END AS 'Age Label'
FROM EmployeeDemographics
WHERE Age IS NOT NULL
ORDER BY Age;
```

## Having Clause
Use this after ```GROUP BY```.

Example:
```sql
SELECT JobTitle, COUNT(JobTitle)
FROM EmployeeDemographics
JOIN EmployeeSalary
ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
GROUP BY JobTitle
HAVING COUNT(JobTitle) > 1
```

The statement above returns Job Titles have more than one active personnel.

> [!NOTE]
> You can use aggregate functions with ```HAVING```. Read more about aggregate functions [here](https://www.postgresql.org/docs/9.5/functions-aggregate.html).

## Updating/Deleting Data
Update Syntax:
```sql
UPDATE table_name
SET column1 = value1, column... = value..., columnn = valuen
WHERE condition;
```

Delete Syntax:
```sql
DELETE 
FROM table_name
WHERE condition;
```

> [!WARNING]
> Deleting a record is irreversible unless you have a ```ROLLBACK```. It is not possible with ```TRUNCATE``` and ```DROP```.

> [!NOTE]
> Use ```SELECT``` before running ```DELETE``` to ensure you are deleting the correct record/s. 

## Aliasing
You can add an alias to columns and tables by adding ```AS``` after their names. This can help you identify and shoren your queries.

## Partition By
Allows you to partition a column from the table.

Example:
```sql
SELECT FirstName, LastName, Gender, Salary,
    COUNT(Gender) OVER (PARTITION BY Gender) AS TotalGender
FROM EmployeeDemographics dem
JOIN EmployeeSalary sal
ON dem.EmployeeID = sal.EmployeeID
```

# Advanced

## Common Table Expressions (CTEs)
CTE allows you to store information in a table. However, it is not a temporary table.

Syntax:
```sql
WITH custom_table_name AS
(
    QUERY
);
SELECT * FROM custom_table_name;
```

> [!NOTE]
> The ```custom_table_name``` only works one query after its declaration.

## Temp Tables
For PostgreSQL, here's the syntax:
```sql
CREATE TEMPORARY TABLE table_name(
    column_name data_type
);
```

Temporary tables are useful for not repeatedly running join queries.


> [!NOTE]
> View the [related SQL File](sql/temp_tables.sql) for more examples on Create Tables and Inserting Data. Read more about tables [here](https://www.postgresql.org/docs/current/sql-createtable.html).

> [!IMPORTANT]
> Run ```DROP TABLE IF EXISTS temp_table_name``` before creating a temporary table to avoid errors.