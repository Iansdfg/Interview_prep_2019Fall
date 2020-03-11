# Write your MySQL query statement below
# SELECT player_id, device_id
# FROM
#   (SELECT player_id, device_id, min(event_date)
#   FROM Activity
#   GROUP BY player_id) AS a1

SELECT Activity.player_id, Activity.device_id
# SELECT *
FROM Activity 
INNER JOIN
    (SELECT player_id, min(event_date) AS MINI
    FROM Activity
    GROUP BY player_id) AS A_MIN
ON Activity.player_id = A_MIN.player_id 
AND Activity.event_date = A_MIN.MINI
# ORDER BY player_id
