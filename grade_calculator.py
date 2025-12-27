3# Student Grade Calculator
# Week 2 Project – Control Flow & Data Structures
# Author: Vinit Kumar

# --------------------------------------------------
# Function to calculate grade and comment
# --------------------------------------------------
def calculate_grade(average):
    """Calculate grade based on average marks"""
    if average >= 90:
        return 'A', 'Excellent! Keep up the great work!'
    elif average >= 80:
        return 'B', "Very Good! You're doing well."
    elif average >= 70:
        return 'C', 'Good. Room for improvement.'
    elif average >= 60:
        return 'D', 'Needs Improvement. Please study more.'
    else:
        return 'F', 'Failed. Please seek help from teacher.'


# --------------------------------------------------
# Function to validate numeric input
# --------------------------------------------------
def get_valid_number(prompt, min_val=0, max_val=100):
    """Get a valid number within specified range"""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input! Please enter a number.")


# --------------------------------------------------
# Main function
# --------------------------------------------------
def main():
    print("=" * 60)
    print("               STUDENT GRADE CALCULATOR")
    print("=" * 60)

    # Get number of students
    while True:
        try:
            num_students = int(input("\nEnter number of students: "))
            if num_students > 0:
                break
            else:
                print("Number of students must be positive.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

    # Data storage
    student_names = []
    student_marks = []
    student_results = []

    # --------------------------------------------------
    # Collect student data
    # --------------------------------------------------
    for i in range(num_students):
        print(f"\n=== STUDENT {i + 1} ===")
        name = input("Student name: ").strip()
        student_names.append(name)

        print("Enter marks (0–100):")
        math = get_valid_number("Math: ")
        science = get_valid_number("Science: ")
        english = get_valid_number("English: ")

        student_marks.append([math, science, english])

        average = (math + science + english) / 3
        grade, comment = calculate_grade(average)

        student_results.append({
            'average': average,
            'grade': grade,
            'comment': comment
        })

    # --------------------------------------------------
    # Display Results Summary (MATCHES SCREENSHOT)
    # --------------------------------------------------
    print("\n" + "=" * 60)
    print("                 RESULTS SUMMARY")
    print("=" * 60)

    print(f"{'Name':<20} | {'Avg':>5} | {'Grade':^5} | Comment")
    print("-" * 75)

    for i in range(num_students):
        name = student_names[i]
        avg = student_results[i]['average']
        grade = student_results[i]['grade']
        comment = student_results[i]['comment']

        print(f"{name:<20} | {avg:>5.1f} | {grade:^5} | {comment}")

    # --------------------------------------------------
    # Class Statistics
    # --------------------------------------------------
    averages = [result['average'] for result in student_results]

    class_avg = sum(averages) / len(averages)
    max_avg = max(averages)
    min_avg = min(averages)

    max_index = averages.index(max_avg)
    min_index = averages.index(min_avg)

    print("\n" + "=" * 60)
    print("                 CLASS STATISTICS")
    print("=" * 60)
    print(f"Total Students: {num_students}")
    print(f"Class Average: {class_avg:.1f}")
    print(f"Highest Average: {max_avg:.1f} ({student_names[max_index]})")
    print(f"Lowest Average: {min_avg:.1f} ({student_names[min_index]})")

    print("\n" + "=" * 60)
    print("Thank you for using the Grade Calculator!")
    print("=" * 60)


# --------------------------------------------------
# Program Entry Point
# --------------------------------------------------
if __name__ == "__main__":
    main()
