import getopt
import json
import os
import random
import string
import sys

from model.group import Group

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
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
    # json.dumps(random_test_data) convert data to json
    file.write(json.dumps(random_test_data, default=lambda x: x.__dict__, indent=2))
