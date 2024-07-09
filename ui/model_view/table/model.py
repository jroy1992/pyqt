from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets


class Proxy(QtCore.QSortFilterProxyModel):
    pass


class Model(QtCore.QAbstractTableModel):

    HEADER = ('name','powerup', 'test')

    def __init__(self, *args, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
        self.items = []

    # ----------------
    # Required methods
    # ----------------

    def rowCount(self, parent):
        return len(self.items)

    def columnCount(self, parent):
        return len(self.HEADER)

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal:
            if role == QtCore.Qt.DisplayRole:
                return self.HEADER[section]

    def index(self, row, column, parent=None):
        if row >= len(self.items):
            return self.createIndex()
        return self.createIndex(
            row, column, self.items[row]
        )

    # ---------------------
    # Required data methods
    # ---------------------

    def flags(self, index):
        col = index.column()

        if self.HEADER[col] == 'powerup':
            return QtCore.Qt.ItemIsEnabled | \
                QtCore.Qt.ItemIsSelectable | \
                QtCore.Qt.ItemIsEditable | \
                QtCore.Qt.ItemIsUserCheckable

        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def data(self, index, role):
        col = index.column()
        item = index.internalPointer()

        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            if self.HEADER[col] == 'name':
                return item['name']
            if self.HEADER[col] == 'powerup':
                return item['powerup']

        if role == QtCore.Qt.BackgroundRole:
            # if self.HEADER[col] == 'name':
            #     return
            if item['checked']:
                # if self.HEADER[col] == 'powerup' or self.HEADER[col] == 'test':
                return QtGui.QColor(100,200,255,75)

        if role == QtCore.Qt.CheckStateRole:
            if self.HEADER[col] == 'powerup':
                return QtCore.Qt.Checked if item['checked'] else QtCore.Qt.Unchecked

        if role == QtCore.Qt.DecorationRole:
            if self.HEADER[col] == 'name':
                return

        if role == QtCore.Qt.ToolTipRole:
            if self.HEADER[col] == 'name':
                return

    def setData(self, index, value, role):
        col = index.column()
        item = index.internalPointer()

        if role == QtCore.Qt.EditRole:
            if self.HEADER[col] == 'powerup':
                item['powerup'] = value
                self.dataChanged.emit(index, index)
        if role == QtCore.Qt.CheckStateRole:
            # if self.HEADER[col] == 'powerup':
            item['checked'] = value == QtCore.Qt.Checked
            print('col count: ', self.columnCount(self.parent))
        # if role == QtCore.Qt.DisplayRole:
            for column in range(0,self.columnCount(self.parent)+1):
                print('row: ', index.row())
                print('column: ', column)
                index_new = self.index(index.row(), col, self.parent)
                self.dataChanged.emit(index_new, index_new)

        return True
