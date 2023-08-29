SELECT location, date, total_cases, new_cases, total_deaths, population
FROM "CovidDeaths"
WHERE continent IS NOT NULL
ORDER BY 1, 2;

SELECT location, date, total_cases, total_deaths, (total_deaths::float / total_cases::float) * 100 AS "Death Percentage" 
FROM "CovidDeaths"
WHERE total_cases IS NOT NULL AND total_deaths IS NOT NULL AND continent IS NOT NULL
ORDER BY 1, 2;

SELECT location, date, total_cases, total_deaths, (total_deaths::float / total_cases::float) * 100 AS "Death Percentage" 
FROM "CovidDeaths"
WHERE location LIKE '%States' AND total_cases IS NOT NULL AND total_deaths IS NOT NULL AND continent IS NOT NULL
ORDER BY 1, 2;

SELECT location, date, population, total_cases, (total_cases::float / population::float) * 100 AS "Infected Population Percentage" 
FROM "CovidDeaths"
WHERE total_cases IS NOT NULL AND continent IS NOT NULL
ORDER BY 1, 2;

SELECT location, population, MAX(total_cases) AS "Total Cases", MAX(((total_cases::float / population::float))) * 100 AS "Infected Population Percentage" 
FROM "CovidDeaths"
WHERE total_cases IS NOT NULL AND continent IS NOT NULL
GROUP BY location, population
ORDER BY "Infected Population Percentage" DESC;

SELECT location, MAX(total_deaths) AS "Total Deaths"
FROM "CovidDeaths"
WHERE total_deaths IS NOT NULL AND continent IS NOT NULL
GROUP BY location, population
ORDER BY "Total Deaths" DESC;

SELECT continent, MAX(total_deaths) AS "Total Deaths"
FROM "CovidDeaths"
WHERE total_deaths IS NOT NULL AND continent IS NOT NULL
GROUP BY continent
ORDER BY "Total Deaths" DESC;

SELECT location, MAX(total_deaths) AS "Total Deaths"
FROM "CovidDeaths"
WHERE total_deaths IS NOT NULL AND continent IS NULL
GROUP BY location
ORDER BY "Total Deaths" DESC;

SELECT SUM(new_cases) as "Total Cases", SUM(new_deaths) as "Total Deaths", SUM(new_deaths)/SUM(new_cases) * 100 AS "Death Percentage"
FROM "CovidDeaths"
WHERE continent IS NOT NULL
ORDER BY 1, 2;

SELECT date, SUM(new_cases) as "Total Cases", SUM(new_deaths) as "Total Deaths", SUM(new_deaths)/SUM(new_cases) * 100 AS "Death Percentage"
FROM "CovidDeaths"
WHERE continent IS NOT NULL
GROUP BY date
ORDER BY 1, 2;

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

CREATE VIEW PercentPopulationVaccinated AS
SELECT death.continent, death.location, death.date, death.population, vaccine.new_vaccinations,
SUM(vaccine.new_vaccinations) OVER (PARTITION BY death.location ORDER BY death.location, death.date) AS "Rolling People Vaccinated"
FROM "CovidDeaths" death
JOIN "CovidVaccinations" vaccine
    ON death.location = vaccine.location AND death.date = vaccine.date
WHERE death.continent IS NOT NULL;

SELECT * FROM PercentPopulationVaccinated;