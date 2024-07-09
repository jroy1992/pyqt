from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets

from model import Model


class View(QtWidgets.QListView):
    pass


class Frame(QtWidgets.QFrame):

    def __init__(self, *args, **kwargs):
        super(Frame, self).__init__(*args, **kwargs)

        # widgets
        self.model = Model()
        self.view = View()

        # layout
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        layout.addWidget(self.view)

        self.fill_test_items()

    def fill_test_items(self):
        self.refresh(
            [
                "hello",
                "world"
            ]
        )

    def refresh(self, items):
        # temporarily un-set the model and source model
        self.view.setModel(None)

        # update the objects
        self.model.items = items

        # re-set the model and source model
        self.view.setModel(self.model)
