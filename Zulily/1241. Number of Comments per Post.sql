# Write your MySQL query statement below
SELECT post_id, 
       COUNT(DISTINCT Comments.sub_id) AS number_of_comments
FROM 
    (SELECT DISTINCT sub_id AS post_id, 
            parent_id
    FROM Submissions) AS Post
LEFT JOIN Submissions AS Comments
ON Comments.parent_id = Post.post_id
WHERE Post.parent_id is NULL
GROUP BY post_id

