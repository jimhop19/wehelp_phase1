#3  
INSERT INTO member(name, username, password, follower_count) VALUES('test', 'test', 'test', 23);  
INSERT INTO member(name, username, password, follower_count) VALUES('Barbie', 'Barbie', 'pink', 1959);  
INSERT INTO member(name, username, password, follower_count) VALUES('Ken', 'Ken', 'mojo_dojo', 721);  
INSERT INTO member(name, username, password, follower_count) VALUES('Oppenheimer', 'Oppenheimer', 'atomic_bomb', 1939);  
INSERT INTO member(name, username, password, follower_count) VALUES('BarbenHeimer', 'Barbenheimer', 'warner_bros_universal_pictures', 2023);  
![image](https://github.com/jimhop19/wehelp_phase1/blob/main/week5/screenshot/3-1.png)

SELECT * FROM member;  
![image](https://github.com/jimhop19/wehelp_phase1/blob/main/week5/screenshot/3-2.png)

SELECT * FROM member
ORDER BY time DESC;  
![image](https://github.com/jimhop19/wehelp_phase1/blob/main/week5/screenshot/3-3.png)

SELECT *
FROM member
ORDER BY time DESC
LIMIT 1,3;  
![image](https://github.com/jimhop19/wehelp_phase1/blob/main/week5/screenshot/3-4.png)

SELECT * FROM member
WHERE username = 'test';  
![image](https://github.com/jimhop19/wehelp_phase1/blob/main/week5/screenshot/3-5.png)

SELECT * FROM member
WHERE username = 'test' AND password = 'test';  
![image](https://github.com/jimhop19/wehelp_phase1/blob/main/week5/screenshot/3-6.png)

UPDATE member
SET username = 'test2'
WHERE username = 'test';  
![image](https://github.com/jimhop19/wehelp_phase1/blob/main/week5/screenshot/3-7.png)

#4  
SELECT count(id)
FROM member;  
SELECT sum(follower_count)
FROM member;  
SELECT AVG(follower_count)
FROM member;  
![image](https://github.com/jimhop19/wehelp_phase1/blob/main/week5/screenshot/4.png)

#5  
SELECT message.content,member.username 
FROM message
LEFT JOIN member
ON message.member_id = member.id;  
SELECT message.content,member.username 
FROM message
LEFT JOIN member
ON message.member_id = member.id 
WHERE member.username = 'test';  
SELECT AVG(like_count),member.username
FROM message
LEFT JOIN member
ON message.member_id = member.id
WHERE member.username='test';  
![image](https://github.com/jimhop19/wehelp_phase1/blob/main/week5/screenshot/5.png)
