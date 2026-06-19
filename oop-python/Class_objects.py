'''
Class: 
In object oriented programming class is one of the major pillor
Class defines the structure of an object(How the object should be and what things it should do)
Class gives an blueprint therefore the objects formed in that manner

Technically : 
Class is a blueprint of an object. It defines the attributes and functionality of an object
class doesnot have Internal memory untill the object was created therefore we cannot execute the class 
assume its just writing an intructions in a pieace of paper


Synatax: 
    "class <Class Name>:"


Object:
Technically:
Object is the realtime executable instance of class.
It follows the structure which is defined in the class.
Object performs the functions which is defined in the class.
when the Object is created the memory is created internally to the class
We can create Multiple Objects from a class, those are all different individually but functionality is same.   
each and every object contains their individual attributes which are differ to each other

Assume that Instructions which are written in paper were followed by different peoples each people is not same they are different but 
they are following the same Intructions which is written in pieace of paper. 

Synatax: 
    "obj_reference = <Class_name>()"


Real Life Analogy:
Teachers from a school or college
there are Multiple teachers in a school, they different with respect to the subject they teach.
but we call them all are teachers.

Now from OOP point of view we can say Teacher is a class
Because, Teacher Class contains
Attributes: Teacher name, Teching Subject
Functionality: Teaching, Conducting exams, Monitoring Students

and Each and every teacher is not same in school. 
we have multiple teachers and subjects. each teacher teaches different subject
in OOP point of view we call Individual Teacher as Object
because, every teacher has Name, Subject. they are different but they follows same functionality 
like teaching,  Conducting exams, Monitoring Students

In simply 
Ram and Sita both are Teachers
these two persons are same class "teachers" but different Objects "persons"
they have Attributes like name , Subject they teach
they have functionality(job) Teching subject to students

Practical Example:
'''

class Teacher:                                                                  # Created a class Teacher
    def __init__(self, teacher_name: str, teaching_subject: str):               # Contructor Created and created two instance variables 
        self.name = teacher_name
        self.subject = teaching_subject
    
    def get_details(self) ->str:
        return f'Teacher Name: {self.name}\nTeching Subject: {self.subject}'
    

x = Teacher('Ram', 'Maths')                                                     # Created Object - 1
print(x.get_details())

y = Teacher('Sita', 'Social')                                                   # Created Object - 2
print(y.get_details())