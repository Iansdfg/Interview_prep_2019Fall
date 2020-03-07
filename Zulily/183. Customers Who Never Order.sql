# Write your MySQL query statement below
SELECT Customers.name as Customers
FROM Customers 
LEFT JOIN Orders
ON Customers.Id = Orders.CustomerId
WHERE Orders.id is NULL
