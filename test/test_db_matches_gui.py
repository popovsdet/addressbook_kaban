from model.group import Group


def test_group_list(app, db):
    gui_list = app.group.get_groups()
    db_list = map(clean, db.get_groups())
    assert sorted(gui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def clean(group):
    return Group(id=group.id, name=group.name.strip())
