-- Create Database
CREATE DATABASE InterviewDB;
GO

-- Use Database
USE InterviewDB;
GO

--------------------------------------------------
-- USERS TABLE
--------------------------------------------------

CREATE TABLE Users (
    User_ID INT IDENTITY(1,1) PRIMARY KEY,
    User_Name VARCHAR(50) NOT NULL,
    User_Email VARCHAR(100) NOT NULL UNIQUE,
    User_Password VARCHAR(255) NOT NULL,
    Created_At DATETIME DEFAULT GETDATE()
);
GO

--------------------------------------------------
-- QUESTIONS TABLE
--------------------------------------------------

CREATE TABLE Questions (
    Question_ID INT IDENTITY(1,1) PRIMARY KEY,
    Technology VARCHAR(50) NOT NULL,
    Topic VARCHAR(50) NOT NULL,
    Difficulty VARCHAR(20) NOT NULL,
    Question TEXT NOT NULL,
    Answer TEXT NOT NULL
);
GO

--------------------------------------------------
-- ATTEMPTS TABLE
--------------------------------------------------

CREATE TABLE Attempts (
    Attempt_ID INT IDENTITY(1,1) PRIMARY KEY,

    User_ID INT NOT NULL,
    Question_ID INT NOT NULL,

    Status VARCHAR(20) NOT NULL,

    Attempt_Date DATETIME DEFAULT GETDATE(),

    FOREIGN KEY (User_ID)
        REFERENCES Users(User_ID),

    FOREIGN KEY (Question_ID)
        REFERENCES Questions(Question_ID)
);
GO