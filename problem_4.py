class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    # base case: find out the user
    if user in group.get_users():
        return True
    else:
        # recursively find users in all subgroup
        for i in group.get_groups():
            if i is None:
                return False 
            if is_user_in_group(user, i):
                return True
    # cannot find
    return False


# TEST
parent = Group("parent")
child = Group("child")
sub_child = Group("sub_child")

sub_child_user = "sub_child_user"
parent_user = "parent_user"
sub_child.add_user(sub_child_user)
parent.add_user(parent_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group(sub_child_user, parent))
# True

print(is_user_in_group(sub_child_user, child))
# True

print(is_user_in_group("not_existed_user", child))
# False
# (not exist at all)

print(is_user_in_group(parent_user, sub_child))
# False
# (not in the group)