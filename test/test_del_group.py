import random

from model.group import Group


def test_delete_first_group_with_fixture(app, db, check_gui, add_first_group):
    old_group_list = db.get_groups()
    # Get random number in range (0, len(old_group_list))
    # index = randrange(len(old_group_list))
    group = random.choice(old_group_list)
    app.group.delete(id=group.id)
    new_group_list = db.get_groups()
    assert len(old_group_list) - 1 == len(new_group_list), \
        f"Len of old list '{old_group_list}' != new list '{new_group_list}'"
    # Remove group with index from old group list
    old_group_list.remove(group)
    assert old_group_list == new_group_list, f"Old list '{old_group_list}' != new list '{new_group_list}'"
    # list from DB and from GUI
    if check_gui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(app.group.get_groups(), key=Group.id_or_max)
