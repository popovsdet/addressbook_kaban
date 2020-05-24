from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_groups()
    group = Group(name="name_1", header="header_1", footer="footer_1")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count(), f"Old list '{old_groups}' != new list '{new_groups}'"

    new_groups = app.group.get_groups()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max), \
        f"Old list '{old_groups}' != new list '{new_groups}'"


# def test_add_empty_group(app):
#     old_groups = app.group.get_groups()
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     assert len(old_groups) + 1 == app.group.count(), f"Old list '{old_groups}' != new list '{new_groups}'"
#
#     new_groups = app.group.get_groups()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max), \
#         f"Old list '{old_groups}' != new list '{new_groups}'"
