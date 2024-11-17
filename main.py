CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    grade_level INT,
    gpa DECIMAL(3, 2),
    enrollment_date DATE
);

CREATE TABLE courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100),
    instructor VARCHAR(50),
    credits INT
);

CREATE TABLE enrollments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    grade VARCHAR(2),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

INSERT INTO students (first_name, last_name, grade_level, gpa, enrollment_date) VALUES
('Emma', 'Williams', 10, 3.8, '2021-08-20'),
('Liam', 'Johnson', 11, 3.6, '2020-08-20'),
('Sophia', 'Brown', 12, 3.9, '2019-08-20');

INSERT INTO courses (course_name, instructor, credits) VALUES
('Mathematics', 'Dr. Smith', 4),
('Physics', 'Dr. Lee', 3),
('Literature', 'Dr. Taylor', 3);

INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES
(1, 1, '2021-09-01', 'A'),
(2, 2, '2020-09-01', 'B'),
(3, 3, '2019-09-01', 'A');

SELECT * FROM students;
SELECT * FROM courses;
SELECT * FROM enrollments;

SELECT * FROM students WHERE gpa > 3.7;
SELECT * FROM courses WHERE credits >= 3;
SELECT * FROM enrollments WHERE grade = 'A';

SELECT * FROM students ORDER BY gpa DESC;
SELECT * FROM courses ORDER BY credits ASC;
SELECT * FROM enrollments ORDER BY enrollment_date DESC;

SELECT AVG(gpa) AS average_gpa FROM students;
SELECT MAX(gpa) AS max_gpa FROM students;
SELECT SUM(credits) AS total_credits FROM courses;

SELECT grade_level, COUNT(*) AS student_count FROM students GROUP BY grade_level;
SELECT instructor, COUNT(*) AS course_count FROM courses GROUP BY instructor;

SELECT s.first_name, s.last_name, c.course_name FROM students s
JOIN enrollments e ON s.id = e.student_id
JOIN courses c ON e.course_id = c.id;

SELECT s.first_name, s.last_name FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id;

SELECT c.course_name FROM courses c
WHERE EXISTS (SELECT 1 FROM enrollments e WHERE e.course_id = c.id AND e.grade = 'A');

SELECT DISTINCT grade FROM enrollments;

SELECT COUNT(*) FROM students;
SELECT COUNT(DISTINCT grade) FROM enrollments;

SELECT * FROM students WHERE enrollment_date BETWEEN '2020-01-01' AND '2022-12-31';

SELECT * FROM students LIMIT 2;

SELECT * FROM students WHERE first_name LIKE 'E%';
SELECT * FROM courses WHERE course_name LIKE '%Math%';

DELETE FROM enrollments WHERE id = 2;

UPDATE students SET gpa = gpa + 0.1 WHERE grade_level = 10;
