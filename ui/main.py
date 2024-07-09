__application__ = 'Model-View demo'
__version__ = '0.0.0'

import os
import sys
import logging

from Qt import QtGui
from Qt import QtCore
from Qt import QtWidgets

import settings_ui

import model_view.list.view as list_view
import model_view.table.view as table_view
import model_view.tree.view as tree_view

LOG = logging.getLogger(__application__)
if not LOG.handlers:
    LOG.addHandler(logging.StreamHandler())

STYLE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'style')


class Main(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        print 'we are in main init now'
        super(Main, self).__init__(*args, **kwargs)
        self.setObjectName(__application__)

        # window options
        self.setWindowTitle('%s - %s' % (__application__, __version__))
        self.resize(900, 500)

        # widgets
        tabs = QtWidgets.QTabWidget()
        self.list_view = list_view.Frame()
        self.table_view = table_view.Frame()
        self.tree_view = tree_view.Frame()

        tabs.addTab(self.list_view, 'list')
        tabs.addTab(self.table_view, 'table')
        tabs.addTab(self.tree_view, 'tree')

        # layout
        widg = QtWidgets.QWidget(parent=self)
        layout = QtWidgets.QVBoxLayout()

        widg.setLayout(layout)
        self.setCentralWidget(widg)
        layout.addWidget(tabs)

        # signals


def run():
    print 'in run'
    # create application instance
    app = QtWidgets.QApplication(sys.argv)

    # apply style sheet
    settings_ui.STYLE_PATH = STYLE_PATH
    qss = QtCore.QFile(STYLE_PATH + '\\app.css')
    qss.open(QtCore.QFile.ReadOnly)
    qss_fixed = str(
        qss.readAll()).replace('$STYLE_PATH$', STYLE_PATH.replace('\\', '/')
    )
    app.setStyleSheet(qss_fixed)
    qss.close()

    # open window
    wind = Main()
    settings_ui.main_ui = wind
    wind.show()
    app.exec_()
