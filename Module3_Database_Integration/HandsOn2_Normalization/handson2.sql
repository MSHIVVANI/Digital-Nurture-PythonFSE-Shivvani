-- ==========================================================
-- HANDS-ON 2 : VERIFY NORMALIZATION
-- ==========================================================

-- 1NF ANALYSIS
-- All tables satisfy First Normal Form (1NF).
-- Each column contains atomic values only.
-- No repeating groups or multi-valued attributes exist.
-- Example violation:
-- phone_numbers = '9876543210,9123456780'
-- Multiple phone numbers in one column would violate 1NF.

-- 2NF ANALYSIS
-- All tables satisfy Second Normal Form (2NF).
-- Non-key attributes depend on the entire primary key.
-- In enrollments, the candidate key is (student_id, course_id).
-- grade and enrollment_date depend on the full enrollment relationship.
-- Therefore no partial dependency exists.

-- 3NF ANALYSIS
-- All tables satisfy Third Normal Form (3NF).
-- No non-key attribute depends on another non-key attribute.
-- students stores department_id rather than department_name.
-- department_name is stored only in departments table.
-- This removes transitive dependencies.

-- ENROLLMENTS TABLE 3NF ANALYSIS
-- enrollment_id uniquely identifies each enrollment.
-- student_id and course_id are foreign keys.
-- enrollment_date depends directly on enrollment.
-- grade depends directly on enrollment.
-- No non-key attribute determines another non-key attribute.
-- Therefore enrollments satisfies 3NF.

