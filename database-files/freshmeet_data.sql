DROP DATABASE IF EXISTS FreshMeet;
CREATE DATABASE IF NOT EXISTS FreshMeet;
USE FreshMeet;

-- Creating the Advisors table
CREATE TABLE Advisors (
    advisorId INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL
);

-- Creating the Students table
CREATE TABLE Students (
    studentId INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    advisorId INT,
    -- major can also be undeclared
    major VARCHAR (50) NOT NULL,
    GPA INT NOT NULL,
    demographics VARCHAR(50) NOT NULL,
    FOREIGN KEY (advisorId) REFERENCES Advisors(advisorId)
);

-- Creating the Skills table
CREATE TABLE Skills (
    skillId INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
);

-- Creating the StudentSkills table (resolving many-to-many relationship)
CREATE TABLE StudentSkills (
    studentId INT,
    skillId INT,
    PRIMARY KEY (studentId, skillId),
    FOREIGN KEY (studentId) REFERENCES Students(studentId),
    FOREIGN KEY (skillId) REFERENCES Skills(skillId)
);

-- Creating the Employers table
CREATE TABLE Companies (
    empId INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    LinkedIn VARCHAR(200),
    size VARCHAR(50),
    industry VARCHAR(100)
);


-- Creating the Alumni table
CREATE TABLE Alumni (
    alumniId INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(100) NOT NULL,
    lastName VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10, 2),
    industry VARCHAR(100),
    LinkedIn VARCHAR(200),
    empId INT,
    jobTitle VARCHAR(50),
    FOREIGN KEY (empId) REFERENCES Companies(empId)
);

-- Creating the Recruiters table
CREATE TABLE Recruiters (
    recruiterId INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(100) NOT NULL,
    lastName VARCHAR(100) NOT NULL,
    email VARCHAR(50) NOT NULL,
    empId INT,
    FOREIGN KEY (empId) REFERENCES Companies(empId)
);
-- Creating the Job Postings table
CREATE TABLE JobPosting (
    jobId INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50),
    location VARCHAR(100),
    industry VARCHAR(100),
    applyByDate DATE,
    description TEXT,
    salary DECIMAL(10, 2),
    recruiterId INT,
    FOREIGN KEY (recruiterId) REFERENCES Recruiters(recruiterId)
);

-- Creating the PostingSkills table (resolving many-to-many relationship)
CREATE TABLE PostingSkills (
    jobId INT,
    skillId INT,
    PRIMARY KEY (jobId, skillId),
    FOREIGN KEY (jobId) REFERENCES JobPosting(jobId),
    FOREIGN KEY (skillId) REFERENCES Skills(skillId)
);

-- Creating the Applications table
CREATE TABLE Applications (
    appId INT PRIMARY KEY AUTO_INCREMENT,
    studentId INT,
    jobId INT,
    status VARCHAR(50) CHECK (status IN ('Pending', 'Accepted', 'Rejected')),
    date DATE,
    FOREIGN KEY (studentId) REFERENCES Students(studentId),
    FOREIGN KEY (jobId) REFERENCES JobPosting(jobId) ON DELETE CASCADE
);

-- Creating the StudentReviews table
CREATE TABLE ReviewsOnStudents (
    studentId INT,
    reviewId INT AUTO_INCREMENT PRIMARY KEY,
    review TEXT,
    FOREIGN KEY (studentId) REFERENCES Students(studentId)
);

-- Creating the ReviewsOnEmployers table
CREATE TABLE ReviewsOnEmployers (
    employerId INT,
    reviewId INT PRIMARY KEY AUTO_INCREMENT,
    review TEXT,
    FOREIGN KEY (employerId) REFERENCES Companies(empId)
);

-- insert into advisors
INSERT INTO Advisors (firstname, lastname, email) VALUES ('Brit', 'Caris', 'bcaris0@northeastern.edu');
INSERT INTO Advisors (firstname, lastname, email) VALUES ('Sayer', 'Cowe', 'scowe1@northeastern.edu');
INSERT INTO Advisors (firstname, lastname, email) VALUES ('Dorothea', 'Vosse', 'dvosse2@northeastern.edu');
INSERT INTO Advisors (firstname, lastname, email) VALUES ('Kandace', 'Ivamy', 'kivamy3@northeastern.edu');
INSERT INTO Advisors (firstname, lastname, email) VALUES ( 'Timothee', 'Bagnal', 'tbagnal4@northeastern.edu');
INSERT INTO Advisors (firstname, lastname, email) VALUES ( 'Karoly', 'Shipway', 'kshipway5@northeastern.edu');
INSERT INTO Advisors (firstname, lastname, email) VALUES ( 'Gavan', 'Aleksankov', 'galeksankov6@northeastern.edu');
INSERT INTO Advisors (firstname, lastname, email) VALUES ( 'Dynah', 'Painten', 'dpainten7@northeastern.edu');
INSERT INTO Advisors (firstname, lastname, email) VALUES ( 'Babbie', 'Kettell', 'bkettell8@northeastern.edu');
INSERT INTO Advisors (firstname, lastname, email) VALUES ( 'Kacie', 'Armstead', 'karmstead9@northeastern.edu');

-- insert into students
INSERT INTO Students (firstName, lastName, email, advisorId, major, GPA, demographics)
VALUES
('Nani', 'Naile', 'nnaile0@northeastern.edu', 6, 'Computer Science', 2.9, 'White'),
('Amalle', 'Guildford', 'aguildford1@northeastern.edu', 3, 'Environmental Science', 2.1, 'White'),
('Herc', 'Stadding', 'hstadding2@northeastern.edu', 5, 'Environmental Science', 3.8, 'White'),
('Aharon', 'Carpenter', 'acarpenter3@northeastern.edu', 6, 'Mathematics', 2.6, 'Asian'),
('Angelica', 'Fawcett', 'afawcett4@northeastern.edu', 10, 'Environmental Science', 2.8, 'White'),
('Granny', 'Deavall', 'gdeavall5@northeastern.edu', 3, 'Environmental Science', 3.9, 'White'),
('Elisha', 'Bratcher', 'ebratcher6@northeastern.edu', 1, 'Statistics', 2.6, 'White'),
('Andra', 'Christauffour', 'achristauffour7@northeastern.edu', 3, 'Statistics', 2.9, 'Asian'),
('Dee dee', 'Awde', 'dawde8@northeastern.edu', 2, 'Computer Science', 3.7, 'Alaska Native'),
('Waiter', 'Savatier', 'wsavatier9@northeastern.edu', 10, 'Biology', 3.0, 'Asian'),
('Ofilia', 'Virgin', 'ovirgina@northeastern.edu', 5, 'Engineering', 3.9, 'White'),
('Debbie', 'Duffield', 'dduffieldb@northeastern.edu', 2, 'Biology', 2.1, 'White'),
('Ham', 'Crombleholme', 'hcrombleholmec@northeastern.edu', 3, 'Environmental Science', 2.1, 'Asian'),
('Vilma', 'Angric', 'vangricd@northeastern.edu', 5, 'Statistics', 3.9, 'White'),
('Tailor', 'Kleewein', 'tkleeweine@northeastern.edu', 2, 'Mathematics', 3.1, 'Native Hawaiian'),
('Jeffrey', 'Haggath', 'jhaggathf@northeastern.edu', 6, 'Computer Science', 3.8, 'White'),
('Munroe', 'Reuben', 'mreubeng@northeastern.edu', 9, 'Environmental Science', 3.1, 'Asian'),
('Frants', 'Sauven', 'fsauvenh@northeastern.edu', 10, 'Computer Science', 2.5, 'American Indian'),
('Konstantine', 'Flewett', 'kflewetti@northeastern.edu', 5, 'Physics', 4.0, 'White'),
('Kriste', 'McRobbie', 'kmcrobbiej@northeastern.edu', 9, 'Information Technology', 3.1, 'White'),
('Veronika', 'Rosenzveig', 'vrosenzveigk@northeastern.edu', 9, 'Engineering', 2.0, 'Asian'),
('Aurie', 'Beardsdale', 'abeardsdalel@northeastern.edu', 4, 'Statistics', 3.5, 'Asian'),
('Dynah', 'Olennikov', 'dolennikovm@northeastern.edu', 8, 'Chemistry', 3.1, 'White'),
('Marylin', 'Porson', 'mporsonn@northeastern.edu', 8, 'Biology', 2.9, 'Asian'),
('Shelly', 'Silbermann', 'ssilbermanno@northeastern.edu', 10, 'Chemistry', 2.7, 'White'),
('Maressa', 'Innman', 'minnmanp@northeastern.edu', 10, 'Computer Science', 3.5, 'Asian'),
('Gare', 'Fuchs', 'gfuchsq@northeastern.edu', 3, 'Chemistry', 2.8, 'White'),
('Biron', 'Dondon', 'bdondonr@northeastern.edu', 3, 'Computer Science', 2.5, 'Asian'),
('Gaston', 'Hoble', 'ghobles@northeastern.edu', 1, 'Chemistry', 2.1, 'White'),
('Hortense', 'Goodley', 'hgoodleyt@northeastern.edu', 5, 'Environmental Science', 3.6, 'Asian'),
('Shoshana', 'Salkild', 'ssalkildu@northeastern.edu', 9, 'Chemistry', 3.9, 'White'),
('Magdalen', 'De Witt', 'mdewittv@northeastern.edu', 8, 'Environmental Science', 3.5, 'White'),
('Bonny', 'Spensly', 'bspenslyw@northeastern.edu', 5, 'Environmental Science', 2.4, 'American Indian'),
('Candide', 'Christofe', 'cchristofex@northeastern.edu', 1, 'Statistics', 2.7, 'White'),
('Emelyne', 'Turpin', 'eturpiny@northeastern.edu', 7, 'Engineering', 3.6, 'White'),
('Carmelle', 'Bare', 'cbarez@northeastern.edu', 5, 'Computer Science', 3.7, 'Alaska Native'),
('Gavra', 'Spiteri', 'gspiteri10@northeastern.edu', 8, 'Physics', 3.2, 'Alaska Native'),
('Oren', 'McCaskell', 'omccaskell11@northeastern.edu', 6, 'Computer Science', 3.1, 'Asian'),
('Chico', 'Yurocjhin', 'cyurocjhin12@northeastern.edu', 3, 'Chemistry', 3.0, 'Other Pacific Islander'),
('Barbra', 'Rosengren', 'brosengren13@northeastern.edu', 9, 'Biology', 3.4, 'White'),
('Luz', 'Bargh', 'lbargh14@northeastern.edu', 8, 'Physics', 2.8, 'White'),
('Allison', 'Wapol', 'awapol15@northeastern.edu', 4, 'Engineering', 2.8, 'Asian'),
('Thayne', 'Shrubsall', 'tshrubsall16@northeastern.edu', 7, 'Environmental Science', 3.2, 'Asian'),
('Hollie', 'Temperton', 'htemperton17@northeastern.edu', 7, 'Statistics', 2.9, 'White'),
('Melodee', 'Davydoch', 'mdavydoch18@northeastern.edu', 3, 'Mathematics', 2.7, 'White'),
('Hunfredo', 'Gregoriou', 'hgregoriou19@northeastern.edu', 2, 'Biology', 3.6, 'Asian'),
('Cherye', 'Fery', 'cfery1a@northeastern.edu', 5, 'Environmental Science', 3.0, 'Asian'),
('Lynett', 'Simoes', 'lsimoes1b@northeastern.edu', 4, 'Engineering', 3.1, 'Alaska Native'),
('Mal', 'McGeachy', 'mmcgeachy1c@northeastern.edu', 10, 'Engineering', 3.9, 'Native Hawaiian'),
('Brocky', 'Carlill', 'bcarlill1d@northeastern.edu', 5, 'Physics', 2.4, 'Asian');

-- inset into skills
insert into Skills (name) values ('Python');
insert into Skills (name) values ('Node.js');
insert into Skills (name) values ('SQL');
insert into Skills (name) values ('Power BI');
insert into Skills (name) values ('Tableau');
insert into Skills (name) values ('JavaScript');
insert into Skills (name) values ('React.js');
insert into Skills (name) values ('HTML/CSS');
insert into Skills (name) values ('Java');
insert into Skills (name) values ('C++');
insert into Skills (name) values ('AWS');
insert into Skills (name) values ('Docker');
insert into Skills (name) values ('Kubernetes');
insert into Skills (name) values ('Git/GitHub');
insert into Skills (name) values ('MongoDB');
insert into Skills (name) values ('MySQL');
insert into Skills (name) values ('TensorFlow');
insert into Skills (name) values ('RESTful API Development');
insert into Skills (name) values ('R (Programming Language)');
insert into Skills (name) values ('Data Analysis and Visualization');
insert into Skills (name) values ('Communication Skills');
insert into Skills (name) values ('Time Management');
insert into Skills (name) values ('Critical Thinking');
insert into Skills (name) values ('Collaboration');
insert into Skills (name) values ('Leadership');
insert into Skills (name) values ('Adaptability');
insert into Skills (name) values ('Problem-Solving');
insert into Skills (name) values ('Creativity');
insert into Skills (name) values ('Emotional Intelligence');
insert into Skills (name) values ('Networking');
insert into Skills (name) values ('Teamwork');
insert into Skills (name) values ('Conflict Resolution');
insert into Skills (name) values ('Presentation Skills');
insert into Skills (name) values ('Decision-Making');
insert into Skills (name) values ('Active Listening');
insert into Skills (name) values ('Negotiation');
insert into Skills (name) values ('Public Speaking');
insert into Skills (name) values ('Self-Motivation');
insert into Skills (name) values ('Interpersonal Skills');
insert into Skills (name) values ('Organization Skills');

-- insert into studentskills
insert into StudentSkills (studentId, skillId) values (22, 15);
insert into StudentSkills (studentId, skillId) values (26, 31);
insert into StudentSkills (studentId, skillId) values (28, 36);
insert into StudentSkills (studentId, skillId) values (48, 38);
insert into StudentSkills (studentId, skillId) values (49, 26);
insert into StudentSkills (studentId, skillId) values (15, 40);
insert into StudentSkills (studentId, skillId) values (38, 13);
insert into StudentSkills (studentId, skillId) values (26, 25);
insert into StudentSkills (studentId, skillId) values (39, 6);
insert into StudentSkills (studentId, skillId) values (41, 9);
insert into StudentSkills (studentId, skillId) values (21, 2);
insert into StudentSkills (studentId, skillId) values (29, 8);
insert into StudentSkills (studentId, skillId) values (37, 12);
insert into StudentSkills (studentId, skillId) values (46, 31);
insert into StudentSkills (studentId, skillId) values (7, 8);
insert into StudentSkills (studentId, skillId) values (1, 33);
insert into StudentSkills (studentId, skillId) values (42, 35);
insert into StudentSkills (studentId, skillId) values (18, 18);
insert into StudentSkills (studentId, skillId) values (25, 3);
insert into StudentSkills (studentId, skillId) values (48, 35);
insert into StudentSkills (studentId, skillId) values (35, 8);
insert into StudentSkills (studentId, skillId) values (43, 5);
insert into StudentSkills (studentId, skillId) values (17, 37);
insert into StudentSkills (studentId, skillId) values (36, 5);
insert into StudentSkills (studentId, skillId) values (3, 2);
insert into StudentSkills (studentId, skillId) values (12, 6);
insert into StudentSkills (studentId, skillId) values (17, 21);
insert into StudentSkills (studentId, skillId) values (26, 19);
insert into StudentSkills (studentId, skillId) values (31, 31);
insert into StudentSkills (studentId, skillId) values (28, 10);
insert into StudentSkills (studentId, skillId) values (44, 21);
insert into StudentSkills (studentId, skillId) values (21, 38);
insert into StudentSkills (studentId, skillId) values (30, 5);
insert into StudentSkills (studentId, skillId) values (28, 34);
insert into StudentSkills (studentId, skillId) values (38, 22);
insert into StudentSkills (studentId, skillId) values (18, 24);
insert into StudentSkills (studentId, skillId) values (9, 39);
insert into StudentSkills (studentId, skillId) values (44, 35);
insert into StudentSkills (studentId, skillId) values (12, 40);
insert into StudentSkills (studentId, skillId) values (20, 13);
insert into StudentSkills (studentId, skillId) values (35, 1);
insert into StudentSkills (studentId, skillId) values (9, 27);
insert into StudentSkills (studentId, skillId) values (42, 3);
insert into StudentSkills (studentId, skillId) values (16, 38);
insert into StudentSkills (studentId, skillId) values (16, 35);
insert into StudentSkills (studentId, skillId) values (43, 12);
insert into StudentSkills (studentId, skillId) values (32, 23);
insert into StudentSkills (studentId, skillId) values (1, 36);
insert into StudentSkills (studentId, skillId) values (1, 24);
insert into StudentSkills (studentId, skillId) values (11, 18);
insert into StudentSkills (studentId, skillId) values (28, 13);
insert into StudentSkills (studentId, skillId) values (46, 13);
insert into StudentSkills (studentId, skillId) values (30, 14);
insert into StudentSkills (studentId, skillId) values (7, 32);
insert into StudentSkills (studentId, skillId) values (17, 32);
insert into StudentSkills (studentId, skillId) values (33, 27);
insert into StudentSkills (studentId, skillId) values (23, 20);
insert into StudentSkills (studentId, skillId) values (28, 26);
insert into StudentSkills (studentId, skillId) values (50, 5);
insert into StudentSkills (studentId, skillId) values (30, 38);
insert into StudentSkills (studentId, skillId) values (29, 39);
insert into StudentSkills (studentId, skillId) values (26, 26);
insert into StudentSkills (studentId, skillId) values (8, 39);
insert into StudentSkills (studentId, skillId) values (24, 14);
insert into StudentSkills (studentId, skillId) values (3, 1);
insert into StudentSkills (studentId, skillId) values (24, 4);
insert into StudentSkills (studentId, skillId) values (39, 33);
insert into StudentSkills (studentId, skillId) values (25, 24);
insert into StudentSkills (studentId, skillId) values (44, 24);
insert into StudentSkills (studentId, skillId) values (19, 40);
insert into StudentSkills (studentId, skillId) values (48, 25);
insert into StudentSkills (studentId, skillId) values (41, 22);
insert into StudentSkills (studentId, skillId) values (8, 18);
insert into StudentSkills (studentId, skillId) values (46, 30);
insert into StudentSkills (studentId, skillId) values (8, 3);
insert into StudentSkills (studentId, skillId) values (43, 38);
insert into StudentSkills (studentId, skillId) values (18, 7);
insert into StudentSkills (studentId, skillId) values (21, 5);
insert into StudentSkills (studentId, skillId) values (24, 18);
insert into StudentSkills (studentId, skillId) values (19, 32);
insert into StudentSkills (studentId, skillId) values (27, 24);
insert into StudentSkills (studentId, skillId) values (37, 36);
insert into StudentSkills (studentId, skillId) values (18, 1);
insert into StudentSkills (studentId, skillId) values (10, 11);
insert into StudentSkills (studentId, skillId) values (38, 19);
insert into StudentSkills (studentId, skillId) values (43, 6);
insert into StudentSkills (studentId, skillId) values (48, 8);
insert into StudentSkills (studentId, skillId) values (36, 25);
insert into StudentSkills (studentId, skillId) values (11, 23);
insert into StudentSkills (studentId, skillId) values (28, 9);
insert into StudentSkills (studentId, skillId) values (3, 34);
insert into StudentSkills (studentId, skillId) values (45, 20);
insert into StudentSkills (studentId, skillId) values (23, 39);
insert into StudentSkills (studentId, skillId) values (8, 24);
insert into StudentSkills (studentId, skillId) values (34, 29);
insert into StudentSkills (studentId, skillId) values (50, 2);
insert into StudentSkills (studentId, skillId) values (25, 30);
insert into StudentSkills (studentId, skillId) values (26, 36);
insert into StudentSkills (studentId, skillId) values (40, 27);
insert into StudentSkills (studentId, skillId) values (41, 24);

-- insert into Companies
insert into Companies (name, linkedin, size, industry) values ('Realfire', 'https://www.linkedin.com/in/example2', 'Large (4000+)', 'Healthcare');
insert into Companies (name, linkedin, size, industry) values ('JumpXS', 'https://www.linkedin.com/in/example5', 'Small (10- 250)', 'Retail');
insert into Companies (name, linkedin, size, industry) values ('Yozio', 'https://www.linkedin.com/in/example2', 'Startup (<10)', 'Technology');
insert into Companies (name, linkedin, size, industry) values ('Tagtune', 'https://www.linkedin.com/in/example3', 'Medium (250-4000)', 'Education');
insert into Companies (name, linkedin, size, industry) values ('Tagchat', 'https://www.linkedin.com/in/example4', 'Large (4000+)', 'Finance');
insert into Companies (name, linkedin, size, industry) values ('Voomm', 'https://www.linkedin.com/in/example4', 'Small (10- 250)', 'Retail');
insert into Companies (name, linkedin, size, industry) values ('Wikibox', 'https://www.linkedin.com/in/example4', 'Small (10- 250)', 'Education');
insert into Companies (name, linkedin, size, industry) values ('Kayveo', 'https://www.linkedin.com/in/example4', 'Large (4000+)', 'Manufacturing');
insert into Companies (name, linkedin, size, industry) values ('Cogidoo', 'https://www.linkedin.com/in/example1', 'Small (10- 250)', 'Retail');
insert into Companies (name, linkedin, size, industry) values ('Zoonoodle', 'https://www.linkedin.com/in/example4', 'Small (10- 250)', 'Education');
insert into Companies (name, linkedin, size, industry) values ('Devcast', 'https://www.linkedin.com/in/example3', 'Small (10- 250)', 'Construction');
insert into Companies (name, linkedin, size, industry) values ('Bluejam', 'https://www.linkedin.com/in/example2', 'Medium (250-4000)', 'Education');
insert into Companies (name, linkedin, size, industry) values ('Browsetype', 'https://www.linkedin.com/in/example4', 'Small (10- 250)', 'Education');
insert into Companies (name, linkedin, size, industry) values ('Wordtune', 'https://www.linkedin.com/in/example2', 'Startup (<10)', 'Retail');
insert into Companies (name, linkedin, size, industry) values ('Ooba', 'https://www.linkedin.com/in/example3', 'Small (10- 250)', 'Entertainment');
insert into Companies (name, linkedin, size, industry) values ('Gabvine', 'https://www.linkedin.com/in/example5', 'Large (4000+)', 'Technology');
insert into Companies (name, linkedin, size, industry) values ('Twimbo', 'https://www.linkedin.com/in/example4', 'Small (10- 250)', 'Healthcare');
insert into Companies (name, linkedin, size, industry) values ('Mydeo', 'https://www.linkedin.com/in/example3', 'Small (10- 250)', 'Education');
insert into Companies (name, linkedin, size, industry) values ('Yacero', 'https://www.linkedin.com/in/example2', 'Medium (250-4000)', 'Manufacturing');
insert into Companies (name, linkedin, size, industry) values ('Centidel', 'https://www.linkedin.com/in/example5', 'Medium (250-4000)', 'Healthcare');
insert into Companies (name, linkedin, size, industry) values ('Buzzshare', 'https://www.linkedin.com/in/example4', 'Large (4000+)', 'Construction');
insert into Companies (name, linkedin, size, industry) values ('Blogtag', 'https://www.linkedin.com/in/example1', 'Medium (250-4000)', 'Construction');
insert into Companies (name, linkedin, size, industry) values ('Lazzy', 'https://www.linkedin.com/in/example2', 'Large (4000+)', 'Finance');
insert into Companies (name, linkedin, size, industry) values ('Zoonoodle', 'https://www.linkedin.com/in/example3', 'Small (10- 250)', 'Education');
insert into Companies (name, linkedin, size, industry) values ('Thoughtbridge', 'https://www.linkedin.com/in/example2', 'Medium (250-4000)', 'Manufacturing');
insert into Companies (name, linkedin, size, industry) values ('Blognation', 'https://www.linkedin.com/in/example1', 'Medium (250-4000)', 'Entertainment');
insert into Companies (name, linkedin, size, industry) values ('Buzzster', 'https://www.linkedin.com/in/example1', 'Large (4000+)', 'Retail');
insert into Companies (name, linkedin, size, industry) values ('Gabvine', 'https://www.linkedin.com/in/example3', 'Startup (<10)', 'Retail');
insert into Companies (name, linkedin, size, industry) values ('Pixope', 'https://www.linkedin.com/in/example4', 'Small (10- 250)', 'Education');
insert into Companies (name, linkedin, size, industry) values ('Pixope', 'https://www.linkedin.com/in/example5', 'Medium (250-4000)', 'Construction');
insert into Companies (name, linkedin, size, industry) values ('Thoughtstorm', 'https://www.linkedin.com/in/example4', 'Startup (<10)', 'Education');
insert into Companies (name, linkedin, size, industry) values ('Meedoo', 'https://www.linkedin.com/in/example3', 'Startup (<10)', 'Finance');
insert into Companies (name, linkedin, size, industry) values ('Trudoo', 'https://www.linkedin.com/in/example1', 'Medium (250-4000)', 'Construction');
insert into Companies (name, linkedin, size, industry) values ('Feedfish', 'https://www.linkedin.com/in/example1', 'Large (4000+)', 'Construction');
insert into Companies (name, linkedin, size, industry) values ('Bubblemix', 'https://www.linkedin.com/in/example1', 'Small (10- 250)', 'Technology');
insert into Companies (name, linkedin, size, industry) values ('Vinte', 'https://www.linkedin.com/in/example4', 'Startup (<10)', 'Retail');
insert into Companies (name, linkedin, size, industry) values ('Voonder', 'https://www.linkedin.com/in/example2', 'Small (10- 250)', 'Technology');
insert into Companies (name, linkedin, size, industry) values ('Rhynyx', 'https://www.linkedin.com/in/example2', 'Large (4000+)', 'Finance');
insert into Companies (name, linkedin, size, industry) values ('Youbridge', 'https://www.linkedin.com/in/example2', 'Large (4000+)', 'Healthcare');
insert into Companies (name, linkedin, size, industry) values ('Chatterpoint', 'https://www.linkedin.com/in/example5', 'Small (10- 250)', 'Entertainment');
insert into Companies (name, linkedin, size, industry) values ('Eire', 'https://www.linkedin.com/in/example1', 'Medium (250-4000)', 'Manufacturing');
insert into Companies (name, linkedin, size, industry) values ('Jabbertype', 'https://www.linkedin.com/in/example1', 'Startup (<10)', 'Finance');
insert into Companies (name, linkedin, size, industry) values ('Fivechat', 'https://www.linkedin.com/in/example3', 'Medium (250-4000)', 'Retail');
insert into Companies (name, linkedin, size, industry) values ('Oyonder', 'https://www.linkedin.com/in/example5', 'Small (10- 250)', 'Finance');
insert into Companies (name, linkedin, size, industry) values ('Gigashots', 'https://www.linkedin.com/in/example5', 'Large (4000+)', 'Manufacturing');
insert into Companies (name, linkedin, size, industry) values ('Quire', 'https://www.linkedin.com/in/example5', 'Medium (250-4000)', 'Entertainment');
insert into Companies (name, linkedin, size, industry) values ('Devpulse', 'https://www.linkedin.com/in/example3', 'Large (4000+)', 'Entertainment');
insert into Companies (name, linkedin, size, industry) values ('Photospace', 'https://www.linkedin.com/in/example5', 'Large (4000+)', 'Finance');
insert into Companies (name, linkedin, size, industry) values ('Rhynyx', 'https://www.linkedin.com/in/example2', 'Startup (<10)', 'Technology');
insert into Companies (name, linkedin, size, industry) values ('Buzzbean', 'https://www.linkedin.com/in/example4', 'Small (10- 250)', 'Construction');
insert into Companies (name, linkedin, size, industry) values ('Ainyx', 'https://www.linkedin.com/in/example3', 'Medium (250-4000)', 'Construction');
insert into Companies (name, linkedin, size, industry) values ('Flashspan', 'https://www.linkedin.com/in/example2', 'Startup (<10)', 'Entertainment');
insert into Companies (name, linkedin, size, industry) values ('Oba', 'https://www.linkedin.com/in/example1', 'Startup (<10)', 'Education');
insert into Companies (name, linkedin, size, industry) values ('Plajo', 'https://www.linkedin.com/in/example3', 'Large (4000+)', 'Manufacturing');
insert into Companies (name, linkedin, size, industry) values ('Yozio', 'https://www.linkedin.com/in/example1', 'Startup (<10)', 'Entertainment');

-- insert into alumni table
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Augusta', 'Bowness', 'abowness0@infoseek.co.jp', 141264, 'Entertainment', 'Statistician I', 'https://www.linkedin.com/profile/443109031', 22);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Davie', 'Emanueli', 'demanueli1@vk.com', 166126, 'Education', 'Administrative Officer', 'https://www.linkedin.com/profile/916484488', 9);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Renee', 'Cudmore', 'rcudmore2@forbes.com', 115599, 'Entertainment', 'Recruiting Manager', 'https://www.linkedin.com/profile/458776117', 16);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Dulcia', 'Drew', 'ddrew3@drupal.org', 357090, 'Manufacturing', 'Analog Circuit Design manager', 'https://www.linkedin.com/profile/584718053', 27);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Rikki', 'Mercer', 'rmercer4@g.co', 101062, 'Technology', 'Cost Accountant', 'https://www.linkedin.com/profile/820586957', 16);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Leanor', 'Perryn', 'lperryn5@ibm.com', 360325, 'Education', 'Account Coordinator', 'https://www.linkedin.com/profile/488664316', 15);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Willie', 'Holyard', 'wholyard6@skype.com', 444746, 'Manufacturing', 'Geological Engineer', 'https://www.linkedin.com/profile/392291411', 34);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Hakeem', 'Cuthbertson', 'hcuthbertson7@archive.org', 216204, 'Construction', 'Registered Nurse', 'https://www.linkedin.com/profile/904512443', 2);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Shaina', 'Chittem', 'schittem8@ask.com', 175767, 'Retail', 'Environmental Specialist', 'https://www.linkedin.com/profile/827829708', 53);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Creigh', 'Taffurelli', 'ctaffurelli9@qq.com', 395096, 'Technology', 'Programmer Analyst III', 'https://www.linkedin.com/profile/749717643', 39);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Alanna', 'Starton', 'astartona@uiuc.edu', 382716, 'Healthcare', 'Marketing Manager', 'https://www.linkedin.com/profile/491402449', 47);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Nealon', 'Worrill', 'nworrillb@miibeian.gov.cn', 227110, 'Finance', 'VP Accounting', 'https://www.linkedin.com/profile/318851887', 14);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Lilia', 'Hyatt', 'lhyattc@php.net', 213991, 'Entertainment', 'Internal Auditor', 'https://www.linkedin.com/profile/731557037', 40);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Kaine', 'Pestell', 'kpestelld@squidoo.com', 397254, 'Retail', 'Speech Pathologist', 'https://www.linkedin.com/profile/476176521', 12);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Alayne', 'Scholar', 'ascholare@ftc.gov', 438590, 'Education', 'Account Executive', 'https://www.linkedin.com/profile/820298970', 26);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Mireielle', 'Strood', 'mstroodf@odnoklassniki.ru', 198808, 'Healthcare', 'Teacher', 'https://www.linkedin.com/profile/635518654', 39);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Wang', 'Juanico', 'wjuanicog@cbc.ca', 314234, 'Retail', 'Associate Professor', 'https://www.linkedin.com/profile/183753098', 29);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Mariele', 'Kubasiewicz', 'mkubasiewiczh@weebly.com', 366282, 'Technology', 'General Manager', 'https://www.linkedin.com/profile/910504859', 22);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Margette', 'Duignan', 'mduignani@house.gov', 439254, 'Technology', 'Legal Assistant', 'https://www.linkedin.com/profile/935548144', 3);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Othella', 'Hurch', 'ohurchj@webmd.com', 153734, 'Technology', 'Compensation Analyst', 'https://www.linkedin.com/profile/315216417', 2);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Wallace', 'Egger', 'weggerk@sina.com.cn', 159433, 'Healthcare', 'Financial Analyst', 'https://www.linkedin.com/profile/184982563', 23);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Ingar', 'Vasyukov', 'ivasyukovl@nydailynews.com', 148262, 'Entertainment', 'Programmer Analyst III', 'https://www.linkedin.com/profile/281318035', 43);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Crawford', 'Guiraud', 'cguiraudm@seesaa.net', 432729, 'Finance', 'Design Engineer', 'https://www.linkedin.com/profile/650906134', 38);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Susanetta', 'Cosens', 'scosensn@dailymail.co.uk', 200046, 'Technology', 'Occupational Therapist', 'https://www.linkedin.com/profile/864644064', 35);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Merissa', 'McClory', 'mmccloryo@wikia.com', 413784, 'Technology', 'Pharmacist', 'https://www.linkedin.com/profile/867719747', 5);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Tiebold', 'Epdell', 'tepdellp@sciencedirect.com', 294039, 'Healthcare', 'Associate Professor', 'https://www.linkedin.com/profile/631275568', 33);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Tomaso', 'Alston', 'talstonq@wikia.com', 365369, 'Manufacturing', 'Editor', 'https://www.linkedin.com/profile/851240593', 5);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Abbe', 'Klein', 'akleinr@behance.net', 438194, 'Entertainment', 'Nuclear Power Engineer', 'https://www.linkedin.com/profile/748874901', 29);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Reinwald', 'Linham', 'rlinhams@sourceforge.net', 213935, 'Manufacturing', 'Human Resources Assistant IV', 'https://www.linkedin.com/profile/414062715', 25);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Debby', 'Fain', 'dfaint@last.fm', 243664, 'Construction', 'Data Coordinator', 'https://www.linkedin.com/profile/276115266', 32);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Stevena', 'Degoey', 'sdegoeyu@wikia.com', 127561, 'Technology', 'Analog Circuit Design manager', 'https://www.linkedin.com/profile/698429606', 55);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Rafe', 'Jordeson', 'rjordesonv@wordpress.org', 82954, 'Technology', 'Web Designer I', 'https://www.linkedin.com/profile/932884228', 9);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Wallace', 'Weavers', 'wweaversw@imageshack.us', 250578, 'Technology', 'Electrical Engineer', 'https://www.linkedin.com/profile/327028777', 23);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Ebonee', 'Klauer', 'eklauerx@webnode.com', 480811, 'Manufacturing', 'Nuclear Power Engineer', 'https://www.linkedin.com/profile/514931121', 5);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Ely', 'Olyunin', 'eolyuniny@netvibes.com', 416141, 'Entertainment', 'Accounting Assistant IV', 'https://www.linkedin.com/profile/335974952', 40);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Pippy', 'Maccari', 'pmaccariz@simplemachines.org', 52864, 'Finance', 'Teacher', 'https://www.linkedin.com/profile/370186602', 48);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Mina', 'Cubberley', 'mcubberley10@infoseek.co.jp', 201660, 'Education', 'Design Engineer', 'https://www.linkedin.com/profile/966181372', 42);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Jack', 'Lindop', 'jlindop11@wikispaces.com', 215217, 'Manufacturing', 'Accounting Assistant I', 'https://www.linkedin.com/profile/693342194', 55);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Bobby', 'Quesne', 'bquesne12@flavors.me', 318320, 'Manufacturing', 'Assistant Media Planner', 'https://www.linkedin.com/profile/980182704', 31);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Bibby', 'Cornelius', 'bcornelius13@auda.org.au', 286906, 'Education', 'Electrical Engineer', 'https://www.linkedin.com/profile/187624394', 1);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Ephrem', 'O''Feeney', 'eofeeney14@google.com', 45466, 'Entertainment', 'Nuclear Power Engineer', 'https://www.linkedin.com/profile/658232084', 44);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Kendra', 'Wattinham', 'kwattinham15@nsw.gov.au', 391223, 'Healthcare', 'Senior Editor', 'https://www.linkedin.com/profile/623240841', 14);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Pascal', 'Siggers', 'psiggers16@google.it', 222360, 'Technology', 'Environmental Specialist', 'https://www.linkedin.com/profile/772553984', 46);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Avictor', 'Millier', 'amillier17@devhub.com', 433451, 'Finance', 'Technical Writer', 'https://www.linkedin.com/profile/999214925', 6);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Ursula', 'Dulin', 'udulin18@weibo.com', 138368, 'Technology', 'Environmental Tech', 'https://www.linkedin.com/profile/613174814', 4);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Lilias', 'Shalcras', 'lshalcras19@mozilla.com', 447631, 'Entertainment', 'Technical Writer', 'https://www.linkedin.com/profile/650924486', 26);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Chancey', 'Ferrea', 'cferrea1a@vinaora.com', 478306, 'Technology', 'Senior Financial Analyst', 'https://www.linkedin.com/profile/345686785', 33);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Steffie', 'Broadbear', 'sbroadbear1b@usa.gov', 54337, 'Retail', 'Paralegal', 'https://www.linkedin.com/profile/220081181', 29);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Liv', 'Santi', 'lsanti1c@hibu.com', 314564, 'Technology', 'Structural Engineer', 'https://www.linkedin.com/profile/207852922', 13);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Tremain', 'Phipson', 'tphipson1d@usa.gov', 322025, 'Finance', 'Staff Accountant I', 'https://www.linkedin.com/profile/689952237', 37);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Aldwin', 'Fante', 'afante1e@surveymonkey.com', 378091, 'Technology', 'Programmer Analyst I', 'https://www.linkedin.com/profile/479290929', 1);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Field', 'Fursland', 'ffursland1f@mac.com', 53083, 'Education', 'Senior Cost Accountant', 'https://www.linkedin.com/profile/228280722', 7);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Ema', 'Piotr', 'epiotr1g@yandex.ru', 459018, 'Retail', 'Administrative Assistant I', 'https://www.linkedin.com/profile/254086653', 31);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Deena', 'Skingley', 'dskingley1h@whitehouse.gov', 323495, 'Education', 'Assistant Media Planner', 'https://www.linkedin.com/profile/739904105', 2);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Olly', 'McMorran', 'omcmorran1i@springer.com', 332226, 'Healthcare', 'Staff Accountant II', 'https://www.linkedin.com/profile/834487469', 33);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Mattie', 'Pren', 'mpren1j@skyrock.com', 138158, 'Technology', 'Technical Writer', 'https://www.linkedin.com/profile/183323120', 44);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Denni', 'Kemson', 'dkemson1k@ucoz.com', 259487, 'Education', 'Data Coordinator', 'https://www.linkedin.com/profile/520663977', 34);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Kaye', 'Gillmore', 'kgillmore1l@virginia.edu', 305700, 'Retail', 'Clinical Specialist', 'https://www.linkedin.com/profile/825652747', 19);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Austine', 'Ponde', 'aponde1m@hud.gov', 212984, 'Technology', 'Senior Financial Analyst', 'https://www.linkedin.com/profile/981431336', 34);
insert into Alumni (firstname, lastname, email, salary, industry, jobTitle, linkedin, empid) values ('Willem', 'Deane', 'wdeane1n@answers.com', 68863, 'Education', 'Web Developer I', 'https://www.linkedin.com/profile/344038260', 19);

-- insert into recruiters
insert into Recruiters (firstname, lastname, email, empid) values ('Kristi', 'Jesse', 'kjesse0@nbcnews.com', 1);
insert into Recruiters (firstname, lastname, email, empid) values ('Drucill', 'Martello', 'dmartello1@artisteer.com', 2);
insert into Recruiters (firstname, lastname, email, empid) values ('Mathilde', 'Durbridge', 'mdurbridge2@craigslist.org', 3);
insert into Recruiters (firstname, lastname, email, empid) values ('Dennie', 'Heathorn', 'dheathorn3@vimeo.com', 4);
insert into Recruiters (firstname, lastname, email, empid) values ('Florance', 'Chadwell', 'fchadwell4@prweb.com', 5);
insert into Recruiters (firstname, lastname, email, empid) values ('Elnore', 'Edgin', 'eedgin5@apple.com', 6);
insert into Recruiters (firstname, lastname, email, empid) values ('Dun', 'Fireman', 'dfireman6@geocities.com', 7);
insert into Recruiters (firstname, lastname, email, empid) values ('Nesta', 'Postan', 'npostan7@businessinsider.com', 8);
insert into Recruiters (firstname, lastname, email, empid) values ('Isiahi', 'Merida', 'imerida8@google.nl', 9);
insert into Recruiters (firstname, lastname, email, empid) values ('Davie', 'Blabie', 'dblabie9@cornell.edu', 10);
insert into Recruiters (firstname, lastname, email, empid) values ('Lauree', 'Giovannazzi', 'lgiovannazzia@cyberchimps.com', 11);
insert into Recruiters (firstname, lastname, email, empid) values ('Orrin', 'Ziemecki', 'oziemeckib@elegantthemes.com', 12);
insert into Recruiters (firstname, lastname, email, empid) values ('Blinny', 'Mitkin', 'bmitkinc@paginegialle.it', 13);
insert into Recruiters (firstname, lastname, email, empid) values ('Lewiss', 'Scarratt', 'lscarrattd@wiley.com', 14);
insert into Recruiters (firstname, lastname, email, empid) values ('Anselm', 'Gumme', 'agummee@typepad.com', 15);
insert into Recruiters (firstname, lastname, email, empid) values ('Phebe', 'Laming', 'plamingf@blogger.com', 16);
insert into Recruiters (firstname, lastname, email, empid) values ('Oralie', 'Drakes', 'odrakesg@vimeo.com', 17);
insert into Recruiters (firstname, lastname, email, empid) values ('Norbert', 'Brusin', 'nbrusinh@engadget.com', 18);
insert into Recruiters (firstname, lastname, email, empid) values ('Timothee', 'Ansty', 'tanstyi@hostgator.com', 19);
insert into Recruiters (firstname, lastname, email, empid) values ('Lavena', 'Van Bruggen', 'lvanbruggenj@bandcamp.com', 20);
insert into Recruiters (firstname, lastname, email, empid) values ('Dwain', 'McCoole', 'dmccoolek@independent.co.uk', 21);
insert into Recruiters (firstname, lastname, email, empid) values ('Laurette', 'Reeman', 'lreemanl@w3.org', 22);
insert into Recruiters (firstname, lastname, email, empid) values ('Guinevere', 'Forshaw', 'gforshawm@homestead.com', 23);
insert into Recruiters (firstname, lastname, email, empid) values ('Ali', 'Margarson', 'amargarsonn@sphinn.com', 24);
insert into Recruiters (firstname, lastname, email, empid) values ('Nerty', 'Stratford', 'nstratfordo@blinklist.com', 25);
insert into Recruiters (firstname, lastname, email, empid) values ('Worth', 'Steuart', 'wsteuartp@howstuffworks.com', 26);
insert into Recruiters (firstname, lastname, email, empid) values ('Ephrem', 'Bartlomiej', 'ebartlomiejq@va.gov', 27);
insert into Recruiters (firstname, lastname, email, empid) values ('Briney', 'Dowers', 'bdowersr@wikia.com', 28);
insert into Recruiters (firstname, lastname, email, empid) values ('Jeannine', 'Gabbidon', 'jgabbidons@posterous.com', 29);
insert into Recruiters (firstname, lastname, email, empid) values ('Catarina', 'Whiteoak', 'cwhiteoakt@nba.com', 30);
insert into Recruiters (firstname, lastname, email, empid) values ('Bibbye', 'Goford', 'bgofordu@edublogs.org', 31);
insert into Recruiters (firstname, lastname, email, empid) values ('Ingar', 'Gaiter', 'igaiterv@cbsnews.com', 32);
insert into Recruiters (firstname, lastname, email, empid) values ('Ruperta', 'Smurfitt', 'rsmurfittw@gravatar.com', 33);
insert into Recruiters (firstname, lastname, email, empid) values ('Barbee', 'Abdy', 'babdyx@shareasale.com', 34);
insert into Recruiters (firstname, lastname, email, empid) values ('Dorthea', 'Urey', 'dureyy@php.net', 35);
insert into Recruiters (firstname, lastname, email, empid) values ('Joanne', 'Halpin', 'jhalpinz@cornell.edu', 36);
insert into Recruiters (firstname, lastname, email, empid) values ('Wright', 'Lindroos', 'wlindroos10@ed.gov', 37);
insert into Recruiters (firstname, lastname, email, empid) values ('Anthony', 'Scutt', 'ascutt11@zimbio.com', 38);
insert into Recruiters (firstname, lastname, email, empid) values ('Crissy', 'Kaygill', 'ckaygill12@samsung.com', 39);
insert into Recruiters (firstname, lastname, email, empid) values ('Emylee', 'Goudard', 'egoudard13@latimes.com', 40);
insert into Recruiters (firstname, lastname, email, empid) values ('Lesly', 'Ughini', 'lughini14@sourceforge.net', 41);
insert into Recruiters (firstname, lastname, email, empid) values ('Alayne', 'Grisley', 'agrisley15@hp.com', 42);
insert into Recruiters (firstname, lastname, email, empid) values ('Glad', 'Larter', 'glarter16@hugedomains.com', 43);
insert into Recruiters (firstname, lastname, email, empid) values ('Christiano', 'Jacke', 'cjacke17@ucla.edu', 44);
insert into Recruiters (firstname, lastname, email, empid) values ('Tobi', 'Duckworth', 'tduckworth18@oaic.gov.au', 45);
insert into Recruiters (firstname, lastname, email, empid) values ('Vanny', 'Willicott', 'vwillicott19@oakley.com', 46);
insert into Recruiters (firstname, lastname, email, empid) values ('Bryana', 'Indgs', 'bindgs1a@techcrunch.com', 47);
insert into Recruiters (firstname, lastname, email, empid) values ('Sidoney', 'Blundell', 'sblundell1b@github.com', 48);
insert into Recruiters (firstname, lastname, email, empid) values ('Nadeen', 'Dinan', 'ndinan1c@tripadvisor.com', 49);
insert into Recruiters (firstname, lastname, email, empid) values ('Bord', 'Lamburn', 'blamburn1d@theatlantic.com', 50);
insert into Recruiters (firstname, lastname, email, empid) values ('Valentijn', 'Prise', 'vprise1e@gravatar.com', 51);
insert into Recruiters (firstname, lastname, email, empid) values ('Bekki', 'Edes', 'bedes1f@cloudflare.com', 52);
insert into Recruiters (firstname, lastname, email, empid) values ('Skipp', 'Godfery', 'sgodfery1g@icio.us', 53);
insert into Recruiters (firstname, lastname, email, empid) values ('Glennie', 'Brann', 'gbrann1h@netscape.com', 54);
insert into Recruiters (firstname, lastname, email, empid) values ('Sylvan', 'Daldan', 'sdaldan1i@usa.gov', 55);

-- insert into jobposting
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Human Resources Intern', 'Konde', 'Construction', '2023-05-10 03:20:25', 'budgeting', 50, 42);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Accounting Intern', 'Tammela', 'Education', '2024-10-23 21:16:34', 'Collaborate with the development team to design', 18, 1);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Sales Intern', 'Tianguá', 'Entertainment', '2022-12-21 00:26:12', 'Help identify new business opportunities', 19, 9);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Social Media Intern', 'Solotcha', 'Retail', '2022-12-12 02:56:16', 'Assist with financial analysis', 37, 43);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Software Engineer Intern', 'San Rafael', 'Education', '2023-04-22 07:20:50', 'including graphics and layouts for digital and print media', 35, 32);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Social Media Intern', 'Falun', 'Finance', '2023-05-09 23:49:42', 'while learning about design tools and branding', 35, 21);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Software Engineer Intern', 'Liuduzhai', 'Construction', '2023-07-21 10:34:51', 'and maintaining personnel records', 24, 54);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Research Assistant Intern', 'Koani Ndogo', 'Finance', '2023-09-18 15:55:05', 'and preparing reports while gaining exposure to accounting and financial modeling', 33, 26);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Business Development Intern', 'Omaha', 'Healthcare', '2024-08-09 03:51:06', 'Assist with financial analysis', 31, 46);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Accounting Intern', 'Itaguaí', 'Healthcare', '2024-08-09 07:30:22', 'and providing excellent service through phone and email communication', 47, 48);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Data Analyst Intern', 'Novyye Kuz’minki', 'Healthcare', '2023-01-29 19:28:58', 'and creating content for social media and digital platforms', 46, 8);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Human Resources Intern', 'Slobidka', 'Healthcare', '2023-03-10 21:45:37', 'analyzing', 36, 45);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Content Writer Intern', 'Baisha', 'Entertainment', '2024-10-20 08:17:34', 'and providing excellent service through phone and email communication', 30, 53);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Web Developer Intern', 'Dundbürd', 'Manufacturing', '2023-05-22 05:55:33', 'budgeting', 47, 10);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Data Analyst Intern', 'Harjavalta', 'Entertainment', '2024-06-07 10:06:11', 'Assist in developing marketing strategies', 27, 24);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Business Development Intern', 'Novo Aripuanã', 'Retail', '2024-03-20 09:30:51', 'Assist in collecting', 39, 35);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Customer Service Intern', 'Xingfeng', 'Finance', '2024-09-09 20:56:15', 'Work on creating visual content', 40, 49);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Data Analyst Intern', 'San Javier', 'Entertainment', '2023-11-03 05:33:07', 'improve efficiency', 30, 55);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Business Development Intern', 'Sibulan', 'Finance', '2023-08-06 09:25:16', 'Work on creating visual content', 28, 31);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Project Manager Intern', 'Semarapura', 'Retail', '2024-10-05 11:44:14', 'Help identify new business opportunities', 30, 2);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Content Writer Intern', 'Heping', 'Finance', '2023-05-25 04:28:40', 'articles', 19, 1);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Social Media Intern', 'Alvito de São Pedro', 'Manufacturing', '2024-02-27 23:32:48', 'while learning about design tools and branding', 21, 52);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Network Administrator Intern', 'Tancheng', 'Retail', '2023-08-31 07:20:39', 'Support the customer service team by handling inquiries', 48, 54);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Research Assistant Intern', 'La Unión', 'Healthcare', '2024-04-16 23:22:34', 'budgeting', 39, 36);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Web Developer Intern', 'Basa', 'Technology', '2023-12-01 23:36:35', 'Assist in collecting', 44, 12);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Research Assistant Intern', 'Qiaodong', 'Entertainment', '2024-01-24 12:17:01', 'conducting market research', 19, 31);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('UX/UI Designer Intern', 'Antes', 'Technology', '2024-03-29 22:41:06', 'and providing excellent service through phone and email communication', 44, 30);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Customer Service Intern', 'Dayapan', 'Education', '2022-12-28 00:41:29', 'Assist in collecting', 31, 45);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Sales Intern', 'Yangdu', 'Education', '2023-01-05 09:59:58', 'Support the HR team with recruitment processes', 40, 15);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Data Analyst Intern', 'Vale Mourão', 'Construction', '2024-06-13 07:41:03', 'and maintaining personnel records', 50, 21);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Business Development Intern', 'Xiadu', 'Finance', '2023-02-18 05:08:52', 'Assist in developing marketing strategies', 45, 5);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Accounting Intern', 'Crossmolina', 'Education', '2023-04-21 06:51:40', 'Assist in collecting', 28, 14);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Sales Intern', 'Gomel', 'Education', '2024-02-10 18:40:02', 'and support the sales team with administrative tasks', 49, 51);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Customer Service Intern', 'Castrovirreyna', 'Retail', '2024-08-04 18:09:08', 'analyzing', 29, 55);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('UX/UI Designer Intern', 'Xingfu', 'Technology', '2023-05-04 16:30:13', 'and creating content for social media and digital platforms', 46, 42);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Project Manager Intern', 'Chengguan', 'Construction', '2023-03-11 21:24:38', 'Assist in developing marketing strategies', 35, 39);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Data Analyst Intern', 'Yihe', 'Construction', '2024-07-03 00:44:35', 'test', 21, 41);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Business Development Intern', 'Knyazhichi', 'Construction', '2023-09-15 16:27:28', 'and social media content', 32, 5);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Human Resources Intern', 'Kuala Lumpur', 'Healthcare', '2024-08-06 12:36:10', 'Work alongside the operations team to streamline processes', 32, 33);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Quality Assurance Intern', 'Bretaña', 'Education', '2024-06-19 06:39:00', 'Help identify new business opportunities', 50, 13);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Human Resources Intern', 'Caluire-et-Cuire', 'Education', '2023-08-07 06:46:27', 'Assist with financial analysis', 23, 2);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Project Manager Intern', 'Sokol', 'Manufacturing', '2023-07-21 10:25:15', 'Support the HR team with recruitment processes', 18, 15);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Legal Intern', 'Cangkreng', 'Education', '2024-02-19 01:45:18', 'and social media content', 35, 27);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Accounting Intern', 'Alminhas', 'Construction', '2024-05-09 05:00:43', 'employee onboarding', 49, 27);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Quality Assurance Intern', 'Qarāwul', 'Healthcare', '2024-09-14 12:51:55', 'and deploy new software features while gaining hands-on experience with coding and development tools', 37, 42);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Network Administrator Intern', 'Shatura', 'Education', '2023-11-29 21:28:57', 'and deploy new software features while gaining hands-on experience with coding and development tools', 23, 29);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Accounting Intern', 'Gibbons', 'Healthcare', '2024-05-31 15:47:21', 'Write and edit blog posts', 29, 30);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('IT Support Intern', 'Al ‘Azīzīyah', 'Entertainment', '2023-07-01 07:32:28', 'Assist in developing marketing strategies', 18, 40);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Research Assistant Intern', 'Shucheng Chengguanzhen', 'Finance', '2024-09-13 10:17:26', 'articles', 49, 46);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Product Manager Intern', 'Balung Barat', 'Technology', '2023-02-27 04:43:18', 'employee onboarding', 23, 4);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Network Administrator Intern', 'San Luis', 'Entertainment', '2022-12-14 19:33:07', 'budgeting', 34, 15);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Sales Intern', 'Dianwan', 'Technology', '2024-03-12 01:45:32', 'articles', 23, 20);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Business Development Intern', 'Nymburk', 'Manufacturing', '2024-04-28 09:13:54', 'and deploy new software features while gaining hands-on experience with coding and development tools', 46, 42);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('IT Support Intern', 'Sant Cugat Del Valles', 'Manufacturing', '2023-01-14 16:10:00', 'assist in managing client relationships', 46, 49);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Data Analyst Intern', 'Kiernozia', 'Technology', '2023-12-07 06:39:05', 'Support the customer service team by handling inquiries', 45, 9);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Software Engineer Intern', 'Zheleznogorsk', 'Finance', '2023-10-21 16:27:31', 'Work alongside the operations team to streamline processes', 46, 46);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Content Writer Intern', 'New York City', 'Education', '2023-04-19 18:49:56', 'and deploy new software features while gaining hands-on experience with coding and development tools', 37, 54);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Graphic Designer Intern', 'Pita', 'Entertainment', '2023-09-25 10:23:26', 'and social media content', 28, 45);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Accounting Intern', 'Cubará', 'Healthcare', '2023-01-30 00:40:08', 'test', 28, 22);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('UX/UI Designer Intern', 'Madīnat ash Shamāl', 'Entertainment', '2022-12-10 02:50:59', 'Assist in collecting', 46, 18);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Social Media Intern', 'Båstad', 'Education', '2023-09-30 20:47:16', 'test', 29, 12);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Product Manager Intern', 'Anseong', 'Manufacturing', '2023-04-25 05:14:00', 'resolving issues', 39, 35);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Product Manager Intern', 'Guishan', 'Construction', '2023-12-12 23:11:54', 'and providing excellent service through phone and email communication', 46, 44);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Business Development Intern', 'Prámanta', 'Finance', '2024-05-30 16:36:25', 'Collaborate with the development team to design', 45, 6);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Web Developer Intern', 'Aniso', 'Technology', '2023-04-14 16:48:11', 'and providing excellent service through phone and email communication', 45, 41);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Customer Service Intern', '‘Anātā', 'Healthcare', '2023-09-02 22:02:12', 'and social media content', 38, 2);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Sales Intern', 'Terong', 'Entertainment', '2024-02-18 01:29:27', 'budgeting', 47, 41);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Human Resources Intern', 'Rawson', 'Healthcare', '2024-03-08 05:33:08', 'and creating content for social media and digital platforms', 40, 20);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('Marketing Intern', 'Austin', 'Technology', '2023-01-30 17:49:14', 'employee onboarding', 24, 7);
insert into JobPosting (title, location, industry, applybydate, description, salary, recruiterid) values ('UX/UI Designer Intern', 'Valerianovsk', 'Manufacturing', '2024-10-25 17:22:32', 'and social media content', 25, 21);

-- insert into postingskills
insert into PostingSkills (jobid, skillid) values (28, 27);
insert into PostingSkills (jobid, skillid) values (53, 28);
insert into PostingSkills (jobid, skillid) values (59, 32);
insert into PostingSkills (jobid, skillid) values (70, 34);
insert into PostingSkills (jobid, skillid) values (66, 31);
insert into PostingSkills (jobid, skillid) values (32, 31);
insert into PostingSkills (jobid, skillid) values (7, 6);
insert into PostingSkills (jobid, skillid) values (46, 1);
insert into PostingSkills (jobid, skillid) values (35, 4);
insert into PostingSkills (jobid, skillid) values (27, 7);
insert into PostingSkills (jobid, skillid) values (54, 36);
insert into PostingSkills (jobid, skillid) values (35, 13);
insert into PostingSkills (jobid, skillid) values (25, 33);
insert into PostingSkills (jobid, skillid) values (38, 23);
insert into PostingSkills (jobid, skillid) values (25, 26);
insert into PostingSkills (jobid, skillid) values (19, 11);
insert into PostingSkills (jobid, skillid) values (27, 37);
insert into PostingSkills (jobid, skillid) values (36, 9);
insert into PostingSkills (jobid, skillid) values (49, 20);
insert into PostingSkills (jobid, skillid) values (50, 39);
insert into PostingSkills (jobid, skillid) values (38, 13);
insert into PostingSkills (jobid, skillid) values (13, 28);
insert into PostingSkills (jobid, skillid) values (51, 39);
insert into PostingSkills (jobid, skillid) values (48, 37);
insert into PostingSkills (jobid, skillid) values (1, 3);
insert into PostingSkills (jobid, skillid) values (56, 19);
insert into PostingSkills (jobid, skillid) values (41, 10);
insert into PostingSkills (jobid, skillid) values (57, 5);
insert into PostingSkills (jobid, skillid) values (44, 24);
insert into PostingSkills (jobid, skillid) values (70, 10);
insert into PostingSkills (jobid, skillid) values (30, 38);
insert into PostingSkills (jobid, skillid) values (38, 18);
insert into PostingSkills (jobid, skillid) values (10, 38);
insert into PostingSkills (jobid, skillid) values (7, 16);
insert into PostingSkills (jobid, skillid) values (19, 30);
insert into PostingSkills (jobid, skillid) values (39, 27);
insert into PostingSkills (jobid, skillid) values (33, 27);
insert into PostingSkills (jobid, skillid) values (34, 8);
insert into PostingSkills (jobid, skillid) values (70, 7);
insert into PostingSkills (jobid, skillid) values (9, 19);
insert into PostingSkills (jobid, skillid) values (63, 6);
insert into PostingSkills (jobid, skillid) values (48, 28);
insert into PostingSkills (jobid, skillid) values (41, 9);
insert into PostingSkills (jobid, skillid) values (3, 34);
insert into PostingSkills (jobid, skillid) values (4, 34);
insert into PostingSkills (jobid, skillid) values (24, 14);
insert into PostingSkills (jobid, skillid) values (21, 4);
insert into PostingSkills (jobid, skillid) values (37, 30);
insert into PostingSkills (jobid, skillid) values (49, 25);
insert into PostingSkills (jobid, skillid) values (2, 27);
insert into PostingSkills (jobid, skillid) values (51, 12);
insert into PostingSkills (jobid, skillid) values (18, 17);
insert into PostingSkills (jobid, skillid) values (39, 19);
insert into PostingSkills (jobid, skillid) values (61, 3);
insert into PostingSkills (jobid, skillid) values (13, 27);
insert into PostingSkills (jobid, skillid) values (2, 9);
insert into PostingSkills (jobid, skillid) values (69, 29);
insert into PostingSkills (jobid, skillid) values (26, 25);
insert into PostingSkills (jobid, skillid) values (8, 37);
insert into PostingSkills (jobid, skillid) values (32, 26);
insert into PostingSkills (jobid, skillid) values (60, 7);
insert into PostingSkills (jobid, skillid) values (52, 5);
insert into PostingSkills (jobid, skillid) values (31, 10);
insert into PostingSkills (jobid, skillid) values (17, 21);
insert into PostingSkills (jobid, skillid) values (67, 3);
insert into PostingSkills (jobid, skillid) values (55, 23);
insert into PostingSkills (jobid, skillid) values (44, 22);
insert into PostingSkills (jobid, skillid) values (17, 5);
insert into PostingSkills (jobid, skillid) values (26, 40);
insert into PostingSkills (jobid, skillid) values (29, 13);
insert into PostingSkills (jobid, skillid) values (43, 6);
insert into PostingSkills (jobid, skillid) values (31, 11);
insert into PostingSkills (jobid, skillid) values (21, 16);
insert into PostingSkills (jobid, skillid) values (17, 9);
insert into PostingSkills (jobid, skillid) values (49, 3);
insert into PostingSkills (jobid, skillid) values (20, 34);
insert into PostingSkills (jobid, skillid) values (46, 5);
insert into PostingSkills (jobid, skillid) values (41, 3);
insert into PostingSkills (jobid, skillid) values (53, 23);
insert into PostingSkills (jobid, skillid) values (16, 14);
insert into PostingSkills (jobid, skillid) values (14, 38);
insert into PostingSkills (jobid, skillid) values (69, 9);
insert into PostingSkills (jobid, skillid) values (24, 39);
insert into PostingSkills (jobid, skillid) values (68, 28);
insert into PostingSkills (jobid, skillid) values (7, 21);
insert into PostingSkills (jobid, skillid) values (8, 28);
insert into PostingSkills (jobid, skillid) values (60, 6);
insert into PostingSkills (jobid, skillid) values (16, 10);
insert into PostingSkills (jobid, skillid) values (69, 21);
insert into PostingSkills (jobid, skillid) values (43, 13);
insert into PostingSkills (jobid, skillid) values (34, 14);
insert into PostingSkills (jobid, skillid) values (56, 37);
insert into PostingSkills (jobid, skillid) values (68, 2);
insert into PostingSkills (jobid, skillid) values (21, 29);
insert into PostingSkills (jobid, skillid) values (42, 29);
insert into PostingSkills (jobid, skillid) values (45, 17);
insert into PostingSkills (jobid, skillid) values (3, 23);
insert into PostingSkills (jobid, skillid) values (38, 2);
insert into PostingSkills (jobid, skillid) values (11, 35);
insert into PostingSkills (jobid, skillid) values (16, 38);

-- insert into Applications
insert into Applications (studentid, jobid, status, date) values (47, 26, 'Rejected', '2022-05-11 08:10:40');
insert into Applications (studentid, jobid, status, date) values (37, 57, 'Accepted', '2022-05-23 16:03:03');
insert into Applications (studentid, jobid, status, date) values (49, 10, 'Accepted', '2022-05-17 12:27:56');
insert into Applications (studentid, jobid, status, date) values (3, 39, 'Pending', '2021-11-23 08:37:22');
insert into Applications (studentid, jobid, status, date) values (23, 56, 'Pending', '2022-10-09 07:42:12');
insert into Applications (studentid, jobid, status, date) values (11, 50, 'Pending', '2022-03-03 15:45:15');
insert into Applications (studentid, jobid, status, date) values (36, 56, 'Accepted', '2022-07-29 22:56:00');
insert into Applications (studentid, jobid, status, date) values (16, 29, 'Pending', '2022-02-05 21:06:34');
insert into Applications (studentid, jobid, status, date) values (49, 35, 'Pending', '2022-01-19 13:12:03');
insert into Applications (studentid, jobid, status, date) values (8, 12, 'Accepted', '2022-03-22 22:55:49');
insert into Applications (studentid, jobid, status, date) values (29, 69, 'Pending', '2022-07-10 16:20:10');
insert into Applications (studentid, jobid, status, date) values (4, 47, 'Rejected', '2022-06-28 06:54:29');
insert into Applications (studentid, jobid, status, date) values (28, 33, 'Rejected', '2021-11-26 11:31:11');
insert into Applications (studentid, jobid, status, date) values (21, 14, 'Pending', '2022-06-18 03:28:27');
insert into Applications (studentid, jobid, status, date) values (15, 38, 'Pending', '2022-05-15 23:51:46');
insert into Applications (studentid, jobid, status, date) values (48, 59, 'Pending', '2022-10-25 06:53:45');
insert into Applications (studentid, jobid, status, date) values (39, 55, 'Rejected', '2022-08-16 02:10:45');
insert into Applications (studentid, jobid, status, date) values (11, 12, 'Rejected', '2022-04-28 14:36:04');
insert into Applications (studentid, jobid, status, date) values (16, 52, 'Rejected', '2022-06-02 22:35:58');
insert into Applications (studentid, jobid, status, date) values (11, 46, 'Accepted', '2021-12-20 20:11:51');
insert into Applications (studentid, jobid, status, date) values (6, 40, 'Pending', '2022-06-21 20:17:47');
insert into Applications (studentid, jobid, status, date) values (42, 62, 'Rejected', '2022-01-09 04:50:14');
insert into Applications (studentid, jobid, status, date) values (38, 8, 'Rejected', '2022-06-09 19:47:55');
insert into Applications (studentid, jobid, status, date) values (49, 49, 'Rejected', '2022-03-11 03:24:57');
insert into Applications (studentid, jobid, status, date) values (25, 13, 'Rejected', '2022-04-16 12:24:34');
insert into Applications (studentid, jobid, status, date) values (18, 52, 'Pending', '2022-06-10 02:18:57');
insert into Applications (studentid, jobid, status, date) values (44, 38, 'Rejected', '2022-08-03 13:11:57');
insert into Applications (studentid, jobid, status, date) values (50, 39, 'Pending', '2022-05-09 16:52:42');
insert into Applications (studentid, jobid, status, date) values (27, 39, 'Rejected', '2022-10-25 05:14:13');
insert into Applications (studentid, jobid, status, date) values (33, 32, 'Accepted', '2022-07-27 14:03:50');
insert into Applications (studentid, jobid, status, date) values (43, 18, 'Pending', '2022-06-16 01:19:51');
insert into Applications (studentid, jobid, status, date) values (5, 52, 'Accepted', '2022-04-09 16:12:34');
insert into Applications (studentid, jobid, status, date) values (30, 35, 'Rejected', '2022-08-19 22:24:18');
insert into Applications (studentid, jobid, status, date) values (45, 25, 'Rejected', '2022-06-10 03:34:10');
insert into Applications (studentid, jobid, status, date) values (15, 59, 'Rejected', '2021-12-05 05:04:20');
insert into Applications (studentid, jobid, status, date) values (5, 36, 'Pending', '2022-07-19 17:46:44');
insert into Applications (studentid, jobid, status, date) values (20, 41, 'Pending', '2022-10-22 22:55:59');
insert into Applications (studentid, jobid, status, date) values (19, 16, 'Pending', '2022-11-02 09:42:20');
insert into Applications (studentid, jobid, status, date) values (37, 22, 'Rejected', '2022-09-28 05:05:37');
insert into Applications (studentid, jobid, status, date) values (22, 64, 'Pending', '2021-12-10 10:26:30');
insert into Applications (studentid, jobid, status, date) values (11, 11, 'Accepted', '2022-07-08 07:23:06');
insert into Applications (studentid, jobid, status, date) values (33, 64, 'Pending', '2022-03-11 12:57:24');
insert into Applications (studentid, jobid, status, date) values (40, 25, 'Accepted', '2022-03-12 14:05:51');
insert into Applications (studentid, jobid, status, date) values (37, 62, 'Rejected', '2022-11-03 05:37:34');
insert into Applications (studentid, jobid, status, date) values (10, 15, 'Accepted', '2022-07-16 10:29:42');
insert into Applications (studentid, jobid, status, date) values (3, 19, 'Accepted', '2022-03-31 06:50:47');
insert into Applications (studentid, jobid, status, date) values (4, 55, 'Accepted', '2022-09-08 03:38:27');
insert into Applications (studentid, jobid, status, date) values (16, 25, 'Accepted', '2022-06-26 17:12:19');
insert into Applications (studentid, jobid, status, date) values (27, 1, 'Pending', '2022-02-24 22:55:15');
insert into Applications (studentid, jobid, status, date) values (17, 20, 'Pending', '2022-03-24 03:17:07');
insert into Applications (studentid, jobid, status, date) values (14, 63, 'Pending', '2022-08-05 09:57:13');
insert into Applications (studentid, jobid, status, date) values (8, 42, 'Accepted', '2022-10-17 07:00:33');
insert into Applications (studentid, jobid, status, date) values (1, 42, 'Rejected', '2022-06-28 09:23:30');
insert into Applications (studentid, jobid, status, date) values (32, 39, 'Pending', '2022-04-01 03:10:56');
insert into Applications (studentid, jobid, status, date) values (17, 15, 'Rejected', '2022-06-02 11:59:16');
insert into Applications (studentid, jobid, status, date) values (11, 5, 'Accepted', '2022-06-02 22:19:25');
insert into Applications (studentid, jobid, status, date) values (33, 12, 'Accepted', '2022-02-07 00:36:11');
insert into Applications (studentid, jobid, status, date) values (17, 28, 'Rejected', '2022-04-08 18:47:51');
insert into Applications (studentid, jobid, status, date) values (4, 62, 'Pending', '2022-10-26 13:57:42');
insert into Applications (studentid, jobid, status, date) values (11, 6, 'Rejected', '2022-05-06 14:35:14');
insert into Applications (studentid, jobid, status, date) values (47, 10, 'Pending', '2022-05-15 08:53:23');
insert into Applications (studentid, jobid, status, date) values (33, 14, 'Accepted', '2022-03-10 21:22:49');
insert into Applications (studentid, jobid, status, date) values (25, 4, 'Accepted', '2022-01-18 16:24:47');
insert into Applications (studentid, jobid, status, date) values (25, 55, 'Rejected', '2022-02-06 16:19:34');
insert into Applications (studentid, jobid, status, date) values (7, 45, 'Pending', '2022-06-13 12:30:04');
insert into Applications (studentid, jobid, status, date) values (45, 65, 'Accepted', '2022-03-04 16:14:21');
insert into Applications (studentid, jobid, status, date) values (1, 66, 'Accepted', '2022-06-30 21:03:33');
insert into Applications (studentid, jobid, status, date) values (33, 67, 'Accepted', '2021-12-30 11:14:11');
insert into Applications (studentid, jobid, status, date) values (22, 58, 'Accepted', '2022-10-16 23:36:41');
insert into Applications (studentid, jobid, status, date) values (21, 3, 'Accepted', '2022-06-13 10:09:55');
insert into Applications (studentid, jobid, status, date) values (9, 42, 'Accepted', '2022-03-25 08:03:39');
insert into Applications (studentid, jobid, status, date) values (38, 66, 'Rejected', '2022-05-01 11:19:39');
insert into Applications (studentid, jobid, status, date) values (48, 62, 'Rejected', '2022-07-13 08:12:27');
insert into Applications (studentid, jobid, status, date) values (21, 50, 'Rejected', '2022-02-04 14:08:49');
insert into Applications (studentid, jobid, status, date) values (1, 63, 'Accepted', '2022-07-21 14:54:07');
insert into Applications (studentid, jobid, status, date) values (44, 38, 'Rejected', '2021-12-31 13:55:14');
insert into Applications (studentid, jobid, status, date) values (49, 22, 'Pending', '2022-06-01 09:08:15');
insert into Applications (studentid, jobid, status, date) values (24, 33, 'Pending', '2022-02-26 12:43:03');
insert into Applications (studentid, jobid, status, date) values (25, 1, 'Accepted', '2021-12-18 02:08:05');
insert into Applications (studentid, jobid, status, date) values (46, 32, 'Rejected', '2022-09-08 03:02:51');
insert into Applications (studentid, jobid, status, date) values (47, 5, 'Pending', '2022-02-12 14:07:37');
insert into Applications (studentid, jobid, status, date) values (20, 48, 'Pending', '2022-09-05 23:21:17');
insert into Applications (studentid, jobid, status, date) values (29, 66, 'Rejected', '2022-09-02 15:05:29');
insert into Applications (studentid, jobid, status, date) values (2, 37, 'Pending', '2022-02-16 11:45:05');
insert into Applications (studentid, jobid, status, date) values (36, 61, 'Accepted', '2022-10-28 08:25:40');
insert into Applications (studentid, jobid, status, date) values (23, 13, 'Pending', '2021-12-08 10:12:47');
insert into Applications (studentid, jobid, status, date) values (11, 22, 'Accepted', '2022-03-22 12:47:38');
insert into Applications (studentid, jobid, status, date) values (17, 2, 'Pending', '2022-07-26 15:55:27');
insert into Applications (studentid, jobid, status, date) values (19, 58, 'Pending', '2022-11-21 18:35:21');
insert into Applications (studentid, jobid, status, date) values (26, 69, 'Rejected', '2022-06-07 19:18:29');
insert into Applications (studentid, jobid, status, date) values (50, 3, 'Accepted', '2022-07-24 23:48:23');
insert into Applications (studentid, jobid, status, date) values (27, 25, 'Rejected', '2022-03-03 07:37:29');
insert into Applications (studentid, jobid, status, date) values (38, 68, 'Rejected', '2022-11-03 06:55:08');
insert into Applications (studentid, jobid, status, date) values (49, 3, 'Rejected', '2022-04-14 08:40:40');
insert into Applications (studentid, jobid, status, date) values (32, 43, 'Pending', '2022-11-22 19:12:57');
insert into Applications (studentid, jobid, status, date) values (13, 70, 'Rejected', '2022-09-23 04:15:36');
insert into Applications (studentid, jobid, status, date) values (50, 41, 'Accepted', '2022-03-07 16:32:16');
insert into Applications (studentid, jobid, status, date) values (7, 25, 'Pending', '2022-07-13 06:05:01');
insert into Applications (studentid, jobid, status, date) values (17, 15, 'Accepted', '2022-10-18 13:04:16');
insert into Applications (studentid, jobid, status, date) values (6, 32, 'Rejected', '2022-11-06 21:17:38');
insert into Applications (studentid, jobid, status, date) values (39, 42, 'Pending', '2022-06-22 12:19:09');
insert into Applications (studentid, jobid, status, date) values (23, 34, 'Accepted', '2022-06-27 11:43:10');
insert into Applications (studentid, jobid, status, date) values (8, 40, 'Accepted', '2022-03-19 04:09:40');
insert into Applications (studentid, jobid, status, date) values (30, 7, 'Rejected', '2021-12-08 00:32:15');
insert into Applications (studentid, jobid, status, date) values (44, 31, 'Accepted', '2022-02-01 18:18:20');
insert into Applications (studentid, jobid, status, date) values (9, 66, 'Accepted', '2022-07-18 18:31:18');
insert into Applications (studentid, jobid, status, date) values (21, 62, 'Accepted', '2022-08-11 02:28:46');
insert into Applications (studentid, jobid, status, date) values (9, 57, 'Rejected', '2022-07-31 10:51:50');
insert into Applications (studentid, jobid, status, date) values (22, 69, 'Accepted', '2022-11-17 03:54:38');
insert into Applications (studentid, jobid, status, date) values (48, 69, 'Accepted', '2022-05-14 19:46:56');
insert into Applications (studentid, jobid, status, date) values (29, 7, 'Pending', '2022-06-13 03:41:09');
insert into Applications (studentid, jobid, status, date) values (26, 60, 'Accepted', '2022-11-07 04:11:48');
insert into Applications (studentid, jobid, status, date) values (30, 9, 'Accepted', '2022-05-23 06:44:16');
insert into Applications (studentid, jobid, status, date) values (3, 1, 'Pending', '2022-04-18 12:32:34');
insert into Applications (studentid, jobid, status, date) values (1, 61, 'Rejected', '2021-12-31 02:30:35');
insert into Applications (studentid, jobid, status, date) values (28, 2, 'Rejected', '2022-10-24 23:38:06');
insert into Applications (studentid, jobid, status, date) values (21, 26, 'Rejected', '2022-04-30 20:24:59');
insert into Applications (studentid, jobid, status, date) values (36, 6, 'Rejected', '2022-09-10 05:03:22');
insert into Applications (studentid, jobid, status, date) values (45, 44, 'Accepted', '2021-12-09 15:35:09');
insert into Applications (studentid, jobid, status, date) values (47, 43, 'Rejected', '2022-06-27 17:03:26');
insert into Applications (studentid, jobid, status, date) values (50, 67, 'Accepted', '2021-12-26 22:54:40');
insert into Applications (studentid, jobid, status, date) values (7, 3, 'Pending', '2022-07-06 02:36:11');
insert into Applications (studentid, jobid, status, date) values (44, 60, 'Rejected', '2021-12-20 00:23:14');
insert into Applications (studentid, jobid, status, date) values (4, 38, 'Accepted', '2022-07-20 13:00:09');
insert into Applications (studentid, jobid, status, date) values (29, 12, 'Pending', '2021-12-31 19:14:29');
insert into Applications (studentid, jobid, status, date) values (37, 20, 'Pending', '2022-04-12 14:35:26');
insert into Applications (studentid, jobid, status, date) values (40, 22, 'Accepted', '2022-07-28 15:10:35');
insert into Applications (studentid, jobid, status, date) values (24, 42, 'Pending', '2022-04-27 13:36:49');
insert into Applications (studentid, jobid, status, date) values (8, 19, 'Accepted', '2022-08-12 09:34:24');
insert into Applications (studentid, jobid, status, date) values (24, 4, 'Pending', '2022-08-16 22:26:55');
insert into Applications (studentid, jobid, status, date) values (36, 43, 'Rejected', '2022-05-17 03:49:23');
insert into Applications (studentid, jobid, status, date) values (10, 70, 'Pending', '2022-08-25 16:57:05');
insert into Applications (studentid, jobid, status, date) values (40, 9, 'Pending', '2022-04-04 00:02:17');
insert into Applications (studentid, jobid, status, date) values (11, 13, 'Pending', '2021-11-29 14:50:37');
insert into Applications (studentid, jobid, status, date) values (37, 66, 'Pending', '2022-02-05 00:46:30');
insert into Applications (studentid, jobid, status, date) values (43, 27, 'Rejected', '2021-12-18 10:47:53');
insert into Applications (studentid, jobid, status, date) values (25, 47, 'Rejected', '2022-10-26 09:49:53');
insert into Applications (studentid, jobid, status, date) values (9, 50, 'Pending', '2022-01-25 18:00:43');
insert into Applications (studentid, jobid, status, date) values (41, 2, 'Rejected', '2021-12-18 23:32:01');
insert into Applications (studentid, jobid, status, date) values (41, 53, 'Accepted', '2022-09-29 01:29:25');
insert into Applications (studentid, jobid, status, date) values (5, 37, 'Accepted', '2022-06-09 11:18:18');
insert into Applications (studentid, jobid, status, date) values (20, 35, 'Rejected', '2022-04-28 07:00:44');
insert into Applications (studentid, jobid, status, date) values (29, 66, 'Accepted', '2022-05-11 18:07:09');
insert into Applications (studentid, jobid, status, date) values (45, 8, 'Accepted', '2021-12-08 06:57:16');
insert into Applications (studentid, jobid, status, date) values (46, 22, 'Rejected', '2021-12-08 01:29:31');
insert into Applications (studentid, jobid, status, date) values (49, 39, 'Pending', '2022-05-02 04:19:09');
insert into Applications (studentid, jobid, status, date) values (26, 34, 'Pending', '2021-12-23 02:00:46');
insert into Applications (studentid, jobid, status, date) values (41, 21, 'Accepted', '2022-03-11 11:33:15');
insert into Applications (studentid, jobid, status, date) values (40, 57, 'Rejected', '2022-05-06 12:20:44');
insert into Applications (studentid, jobid, status, date) values (48, 41, 'Accepted', '2022-05-11 11:58:54');
insert into Applications (studentid, jobid, status, date) values (32, 67, 'Pending', '2022-06-05 04:16:26');
insert into Applications (studentid, jobid, status, date) values (34, 49, 'Rejected', '2021-12-05 18:38:16');
insert into Applications (studentid, jobid, status, date) values (21, 45, 'Pending', '2022-07-02 04:51:39');
insert into Applications (studentid, jobid, status, date) values (3, 49, 'Rejected', '2022-05-19 12:05:44');
insert into Applications (studentid, jobid, status, date) values (42, 59, 'Pending', '2022-06-24 00:02:58');
insert into Applications (studentid, jobid, status, date) values (19, 34, 'Rejected', '2022-05-09 17:25:42');
insert into Applications (studentid, jobid, status, date) values (27, 42, 'Rejected', '2022-04-09 20:54:43');
insert into Applications (studentid, jobid, status, date) values (47, 46, 'Accepted', '2022-10-11 15:44:53');
insert into Applications (studentid, jobid, status, date) values (43, 1, 'Rejected', '2021-12-05 12:23:42');
insert into Applications (studentid, jobid, status, date) values (15, 54, 'Pending', '2022-02-19 03:53:00');
insert into Applications (studentid, jobid, status, date) values (10, 28, 'Pending', '2022-05-04 16:03:50');
insert into Applications (studentid, jobid, status, date) values (21, 15, 'Accepted', '2022-07-03 15:36:23');
insert into Applications (studentid, jobid, status, date) values (17, 9, 'Accepted', '2022-11-13 10:06:24');
insert into Applications (studentid, jobid, status, date) values (29, 60, 'Pending', '2022-09-25 15:55:06');
insert into Applications (studentid, jobid, status, date) values (25, 59, 'Rejected', '2022-08-01 07:45:32');
insert into Applications (studentid, jobid, status, date) values (24, 17, 'Accepted', '2022-03-24 02:33:56');
insert into Applications (studentid, jobid, status, date) values (40, 27, 'Pending', '2022-04-25 12:09:39');
insert into Applications (studentid, jobid, status, date) values (44, 56, 'Accepted', '2022-07-11 01:53:03');
insert into Applications (studentid, jobid, status, date) values (12, 2, 'Rejected', '2022-09-19 06:30:53');
insert into Applications (studentid, jobid, status, date) values (41, 10, 'Pending', '2022-10-03 14:48:29');
insert into Applications (studentid, jobid, status, date) values (12, 11, 'Accepted', '2022-09-29 20:19:41');
insert into Applications (studentid, jobid, status, date) values (31, 36, 'Rejected', '2022-09-20 20:40:54');
insert into Applications (studentid, jobid, status, date) values (34, 62, 'Rejected', '2022-03-18 07:10:42');
insert into Applications (studentid, jobid, status, date) values (10, 28, 'Pending', '2022-10-29 22:50:07');
insert into Applications (studentid, jobid, status, date) values (40, 4, 'Rejected', '2022-04-04 10:55:09');
insert into Applications (studentid, jobid, status, date) values (50, 10, 'Accepted', '2022-04-12 07:56:55');
insert into Applications (studentid, jobid, status, date) values (20, 61, 'Pending', '2022-06-06 05:00:20');
insert into Applications (studentid, jobid, status, date) values (31, 45, 'Accepted', '2022-02-02 02:28:53');
insert into Applications (studentid, jobid, status, date) values (22, 18, 'Pending', '2022-04-19 09:52:54');
insert into Applications (studentid, jobid, status, date) values (2, 42, 'Pending', '2022-04-28 19:24:50');
insert into Applications (studentid, jobid, status, date) values (20, 14, 'Rejected', '2022-03-24 08:29:46');
insert into Applications (studentid, jobid, status, date) values (47, 13, 'Pending', '2022-01-17 10:25:24');
insert into Applications (studentid, jobid, status, date) values (41, 67, 'Rejected', '2022-04-27 17:55:29');
insert into Applications (studentid, jobid, status, date) values (47, 49, 'Rejected', '2022-01-02 05:41:03');
insert into Applications (studentid, jobid, status, date) values (28, 24, 'Rejected', '2022-08-12 09:04:57');
insert into Applications (studentid, jobid, status, date) values (45, 11, 'Rejected', '2021-12-31 01:28:19');
insert into Applications (studentid, jobid, status, date) values (14, 30, 'Accepted', '2022-03-02 20:37:04');
insert into Applications (studentid, jobid, status, date) values (19, 11, 'Pending', '2022-05-26 21:33:46');
insert into Applications (studentid, jobid, status, date) values (44, 5, 'Rejected', '2022-09-13 00:57:36');
insert into Applications (studentid, jobid, status, date) values (33, 5, 'Rejected', '2022-01-18 23:22:13');
insert into Applications (studentid, jobid, status, date) values (2, 14, 'Accepted', '2022-08-25 03:31:24');
insert into Applications (studentid, jobid, status, date) values (33, 42, 'Rejected', '2022-06-26 16:32:17');
insert into Applications (studentid, jobid, status, date) values (11, 60, 'Accepted', '2022-10-05 23:23:15');
insert into Applications (studentid, jobid, status, date) values (6, 65, 'Rejected', '2022-11-04 04:21:53');
insert into Applications (studentid, jobid, status, date) values (1, 32, 'Rejected', '2022-02-07 06:17:37');
insert into Applications (studentid, jobid, status, date) values (4, 5, 'Accepted', '2022-10-25 05:19:46');
insert into Applications (studentid, jobid, status, date) values (39, 58, 'Rejected', '2022-01-02 00:40:44');
insert into Applications (studentid, jobid, status, date) values (9, 65, 'Accepted', '2022-11-04 06:36:55');
insert into Applications (studentid, jobid, status, date) values (30, 28, 'Accepted', '2022-01-06 06:30:30');
insert into Applications (studentid, jobid, status, date) values (43, 6, 'Rejected', '2022-07-24 04:05:55');

-- insert into student reviews
insert into ReviewsOnStudents (studentid, review) values (9, 'Always enthusiastic');
insert into ReviewsOnStudents (studentid, review) values (25, 'Great team player who contributed effectively in group projects');
insert into ReviewsOnStudents (studentid, review) values (4, 'Took on complex tasks and completed them with minimal guidance');
insert into ReviewsOnStudents (studentid, review) values (13, 'Worked well under pressure and handled multiple tasks efficiently');
insert into ReviewsOnStudents (studentid, review) values (13, 'Showed excellent time management skills and stayed organized');
insert into ReviewsOnStudents (studentid, review) values (20, 'Took on complex tasks and completed them with minimal guidance');
insert into ReviewsOnStudents (studentid, review) values (29, 'and contribute to team goals');
insert into ReviewsOnStudents (studentid, review) values (5, 'Worked well under pressure and handled multiple tasks efficiently');
insert into ReviewsOnStudents (studentid, review) values (29, 'Always enthusiastic');
insert into ReviewsOnStudents (studentid, review) values (23, 'eager to learn');
insert into ReviewsOnStudents (studentid, review) values (12, 'Exhibited creativity in problem-solving and idea generation');
insert into ReviewsOnStudents (studentid, review) values (5, 'Took on complex tasks and completed them with minimal guidance');
insert into ReviewsOnStudents (studentid, review) values (22, 'Worked well under pressure and handled multiple tasks efficiently');
insert into ReviewsOnStudents (studentid, review) values (26, 'demonstrating a strong work ethic.');
insert into ReviewsOnStudents (studentid, review) values (27, 'and contribute to team goals');
insert into ReviewsOnStudents (studentid, review) values (5, 'Showed initiative and was always willing to take on new tasks');
insert into ReviewsOnStudents (studentid, review) values (1, 'Worked well under pressure and handled multiple tasks efficiently');
insert into ReviewsOnStudents (studentid, review) values (14, 'Always enthusiastic');
insert into ReviewsOnStudents (studentid, review) values (12, 'Handled challenges with a calm and solution-oriented approach');
insert into ReviewsOnStudents (studentid, review) values (27, 'Adapted quickly to the work environment and showed growth throughout the term');
insert into ReviewsOnStudents (studentid, review) values (12, 'Took on complex tasks and completed them with minimal guidance');
insert into ReviewsOnStudents (studentid, review) values (19, 'Showed initiative and was always willing to take on new tasks');
insert into ReviewsOnStudents (studentid, review) values (6, 'demonstrating a strong work ethic.');
insert into ReviewsOnStudents (studentid, review) values (2, 'Demonstrated a strong understanding of industry tools and technologies');
insert into ReviewsOnStudents (studentid, review) values (28, 'Quickly grasped new concepts and applied them to tasks with minimal supervision');
insert into ReviewsOnStudents (studentid, review) values (20, 'Showed excellent time management skills and stayed organized');
insert into ReviewsOnStudents (studentid, review) values (21, 'Proactive and detail-oriented in completing assignments');
insert into ReviewsOnStudents (studentid, review) values (29, 'Quickly grasped new concepts and applied them to tasks with minimal supervision');
insert into ReviewsOnStudents (studentid, review) values (2, 'Showed initiative and was always willing to take on new tasks');
insert into ReviewsOnStudents (studentid, review) values (17, 'Consistently met deadlines and delivered quality work');
insert into ReviewsOnStudents (studentid, review) values (24, 'Took on complex tasks and completed them with minimal guidance');
insert into ReviewsOnStudents (studentid, review) values (29, 'Demonstrated a strong understanding of industry tools and technologies');
insert into ReviewsOnStudents (studentid, review) values (24, 'Proactive and detail-oriented in completing assignments');
insert into ReviewsOnStudents (studentid, review) values (22, 'Worked well with colleagues and maintained positive relationships');
insert into ReviewsOnStudents (studentid, review) values (2, 'Always enthusiastic');
insert into ReviewsOnStudents (studentid, review) values (25, 'Showed initiative and was always willing to take on new tasks');
insert into ReviewsOnStudents (studentid, review) values (15, 'and contribute to team goals');
insert into ReviewsOnStudents (studentid, review) values (10, 'Great team player who contributed effectively in group projects');
insert into ReviewsOnStudents (studentid, review) values (7, 'always showing up on time and prepared');
insert into ReviewsOnStudents (studentid, review) values (13, 'Quickly grasped new concepts and applied them to tasks with minimal supervision');
insert into ReviewsOnStudents (studentid, review) values (19, 'Exhibited creativity in problem-solving and idea generation');
insert into ReviewsOnStudents (studentid, review) values (25, 'Handled challenges with a calm and solution-oriented approach');
insert into ReviewsOnStudents (studentid, review) values (30, 'Exhibited creativity in problem-solving and idea generation');
insert into ReviewsOnStudents (studentid, review) values (17, 'Adapted quickly to the work environment and showed growth throughout the term');
insert into ReviewsOnStudents (studentid, review) values (23, 'eager to learn');
insert into ReviewsOnStudents (studentid, review) values (14, 'Handled challenges with a calm and solution-oriented approach');
insert into ReviewsOnStudents (studentid, review) values (15, 'Provided great support during projects and added value with fresh perspectives');
insert into ReviewsOnStudents (studentid, review) values (25, 'Exhibited creativity in problem-solving and idea generation');
insert into ReviewsOnStudents (studentid, review) values (16, 'Quickly grasped new concepts and applied them to tasks with minimal supervision');
insert into ReviewsOnStudents (studentid, review) values (17, 'Showed initiative and was always willing to take on new tasks');

-- insert into EmployerReviews
insert into ReviewsOnEmployers (employerId, review) values (39, 'The management team was always open to suggestions and new ideas');
insert into ReviewsOnEmployers (employerId, review) values (51, 'and the workplace was friendly');
insert into ReviewsOnEmployers (employerId, review) values (54, 'The company culture was not very inclusive');
insert into ReviewsOnEmployers (employerId, review) values (35, 'My supervisor was not approachable and gave little constructive feedback');
insert into ReviewsOnEmployers (employerId, review) values (26, 'Sometimes felt like I was treated as just an extra pair of hands');
insert into ReviewsOnEmployers (employerId, review) values (15, 'My supervisor was not approachable and gave little constructive feedback');
insert into ReviewsOnEmployers (employerId, review) values (22, 'The internship allowed me to work independently while still receiving guidance');
insert into ReviewsOnEmployers (employerId, review) values (20, 'I did not feel like my work was appreciated or acknowledged');
insert into ReviewsOnEmployers (employerId, review) values (1, 'I did not feel like my work was appreciated or acknowledged');
insert into ReviewsOnEmployers (employerId, review) values (16, 'A fast-paced environment that kept me engaged');
insert into ReviewsOnEmployers (employerId, review) values (21, 'The team was welcoming and always willing to assist');
insert into ReviewsOnEmployers (employerId, review) values (14, 'The company supported my career development with helpful feedback');
insert into ReviewsOnEmployers (employerId, review) values (1, 'The internship allowed me to work independently while still receiving guidance');
insert into ReviewsOnEmployers (employerId, review) values (30, 'Felt valued as an intern');
insert into ReviewsOnEmployers (employerId, review) values (38, 'The team was welcoming and always willing to assist');
insert into ReviewsOnEmployers (employerId, review) values (41, 'and communication was poor');
insert into ReviewsOnEmployers (employerId, review) values (54, 'The company culture was inclusive and encouraging');
insert into ReviewsOnEmployers (employerId, review) values (33, 'The company culture was inclusive and encouraging');
insert into ReviewsOnEmployers (employerId, review) values (49, 'The company supported my career development with helpful feedback');
insert into ReviewsOnEmployers (employerId, review) values (3, 'The team wasn’t very supportive');
insert into ReviewsOnEmployers (employerId, review) values (47, 'The company supported my career development with helpful feedback');
insert into ReviewsOnEmployers (employerId, review) values (32, 'A rewarding experience that prepared me well for my future career');
insert into ReviewsOnEmployers (employerId, review) values (3, 'Felt valued as an intern');
insert into ReviewsOnEmployers (employerId, review) values (32, 'Excellent mentorship that helped me develop new skills');
insert into ReviewsOnEmployers (employerId, review) values (25, 'The expectations were unrealistic and not communicated well.');
insert into ReviewsOnEmployers (employerId, review) values (23, 'A collaborative environment where I was able to contribute meaningfully');
insert into ReviewsOnEmployers (employerId, review) values (51, 'Felt valued as an intern');
insert into ReviewsOnEmployers (employerId, review) values (23, 'Excellent mentorship that helped me develop new skills');
insert into ReviewsOnEmployers (employerId, review) values (44, 'The team wasn’t very supportive');
insert into ReviewsOnEmployers (employerId, review) values (4, 'Good work-life balance and a positive atmosphere');
insert into ReviewsOnEmployers (employerId, review) values (38, 'I did not receive enough guidance to succeed in my tasks');
insert into ReviewsOnEmployers (employerId, review) values (37, 'Lack of mentorship made it hard to learn and grow');
insert into ReviewsOnEmployers (employerId, review) values (33, 'and I felt disconnected');
insert into ReviewsOnEmployers (employerId, review) values (47, 'Good work-life balance and a positive atmosphere');
insert into ReviewsOnEmployers (employerId, review) values (19, 'The team wasn’t very supportive');
insert into ReviewsOnEmployers (employerId, review) values (49, 'A collaborative environment where I was able to contribute meaningfully');
insert into ReviewsOnEmployers (employerId, review) values (44, 'I did not feel like my work was appreciated or acknowledged');
insert into ReviewsOnEmployers (employerId, review) values (44, 'A collaborative environment where I was able to contribute meaningfully');
insert into ReviewsOnEmployers (employerId, review) values (41, 'The company provided ample opportunities for professional growth');
insert into ReviewsOnEmployers (employerId, review) values (20, 'Gained hands-on experience in my field of study');
insert into ReviewsOnEmployers (employerId, review) values (49, 'The team wasn’t very supportive');
insert into ReviewsOnEmployers (employerId, review) values (54, 'The team was welcoming and always willing to assist');
insert into ReviewsOnEmployers (employerId, review) values (11, 'leading to confusion');
insert into ReviewsOnEmployers (employerId, review) values (33, 'and communication was poor');
insert into ReviewsOnEmployers (employerId, review) values (2, 'Limited opportunities for networking and professional connections');
insert into ReviewsOnEmployers (employerId, review) values (42, 'A rewarding experience that prepared me well for my future career');
insert into ReviewsOnEmployers (employerId, review) values (18, 'Everyone was approachable');
insert into ReviewsOnEmployers (employerId, review) values (8, 'Great learning experience with supportive colleagues');
insert into ReviewsOnEmployers (employerId, review) values (53, 'A fast-paced environment that kept me engaged');
insert into ReviewsOnEmployers (employerId, review) values (32, 'The work environment was disorganized and stressful');