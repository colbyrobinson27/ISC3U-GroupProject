class Option:
    #Canvas,TextOrOptions,Text,Option1,Option2,Option3,Option4
    def __init__(self,package):
        self.canvas  =  package[0]
        self.optionOne = package[1]
        self.optionOneText = package[2]
        self.optionTwo = package[3]
        self.optionTwoText = package[4]
        try:
            self.optionThree = package[5]
            self.optionThreeText = package[6]
        except:
            pass
        try:
            self.optionFour = package[7]
            self.optionFour = package[8]
        except:
            pass


class TextDisplay:
    def __init__(self):
        print()