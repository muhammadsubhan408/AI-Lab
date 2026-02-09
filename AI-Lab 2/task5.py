class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0   # private variable

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade!")

    def get_grade(self):
        return self.__grade

    def display_info(self):
        print(f"Student Name: {self.name}, Grade: {self.__grade}")


# Creating objects
s1 = Student("Ali")
s2 = Student("Sara")

# Updating grades
s1.set_grade(85)
s2.set_grade(92)

# Retrieving grades
print(s1.get_grade())
print(s2.get_grade())

# Display info
s1.display_info()
s2.display_info()
