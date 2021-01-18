class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
    
    def update_name(self, new_name):
        self.name = new_name

    def change_cohort(self, new_cohort):
        self.cohort = new_cohort

    def talk(self):
        return "I can talk!"

    def say_favourite_language(self, favourite_language):
        return "I love " + favourite_language

