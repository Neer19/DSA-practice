class student:
    def __init__(self):
        self.__marks=70   #__ meansprivate data
        self._name="AAA"    #_ means protected data

f1=student()
print(f1.__dict__)
class HOD:
    def __init__(self):
        self.pass_student=32
        print(f1.__marks)

h1=HOD()
print(f1.__dict__)