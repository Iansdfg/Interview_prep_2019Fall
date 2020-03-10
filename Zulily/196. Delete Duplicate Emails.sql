DELETE p1.*
FROM Person p1
Left Join Person p2
On  p1.Email = p2.Email 
WHERE p1.id > p2.id
