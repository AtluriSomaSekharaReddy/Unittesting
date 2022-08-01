import requests
class Employee :
    raiseP=1.5
    def __init__(self,firstname,lastname,income):
        self.firstname=firstname
        self.lastname=lastname
        self.income=income
    def email(self):
        return("{}_{}@gmail.com".format(self.firstname,self.lastname))
    def fullname(self):
        return("{}{}".format(self.firstname,self.lastname))
    def new_income(self):
        return(self.income*self.raiseP)
    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.lastname}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
emp1=Employee("s","ss",22)
print(emp1.email())