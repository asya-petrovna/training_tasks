def grading_students(grades):
    improved_grades = []
    for i in range(len(grades)):
        if grades[i] < 38 or (grades[i]) % 5 <= 2:
            improved_grades.append(grades[i])
        else:
            improved_grades.append(int(grades[i] + (5 - ((grades[i]) % 5))))
    print(improved_grades)


def test():
    return grading_students([73, 67, 38, 33])


if __name__ == '__main__':
    test()
