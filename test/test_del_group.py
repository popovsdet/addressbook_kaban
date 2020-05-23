from model.group import Group


def test_delete_first_group(app):
    if not app.group.number():
        app.group.create(Group(name="test"))
    app.group.delete()


def test_delete_first_group_with_fixture(app, check_group):
    app.group.delete()
