# Hands-On 8 - REST API Design Best Practices

## Resource Naming

Correct:
- /api/v1/courses/
- /api/v1/students/
- /api/v1/departments/

Incorrect:
- /api/getCourses/
- /api/course_list/
- /api/get_students/

Rules:
- Use nouns instead of verbs.
- Use plural resource names.
- Use hyphens instead of underscores.

---

## HTTP Methods

GET    -> Retrieve resources
POST   -> Create resource
PUT    -> Replace entire resource
PATCH  -> Partial update
DELETE -> Delete resource

Examples:

GET    /api/v1/courses/
POST   /api/v1/courses/
PUT    /api/v1/courses/1/
PATCH  /api/v1/courses/1/
DELETE /api/v1/courses/1/

---

## Status Codes

200 OK
201 Created
204 No Content
400 Bad Request
401 Unauthorized
404 Not Found
409 Conflict
422 Unprocessable Entity

---

## API Versioning

Current approach:

/api/v1/courses/

Alternative approach:

Accept: application/json;version=1

URL versioning is easier to test and maintain.

---

## Pagination Response

{
    "count": 10,
    "next": "/api/v1/courses/?page=2&page_size=2",
    "previous": null,
    "results": []
}

---

## Standard Error Response

{
    "error": {
        "code": "NOT_FOUND",
        "message": "Course with id 99 does not exist",
        "field": null
    }
}