# Write your MySQL query statement below
SELECT Employee.Name AS Employee
FROM Employee
LEFT JOIN Employee AS Boss
ON Employee.ManagerId = Boss.Id
WHERE Employee.Salary > Boss.Salary
