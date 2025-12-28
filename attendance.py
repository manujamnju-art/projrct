# attendance.py
import sys

def calculate_attendance_percentage(attended, total):
    return (attended / total) * 100

def get_exam_eligibility(percentage):
    return "Eligible" if percentage >= 75 else "Not Eligible"

if __name__ == "__main__":
    name = sys.argv[1]
    total_classes = int(sys.argv[2])
    attended_classes = int(sys.argv[3])

    percentage = calculate_attendance_percentage(attended_classes, total_classes)
    eligibility = get_exam_eligibility(percentage)

    print(f"Name: {name}")
    print(f"Attendance Percentage: {percentage:.2f}%")
    print(f"Status: {eligibility}")
