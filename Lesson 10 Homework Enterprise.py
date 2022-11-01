class People:
    __slots__ = ('name', 'surname', 'patronymic', 'birth_date', 'phone')
    def __init__(self, name, surname, patronymic, birth_date, phone):
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__birth_date = birth_date
        self.__phone = phone


class Employee(People):
    def __init__(self, name, surname, patronymic, birth_date, phone, identification, section_code, salary):
        People.__init__(self, name, surname, patronymic, birth_date, phone)
        self.__identification = identification
        self.__section_code = section_code
        self.__salary = salary
    def get_salary(self):
        return self.__salary

    def set_salary(self, value):
        self.__salary = value

    def minimize_salary(self):
        self.__salary = 15000

    salary = property(get_salary, set_salary, minimize_salary)


class Enterprise(Employee):
    def __init__(self):
        Employee.__init__(self)


empl = Employee("Grisha", "Petrov", "Kirillovich", "30.08.1999", "89274469009", "77 38 62", "44 D", 32000)
