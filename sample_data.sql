USE InterviewDB;
go

--inserting values in users:
INSERT INTO Users
(User_Name, User_Email, User_Password)
VALUES
('Tanvi', 'tanvi@gmail.com', 'Tanvi123'),
('Rahul', 'rahul@gmail.com', 'Rahul123');
GO


--inserting values in questions:
INSERT INTO Questions
(Technology, Topic, Difficulty, Question, Answer)
VALUES

('Python', 'OOP', 'Easy',
'What is a class?',
'A class is a blueprint for creating objects.'),

('Python', 'OOP', 'Medium',
'What is polymorphism?',
'Polymorphism allows objects to take multiple forms.'),

('SQL', 'Joins', 'Easy',
'What is INNER JOIN?',
'INNER JOIN returns matching rows from both tables.'),

('DBMS', 'Normalization', 'Medium',
'What is 3NF?',
'Third Normal Form removes transitive dependencies.'),

('Operating System', 'Scheduling', 'Easy',
'What is FCFS scheduling?',
'First Come First Serve scheduling executes processes in arrival order.');
GO

--inserting values in attempts:
INSERT INTO Attempts
(User_ID, Question_ID, Status)
VALUES

(1, 1, 'Attempted'),
(1, 2, 'Skipped'),
(2, 3, 'Attempted');
GO

SELECT * FROM Users;

SELECT * FROM Questions;

SELECT * FROM Attempts;


DELETE FROM Attempts;
DELETE FROM Questions;
DELETE FROM Users;

DBCC CHECKIDENT ('Users', RESEED, 0);
DBCC CHECKIDENT ('Questions', RESEED, 0);
DBCC CHECKIDENT ('Attempts', RESEED, 0);
