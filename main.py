class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_course = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def avg_rate(self):
        avg_rating = list(map(lambda x: x[0], self.grades.values()))
        avg = sum(avg_rating) / len(avg_rating)
        return avg


    def __str__(self):
        return '\n'.join([
        f'Имя: {self.name}',
        f'Фамилия: {self.surname}',
        f'Средняя оценка за домашние задания: {self.avg_rate()}',
        f'Курсы в процессе изучения: {self.courses_in_progress}',
        f'Завершенные курсы: {self.finished_course}'
    ])


    def __eq__(self, other):
        if isinstance(other, Student):
            return self.avg_rate() == other.avg_rate()
        else:
            return 'Ошибка'


    def __lt__(self, other):
        if isinstance(other, Student):
            return self.avg_rate() < other.avg_rate()
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, ):
        super().__init__(name, surname)
        self.grades = {}


    def avg_rate(self):
        avg_rating = list(map(lambda x: x[0], self.grades.values()))
        avg = sum(avg_rating) / len(avg_rating)
        return avg


    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.avg_rate()}'''


    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_rate() == other.avg_rate()
        else:
            return 'Ошибка'


    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_rate() < other.avg_rate()
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


lecturer_1 = Lecturer('Oleg', 'Buligin')
lecturer_1.courses_attached += ['Python', 'Git', 'DB']
student_1 = Student('Ivan', 'Ivanov', 'm')
student_1.finished_course += ['Введение в программирование']
student_1.courses_in_progress += ['Python', 'Git', 'DB']
student_1.rate_lecture(lecturer_1, 'Python', 5)
student_1.rate_lecture(lecturer_1, 'Git', 9)
student_1.rate_lecture(lecturer_1, 'DB', 7)
reviewer_1 = Reviewer('Timur', 'Anvartdinov')
reviewer_1.courses_attached += ['Python', 'Git', 'DB']
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_1, 'DB', 8)


lecturer_2 = Lecturer('Elena', 'Ivanova')
lecturer_2.courses_attached += ['Django', 'Api', 'DB']
student_2 = Student('Anna', 'Petrova', 'w')
student_2.finished_course += ['Введение в программирование', 'Python', 'Git']
student_2.courses_in_progress += ['Django', 'Api', 'DB']
student_2.rate_lecture(lecturer_2, 'Django', 6)
student_2.rate_lecture(lecturer_2, 'Api', 10)
student_2.rate_lecture(lecturer_2, 'DB', 9)
reviewer_2 = Reviewer('Petr', 'Smirnov')
reviewer_2.courses_attached += ['Django', 'Api', 'DB']
reviewer_2.rate_hw(student_2, 'Django', 10)
reviewer_2.rate_hw(student_2, 'Api', 8)
reviewer_2.rate_hw(student_2, 'DB', 10)


# print(lector_1)
# print(lector_2)

# print(student_1)
# print(student_2)

# print(reviewer_1)
# print(reviewer_2)


def avg_student_grade(students, course):
    grade_ = []
    for student in students:
        if course in student.courses_in_progress:
            grade_.extend(student.grades[course])
    avg_grade_ = sum(grade_) / len(grade_)
    return f'Средняя оценка студентов на курсе {course} - {avg_grade_}'


def avg_lecturer_grade(lectors, course):
    grade_ = []
    for lecturer in lectors:
        if course in lecturer.courses_attached:
            grade_.extend(lecturer.grades[course])
    avg_grade_ = sum(grade_) / len(grade_)
    return f'Средняя оценка лекторов на курсе {course} - {avg_grade_}'


print(avg_student_grade([student_1, student_2], 'DB'))
print(avg_lecturer_grade([lecturer_1, lecturer_2], 'DB'))
