SELECT a."ParcelID", a."PropertyAddress", b."ParcelID", b."PropertyAddress", COALESCE(a."PropertyAddress", b."PropertyAddress")
FROM "NashvilleHousing" a
JOIN "NashvilleHousing" b
	ON a."ParcelID" = b."ParcelID"
	AND a."UniqueID" != b."UniqueID"
WHERE a."PropertyAddress" IS NULL;

UPDATE "NashvilleHousing" a
SET "PropertyAddress" = COALESCE(a."PropertyAddress", b."PropertyAddress")
FROM "NashvilleHousing" b
WHERE a."ParcelID" = b."ParcelID" AND a."UniqueID" != b."UniqueID";

SELECT SUBSTRING("PropertyAddress", 1, POSITION(',' IN "PropertyAddress") - 1) as "Address",
SUBSTRING("PropertyAddress", POSITION(',' IN "PropertyAddress") + 2, LENGTH("PropertyAddress"))
FROM "NashvilleHousing";

ALTER TABLE "NashvilleHousing"
ADD "PropertySplitAddress" text;

UPDATE "NashvilleHousing"
SET "PropertySplitAddress" = SUBSTRING("PropertyAddress", 1, POSITION(',' IN "PropertyAddress") - 1);

ALTER TABLE "NashvilleHousing"
ADD "PropertySplitCity" text;

UPDATE "NashvilleHousing"
SET "PropertySplitCity" = SUBSTRING("PropertyAddress", POSITION(',' IN "PropertyAddress") + 2, LENGTH("PropertyAddress"));

SELECT TRIM(SPLIT_PART("OwnerAddress", ',', 3))
FROM "NashvilleHousing";

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

SELECT DISTINCT("SoldAsVacant"), COUNT("SoldAsVacant")
FROM "NashvilleHousing"
GROUP BY "SoldAsVacant"
ORDER BY 2;

SELECT "SoldAsVacant",
CASE WHEN "SoldAsVacant" = 'Y' THEN 'Yes'
    WHEN "SoldAsVacant" = 'N' THEN 'No'
    ELSE "SoldAsVacant"
END
FROM "NashvilleHousing";

UPDATE "NashvilleHousing"
SET "SoldAsVacant" = CASE WHEN "SoldAsVacant" = 'Y', THEN 'Yes'
    WHEN "SoldAsVacant" = 'N', THEN 'No'
    ELSE "SoldAsVacant"
END;

WITH RowNumberCTE AS 
(
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY "ParcelID", "PropertyAddress", "SalePrice", "SaleDate", "LegalReference" ORDER BY "UniqueID") AS row_num
    FROM "NashvilleHousing"
)
SELECT * FROM RowNumberCTE
WHERE row_num > 1;

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

ALTER TABLE "NashvilleHousing"
DROP COLUMN "OwnerAddress",
DROP COLUMN "TaxDistrict",
DROP COLUMN "PropertyAddress",
DROP COLUMN "SaleDate";