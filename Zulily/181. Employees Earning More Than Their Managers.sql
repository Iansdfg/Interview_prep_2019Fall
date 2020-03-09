# Write your MySQL query statement below
SELECT mian.Name AS Employee
FROM Employee AS mian 
LEFT JOIN Employee AS sub
ON mian.ManagerId = sub.Id
WHERE mian.Salary > sub.Salary


