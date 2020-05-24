from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_groups()
    app.group.create(Group(name="name_1", header="header_1", footer="footer_1"))
    new_groups = app.group.get_groups()
    assert len(old_groups) + 1 == len(new_groups), f"Old list '{old_groups}' != new list '{new_groups}'"


def test_add_empty_group(app):
    old_groups = app.group.get_groups()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_groups()
    assert len(old_groups) + 1 == len(new_groups), f"Old list '{old_groups}' != new list '{new_groups}'"
