# SQL

## Basics
I'm using __PostgreSQL__ in implementing the solutions.

### Creating a Table
General Idea:
```sql
CREATE TABLE table_name
(
    first_field type,
    ...,
    last_field type
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

### Inserting Data
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

### Select + From
Syntax:
```sql
SELECT * FROM table_name;
SELECT TOP 5 * FROM table_name;
SELECT field1, field..., fieldn FROM table_name;

SELECT DISTINCT(field_name) FROM table_name;

SELECT COUNT(field_name) AS column_name from table_name;
SELECT MAX(field_name) AS column_name from table_name;
SELECT MIN(field_name) AS column_name from table_name;
SELECT AVG(field_name) AS column_name from table_name;
```

## Intermediate


## Advanced