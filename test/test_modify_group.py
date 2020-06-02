import random

from model.group import Group


def test_modify_group(app, add_first_group, json_groups):
    group = json_groups
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
