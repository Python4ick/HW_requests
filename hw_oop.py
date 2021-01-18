class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        # Присваиваем унивальный id каждому студенту в словаре, объявляем и увеличиваем глобальную переменную на 1
        global student_id
        student_list[student_id] = self.__dict__
        student_id += 1
        print(f'Создаю студента: {self.name} {self.surname}')

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка выставления оценки за лекицю')
            return

    def av_hw_grade(self):
        summary = 0
        numbers = 0
        for grades in self.grades.values():
            for grade in grades:
                summary += grade
                numbers += 1
        av_grade = round(summary / numbers, 2)
        return av_grade

    def __str__(self):
        str_0 = 'Информация о студенте:' + '\n' + '======================' + '\n'
        str_1 = 'Имя: ' + self.name + '\n'
        str_2 = 'Фамилия: ' + self.surname + '\n'
        str_3 = 'Средняя оценка за домашние задания: ' + str(self.av_hw_grade()) + '\n'
        str_4 = 'Курсы в процессе изучения: ' + ', '.join(self.courses_in_progress) + '\n'
        str_5 = 'Завершенные курсы: ' + ', '.join(self.finished_courses) + '\n'
        about = str_0 + str_1 + str_2 + str_3 + str_4 + str_5
        return about

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
        else:
            print(
                'Сравнение средней оценки за домашнее задание у студентов:' + '\n' + '=========================================================')
            print(f'Студент {self.name} {self.surname}, средняя оценка за ДЗ: {str(self.av_hw_grade())} ')
            print(f'Студент {other.name} {other.surname}, средняя оценка за ДЗ: {str(other.av_hw_grade())} ')
            if self.av_hw_grade() > other.av_hw_grade():
                print(f'{self.name} {self.surname} имеет лучшую среднюю оценку за ДЗ' + '\n')
            elif self.av_hw_grade() == other.av_hw_grade():
                print(f'Студенты имеют одинаковую среднюю оценку за ДЗ' + '\n')
            else:
                print(f'{other.name} {other.surname} имеет лучшую среднюю оценку за ДЗ' + '\n')
        return


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        # Присваиваем унивальный id каждому лектору, создаем словарь, объявляем и увеличиваем глобальную переменную на 1
        global lecturer_id
        lecturer_list[lecturer_id] = self.__dict__
        lecturer_id += 1
        print(f'Создаю лектора: {self.name} {self.surname}')

    def av_lecture_grade(self):
        summary = 0
        numbers = 0
        for grades in self.grades.values():
            for grade in grades:
                summary += grade
                numbers += 1
        av_grade = round(summary / numbers, 2)
        return av_grade

    def __str__(self):
        str_0 = 'Информация о лекторе:' + '\n' + '=====================' + '\n'
        str_1 = 'Имя: ' + self.name + '\n'
        str_2 = 'Фамилия: ' + self.surname + '\n'
        str_3 = 'Средняя оценка за лекции:' + str(self.av_lecture_grade()) + '\n'
        about = str_0 + str_1 + str_2 + str_3
        return about

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
        else:
            print(
                'Сравнение средней оценки за лекции у лекторов:' + '\n' + '==============================================')
            print(f'Лектор {self.name} {self.surname}, средняя оценка за лекции: {str(self.av_lecture_grade())} ')
            print(f'Лектор {other.name} {other.surname}, средняя оценка за лекции: {str(other.av_lecture_grade())} ')
            if self.av_lecture_grade() > other.av_lecture_grade():
                print(f'{self.name} {self.surname} имеет лучшую среднюю оценку за лекции' + '\n')
            elif self.av_lecture_grade() == other.av_lecture_grade():
                print(f'Лекторы имеют одинаковую среднюю оценку за лекции' + '\n')
            else:
                print(f'{other.name} {other.surname} имеет лучшую среднюю оценку за лекции' + '\n')
        return


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # Присваиваем унивальный id каждому проверяющему, создаем словарь, объявляем и увеличиваем глобальную переменную на 1
        global reviewer_id
        reviewer_list[reviewer_id] = self.__dict__
        reviewer_id += 1
        print(f'Создаю проверяющего: {self.name} {self.surname}')

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            print(
                f'Процеряющий {self.name} {self.surname} поставил студенту {student.name} {student.surname} по дисциплине {course} оценку {grade}')
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка выставления оценки за домашнюю работу')
            return

    def __str__(self):
        str_0 = 'Информация о проверяющем:' + '\n' + '========================' + '\n'
        str_1 = 'Имя: ' + self.name + '\n'
        str_2 = 'Фамилия: ' + self.surname + '\n'
        about = str_0 + str_1 + str_2
        return about


def av_grade_hw_in_course(stud_list, discipline):
    summary = 0
    values = 0
    for student in stud_list.values():
        summary += sum(student['grades'][discipline])
        values += len(student['grades'][discipline])
    return round(summary / values, 2)


def av_grade_lectors_in_course(lecturers_list, discipline):
    summary = 0
    values = 0
    for lecturer in lecturers_list.values():
        summary += sum(lecturer['grades'][discipline])
        values += len(lecturer['grades'][discipline])
    return round(summary / values, 2)


# Задаем начальные id для словаря словарей с данными о каждом объекте
student_id = 1
student_list = {}

reviewer_id = 1
reviewer_list = {}

lecturer_id = 1
lecturer_list = {}

# Создаем студентов, преподавателей, их курсы, ставим оценки
print('\n' + 'Некоторые логи действий (для примера): ' + '\n' + '======================================')

student_1 = Student('Ivan', 'Petrov', 'm')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Sergey', 'Sidorov', 'm')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

reviewer_1 = Reviewer('Reviewer', 'First')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']

lecturer_1 = Lecturer('Lecturer', 'First')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']

lecturer_2 = Lecturer('Lecturer', 'Second')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Java']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Java', 8)
reviewer_1.rate_hw(student_1, 'Java', 9)

reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Java', 9)
reviewer_1.rate_hw(student_2, 'Java', 9)

student_1.rate_lecturer(lecturer_1, 'Java', 10)
student_1.rate_lecturer(lecturer_2, 'Java', 9)
student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Java', 10)
student_1.rate_lecturer(lecturer_2, 'Python', 10)

student_2.rate_lecturer(lecturer_1, 'Java', 10)
student_2.rate_lecturer(lecturer_2, 'Java', 6)
student_2.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'Java', 8)
student_2.rate_lecturer(lecturer_1, 'Python', 10)


# Выводим отчеты
print()
print(reviewer_1)
print(lecturer_1)
print(student_1)

student_1 > student_2
lecturer_1 > lecturer_2

print(f'Списки словарей, для ручной проверки средних оценок по курсам:' + '\n' + '==============================================================')
print(f'Словарь студентов: {student_list}')
print(f'Словарь лекторов: {lecturer_list}')
print(f'Словарь проверяющих: {reviewer_list}' + '\n')

course = 'Python'
print(f'Средняя оценка всех студентов по курсу {course}: {av_grade_hw_in_course(student_list, course)}')

course = 'Java'
print(f'Средняя оценка всех студентов по курсу {course}: {av_grade_hw_in_course(student_list, course)}')

course = 'Python'
print(f'Средняя оценка всех лекторов по курсу {course}: {av_grade_lectors_in_course(lecturer_list, course)}')

course = 'Java'
print(f'Средняя оценка всех лекторов по курсу {course}: {av_grade_lectors_in_course(lecturer_list, course)}')
