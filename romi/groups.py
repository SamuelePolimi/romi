class Group:

    def __init__(self, group_name, refs):
        self.group_name = group_name
        self.refs = refs

    def __str__(self):
        return "%r: %s" % (self.group_name, str(self.refs))

    def __repr__(self):
        return self.__str__()
