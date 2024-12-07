from .course import Course
class Network(Course):
    def __init__(self,name, P_name, note, min_to_pass):
        self.P_name = P_name
        self.name = name
        super().__init__(self.name, note, min_to_pass)

    def get_prof_name(self):
        return self.P_name