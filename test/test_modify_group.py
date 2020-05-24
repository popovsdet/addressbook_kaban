from model.group import Group


def test_modify_group(app, check_group):
    old_groups = app.group.get_groups()
    app.group.modify(Group(name="name_2", header="header_2", footer="footer_2"))
    new_groups = app.group.get_groups()
    assert len(old_groups) == len(new_groups), f"Old list '{old_groups}' != new list '{new_groups}'"


def test_modify_group_name(app, check_group):
    old_groups = app.group.get_groups()
    app.group.modify(Group(name="name_2"))
    new_groups = app.group.get_groups()
    assert len(old_groups) == len(new_groups), f"Old list '{old_groups}' != new list '{new_groups}'"


def test_modify_group_header(app, check_group):
    old_groups = app.group.get_groups()
    app.group.modify(Group(header="header_2"))
    new_groups = app.group.get_groups()
    assert len(old_groups) == len(new_groups), f"Old list '{old_groups}' != new list '{new_groups}'"
