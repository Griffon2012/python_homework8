class_list = (
    {
        'name': '1A',
        'file': './1A.txt'
    },
    {
        'name': '2Б',
        'file': './2Б.txt'
    },
)


def get_class_list():
    return [class_data['name'] for class_data in class_list]


def get_class_name(number):
    global class_list
    return class_list[number]['name']


def select_class(number):
    classes_data = []
    with open(class_list[number]['file'], 'r', encoding='UTF-8') as file:
        for string in file.readlines():
            class_data = {}
            lesson_students = string.strip().split(':')
            class_data['lesson_name'] = lesson_students[0]

            students = lesson_students[1].split('|')
            class_data['students'] = []

            for student in students:
                students_data = {}
                student_name_and_rating = student.split(';')
                students_data['name'] = student_name_and_rating[0]
                students_data['ratings'] = student_name_and_rating[1].split(
                    ' ')
                class_data['students'].append(students_data)
            classes_data.append(class_data)

    return classes_data


def enter_rating(rating, current_lesson, current_student, classes_data):
    if rating < 1 or rating > 5:
        return False
    classes_data[current_lesson]['students'][current_student]['ratings'].append(
        str(rating))


def save_all(current_class, classes_data):
    global class_list
    lessons_for_string = []
    for lesson in classes_data:
        students = []
        for student in lesson['students']:
            students.append(
                ';'.join([student['name'], ' '.join(student['ratings'])])
            )
        lessons_for_string.append(
            ':'.join([lesson['lesson_name'], '|'. join(students)]))
    with open(class_list[current_class]['file'], 'w', encoding='UTF-8') as file:
        file.write('\n'.join(lessons_for_string))
