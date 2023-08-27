# Setting up the Data into PostgreSQL

## Covid Deaths
1. I created a ```CovidDeaths``` table in PostgreSQL.
2. I created a [CSV file](/datasets/covid_deaths.csv) from the [Excel file](/datasets/covid_deaths.xlsx).

> [!NOTE]
When importing the CSV into PostgreSQL, I encountered a date format error. So, I transformed the date from ```mm/dd/yyyy``` into ```yyyy-mm-dd```.

3. I imported the data into PostgreSQL.

## Covid Vaccinations