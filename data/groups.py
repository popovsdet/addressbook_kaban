"""
Create test data for groups.
"""
import random
import string

from model.group import Group


def random_sting(prefix, max_len):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


random_data = [Group(name="", header="", footer="")] + \
              [Group(name=random_sting("name", 10), header=random_sting("header", 12),
                     footer=random_sting("footer", 15))
               for i in range(5)]

constant_data = [Group(name="name_1", header="header_1", footer="footer_1"),
                 Group(name="name_2", header="header_2", footer="footer_3")]

test_data = random_data

# random_test_data = [Group(name=name, header=header, footer=footer)
#     for name in ["", random_sting("name", 10)]
#     for header in ["", random_sting("header", 10)]
#     for footer in ["", random_sting("footer", 10)]]
