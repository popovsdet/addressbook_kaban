import random
import string

import pytest

from model.group import Group


def random_sting(prefix, max_len):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


test_data = [Group(name="", header="", footer="")] + \
            [Group(name=random_sting("name", 10), header=random_sting("header", 12), footer=random_sting("footer", 15))
             for i in range(5)]


# test_data = [Group(name=name, header=header, footer=footer)
#     for name in ["", random_sting("name", 10)]
#     for header in ["", random_sting("header", 10)]
#     for footer in ["", random_sting("footer", 10)]]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    """
    1. Get all groups from the screen. old_group_list
    2. Create a new group.
    Verification:
    3. Count all groups on the screen and verify it.
    4. Get one more time all groups from the screen. new_groups_count
    5. Add a new group to old_group_list.
    6. Compare old and new sorted lists. Because id generates in JS we cannot add it manually.
       We use key=Group.id_or_max which returns to us a very big number for added group from step #5
    """
    # 1. Get all groups from the screen.
    old_group_list = app.group.get_groups()
    # 2. Create a new group.
    # group = Group(name="name_1", header="header_1", footer="footer_1")
    app.group.create(group)
    # Verification:
    # 3. Count all groups on the screen.
    new_groups_count = app.group.count()
    assert len(old_group_list) + 1 == new_groups_count, f"Old list '{old_group_list}' != new list '{new_groups_count}'"
    # 4. Get one more time all groups from the screen.
    new_group_list = app.group.get_groups()
    # 5. Add a new group to old_group_list.
    old_group_list.append(group)
    # 6. Compare old and new sorted lists.
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max), \
        f"Old list '{old_group_list}' != new list '{new_group_list}'"
