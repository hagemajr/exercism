ALLERGY_MAP = {
    1:'eggs',
    2:'peanuts',
    4:'shellfish',
    8:'strawberries',
    16:'tomatoes',
    32:'chocolate',
    64:'pollen',
    128:'cats'
}

class Allergies:



    def __init__(self,score):
        self._score = score
        self.lst = [x for i, x in ALLERGY_MAP.items() if score & i]


    def is_allergic_to(self,a):
        return a in self.lst

    