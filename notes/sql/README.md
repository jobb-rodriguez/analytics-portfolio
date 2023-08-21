# SQL

## Introduction
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


> Text that is a quote

> [!NOTE]
> Highlights information that users should take into account, even when skimming.

> [!IMPORTANT]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.