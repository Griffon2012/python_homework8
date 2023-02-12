import view
import model

current_position = 'MAIN'
current_class = None
current_lesson = None
current_student = None
classes_data = None


def start():
    global current_position, current_class, classes_data, current_lesson, current_student
    while 1:
        current_class_name = None if current_class == None else model.get_class_name(
            current_class)
        now_position_menu = view.print_menu(
            current_position, current_class_name, current_lesson, current_student, classes_data)
        if (now_position_menu == 2):
            exit()
        if (now_position_menu == 1):
            view.print_class_list(model.get_class_list())
            view.press_enter()
        if (now_position_menu == 3):
            current_position = 'CLASS'
            current_class = view.select_class()
            classes_data = model.select_class(current_class)
            current_lesson = None
            current_student = None
        if (now_position_menu == 6):
            current_position = 'MAIN'
            current_class = None
            current_lesson = None
            classes_data = None
            current_student = None
        if (now_position_menu == 4 and current_class != None):
            view.print_lessons(classes_data)
            view.press_enter()
        if (now_position_menu == 5 and current_class != None):
            current_position = 'LESSON'
            current_lesson = view.select_lesson()
            current_student = None
        if (now_position_menu == 10 and current_class != None):
            current_position = 'CLASS'
            current_lesson = None
            current_student = None
        if (now_position_menu == 8 and current_class != None):
            current_position = 'STUDENT'
            current_student = view.select_student()
        if (now_position_menu == 7 and current_class != None):
            view.print_students(current_lesson, classes_data)
            view.press_enter()
        if (now_position_menu == 9 and current_class != None):
            if (model.enter_rating(view.enter_rating(), current_lesson, current_student, classes_data)) == False:
                view.print_error_rating()
        if (now_position_menu == 11 and current_class != None):
            model.save_all(current_class, classes_data)
            view.print_save_ok()
