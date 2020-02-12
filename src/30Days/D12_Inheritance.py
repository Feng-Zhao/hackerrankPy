
class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
# Class Constructor
#
#   Parameters:
#   firstName - A string denoting the Person's first name.
#   lastName - A string denoting the Person's last name.
#   id - An integer denoting the Person's ID number.
#   scores - An array of integers denoting the Person's test scores.
#
# Write your constructor here
    def __init__(self, firstName, lastName, idNumder, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumder
        self.scores = scores
#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here
    def calculate(self):
        sum = 0
        for i in self.scores:
            sum += i
        avg = sum/len(self.scores)
        if 100 >= avg >= 90:
            return 'O'
        elif 90 > avg >= 80:
            return 'E'
        elif 80 > avg >= 70:
            return 'A'
        elif 70 > avg >= 55:
            return 'P'
        elif 55 > avg >= 40:
            return 'D'
        elif 40 > avg:
            return 'T'
        else:
            return 'err'



