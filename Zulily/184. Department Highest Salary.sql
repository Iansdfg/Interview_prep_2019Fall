# Write your MySQL query statement below
SELECT 
    Department.Name AS Department,
    Employee.Name AS Employee,
    Employee.Salary AS Salary
FROM Employee
LEFT JOIN Department
ON Employee.DepartmentId = Department.Id
WHERE
    (Department.Name, Employee.Salary) IN
        (SELECT Department.Name, MAX(Salary)
        FROM Employee
        LEFT JOIN Department
        ON Employee.DepartmentId = Department.Id
        GROUP BY Department.Name)
        

