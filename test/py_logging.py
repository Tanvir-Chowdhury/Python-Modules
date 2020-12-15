import logging

# logging level: 
# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

'''logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('test.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logging.basicConfig(filename= 'test.log', level= logging.DEBUG, format= '%(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def mul(x, y):
    return x*y

def div(x, y):
    return x/y

num_1 = 25
num_2 = 5

add_result = add(num_1, num_2)
sub_result = sub(num_1, num_2)
mul_result = mul(num_1, num_2)
div_result = div(num_1, num_2)

logging.debug(add_result)
logging.debug(sub_result)
logging.debug(mul_result)
logging.debug(div_result)'''


'''logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(filename)s : %(funcName)s : %(threadName)s : %(levelname)s : %(name)s : %(message)s')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)'''

#logging.basicConfig(filename = 'employee.log', level = logging.INFO, format = '%(filename)s : %(funcName)s : %(threadName)s : %(levelname)s : %(name)s : %(message)s')

import requests

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last 

        #logger.info(f"created employee : {self.fullname} - {self.email}")
        print(f"created employee : {self.fullname} - {self.email}")

    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@gmail.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    def monthly_schedule(self, month):
        response = requests.get(f"http://company.com/{self.last}/{month}")
        if response.ok:
            return response.text
        else :
            return "Bad response!"

em1 = Employee('Tanvir', 'Chowdhury')
em2 = Employee('Tanim', 'Chowdhury')
