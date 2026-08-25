SELECT
    Department,
    Employee,
    Salary
FROM
(
    SELECT
        d.Name AS Department,
        e.Name AS Employee,
        e.Salary,
        DENSE_RANK() OVER (
            PARTITION BY e.DepartmentId
            ORDER BY e.Salary DESC
        ) AS SalaryRank
    FROM Employee e
    JOIN Department d
        ON e.DepartmentId = d.Id
) AS RankedEmployees
WHERE SalaryRank <= 3;