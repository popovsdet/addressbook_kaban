from sys import maxsize


class Group(object):
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        """
        Representation of our class when we print it (not as a place in the memory, but as a sting)
        :return: string with id and name of the group
        """
        return f"id = '{self.id}': name = '{self.name}'"

    def __eq__(self, other):
        """
        Specify way to compare 2 instance of this class.
        For example: if names of each class are the same classes be the same too.
        self.name == other.name
        In our case we compare i
        :param other:
        :return: bool
        """
        return (self.id is None or other.id is None or self.id == other.id) and \
               self.name == other.name

    def id_or_max(self):
        """
        Check id in the group and return it or very big number
        :return: id or maxsize (very big number)
        """
        if self.id:
            return int(self.id)
        else:
            return maxsize
