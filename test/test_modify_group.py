from random import randrange

from model.group import Group


def test_modify_group(app, check_group):
    old_group_list = app.group.get_groups()
    # random group number from old_group_list
    # this group we will modify
    index = randrange(len(old_group_list))
    group_id = old_group_list[index].id
    group = Group(name="name_2", header="header_2", footer="footer_2", id=group_id)
    app.group.modify(group, index)
    new_group_list = app.group.get_groups()

    assert len(old_group_list) == len(new_group_list), f"Old list '{old_group_list}' != new list '{new_group_list}'"

    old_group_list[index] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max), \
        f"Old list '{old_group_list}' != new list '{new_group_list}'"

# def test_modify_group_name(app, check_group):
#     old_groups = app.group.get_groups()
#     app.group.modify(Group(name="name_2"))
#     new_groups = app.group.get_groups()
#     assert len(old_groups) == len(new_groups), f"Old list '{old_groups}' != new list '{new_groups}'"
#
#
# def test_modify_group_header(app, check_group):
#     old_groups = app.group.get_groups()
#     app.group.modify(Group(header="header_2"))
#     new_groups = app.group.get_groups()
#     assert len(old_groups) == len(new_groups), f"Old list '{old_groups}' != new list '{new_groups}'"
