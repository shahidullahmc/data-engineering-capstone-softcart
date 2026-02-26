-- Task 5
SELECT 
    c.country AS country,
    cat.category AS category,
    SUM(f.amount) AS totalsales
FROM "FactSales" f
JOIN "DimCountry" c 
    ON f.countryid = c.countryid
JOIN "DimCategory" cat 
    ON f.categoryid = cat.categoryid
GROUP BY GROUPING SETS (
    (c.country, cat.category),   -- country + category
    (c.country),                 -- country only
    (cat.category),              -- category only
    ()                           -- grand total
)
ORDER BY country, category;

--Task 6
SELECT
    d.year AS year,
    c.country AS country,
    SUM(f.amount) AS totalsales
FROM "FactSales" f
JOIN "DimDate" d
    ON f.dateid = d.dateid
JOIN "DimCountry" c
    ON f.countryid = c.countryid
GROUP BY ROLLUP (d.year, c.country)
ORDER BY year, country;

--Task 7
SELECT
    d.year AS year,
    c.country AS country,
    AVG(f.amount) AS averagesales
FROM "FactSales" f
JOIN "DimDate" d
    ON f.dateid = d.dateid
JOIN "DimCountry" c
    ON f.countryid = c.countryid
GROUP BY CUBE (d.year, c.country)
ORDER BY year, country;

-- Task 8

-- step 1
CREATE MATERIALIZED VIEW total_sales_per_country AS
SELECT
    c.country AS country,
    SUM(f.amount) AS total_sales
FROM "FactSales" f
JOIN "DimCountry" c
    ON f.countryid = c.countryid
GROUP BY c.country
ORDER BY c.country;

-- step 2
SELECT *
FROM total_sales_per_country
ORDER BY country;

-- step to refresh
REFRESH MATERIALIZED VIEW total_sales_per_country;

