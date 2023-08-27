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
1. Descriptive Staistics
2. Window Functions and Aggregate Functions
3. Type Conversion
4. Joins
5. CTE's and Temp Tables

## Select Data that we are going to be starting with
```sql
SELECT location, date, total_cases, new_cases, total_deaths, population
FROM "CovidDeaths"
WHERE continent IS NOT NULL
ORDER BY 1, 2;
```

## Total Cases vs Total Deaths
The ```Death Percentage``` shows the likelihood of dying if a person contracts covid in a country.

```sql
SELECT location, date, total_cases, total_deaths, (total_deaths::float / total_cases::float) * 100 AS "Death Percentage" 
FROM "CovidDeaths"
WHERE total_cases IS NOT NULL AND total_deaths IS NOT NULL AND continent IS NOT NULL
ORDER BY 1, 2;
```
> [!NOTE]
> I added ```::float``` to make Death Rate's data type ```double precision```.

Check the Death Percentage in the United States.
```sql
SELECT location, date, total_cases, total_deaths, (total_deaths::float / total_cases::float) * 100 AS "Death Percentage" 
FROM "CovidDeaths"
WHERE location LIKE '%States' AND total_cases IS NOT NULL AND total_deaths IS NOT NULL AND continent IS NOT NULL
ORDER BY 1, 2;
```

## Total Cases vs Population
The ```Infected Population Percentage``` shows the total Covid cases based on the country's population.

```sql
SELECT location, date, population, total_cases, (total_cases::float / population::float) * 100 AS "Infected Population Percentage" 
FROM "CovidDeaths"
WHERE total_cases IS NOT NULL AND continent IS NOT NULL
ORDER BY 1, 2;
```

## Countries with Highest Infection Rate compared to Population
```sql
SELECT location, population, MAX(total_cases) AS "Total Cases", MAX(((total_cases::float / population::float))) * 100 AS "Infected Population Percentage" 
FROM "CovidDeaths"
WHERE total_cases IS NOT NULL AND continent IS NOT NULL
GROUP BY location, population
ORDER BY "Infected Population Percentage" DESC;
```

## Countries with Highest Death Count
```sql
SELECT location, MAX(total_deaths) AS "Total Deaths"
FROM "CovidDeaths"
WHERE total_deaths IS NOT NULL AND continent IS NOT NULL
GROUP BY location, population
ORDER BY "Total Deaths" DESC;
```


## Continents with Highest Death Count
View by continents
```sql
SELECT continent, MAX(total_deaths) AS "Total Deaths"
FROM "CovidDeaths"
WHERE total_deaths IS NOT NULL AND continent IS NOT NULL
GROUP BY continent
ORDER BY "Total Deaths" DESC;
```

Get the complete list (including the continents)
```sql
SELECT location, MAX(total_deaths) AS "Total Deaths"
FROM "CovidDeaths"
WHERE total_deaths IS NOT NULL AND continent IS NULL
GROUP BY location
ORDER BY "Total Deaths" DESC;
```

## Death Percentage
```sql
SELECT SUM(new_cases) as "Total Cases", SUM(new_deaths) as "Total Deaths", SUM(new_deaths)/SUM(new_cases) * 100 AS "Death Percentage"
FROM "CovidDeaths"
WHERE continent IS NOT NULL
ORDER BY 1, 2;
```

## Death Percentage by Date
```sql
SELECT date, SUM(new_cases) as "Total Cases", SUM(new_deaths) as "Total Deaths", SUM(new_deaths)/SUM(new_cases) * 100 AS "Death Percentage"
FROM "CovidDeaths"
WHERE continent IS NOT NULL
GROUP BY date
ORDER BY 1, 2;
```

## Total Population vs Vaccinations

### Using CTE to perform Calculation on Partition By in previous query
```sql
WITH PopvsVac(Continent, Location, Date, Population, New_Vaccinations, RollingPeopleVaccinated) AS
(
SELECT death.continent, death.location, death.date, death.population, vaccine.new_vaccinations,
SUM(vaccine.new_vaccinations) OVER (PARTITION BY death.location ORDER BY death.location, death.date) AS "Rolling People Vaccinated"
FROM "CovidDeaths" death
JOIN "CovidVaccinations" vaccine
    ON death.location = vaccine.location AND death.date = vaccine.date
WHERE death.continent IS NOT NULL
ORDER BY 2, 3
)

SELECT *, (RollingPeopleVaccinated / Population) * 100 AS "Rolling Vaccination Percentage"
FROM PopvsVac;
```

## Using Temp Table to perform Calculation on Partition By in previous query
```sql
DROP TABLE IF EXISTS PopvsVac;

CREATE TEMPORARY TABLE PopvsVac(
    continent text,
    location text,
    date date,
    population bigint,
    new_vaccinations bigint,
    rolling_people_vaccinated real
);

INSERT INTO PopvsVac
SELECT death.continent, death.location, death.date, death.population, vaccine.new_vaccinations,
SUM(vaccine.new_vaccinations) OVER (PARTITION BY death.location ORDER BY death.location, death.date) AS "Rolling People Vaccinated"
FROM "CovidDeaths" death
JOIN "CovidVaccinations" vaccine
    ON death.location = vaccine.location AND death.date = vaccine.date
WHERE death.continent IS NOT NULL
ORDER BY 2, 3
;

SELECT *, (rolling_people_vaccinated / population) * 100 AS "Rolling Vaccination Percentage"
FROM PopvsVac;
```

## Creating View to store data for later visualizations
```sql
CREATE VIEW PercentPopulationVaccinated AS
SELECT death.continent, death.location, death.date, death.population, vaccine.new_vaccinations,
SUM(vaccine.new_vaccinations) OVER (PARTITION BY death.location ORDER BY death.location, death.date) AS "Rolling People Vaccinated"
FROM "CovidDeaths" death
JOIN "CovidVaccinations" vaccine
    ON death.location = vaccine.location AND death.date = vaccine.date
WHERE death.continent IS NOT NULL;

SELECT * FROM PercentPopulationVaccinated;
```

> [!NOTE]
> A view is the result set of a stored query.