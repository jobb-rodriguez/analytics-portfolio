# Setting up the Data into PostgreSQL

## Covid Deaths
1. I created a ```CovidDeaths``` table in PostgreSQL.

> [!NOTE]
> I made sure all integer columns uses ```bigint``` to accommodate large inputs.

2. I created a [CSV file](/datasets/covid_deaths.csv) from the [Excel file](/datasets/covid_deaths.xlsx).

> [!NOTE]
> When importing the CSV into PostgreSQL, I encountered a date format error. So, I transformed the date from ```mm/dd/yyyy``` into ```yyyy-mm-dd```.

3. I imported the data into PostgreSQL.

## Covid Vaccinations
1. I created a ```CovidVaccinations``` table in PostgreSQL.

> [!NOTE]
> I made sure all integer columns uses ```bigint``` to accommodate large inputs.

2. I created a [CSV file](/datasets/covid_vaccinations.csv) from the [Excel file](/datasets/covid_vaccinations.xlsx).

> [!NOTE]
> When importing the CSV into PostgreSQL, I encountered a date format error. So, I transformed the date from ```mm/dd/yyyy``` into ```yyyy-mm-dd```.

3. I imported the data into PostgreSQL.

# Data Exploration
**Skills Used:**



## Select Data that we are going to be starting with
```sql
SELECT location, date, total_cases, new_cases, total_deaths, population
FROM "CovidDeaths"
ORDER BY 1, 2;
```

## Total Cases vs Total Deaths
The ```Death Percentage``` shows the likelihood of dying if a person contracts covid in a country.

```sql
SELECT location, date, total_cases, total_deaths, (total_deaths::float / total_cases::float) * 100 AS "Death Percentage" 
FROM "CovidDeaths"
WHERE total_cases IS NOT NULL AND total_deaths IS NOT NULL
ORDER BY 1, 2;
```
> [!NOTE]
> I added ```::float``` to make Death Rate's data type ```double precision```.

Check the Death Percentage in the United States.
```sql
SELECT location, date, total_cases, total_deaths, (total_deaths::float / total_cases::float) * 100 AS "Death Percentage" 
FROM "CovidDeaths"
WHERE location LIKE '%States'
ORDER BY 1, 2;
```

## Total Cases vs Population


## Countries with Highest Infection Rate compared to Population


## Countries with Highest Death Count per Population


## BREAKING THINGS DOWN BY CONTINENT


## GLOBAL NUMBERS


## Total Population vs Vaccinations

## Using CTE to perform Calculation on Partition By in previous query


## Using Temp Table to perform Calculation on Partition By in previous query

## Creating View to store data for later visualizations
