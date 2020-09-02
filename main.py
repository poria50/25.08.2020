from person import Person

# I succesfully added my project to github.

class Student(Person):
    def __init__(self, psn, first_name, last_name, date_of_birth, phone_nr, address, student_id, admission_date,
                 field_of_study):
        super().__init__(psn, first_name, last_name, date_of_birth, phone_nr, address)
        self.student_id = student_id
        self.admission_date = admission_date
        self.field_of_study = field_of_study


class Teacher(Person):
    def __init__(self, psn, first_name, last_name, date_of_birth, phone_nr, address, teacher_id, hire_date,
                 field_of_study, courses=None):
        super().__init__(psn, first_name, last_name, date_of_birth, phone_nr, address)
        self.teacher_id = teacher_id
        self.hire_date = hire_date
        self.field_of_study = field_of_study

        if courses is not None:
            self.courses = courses
        else:
            self.courses = []


class Department:
    def __init__(self, department_id, department_name, courses=None):
        self.department_id = department_id
        self.department_name = department_name

        if courses is not None:
            self.courses = courses
        else:
            self.courses = []


class Course:
    def __init__(self, course_id, course_name, unit, department):
        self.course_id = course_id
        self.course_name = course_name
        self.unit = unit
        self.department = department


class Subject:
    def __init__(self, subject_id, course, teacher, start_date, end_date, exam_date, class_nr):
        self.subject_id = subject_id
        self.course = course
        self.teacher = teacher
        self.start_date = start_date
        self.end_date = end_date
        self.exam_date = exam_date
        self.class_nr = class_nr


class Registration:
    def __init__(self, subject, student):
        self.subject = subject
        self.student = student


cs = Department('D1', 'Computer Science', None)

python = Course('C100', 'Programing with Python', 3, cs)
ds = Course('C110', 'data structure', 3, cs)

cs.courses.append(python)
cs.courses.append(ds)
# cs.courses.extend([python,ds])

art = Department('D2', 'Art', None)

painting = Course('C101', 'pastel painting', 3, art)

teacher_1 = Teacher(111275, 'john', 'doe', '11-10-1970', '004740237844', 'oslo', 't112', '01.01.2019', 'I.T',
                    [python, ds])

student = Student(5220015, 'ole', 'nordman', '11-05-1990', '004740290109', 'rasta', 's101', '16.07.2019', 'I.T')

subject = Subject('s10', ds, teacher_1, '01-02-2020', '01-12-2020', '05-10.2020', 'r101')

reg1 = Registration(subject, student)

