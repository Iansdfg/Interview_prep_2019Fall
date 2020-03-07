# Write your MySQL query statement below
SELECT main.Score, 
       ( SELECT COUNT(DISTINCT sub.Score)
           FROM Scores AS sub
           WHERE main.Score <= sub.Score 
       ) AS Rank
FROM Scores AS main
ORDER BY Score DESC
