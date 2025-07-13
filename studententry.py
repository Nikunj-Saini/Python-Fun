def main():
    students = []
    for _ in range(int(input("How many students?: "))):
        name = input("Student name: ")
        student_class = input("Class: ")
        total_marks = input("Total marks: ")
        students.append((name, student_class, total_marks))
    print("\nStudent Information:")
    for i, student in enumerate(students, 1):
        print(f"Student {i}: {student}")
if __name__ == "__main__":
    main()