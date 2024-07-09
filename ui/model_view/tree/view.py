from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets

from item import HierarchyItem
from model import Model, Proxy


class View(QtWidgets.QTreeView):

    def __init__(self, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)
        self.setSortingEnabled(True)
        self.setAlternatingRowColors(True)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        # self.setExpanded(1,True)


class Frame(QtWidgets.QFrame):

    def __init__(self, *args, **kwargs):
        super(Frame, self).__init__(*args, **kwargs)

        # widgets
        self.model = Model()
        self.proxy = Proxy()
        self.view = View()

        # layout
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        layout.addWidget(self.view)

        # signals

        # init
        self.fill_test_items()

    def fill_test_items(self):
        root = HierarchyItem(None)
        files = ['groom.cpio', 'base.cpio']
        for t in range(3):
            toplevel = HierarchyItem('top_{}'.format(t))
            toplevel.parent = root

            for c in range(5):
                sublevel = HierarchyItem('sub_{}'.format(c))
                sublevel.parent = toplevel

                for f in files:
                    if f =='groom.cpio':
                        baselevel = HierarchyItem('groom')
                    elif f == 'base.cpio':
                        baselevel = HierarchyItem('base')
                    filelevel = HierarchyItem(''.format(f))
                    baselevel.parent = sublevel
                    filelevel.parent = baselevel

        self.refresh(root)

    def refresh(self, root=None):
        # temporarily un-set the model and source model
        self.view.setModel(None)
        self.proxy.setSourceModel(None)

        # update the objects
        self.model.root = root

        # re-set the model and source model
        self.proxy.setSourceModel(self.model)
        self.view.setModel(self.proxy)
