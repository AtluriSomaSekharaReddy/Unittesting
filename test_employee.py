from employee import Employee
import unittest
from unittest.mock import patch
class TestingEmployee(unittest.TestCase):
    def setUp(self):
        # print('setUp\n')
        self.emp_1 = Employee('s', 'ss', 22)
        
    def tearDown(self):
        pass
    def test_email(self):
        self.assertEqual(self.emp_1.email(), 's_ss@gmail.com')
    def test_pay(self):
        self.assertEqual(self.emp_1.new_income(),33)  
    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname(),"sss")
    def test_inpur(self):
        self.assertIn(type(self.emp_1.firstname),[str])
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/ss/May')
            self.assertEqual(schedule, 'Success')

if __name__ == '__main__':
    unittest.main()