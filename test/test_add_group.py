from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="name_1", header="header_1", footer="footer_1"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
