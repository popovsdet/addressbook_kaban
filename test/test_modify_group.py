from model.group import Group


def test_modify_group(app):
    app.group.modify(Group(name="name_2", header="header_2", footer="footer_2"))


def test_modify_group_name(app):
    app.group.modify(Group(name="name_2"))


def test_modify_group_header(app):
    app.group.modify(Group(header="header_2"))
