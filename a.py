#Question:1

data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter(lambda x:x > 4 , data)
print(list(result))

#Expected Output is : [10, 501, 22, 37, 100, 999, 87, 351]
#Explanation: Now, this code will filter out elements from the data list that are greater than  and print the result as a list.

#Question:2
#To check every element of a list is an integer or string

my_list = [1, 'apple', 2, 'banana','suba']

result1 = all(map(lambda x: isinstance(x, (int,str)) ,my_list))

print(result1)

#Question:3
# Using Python lambda function to create a fibonacci series 1 to 50:

from functools import reduce

num_elements = 50

fibanocci_series = reduce(lambda x, _:x+[x[-2]+x[-1]],range(num_elements-2),[0,1])

print(fibanocci_series)

#Question:4

import re

def validate_regex(pattern,test_strings):
    regex=re.compile(pattern)
    return [bool(regex.match(test_string)) for test_string in test_strings]

#Email Address:
email_pattern = (r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
email_tests=["user@example.com","invalid.email@,com","another_user@gmail"]
email_results=validate_regex(email_pattern,email_tests)
print("Email Validation:", email_results)

#Mobile Numbers of bangladesh:
bangladesh_mobile_pattern=r'^\+8801[3-9]\d{8}$'
bangladesh_mobile_tests=["+880171235678","+88019123456789","invalid_number"]

bangladesh_mobile_results=validate_regex(bangladesh_mobile_pattern,bangladesh_mobile_tests)
print("Bangladesh Mobile Validation:",bangladesh_mobile_results)

#Telephone number of USA

usa_telephone_pattern=r'^\+1-\d{3}-\d{3}-\d{4}$'

usa_telephone_tests=["+1=123-456-7890", "+1-9876543210", "invaild_number"]

usa_telephone_results=validate_regex(usa_telephone_pattern,usa_telephone_tests)

print("USA Telephone Validation:",usa_telephone_results)

#16 characters Aplha-Numeric password:
password_pattern=r'^[A-Za-z0-9!@#$%^&*()_+=-]{16}$'
password_tests=["Abc123!@456DEF","invalid_password","ShortPwd123!@#"]
password_results=validate_regex(password_pattern,password_tests)
print("Password Validation:",password_results)



