class Programmer:
    def __init__(self, name, language, skills):
        self.skills = skills
        self.language = language
        self.name = name

    def watch_course(self, course_name, language_value, skills_earned):
        if self.language == language_value:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language_value}"

    def change_language(self, new_language, skills_needed):
        if self.skills >= skills_needed and new_language != self.language:
            old_language = self.language
            self.language = new_language
            return f"{self.name} switched from {old_language} to {new_language}"
        elif self.skills >= skills_needed and new_language == self.language:
            return f"{self.name} already knows {self.language}"
        else:
            return f"{self.name} needs {abs(self.skills - skills_needed)} more skills"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
