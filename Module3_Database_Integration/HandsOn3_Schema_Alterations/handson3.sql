-- ==========================================================
-- HANDS-ON 3 : ALTER TABLE OPERATIONS
-- ==========================================================

-- Task 10
ALTER TABLE students
ADD phone_number VARCHAR(15);

-- Task 11
ALTER TABLE courses
ADD max_seats INT DEFAULT 60;

-- Task 12
ALTER TABLE enrollments
ADD CONSTRAINT chk_grade
CHECK (grade IN ('A','B','C','D','F') OR grade IS NULL);

-- Task 13
ALTER TABLE departments
RENAME COLUMN hod_name TO head_of_dept;

-- Task 14
ALTER TABLE students
DROP COLUMN phone_number;

-- Verify schema changes

SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA='college_db'
AND TABLE_NAME='courses';

SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA='college_db'
AND TABLE_NAME='departments';
