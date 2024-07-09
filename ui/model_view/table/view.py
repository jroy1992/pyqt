from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets

from model import Model, Proxy


class View(QtWidgets.QTableView):

    def __init__(self, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)
        self.setAlternatingRowColors(True)
        self.setSortingEnabled(True)
        self.setShowGrid(False)

        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        self.verticalHeader().setHidden(True)
        self.verticalHeader().setDefaultSectionSize(20)

        self.horizontalHeader().setHidden(False)
        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setHighlightSections(False)


class Frame(QtWidgets.QFrame):

    def __init__(self, *args, **kwargs):
        super(Frame, self).__init__(*args, **kwargs)

        # widgets
        self.model = Model()
        self.proxy = Proxy()
        self.view = View()

        self.filter_field = QtWidgets.QLineEdit()
        self.change_button = QtWidgets.QPushButton('change data')

        # layout
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        layout.addWidget(self.filter_field)
        layout.addWidget(self.view)
        layout.addWidget(self.change_button)

        # signals
        self.change_button.clicked.connect(self.do_change_data)
        self.filter_field.textChanged.connect(self.update_filter)

        # init
        self.fill_test_items()

    def fill_test_items(self):
        self.refresh(
            [
                {
                    'name': 'mario',
                    'powerup': 'mushroom',
                    'checked': False
                },
                {
                    'name': 'luigi',
                    'powerup': 'fireflower',
                    'checked': False
                },
            ]
        )

    def update_filter(self, new_filter):
        self.proxy.setFilterRegExp(new_filter or '.*')

    def do_change_data(self):
        for n, i in enumerate(self.model.items):
            i['powerup'] = 'star'
            index = self.model.index(n, self.model.HEADER.index('powerup'))
            self.model.dataChanged.emit(index, index)

    def refresh(self, items):
        # temporarily un-set the model and source model
        self.view.setModel(None)
        self.proxy.setSourceModel(None)

        # update the objects
        self.model.items = items

        # re-set the model and source model
        self.proxy.setSourceModel(self.model)
        self.view.setModel(self.proxy)
