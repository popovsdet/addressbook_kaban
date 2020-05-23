from model.group import Group


def test_modify_group(app):
    if not app.group.number():
        app.group.create(Group(name="test"))
    app.group.modify(Group(name="name_2", header="header_2", footer="footer_2"))


def test_modify_group_name(app):
    if not app.group.number():
        app.group.create(Group(name="test"))
    app.group.modify(Group(name="name_2"))


def test_modify_group_header(app):
    if not app.group.number():
        app.group.create(Group(name="test"))
    app.group.modify(Group(header="header_2"))
