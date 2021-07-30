StudentRoster = []
Student = namedtuple('Student', 'name last_name grade exam_grade')

s1 = Student('John', 'Doe', 78, 94)
s2 = Student('Jean', 'Davis', 83, 76)
StudentRoster.append(s1)
StudentRoster.append(s2)

def getName(student):
    return student.name
def main():
    StudentRoster.sort(key = getName)

if __name__ == '__main__':
    main()