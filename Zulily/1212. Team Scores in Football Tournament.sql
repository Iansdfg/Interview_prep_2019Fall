# Write your MySQL query statement below
SELECT Teams.team_id,
       Teams.team_name,
       IFNULL(FINAL_SCO.score_sum, 0) AS num_points
FROM Teams
LEFT JOIN 
    (SELECT team, SUM(socre) AS score_sum
    FROM
        (SELECT
            host_team AS team,
            CASE 
               WHEN host_goals > guest_goals Then 3
               WHEN host_goals = guest_goals Then 1
               WHEN host_goals < guest_goals Then 0
            END AS socre
        FROM Matches
        UNION ALL
        SELECT
            guest_team AS team,
            CASE 
               WHEN host_goals > guest_goals Then 0
               WHEN host_goals = guest_goals Then 1
               WHEN host_goals < guest_goals Then 3
            END AS socre
        FROM Matches) AS TEAM_SCO
    GROUP BY team) AS FINAL_SCO
ON FINAL_SCO.team = Teams.team_id
ORDER BY num_points DESC, Teams.team_id
