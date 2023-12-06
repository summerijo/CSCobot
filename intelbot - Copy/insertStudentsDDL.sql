-- Inserting sample students with specified courses and specializations
INSERT INTO students (student_id, student_name, year_level, course, track)
VALUES 
    (1, 'Juan dela Cruz', 3, 'BSIT', 'Data Network'),
    (2, 'Arram Pamisa', 2, 'BSIT', 'Software Development'),
    (3, 'Ritchel Naquinez', 4, 'BSIT', 'Information Management');

-- Inserting sample fines related to college events for students
INSERT INTO Fines (fine_id, student_id, amount, reason)
VALUES 
    (1, 2, 25.00, 'Late submission for college project'),
    (2, 1, 50.00, 'Unregistered for college seminar'),
    (3, 2, 15.00, 'Missed attendance for college workshop'),
    (4, 3, 10.00, 'Late fee for overdue library books'),
    (5, 3, 30.00, 'Unpaid college organization dues');
