"""
Generate test data for contacts.
We have 2 options for a cmd:
n - number of generated contacts
f - file with that generated contacts
t - type of test data: random
Usage: "-n 10 -f data/contacts.json" or put it in "Parameters" in PyCharm. This file doesn't use pytest.
If cmd is empty, we use default values of "n" and "f"
"""
# read options from a command line
import getopt
import json
import os
import random
import string
# get access to options of a command line
import sys

from model.contact import Contact

# default values
number_of_contacts = 5
file_data = "data/contacts.json"
type_of_data = "random"

# 1. READ PARAMETERS FROM A COMMAND LINE
# read options from a command line and put it in "opts"
try:
    # opts returns: [(option, value), (option, value), (option, value)]
    # [('-n', '10'), ('-f', 'data/contacts.json'), ('-t', 'random')]
    opts, args = getopt.getopt(args=sys.argv[1:], shortopts="n:f:t:",
                               longopts=["number of contacts", "file", "random/constant data"])
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

# opts is a list of (option, value) pairs
for option, value in opts:
    if option == "-n":
        number_of_contacts = int(value)
    elif option == "-f":
        file_data = value
    elif option == "-t":
        type_of_data = value


# 2. DATA GENERATION
def random_sting(prefix, max_len):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(max_len))])


if type_of_data == "random":
    test_data = [Contact(first_name="", last_name="", address="", home_phone="", mobile_phone="", work_phone="",
                         secondary_phone="", email="")] + \
                [Contact(first_name=random_sting("first_name", 5), last_name=random_sting("last_name", 5),
                         address=random_sting("address", 5), home_phone=random_sting("h_p", 5),
                         mobile_phone=random_sting("m_p", 5), work_phone=random_sting("w_p", 5),
                         secondary_phone=random_sting("s_p", 10), email=random_sting("email", 5))
                 for _ in range(number_of_contacts)]
elif type_of_data == "constant":
    test_data = [Contact(first_name="first_name_1", last_name="last_name_1", address="address_1",
                         home_phone="home_phone_1", mobile_phone="mobile_phone_1", work_phone="work_phone_1",
                         secondary_phone="secondary_phone_1", email="email_1"),
                 Contact(first_name="first_name_2", last_name="last_name_2", address="address_2",
                         home_phone="home_phone_2", mobile_phone="mobile_phone_2", work_phone="work_phone_2",
                         secondary_phone="secondary_phone_2", email="email_2")]
else:
    test_data = [Contact(first_name="", last_name="", address="", home_phone="", mobile_phone="", work_phone="",
                         secondary_phone="", email="")]

# 3. SAVE DATA TO A FILE
# path to a file with data for contacts
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", file_data)
# open the file for writing
with open(file, "w") as file_data:
    # 1. Convert instance of Contact class to dict using default=lambda x: x.__dict__
    # 2. Write json file using that dict. f.write(json.dumps)
    file_data.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))
