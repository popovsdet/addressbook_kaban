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


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_modify_group(app, add_first_group, group):
    old_group_list = app.group.get_groups()
    # random group number from old_group_list
    # this group we will modify
    index = random.randrange(len(old_group_list))
    group.id = old_group_list[index].id
    app.group.modify(group, index)
    new_group_list = app.group.get_groups()

    assert len(old_group_list) == len(new_group_list), f"Old list '{old_group_list}' != new list '{new_group_list}'"

    old_group_list[index] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max), \
        f"Old list '{old_group_list}' != new list '{new_group_list}'"
