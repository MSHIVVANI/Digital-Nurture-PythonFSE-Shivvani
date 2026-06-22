-- ==========================================================
-- HANDS-ON 4 : QUERY OPTIMIZATION
-- ==========================================================

-- Baseline EXPLAIN

EXPLAIN FORMAT=JSON
SELECT
s.first_name,
s.last_name,
c.course_name
FROM enrollments e
JOIN students s
ON s.student_id=e.student_id
JOIN courses c
ON c.course_id=e.course_id
WHERE s.enrollment_year=2022;

-- MySQL initially performs table scans
-- because dataset size is small.

-- Create indexes

CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);

CREATE UNIQUE INDEX idx_enrollment_student_course
ON enrollments(student_id,course_id);

CREATE INDEX idx_course_code
ON courses(course_code);

-- Re-run explain

EXPLAIN FORMAT=JSON
SELECT
s.first_name,
s.last_name,
c.course_name
FROM enrollments e
JOIN students s
ON s.student_id=e.student_id
JOIN courses c
ON c.course_id=e.course_id
WHERE s.enrollment_year=2022;

-- Result:
-- students table uses enrollment_year index.
-- duplicate student-course enrollments prevented.

