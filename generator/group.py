"""
Usage in cmd: "-n 3 -f data/groups.json -t random"
"""
import getopt
import os
import random
import string
import sys

import jsonpickle

from model.group import Group

# default values
number_of_groups = 5
file_data = "data/groups.json"
type_of_data = "random"

# 1. READ PARAMETERS FROM A COMMAND LINE
try:
    opts, args = getopt.getopt(args=sys.argv[1:], shortopts="n:f:t:",
                               longopts=["number of groups", "file", "random/constant data"])
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

for option, value in opts:
    if option == "-n":
        number_of_groups = int(value)
    elif option == "-f":
        file_data = value
    elif option == "-t":
        type_of_data = value


# 2. DATA GENERATION
def random_sting(prefix, max_len) -> str:
    """
    Generate a random string
    :param prefix: fist characters
    :param max_len: max len of randomly generated sting
    """
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(max_len))])


if type_of_data == "random":
    test_data = [Group(name="", header="", footer="")] + \
                [Group(name=random_sting("name", 10), header=random_sting("header", 12),
                       footer=random_sting("footer", 15))
                 for i in range(number_of_groups)]
elif type_of_data == "constant":
    test_data = [Group(name="name_1", header="header_1", footer="footer_1"),
                 Group(name="name_2", header="header_2", footer="footer_3")]
else:
    test_data = [Group(name="", header="", footer="")]

# 3. SAVE DATA TO A FILE
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"../{file_data}")

with open(file, "w") as file_data:
    # use a format option "json" to represent it in the file
    jsonpickle.set_encoder_options("json", indent=2)
    # in json file create a parameter with link to class file: "py/object": "model.group.Group"
    # rest of parameters it stores too
    file_data.write(jsonpickle.encode(test_data))
