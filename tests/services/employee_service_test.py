import unittest

import pytest

import fortnox
from tests.services.commons import get_credentials


class EmployeeServiceTest(unittest.TestCase):

    def setUp(self):
        token, secret = get_credentials()
        self.client = fortnox.Client(access_token=token, client_secret=secret)
        self.valid_data = {
            'EmployeeId': '007',
            'FirstName': 'John',
            'LastName': 'Doe',
            'HourlyPay': '500',
        }

    @pytest.mark.order(0)
    def test_employee_create(self):
        try:
            employee = self.client.employees.create(**self.valid_data)
        except Exception as e:
            pass
        else:
            self.assertTrue(employee)
            self.assertEqual(employee.FirstName, self.valid_data['FirstName'])
            self.assertEqual(employee.LastName, self.valid_data['LastName'])
            self.assertEqual(employee.HourlyPay, self.valid_data['HourlyPay'])

    @pytest.mark.order(1)
    def test_employee_retrieve(self):
        employee = self.client.employees.retrieve(id='007')
        self.assertTrue(employee)
        self.assertEqual(employee.FirstName, self.valid_data['FirstName'])
        self.assertEqual(employee.LastName, self.valid_data['LastName'])
        self.assertEqual(str(employee.HourlyPay), self.valid_data['HourlyPay'])

    @pytest.mark.order(2)
    def test_employee_update(self):
        data = self.valid_data
        data.update({'id': '007'})
        employee = self.client.employees.update(**data)
        self.assertTrue(employee)
        self.assertEqual(employee.FirstName, self.valid_data['FirstName'])
        self.assertEqual(employee.LastName, self.valid_data['LastName'])
        self.assertEqual(employee.HourlyPay, self.valid_data['HourlyPay'])

    @pytest.mark.order(3)
    def test_employee_list(self):
        employees = self.client.employees.list()
        self.assertTrue(employees)
