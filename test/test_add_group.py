from model.group import Group


def test_add_group(app, json_groups):
    """
    1. Get all groups from the screen. old_group_list
    2. Create a new group.
    Verification:
    3. Count all groups on the screen and verify it.
    4. Get one more time all groups from the screen. new_groups_count
    5. Add a new group to old_group_list.
    6. Compare old and new sorted lists. Because id generates in JS we cannot add it manually.
       We use key=Group.id_or_max which returns to us a very big number for added group from step #5
    :param app: fixture
    :param json_groups: data from json file
    """

    # 1. Get all groups from the screen.
    old_group_list = app.group.get_groups()
    # 2. Create a new group.
    # group = Group(name="name_1", header="header_1", footer="footer_1")
    app.group.create(json_groups)
    # Verification:
    # 3. Count all groups on the screen.
    new_groups_count = app.group.count()
    assert len(old_group_list) + 1 == new_groups_count, f"Old list '{old_group_list}' != new list '{new_groups_count}'"
    # 4. Get one more time all groups from the screen.
    new_group_list = app.group.get_groups()
    # 5. Add a new group to old_group_list.
    old_group_list.append(json_groups)
    # 6. Compare old and new sorted lists.
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max), \
        f"Old list '{old_group_list}' != new list '{new_group_list}'"
