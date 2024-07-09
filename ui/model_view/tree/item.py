import weakref


class HierarchyItem(object):

    def __init__(self, name):
        self._parent = None
        self.children = []
        self.name = name

    @property
    def parent(self):
        if self._parent is not None:
            return self._parent()
        return None

    @parent.setter
    def parent(self, value):
        if value == self.parent:
            return
        # remove self from current parent
        if self.parent is not None and self in self.parent.children:
            self.parent.children.remove(self)
        # set parent on current object
        if value is None:
            self._parent = None
            return
        self._parent = weakref.ref(value)
        # add self as child on new parent
        if self not in value.children:
            value.children.append(self)

    def iter_parents(self):
        parents = []
        if self.parent is not None:
            parents.append(self.parent)
            parents.extend(self.parent.iter_parents())
        return parents

    def iter_children(self):
        children = [c for c in self.children]
        for child in self.children:
            children.extend(child.iter_children())
        return children

    def get_row(self):
        if self.parent is None:
            return 0
        return self.parent.children.index(self)

    def get_item_at_row(self, row):
        return self.children[row]
