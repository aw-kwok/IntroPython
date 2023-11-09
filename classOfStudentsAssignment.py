"""
Name: Andrew Kwok
Group members (first names):
COSC-010
Class of Students Assignment

You can think of the Student class (the first part of this program) as a 
blueprint for creating Student objects. Do not modify anything within this 
Student class, but examine it to get an idea of how it works. Your task is
to modify the two stand-alone functions below (main and calculateAverage)
"""


# A class for working with student information
# Contains 3 attributes: studentName,  gradeList, average
# Contains 4 methods (including the constructor):
#   __init__, addGrade, getName, getAverage
class Student:
    
    def __init__(self, name):
        """
        The __init__ method is called the constructor. It is called when the 
        object is first created. This constructor for the Student class 
        initializes the 3 attributes (studentName, gradeList and average)
        
        Parameters
        ----------
        name : str
            The name of the student

        Returns
        -------
        None.

        """
        self.studentName = name
        self.gradeList = []
        self.average = 0


    def addGrade(self, num):
        """
        addGrade is for adding each individual grade.
        It will append the input to the growing gradeList.
        
        Parameters
        ----------
        num : numeric (int or float)
            The value of a new grade to be added to gradeList.

        Returns
        -------
        None.

        """
        self.gradeList.append(num)


    def getName(self):
        """
        getName is a typical "getter" method. It returns the student's name.

        Returns
        -------
        str
            The name of this particular student

        """
        return self.studentName


    # getAverage returns the student's grade average
    def getAverage(self):
        """
        getAverage is a "getter" method. It calculates the student's average
        and returns that information.

        Returns
        -------
        float
            The average of the student's grades.

        """
        self.average = sum(self.gradeList) / len(self.gradeList)
        return self.average


"""
The main  function should print out a welcome message to user and then ask
for the number of students (numStudents) and the number of grades (numGrades). 
It should then loop through the specified number of times (based on numStudents), 
at each iteration asking for a student name, using that name to create a student
object, and then calling the calculateAverage function (passing the student 
object and numGrades as arguments). It will collect the return value from
calculateAverage and print out the average for thatstudent.
"""
def main():
    studentList = []
    print("Welcome!")
    numStudents = int(input("How many students are there? "))
    numGrades = int(input("How many grades per student? "))
    
    i = 0
    while i < numStudents:
        name = input("What is the name of student " + str(i + 1) + "? ")
        studentList.append(Student(name))
        i += 1

    for i in studentList:
        print("The average for " + i.getName() + " is " + str(calculateAverage(i, numGrades)))

"""
The calculateAverage takes two parameters: a Student object (NOTE: this
parameter is not the name, it is the object) and an integer for the number of 
grades per student. This function should return the average grade for this 
student, but it should not calculate that average here. Instead, it should be
making calls to the student object's addGrade and getAverage methods to do most 
of the work.
"""

def calculateAverage(thisStudent, gradeNumber):
    i = 0
    while i < gradeNumber:
        thisStudent.addGrade(float(input("Enter grade " + str(i+1) + " for " + thisStudent.getName() + ": ")))
        i += 1
    return thisStudent.getAverage()
    
    # HINT: the following adds the grade 92 for thisStudent:
    #   thisStudent.addGrade(92)


main()
