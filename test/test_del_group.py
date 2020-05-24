from model.group import Group


# def test_delete_first_group(app):
#     if not app.group.number():
#         app.group.create(Group(name="test"))
#
#     old_groups = app.group.get_groups()
#     app.group.delete()
#     new_groups = app.group.get_groups()
#     assert len(old_groups) - 1 == len(new_groups), f"Old list '{old_groups}' != new list '{new_groups}'"


def test_delete_first_group_with_fixture(app, check_group):
    old_groups = app.group.get_groups()
    app.group.delete()
    new_groups = app.group.get_groups()
    assert len(old_groups) - 1 == len(new_groups), f"Len of old list '{old_groups}' != new list '{new_groups}'"
    assert old_groups[1:] == new_groups, f"Old list '{old_groups}' != new list '{new_groups}'"
