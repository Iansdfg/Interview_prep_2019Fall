# Write your MySQL query statement below
SELECT 
    DEP_EMP.DEP_NAME AS Department, 
    DEP_EMP.EMP_NAME AS Employee, 
    DEP_EMP.Salary AS Salary
FROM
    (SELECT 
        Department.NAME AS DEP_NAME, 
        Department.id AS DEP_ID, 
        Employee.Name AS EMP_NAME, 
        Salary
    FROM Employee
    LEFT JOIN Department
    ON Employee.DepartmentId = Department.Id) AS DEP_EMP
LEFT JOIN
    (SELECT DepartmentId, max(Salary) AS MAX_SAL
    FROM Employee
    GROUP BY DepartmentId) AS ID_HIGHEST
ON DEP_EMP.DEP_ID = ID_HIGHEST.DepartmentId
WHERE DEP_EMP.Salary = ID_HIGHEST.MAX_SAL
