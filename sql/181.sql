-- 181. Employees Earning More Than Their Managers
-- https://leetcode.com/problems/employees-earning-more-than-their-managers/

SELECT a.name AS 'Employee'
FROM Employee AS a, Employee AS b
WHERE a.managerId = b.id AND a.salary > b.salary;

SELECT
     a.NAME AS Employee
FROM Employee AS a JOIN Employee AS b
     ON a.ManagerId = b.Id
     AND a.Salary > b.Salary
;