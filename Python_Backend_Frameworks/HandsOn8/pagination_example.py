courses = [
    {"id": 1, "name": "DBMS"},
    {"id": 2, "name": "OOP"},
    {"id": 3, "name": "Python"},
    {"id": 4, "name": "Networks"},
]

page = 1
page_size = 2

start = (page - 1) * page_size
end = start + page_size

response = {
    "count": len(courses),
    "next": "/api/v1/courses/?page=2&page_size=2",
    "previous": None,
    "results": courses[start:end]
}

print(response)