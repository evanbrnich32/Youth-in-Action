# Youth in Action

# Introduction

print("Welcome to Youth in Action!")

# Define Resources

students = []
teachers = []
resources = ["books", "laptops", "cameras"]

# Register Students

while True:
    student_name = input("Please enter your name (enter 'done' when finished): ")
    if student_name == "done":
        break
    students.append(student_name)

# Register Teachers

while True:
    teacher_name = input("Please enter the teacher's name (enter 'done' when finished): ")
    if teacher_name == "done":
        break
    teachers.append(teacher_name)

# Allocate Resources

for student in students:
    print("Student %s has been allocated the following resources:" % student)
    for resource in resources:
        print("- %s" % resource)

# Set Up Projects

projects = []

for teacher in teachers:
    project_name = input("Please enter the project name for %s (enter 'done' when finished): " % teacher)
    if project_name == "done":
        break
    projects.append(project_name)

# Assign Students to Projects

for project in projects:
    print("The following students have been assigned to project %s:" % project)
    for student in students:
        print("- %s" % student)

# Provide Resources to Students

for project in projects:
    print("The following resources have been allocated for project %s:" % project)
    for resource in resources:
        print("- %s" % resource)

# Start Projects

for project in projects:
    print("Project %s is now ready to begin!" % project)