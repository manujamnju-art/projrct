def calculate_attendance_percentage(total_classes, attended_classes):
    if total_classes <= 0:
        raise ValueError("Total classes must be greater than zero")
    return (attended_classes / total_classes) * 100


def get_exam_eligibility(percentage):
    if percentage >= 75:
        return "Eligible for Exam"
    return "Not Eligible for Exam"


def generate_report(name, total_classes, attended_classes):
    percentage = calculate_attendance_percentage(total_classes, attended_classes)
    status = get_exam_eligibility(percentage)

    return f"""
Student Name       : {name}
Total Classes      : {total_classes}
Attended Classes   : {attended_classes}
Attendance Percent : {percentage:.2f}%
Status             : {status}
"""


if __name__ == "__main__":
    name = input("Enter student name: ")
    total = int(input("Enter total classes: "))
    attended = int(input("Enter attended classes: "))

    print(generate_report(name, total, attended))
