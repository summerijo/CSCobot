CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    year_level INT,
    course VARCHAR(50),
    track VARCHAR(50)
);

CREATE TABLE Fines (
    fine_id INT PRIMARY KEY,
    student_id INT,
    amount DECIMAL(10, 2),
    reason VARCHAR(200),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);