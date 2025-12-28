import sys

if len(sys.argv) != 4:
    print("Usage: python attendance.py <name> <total_classes> <attended_classes>")
    sys.exit(1)
else:
    # Read inputs
    name = sys.argv[1]
    total_classes = int(sys.argv[2])
    attended_classes = int(sys.argv[3])

    # Validate total classes
    if total_classes <= 0:
        print("Total classes must be greater than zero")
        sys.exit(1)

    # Calculate attendance percentage
    percentage = (attended_classes / total_classes) * 100

    # Determine eligibility using if-else
    if percentage >= 75:
        status = "Eligible for Exam"
    else:
        status = "Not Eligible for Exam"

    # Print report
    print(f"Student Name       : {name}")
    print(f"Total Classes      : {total_classes}")
    print(f"Attended Classes   : {attended_classes}")
    print(f"Attendance Percent : {percentage:.2f}%")
    print(f"Status             : {status}")
