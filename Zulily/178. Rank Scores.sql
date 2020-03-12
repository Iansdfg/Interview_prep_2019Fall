# Write your MySQL query statement below
SELECT main.Score, COUNT(DISTINCT sub.Score) AS RANK
FROM Scores main
LEFT JOIN Scores sub
ON main.Score <= sub.Score 
GROUP BY main.Id
ORDER BY main.Score DESC
