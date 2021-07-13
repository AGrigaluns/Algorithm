SELECT * FROM albums;

SELECT * FROM customers WHERE City = "Prague";

SELECT * FROM invoices WHERE BillingCountry = "Sweden" AND Total = 8.91;

SELECT * FROM genres WHERE GenreId = 1 OR GenreId = 10;

SELECT * FROM artists WHERE ArtistId BETWEEN 1 AND 10;

UPDATE tracks SET UnitPrice = 2.99 WHERE TrackId = 10;

SELECT * FROM customers
LIMIT 42;

SELECT customers.Company, Country.City
FROM customers
RIGHT JOIN customers ON customers.CustomerId = Country.CustomerId
ORDER BY Customers.Country;

SELECT customers.FirstName, invoices.Total
FROM customers
LEFT JOIN invoices ON customers.CustomerID = invoices.CustomerID
ORDER BY customers.FirstName;

SELECT City, Country FROM customers
WHERE Country = 'Prague'
UNION
SELECT BillingCity, BillingCountry FROM invoices
WHERE BillingCountry = 'Prague'
ORDER BY City;

SELECT Total,
CASE
    WHEN Total > 1 THEN "Total is greater than 1"
    WHEN Total = 1 THEN "Total is 1"
    ELSE "Total is under 1"
END
FROM invoices;