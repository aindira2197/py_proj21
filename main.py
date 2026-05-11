courses = [
    {"title": "Python", "students": 120},
    {"title": "Java", "students": 80},
    {"title": "C++", "students": 40},
    {"title": "JavaScript", "students": 150}
]

popular = []

for course in courses:
    if course["students"] >= 100:
        popular.append(course["title"])

print("Mashhur kurslar:")

for item in popular:
    print(item)

max_course = courses[0]

for course in courses:
    if course["students"] > max_course["students"]:
        max_course = course

print("Eng mashhur kurs:", max_course["title"])
