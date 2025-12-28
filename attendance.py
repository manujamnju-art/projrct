import sys

def calculate_attendance_percentage(attended, total):
    return (attended / total) * 100

def get_exam_eligibility(percentage):
    if percentage >= 75:
        return "Eligible"
    else:
        return "Not Eligible"

if __name__ == "__main__":
    if len(sys.argv) == 4:
        name = sys.argv[1]
        total_classes = int(sys.argv[2])
        attended_classes = int(sys.argv[3])

       
    else:
        name = Manju
        total_classes = 100
        attended_classes = 90
        
        percentage = calculate_attendance_percentage(attended_classes, total_classes)
        eligibility = get_exam_eligibility(percentage)

        print(f"Name: {name}")
        print(f"Attendance Percentage: {percentage:.2f}%")
        print(f"Status: {eligibility}")
