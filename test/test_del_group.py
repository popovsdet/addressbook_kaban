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
    old_groups = app.group.get_groups()
    index = randrange(len(old_groups))
    app.group.delete(index=index)
    new_groups = app.group.get_groups()
    assert len(old_groups) - 1 == len(new_groups), f"Len of old list '{old_groups}' != new list '{new_groups}'"
    # Remove group with index from old group list
    old_groups[index:index + 1] = []
    assert old_groups == new_groups, f"Old list '{old_groups}' != new list '{new_groups}'"
