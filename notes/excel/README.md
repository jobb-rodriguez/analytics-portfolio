# Pivot Tables
Pivot Tables allow you to utilize the data in your columns into four different areas:
1. Filters
2. Columns
3. Rows
4. Values

> You can view [this file](excel/pivot_tables.xlsx) for an example. The European Bike Sale Dataset from Kaggle was used in the file. You can access the dataset [here](https://www.kaggle.com/code/sadiqshah/bike-store-sales-in-europe/input).

> [!NOTE]
> Pivot Tables save time in grouping the data for analysis and charting.

> [!IMPORTANT]
> Make sure the is clean before using Pivot Tables.

# Formulas in Excel
| Formula | Description | Sample Use Case |
| --- | --- | --- |
| ```MAX(Numbers or Range)``` | Return the maximum value in a given range | Measures of Central Tendency |
| ```MIN(Numbers or Range)``` | Return the minimum value in a given range | Measures of Central Tendency |
| ```IF(logical_test, value_if_true, value_if_false)``` | Return value based on a condition | Labeling |
| ```IFS(logical_test1, value_if_true1, logical_test..., value_if_true..., logical_testn, value_if_truen)``` | Return value based on a condition | Multiple Conditions for Labeling |
| ```LEN(Text)``` | Return the length of the chosen text | Checking Numbers |
| ```LEFT(Text, num_of_chars)``` | Returns text based on the provided text and number of characters from the left |  |
| ```RIGHT(Text, num_of_chars)``` | Returns text based on the provided text and number of characters from the right | Extract Year from a Date |
| ```TEXT(value, format_text)``` | Transform text based on specified format | Convert text to date with ```TEXT(value, "dd/mm/yyyy") |
| ```TRIM(text)``` | Removes leading and trailing spaces | Data Cleaning |
| ```CONCATENATE(text1, text..., textn)``` | Add 2 or more texts | Text Transformation like creating emails and passwords |
| ```SUBSTITUTE(text, old_text, new_text, [instance_num])``` | Replace existing text with new text in a text string | Data Cleaning like date formats |
| ```SUM(number1, numbern)``` | Return the sum based on the given numbers | Total |
| ```SUMIF(range, criteria, sum_range)``` | Return the sum based on the given numbers that passes a condition | Sum based on a given condition |
| ```SUMIFS(sum_range, criteria_range1, criteria1, criteria_rangen, criterian)``` | Return the sum based on the given numbers that passes specified conditions | Sum based on given conditions |
| ```COUNT(number1, numbern)``` | Return the count based on the given fields | Total |
| ```COUNTIF(range, criteria)``` | Return the count based on the given fields that passes a condition | Total based on a given condition |
| ```COUNTIFS(criteria_range1, criteria1, criteria_rangen, criterian)``` | Return the count based on the given fields that passes specified conditions | Total based on given conditions |
| ```DAYS(end_date, start_date)``` | Return the days based on the given dates | Turnaround |
| ```NETWORKDAYS(end_date, start_date, [holidays])``` | Return the days based on the given dates excluding weekends and holidays| Turnaround in a workspace |


> [!NOTE]
> You can test out this formulas with [Alex the Analyst's Formulas Template](excel/formulas.xlsx).

> [!IMPORTANT]
> You can read [Simplilearn's Top 30 Excel Formulas](https://www.simplilearn.com/tutorials/excel-tutorial/excel-formulas).

# Advanced Lessons
For more advanced topics in Excel, you can review [Excel Skills for Business](https://www.coursera.org/specializations/excel).