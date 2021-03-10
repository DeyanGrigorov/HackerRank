def grading_students(grades):
    new_grades = []
    multiple_five = True
    for num in grades:
        current_grade = num
        multiple_five = True
        while multiple_five:
            if current_grade < 38:
                new_grades.append(current_grade)
                break
            next_multiple = 0
            result_minus = 0
            if num % 5 == 0:
                multiple_five = False
                next_multiple = num
                result_minus = abs(current_grade - next_multiple)
                if result_minus < 3:
                    new_grades.append(next_multiple)
                else:
                    new_grades.append(current_grade)
            num += 1
    return new_grades


if __name__ == '__main__':
    grades_count = int(input())
    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = grading_students(grades)

    print(result)

