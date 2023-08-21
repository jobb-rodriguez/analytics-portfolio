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

Example:
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


> Text that is a quote

> [!NOTE]
> Highlights information that users should take into account, even when skimming.

> [!IMPORTANT]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.