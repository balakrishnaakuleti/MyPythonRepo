# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 17:51:24 2018

@author: I329986
"""

from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
print(client.get_default_database)

db=client.test
employee = db.employee
employee_data = {
    'Name': 'Raj Kumar',
    'Address': 'Sears Streer, NZ',
    'Age': '42'
}
result = employee.insert_one(employee_data)

Queryresult = employee.find_one({'Age': '42'})
pprint(Queryresult)
