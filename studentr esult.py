def calculate_result(marks):
    total = marks[0] + marks[1] + marks[2]
    percentage = total / 300 * 100
    if percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    return total, percentage, grade
students = []
for i in range(5):
    print("Enter details of student", i + 1)
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    print("Enter marks of 3 subjects:")
    python_marks = int(input("Python: "))
    ai_marks = int(input("Artificial Intelligence: "))
    maths_marks = int(input("Mathematics: "))
    marks = [python_marks, ai_marks, maths_marks]
    total, percentage, grade = calculate_result(marks)
    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }
    students.append(student)
    print()
print("Results of all students:")
for s in students:
    print("Name:", s["name"], "| Roll No:", s["roll"],
          "| Total:", s["total"],
          "| Percentage:", round(s["percentage"], 2),
          "| Grade:", s["grade"])
top_student = students[0]
for s in students:
    if s["percentage"] > top_student["percentage"]:
        top_student = s
print()
print("Student with highest percentage:", top_student["name"],
      "-", round(top_student["percentage"], 2), "%")
file = open("results.txt", "w")
file.write("Student Results\n\n")
for s in students:
    file.write("Name: " + s["name"] + ", Roll No: " + s["roll"]
               + ", Total: " + str(s["total"])
               + ", Percentage: " + str(round(s["percentage"], 2))
               + ", Grade: " + s["grade"] + "\n")
file.write("\nHighest percentage: " + top_student["name"]
           + " - " + str(round(top_student["percentage"], 2)) + "%\n")
file.close()
print("Results saved in results.txt")
