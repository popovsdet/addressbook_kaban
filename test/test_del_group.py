from random import randrange


# def test_delete_first_group(app):
#     if not app.group.count():
#         app.group.create(Group(name="test"))
#
#     old_groups = app.group.get_groups()
#     app.group.delete()
#     new_groups = app.group.get_groups()
#     assert len(old_groups) - 1 == len(new_groups), f"Old list '{old_groups}' != new list '{new_groups}'"


def test_delete_first_group_with_fixture(app, check_group):
    old_group_list = app.group.get_groups()
    # Get random number in range (0, len(old_group_list))
    index = randrange(len(old_group_list))
    app.group.delete(index=index)
    new_group_list = app.group.get_groups()
    assert len(old_group_list) - 1 == len(new_group_list), \
        f"Len of old list '{old_group_list}' != new list '{new_group_list}'"
    # Remove group with index from old group list
    del old_group_list[index]
    assert old_group_list == new_group_list, f"Old list '{old_group_list}' != new list '{new_group_list}'"
