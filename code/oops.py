class Student:
    def __init__(self, netid, first, last):
        self.netid = netid
        self.first = first
        self.last = last
        self.homework = []

    def add_homework(self, score):
        self.homework.append(score)

    def __str__(self):
        return f'{self.first} {self.last} {self.homework}'

s = Student('jjv222', 'joe', 'v')
# print(s.netid, s.homework)
s.add_homework(83)
print(s)
        






