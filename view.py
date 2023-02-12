def print_menu(current_position, current_class_name, current_lesson, current_student, classes_data) -> int:
    print('')

    if (current_class_name != None):
        print(f'Текущий класс: {current_class_name}')

    if (current_lesson != None):
        print(f"Текущий урок: {classes_data[current_lesson]['lesson_name']}")

    if (current_student != None):
        print(
            f"Текущий ученик: {classes_data[current_lesson]['students'][current_student]['name']} {' '.join(classes_data[current_lesson]['students'][current_student]['ratings'])}")

    if current_position == 'MAIN':
        print('1: Список классов')
        print('3: Выбрать класс')

    if current_position == 'CLASS' or current_position == 'STUDENT':
        print('4: Список уроков')
        print('5: Выбрать урок')

    if current_position == 'CLASS':
        print('6: Выйти из класса')

    if current_position == 'LESSON' or current_position == 'STUDENT':
        print('7: Список учеников')
        print('8: Выбрать ученика')

    if current_position == 'LESSON':
        print('10: Выйти из уроков')

    if current_position == 'STUDENT':
        print('9: Поставить оценку')

    if current_position in ['STUDENT', 'LESSON', 'CLASS']:
        print('11: Сохранить журнал')
    print('2: Выход')
    print('--------------------------------')

    return int(input('Укажите выбранный пункт: '))


def press_enter(info='') -> None:
    input(f'{info} Press enter to continue')


def print_class_list(class_list: list) -> None:
    for class_list, class_data in enumerate(class_list):
        print(f'{class_list}: {class_data}')


def select_lesson():
    return int(input('Укажите идентификатор урока: '))


def select_class():
    return int(input('Укажите идентификатор класса: '))


def print_lessons(classes_data):
    for number, lesson in enumerate(classes_data):
        print(f"{number}: {lesson['lesson_name']}")


def print_students(current_lesson, classes_data):
    for number, student in enumerate(classes_data[current_lesson]['students']):
        print(f"{number}: {student['name']} {' '. join(student['ratings'])}")


def select_student():
    return int(input('Укажите идентификатор ученика: '))


def enter_rating():
    return int(input('Укажите оценку: '))


def print_error_rating():
    print('Оценка должна быть от 1 до 5.')


def print_save_ok():
    print('Данные сохранены!')
