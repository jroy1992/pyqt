import os

from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets

# from ... import settings_ui



class Model(QtCore.QAbstractListModel):

    def __init__(self, *args, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
        self.items = []

    # ----------------
    # Required methods
    # ----------------

    def rowCount(self, parent):
        return len(self.items)

    def index(self, row, column, parent=None):
        if row >= len(self.items):
            return self.createIndex()
        return self.createIndex(
            row, column, self.items[row]
        )

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    # ---------------------
    # Required data methods
    # ---------------------

    def data(self, index, role):
        item = index.internalPointer()

        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            return item

        if role == QtCore.Qt.BackgroundRole:
            return QtGui.QColor(0, 255, 0, 50)

        # if role == QtCore.Qt.DecorationRole:
        #     return QtGui.QIcon(
        #         os.path.join(
        #             None, 'icons', 'icon_approved.png'
        #         )
        #     )

        if role == QtCore.Qt.ToolTipRole:
            return
