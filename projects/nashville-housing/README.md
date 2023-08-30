# Skills Used
1. Importing Data into PostgreSQL
2. Populating Missing Data
3. Splitting Data
4. Removing Duplicates
5. Dropping Columns
6. Export CSV ([Access the exported CSV](/projects/nashville-housing/nashville_housing_cleaned.csv))

# Populate Property Address data
Some rows do not have a Property Address. Data has shown consistency in address with the ```ParcelID```.
```sql
SELECT a."ParcelID", a."PropertyAddress", b."ParcelID", b."PropertyAddress", COALESCE(a."PropertyAddress", b."PropertyAddress")
FROM "NashvilleHousing" a
JOIN "NashvilleHousing" b
	ON a."ParcelID" = b."ParcelID"
	AND a."UniqueID" != b."UniqueID"
WHERE a."PropertyAddress" IS NULL;
```

> [!NOTE]
> ```COALESCE``` returns the first non-null argument.

```sql
UPDATE "NashvilleHousing" a
SET "PropertyAddress" = COALESCE(a."PropertyAddress", b."PropertyAddress")
FROM "NashvilleHousing" b
WHERE a."ParcelID" = b."ParcelID" AND a."UniqueID" != b."UniqueID";
```

# Breaking out Address into Individual Columns
## Property Address
```sql
SELECT SUBSTRING("PropertyAddress", 1, POSITION(',' IN "PropertyAddress") - 1) as "Address",
SUBSTRING("PropertyAddress", POSITION(',' IN "PropertyAddress") + 2, LENGTH("PropertyAddress"))
FROM "NashvilleHousing";
```

```sql
ALTER TABLE "NashvilleHousing"
ADD "PropertySplitAddress" text;

UPDATE "NashvilleHousing"
SET "PropertySplitAddress" = SUBSTRING("PropertyAddress", 1, POSITION(',' IN "PropertyAddress") - 1);

ALTER TABLE "NashvilleHousing"
ADD "PropertySplitCity" text;

UPDATE "NashvilleHousing"
SET "PropertySplitCity" = SUBSTRING("PropertyAddress", POSITION(',' IN "PropertyAddress") + 2, LENGTH("PropertyAddress"));
```

## Owner Address
```sql
SELECT TRIM(SPLIT_PART("OwnerAddress", ',', 3))
FROM "NashvilleHousing";
```

> [!NOTE]
> ```SPLIT_PART``` returns the substring based on the field_number. [Read more](https://w3resource.com/PostgreSQL/split_part-function.php).

```sql
ALTER TABLE "NashvilleHousing"
ADD "OwnerSplitAddress" text;

UPDATE "NashvilleHousing"
SET "OwnerSplitAddress" = TRIM(SPLIT_PART("OwnerAddress", ',', 1));

ALTER TABLE "NashvilleHousing"
ADD "OwnerSplitCity" text;

UPDATE "NashvilleHousing"
SET "OwnerSplitCity" = TRIM(SPLIT_PART("OwnerAddress", ',', 2));

ALTER TABLE "NashvilleHousing"
ADD "OwnerSplitState" text;

UPDATE "NashvilleHousing"
SET "OwnerSplitState" = TRIM(SPLIT_PART("OwnerAddress", ',', 3));
```

# Change Y and N to Yes and No in "Sold as Vacant" field
```sql
SELECT DISTINCT("SoldAsVacant"), COUNT("SoldAsVacant")
FROM "NashvilleHousing"
GROUP BY "SoldAsVacant"
ORDER BY 2;
```

```sql
SELECT "SoldAsVacant",
CASE WHEN "SoldAsVacant" = 'Y' THEN 'Yes'
    WHEN "SoldAsVacant" = 'N' THEN 'No'
    ELSE "SoldAsVacant"
END
FROM "NashvilleHousing";
```

```sql
UPDATE "NashvilleHousing"
SET "SoldAsVacant" = CASE WHEN "SoldAsVacant" = 'Y', THEN 'Yes'
    WHEN "SoldAsVacant" = 'N', THEN 'No'
    ELSE "SoldAsVacant"
END;
```

# Removing Duplicates
## Check Duplicates
```sql
WITH RowNumberCTE AS 
(
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY "ParcelID", "PropertyAddress", "SalePrice", "SaleDate", "LegalReference" ORDER BY "UniqueID") AS row_num
    FROM "NashvilleHousing"
)
SELECT * FROM RowNumberCTE
WHERE row_num > 1;
```

## Remove Duplicates
```sql
WITH RowNumberCTE AS 
(
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY "ParcelID", "PropertyAddress", "SalePrice", "SaleDate", "LegalReference" ORDER BY "UniqueID") AS row_num
    FROM "NashvilleHousing"
)
DELETE FROM "NashvilleHousing"
WHERE ("ParcelID", "PropertyAddress", "SalePrice", "SaleDate", "LegalReference") IN (
    SELECT "ParcelID", "PropertyAddress", "SalePrice", "SaleDate", "LegalReference"
    FROM RowNumberCTE
    WHERE row_num > 1
);
```

# Delete Unused Columns
```sql
ALTER TABLE "NashvilleHousing"
DROP COLUMN "OwnerAddress",
DROP COLUMN "TaxDistrict",
DROP COLUMN "PropertyAddress",
DROP COLUMN "SaleDate";
```

> [!NOTE]
> For PostgreSQL, you need to call ```DROP COLUMN``` for every column.

# Export Table to CSV
```sql
\COPY (SELECT * FROM "NashvilleHousing") TO '//mac/Documents/github/analytics-portfolio/projects/nashville-housing/nashville_housing_cleaned.csv' DELIMITER ',' CSV HEADER;
```

> [!IMPORTANT]
> I used the ```PSQL Tool``` to run the command.

You can access the [CSV](/projects/nashville-housing/nashville_housing_cleaned.csv) and [raw queries](/projects/nashville-housing/queries.sql).

> [!NOTE]
> Exporting a CSV allows the results to be used in Excel, Tableau, and Python.