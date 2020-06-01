import getopt
import os
import random
import string
import sys

import jsonpickle

from model.group import Group

# read options from a command line
try:
    opts, args = getopt.getopt(args=sys.argv[1:], shortopts="n:f:", longopts=["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_sting(prefix, max_len):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


random_test_data = [Group(name="", header="", footer="")] + \
                   [Group(name=random_sting("name", 10), header=random_sting("header", 12),
                          footer=random_sting("footer", 15))
                    for i in range(n)]

path_to_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"../{f}")

with open(path_to_file, "w") as file:
    # use a format option "json" to represent it in the file
    jsonpickle.set_encoder_options("json", indent=2)
    # in json file create a parameter with link to class file: "py/object": "model.group.Group"
    # rest of parameters it stores too
    file.write(jsonpickle.encode(random_test_data))
