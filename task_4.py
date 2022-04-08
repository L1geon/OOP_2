from statistics import mean


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if grade >= 1 or grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'

    def avg_grades(self):
        avg = 0.0
        for k, v in self.grades.items():
            avg += mean(v)
        return round(avg / len(self.grades), 3)

    def __str__(self):
        text = f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.avg_grades()}
Курсы в процессе изучения: {self.courses_in_progress}
Завершённые курсы: {self.finished_courses}"""
        return text


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grades(self):
        avg = 0
        for k, v in self.grades.items():
            avg += mean(v)
        return round(avg / len(self.grades), 3)

    def __str__(self):
        text = f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.avg_grades()}"""
        return text


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f"""Имя: {self.name}
Фамилия: {self.surname}"""
        return text


def avg_grades_students_course(course, men):
    course_students = []
    for s in men:
        if course in s.courses_in_progress:
            course_students.append(s)
    _sum = 0.0
    for student in course_students:
        _sum += mean(student.grades[course])
    result = round(_sum / len(course_students), 3)
    return result


def avg_grades_lecturer_course(course, lecturers):
    course_lecturers = []
    for l in lecturers:
        if course in l.courses_attached:
            course_lecturers.append(l)
    _sum = 0.0
    for lecturer in course_lecturers:
        _sum += mean(lecturer.grades[course])
    result = round(_sum / len(course_lecturers), 3)
    return result


kirill = Student("Kirill", "Piterov", "male")
denis = Student("Denis", "Smirnov", "male")

anton = Lecturer("Anton", "Antonov")
victor = Lecturer("Victor", "Victovich")

dima = Reviewer("Dima", "Domov")
sasha = Reviewer("Sasha", "Sashova")

kirill.courses_in_progress += ["Python"]
kirill.add_courses("Git")

denis.courses_in_progress += ["Python"]
denis.add_courses("Git")

anton.courses_attached += ["Python"]
victor.courses_attached += ["Python"]

dima.courses_attached += ["Python"]

kirill.rate_hw(anton, "Python", 3)
kirill.rate_hw(anton, "Python", 9)
kirill.rate_hw(anton, "Python", 10)

dima.rate_hw(kirill, "Python", 8)
dima.rate_hw(kirill, "Python", 6)
dima.rate_hw(kirill, "Python", 8)

denis.rate_hw(victor, "Python", 4)
denis.rate_hw(victor, "Python", 1)
denis.rate_hw(victor, "Python", 8)

dima.rate_hw(denis, "Python", 10)
dima.rate_hw(denis, "Python", 8)
dima.rate_hw(denis, "Python", 6)

print(avg_grades_students_course("Python", [kirill, denis]))
print(avg_grades_lecturer_course("Python", [anton, victor]))
