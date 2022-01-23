class Student:
    def __init__(self, firstname, lastname, courses=None):
        self.firstname = firstname
        self.lastname = lastname
        if courses == None:
            self.courses = []
        else:
            self.courses = courses
        #print(self.print_data())
        #print(self.courses)

    def print_data(self):
        fullname = self.firstname + " " + self.lastname
        return fullname

    def studentname_with_enrolledcourses(self):
        return f"{self.firstname} is enrolled in {self.courses}"

    def add_course(self, course):
        if course not in self.courses:
            return self.courses.append(course)
        else:
            print(f"{self.firstname} Already Enrolled in {self.courses}")


courses1 = ["Python", "C#.Net", "ASP.Net"]
courses2 = ["Python", "C#.Net", "Testing"]
sateesh = Student("Sateesh", "Kumar", courses1)
vivek = Student("Vivek", "Varma")
vivek.add_course("AWS")
vivek.add_course("AWS")
print(sateesh.studentname_with_enrolledcourses())
print(vivek.studentname_with_enrolledcourses())


