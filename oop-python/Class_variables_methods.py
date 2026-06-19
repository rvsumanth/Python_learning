'''
Class variables and Methods 
'''

class Teacher:
    '''Class Variables'''
    School_name = 'Harvard University'
    School_address = 'United states of America'
    School_principal = 'Donald Trump'

    '''Class Method'''
    @classmethod
    def change_principal_name(cls, name: str) -> dict:
         ''' This funtion is to change the principal name'''
         cls.School_principal = name
         return {'School principal': cls.School_principal}
    





print(f'Class Variables: {Teacher.School_name}, {Teacher.School_address}, {Teacher.School_principal}')
x = Teacher.change_principal_name('elon musk')
print(f'Class Method:{x}')