class School:
    def __init__(self, name):
        self._name = name
        self._school = {}

    def grade(self,grade_number):
        return self._school[grade_number] if grade_number in self._school.keys() else set([])
    
    def add(self, student, grade_number):
        if grade_number in self._school.keys():
            self._school[grade_number].append(student)
        else:
            self._school[grade_number] = [student]
    
    def sort(self):
        t = []
        a = sorted(self._school)
        for g in a:
            self._school[g].sort()
            if len(self._school[g]) > 0:
                t.append((g,tuple(self._school[g])))
        return t