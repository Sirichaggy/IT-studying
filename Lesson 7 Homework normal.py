# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.
# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class School:
    def __init__(self, forms, teachers):
        self.forms = forms
        self.teachers = teachers
    def __repr__(self):
        return self.forms

class Form:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.student_list = []
        self.teacher_list = []
    def get_teachers_list(self):
        used_teacher_list = [teacher_1, teacher_2, teacher_3, teacher_4]
        required_list = []
        for i in used_teacher_list:
            if self == i.forms[0] or self == i.forms[1]:
                required_list.append(i)
        print(required_list)


form1 = Form("5А", [])
form2 = Form("5Б", [])
form3 = Form("6А", [])
form4 = Form("6Б", [])
form5 = Form("7А", [])
form6 = Form("7Б", [])

class Pupil(Form):
    def __init__(self, surname, name, patronymic, form, parents):
        super().__init__(name, value=[])
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.form = form
        self.parents = parents
        class_list = [form1, form2, form3, form4, form5, form6]
        for form in class_list:
            x = str(self.name)
            y = str(self.patronymic)
            if self.form == form:
                form.value.append(str("{} {}. {}.".format(self.surname, x[0], y[0])))
    def get_subjects(self):
        subjects_list = []
        teacher_list = [teacher_1, teacher_2, teacher_3, teacher_4]
        for i in teacher_list:
            if i.forms[0] == self.form or i.forms[1] == self.form:
                subjects_list.append(i.subject)
        print(subjects_list)

class Teacher(School):
    def __init__(self, surname, name, subject, forms):
        super().__init__(surname, name)
        self.subject = subject
        self.forms = forms
        for form in forms:
            form.teacher_list.append(self)

teacher_1 = Teacher("Дмитриев", "Сергей", "Математика", [form1, form4])
teacher_2 = Teacher("Кашаева", "Анна", "Химия", [form2, form3])
teacher_3 = Teacher("Глущенко", "Наталья", "История", [form4, form5])
teacher_4 = Teacher("Чернышева", "Екатерина", "Англ. яз.", [form1, form5])

school = School([form1, form2, form3, form4, form5, form6], [teacher_1, teacher_2, teacher_3, teacher_4])

pupil_1 = Pupil("Душнилова", "Скотина", "Романовна", form3, "Душнилов Р.А и Душнилова А.В.")
pupil_2 = Pupil("Пупкин", "Вася", "Кириллович", form4, "Петров К.Г. и Петрова Я.У.")
pupil_3 = Pupil("Черкаш", "Петр", "Сергеевич", form1, "Черкаш С.П. и Черкаш А.Г.")
pupil_4 = Pupil("Руинкин", "Глеб", "Семенович", form3, "Гоняев С.М. и Гоняева В.С.")
pupil_5 = Pupil("Арбуз", "Виталий", "Петрович", form6, "Арбуз П.А. и Арбуз К.П.")
pupil_6 = Pupil("Чепуха", "Кирилл", "Ильич", form1, "Чепуха И.В. и Чепуха В.М.")
pupil_7 = Pupil("Задорная", "Анна", "Тимофеевна", form2, "Задорный Т.С. и Задорная И.Н.")
pupil_8 = Pupil("Горбач", "Захар", "Владимирович", form5, "Горбач В.К. и Горбач К.П.")
pupil_9 = Pupil("Тупняк", "Илья", "Романович", form6, "Тупняк Р.С. и Тупняк А.Н.")
pupil_10 = Pupil("Вата", "Константин", "Тимофеевич", form6, "Вата Т.В. и Вата А.Г.")
pupil_11 = Pupil("Оленев", "Боча", "Рахмонович", form5, "Симов Р.В. и Симова Н.А.")
pupil_12 = Pupil("Рыгло", "Глеб", "Викторович", form4, "Рыгло В.К. и Рыгло Г.С.")
pupil_13 = Pupil("Босяков", "Павел", "Пятакович", form1, "Босяков П.М. и Босякова П.Д.")
pupil_14 = Pupil("Королева", "Анастасия", "Викторовна", form4, "Королев В.М. и Королева Ф.Р.")
pupil_15 = Pupil("Дубов", "Ясень", "Березович", form1, "Дубов Б.П. и Дубова В.Г.")
pupil_16 = Pupil("Электролитов", "Транзистор", "Напряженович", form4, "Трансформаторов Н.М. и Трансформаторова Г.С.")
pupil_17 = Pupil("Бателфилдов", "Овервотч", "Хартстоунович", form1, "Бателфилдов Х.К. и Бателфилдова Д.Д.")
pupil_18 = Pupil("Муслимов", "Муслим", "Муслимович", form5, "Муслимов М.М. и Муслимова М.М.")
pupil_19 = Pupil("Кухонный", "Стол", "Изикеевич", form4, "Кухонный И.П. и Кухонная Т.З.")
