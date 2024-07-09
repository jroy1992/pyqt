from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets


class Proxy(QtCore.QSortFilterProxyModel):
    pass


class Model(QtCore.QAbstractItemModel):

    HEADER = ('name',)

    def __init__(self, *args, **kwargs):
        print 'In'
        super(Model, self).__init__(*args, **kwargs)
        self.root = None

    # ----------------
    # Required methods
    # ----------------

    def columnCount(self, parent):
        return len(self.HEADER)

    def headerData(self, section, orientation, role):
        if (
            orientation == QtCore.Qt.Horizontal and
            role == QtCore.Qt.DisplayRole
        ):
            return self.HEADER[section]

    def rowCount(self, parent):
        if parent is None or not parent.isValid():
            return len(self.root.children) if self.root is not None else 0

        parent_item = parent.internalPointer()
        return len(parent_item.children)

    def index(self, row, column, parent=None):
        if parent is None or not parent.isValid():
            return self.createIndex(
                row, column, self.root.get_item_at_row(row)
            )

        parent_item = parent.internalPointer()
        return self.createIndex(
            row,
            column,
            parent_item.get_item_at_row(row)
        )

    def parent(self, index):
        if index is None or not index.isValid():
            return QtCore.QModelIndex()

        item = index.internalPointer()
        parent = item.parent

        if parent == self.root:
            return QtCore.QModelIndex()

        return self.createIndex(
            parent.get_row(),
            index.column(),
            parent
        )

    # ---------------------
    # Required data methods
    # ---------------------

    def flags(self, index):
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled

    def data(self, index, role):
        col = index.column()
        item = index.internalPointer()

        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            if self.HEADER[col] == 'name':
                return item.name

        if role == QtCore.Qt.BackgroundRole:
            if self.HEADER[col] == 'name':
                return

        if role == QtCore.Qt.DecorationRole:
            if self.HEADER[col] == 'name':
                return

        if role == QtCore.Qt.ToolTipRole:
            if self.HEADER[col] == 'name':
                return
