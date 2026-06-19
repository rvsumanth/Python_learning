'''
Instance variables and Methods
'''

class Student:
    def __init__(self, student_name: str, student_roll: int, student_add: str) -> None:
        ''' Below are all Instance Variables'''
        self.name = student_name
        self.rollno = student_roll
        self.address = student_add

    # Instance method
    def get_student_details(self) -> dict:
        return {'name': self.name,'roll number': self.rollno, 'address': self.address}
    


student_1 = Student('Sumanth', 1, 'NewYork')  
details = student_1.get_student_details()
print(details)

