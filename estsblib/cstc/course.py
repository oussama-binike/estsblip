class Course:
    def __init__(self,name, note, min_to_pass):
        self.name = name
        self.note = note
        self.min_to_pass = min_to_pass

    def is_passed(self):
        return self.note >= self.min_to_pass
    
    def _print(self):
        return(f"Model : {self.name},\nNote: {self.note},\nMin to pass: {self.min_to_pass}\n")