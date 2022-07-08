from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pickle as rick
from os import mkdir as md
from os.path import exists
from PyQt5.QtCore import QObject, QThread
from bot import Bot
import images_rc

path = "Storage"

if not exists(path):
    md(path)
try:
    with open("storage/user_websites.pickle", "rb") as handle:
        user_websites = rick.load(handle)
    with open("storage/user_data.pickle", "rb") as handle:
        user_login = rick.load(handle)
    with open("storage/user_config.pickle", "rb") as handle:
        config = rick.load(handle)
except:
    user_websites = {}
    user_login = {}
    config = {}
try:
    with open("storage/user_purchases.pickle", "rb") as handle:
        purchases = rick.load(handle)
except:
    purchases = []
try: 
    test = config["debug"]
except:
    config["debug"] = False
    with open("storage/user_config.pickle", "wb") as handle:
        rick.dump(config, handle, protocol=rick.HIGHEST_PROTOCOL)


class Ui_GPUMagician(object):
    def setupUi(self, GPUMagician):
        # config

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GPUMagician.sizePolicy().hasHeightForWidth())
        GPUMagician.resize(800, 600)
        GPUMagician.setWindowTitle("GPU Magician")
        GPUMagician.setWindowIcon(QtGui.QIcon("logo.ico"))
        GPUMagician.setSizePolicy(sizePolicy)
        GPUMagician.setMaximumSize(QtCore.QSize(800, 600))
        GPUMagician.setStyleSheet("color: white;")

        self.centralwidget = QtWidgets.QWidget(GPUMagician)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 0px; width: 0px;}")
        self.tabWidget.setDocumentMode(True)

        self.home = QtWidgets.QWidget()

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.home)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(280, 330, 241, 191))
        self.home_start_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.home_start_button.sizePolicy().hasHeightForWidth()
        )

        self.home_start_button.setSizePolicy(sizePolicy)
        self.home_start_button.setStyleSheet(
            "background-color: rgb(134, 194, 50); padding: 10px;"
        )
        self.home_start_button.clicked.connect(self.worker_page)
        self.home_start_button.setText("Start")

        self.home_setup_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.home_setup_button.setStyleSheet(
            "background-color: rgb(134, 194, 50);padding: 10px;"
        )
        self.home_setup_button.clicked.connect(self.setup_page)
        self.home_setup_button.setText("Setup")

        self.verticalLayout_2.addWidget(self.home_start_button)
        self.verticalLayout_2.addWidget(self.home_setup_button)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.home)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(269, 0, 261, 331))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.home_title_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.home_title_label.setFont(font)
        self.home_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.home_title_label.setText("Gpu Magician")
        self.home_title_label.raise_()

        self.home_icon_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.home_icon_label.raise_()
        self.home_icon_label.setText(
            '<html><head/><body><p><img src=":/icon/logo.png"/></p></body></html>'
        )

        self.verticalLayout.addWidget(self.home_title_label)
        self.verticalLayout.addWidget(self.home_icon_label)

        self.home_background_label = QtWidgets.QLabel(self.home)
        self.home_background_label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.home_background_label.setMinimumSize(QtCore.QSize(800, 600))

        self.home_background_label.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.verticalLayoutWidget.raise_()

        self.tabWidget.addTab(self.home, "")
        self.worker = QtWidgets.QWidget()

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.worker)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1303, 602))

        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.addItem(spacerItem)

        font = QtGui.QFont()
        font.setPointSize(15)

        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setText("Purchase Log")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.addItem(spacerItem1)
        self.verticalLayout_5.addWidget(self.label_3)

        self.scrollArea_2 = QtWidgets.QScrollArea(self.horizontalLayoutWidget)

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())

        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setStyleSheet("background-color: #222629;")
        self.scrollArea_2.setMinimumSize(QtCore.QSize(548, 300))

        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 548, 111))

        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)

        for x in purchases:

            self.setup_layout_13 = QtWidgets.QHBoxLayout()

            self.worker_name_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
            self.worker_price_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
            self.worker_website_label = QtWidgets.QLabel(
                self.scrollAreaWidgetContents_2
            )
            self.worker_time_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
            self.worker_date_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)

            spacerItem2 = QtWidgets.QSpacerItem(
                40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
            )

            self.worker_name_label.setText(f"Name: {x['name']}")
            self.worker_price_label.setText(f"Price: {x['price']}")
            self.worker_website_label.setText(f"Website: {x['website']}")
            self.worker_time_label.setText(f"Time: {x['time']}")
            self.worker_date_label.setText(f"Date: {x['date']}")

            sizePolicy = QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
            )
            sizePolicy.setHeightForWidth(
                self.worker_name_label.sizePolicy().hasHeightForWidth()
            )

            self.worker_name_label.setSizePolicy(sizePolicy)
            self.worker_name_label.setMinimumSize(QtCore.QSize(0, 25))
            self.worker_name_label.setMaximumSize(QtCore.QSize(16777215, 25))

            self.setup_layout_13.addWidget(self.worker_name_label)
            self.setup_layout_13.addWidget(self.worker_price_label)
            self.setup_layout_13.addWidget(self.worker_website_label)
            self.setup_layout_13.addWidget(self.worker_time_label)
            self.setup_layout_13.addWidget(self.worker_date_label)
            self.setup_layout_13.addItem(spacerItem2)

            self.verticalLayout_8.addLayout(self.setup_layout_13)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )

        self.verticalLayout_5.addWidget(self.scrollArea_2)
        self.verticalLayout_5.addItem(spacerItem5)

        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2.addItem(spacerItem6)

        spacerItem7 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        spacerItem8 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )

        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_2.setStyleSheet("background-color: rgb(134, 194, 50);")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.clicked.connect(self.start_worker)
        self.pushButton_2.setText("Start Worker")

        self.worker_back_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.worker_back_button.setStyleSheet("background-color: rgb(161, 161, 161);")
        self.worker_back_button.setText("Back")
        self.worker_back_button.clicked.connect(self.home_page)

        self.worker_debug_check = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.worker_debug_check.setStyleSheet("background-color: rgb(134, 194, 50);")
        self.worker_debug_check.setText("Debug Mode")
        self.worker_debug_check.stateChanged.connect(self.debug)

        spacerItem9 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )

        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.addItem(spacerItem7)
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout_4.addWidget(self.worker_back_button)
        self.verticalLayout_4.addItem(spacerItem8)
        self.verticalLayout_4.addWidget(self.worker_debug_check)
        self.verticalLayout_4.addItem(spacerItem9)

        self.verticalLayout_7 = QtWidgets.QVBoxLayout()

        spacerItem10 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.Minimum,
        )

        self.home_background_label_2 = QtWidgets.QLabel(self.worker)
        self.home_background_label_2.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.home_background_label_2.setMinimumSize(QtCore.QSize(800, 600))

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.home_background_label_2.raise_()
        self.horizontalLayoutWidget.raise_()
        self.tabWidget.addTab(self.worker, "")
        self.setup = QtWidgets.QWidget()

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.setup)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 110, 751, 401))

        # Main Setup layout
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.setup_website_combo_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.setup_website_combo_2.setFont(font)

        self.setup_website_combo_2.setStyleSheet("background-color: rgb(134, 194, 50);")
        self.setup_website_combo_2.addItem("None")
        self.setup_website_combo_2.addItem("Amazon")
        self.setup_website_combo_2.addItem("BestBuy")
        self.setup_website_combo_2.setItemText(0, "-Website-")
        self.setup_website_combo_2.setItemText(1, "Amazon")
        self.setup_website_combo_2.setItemText(2, "BestBuy(Broken)")

        self.horizontalLayout.addWidget(self.setup_website_combo_2)

        self.setup_website_combo_2.currentTextChanged.connect(self.website_changed)

        self.setup_puchase_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.setup_puchase_label.setFont(font)
        self.setup_puchase_label.setText("Item Purchase Limit")

        self.horizontalLayout.addWidget(self.setup_puchase_label)
        self.setup_items_spinbox = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)

        self.setup_items_spinbox.setMinimum(1)
        self.setup_items_spinbox.setProperty("value", 1)

        self.setup_items_spinbox.setStyleSheet("color: black;")
        try:
            self.setup_items_spinbox.setValue(config["items"])
        except:
            pass

        self.horizontalLayout.addWidget(self.setup_items_spinbox)
        spacerItem11 = QtWidgets.QSpacerItem(
            50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem11)
        self.setup_login_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)

        self.setup_login_button.setStyleSheet("background-color: rgb(134, 194, 50);")
        self.setup_login_button.clicked.connect(self.login)
        self.setup_login_button.setText("Login")
        self.horizontalLayout.addWidget(self.setup_login_button)

        self.setup_add_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.setup_add_button.setStyleSheet("background-color: rgb(134, 194, 50);")
        self.setup_add_button.clicked.connect(self.add_item)
        self.horizontalLayout.addWidget(self.setup_add_button)
        self.setup_add_button.setText("+Add Item")

        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(729, 100))
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 730, 360))

        self.scrollArea.setStyleSheet("background-color: #222629;")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()

        self.setup_save_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.setup_save_button.setStyleSheet("background-color: rgb(134, 194, 50);")
        self.setup_save_button.clicked.connect(self.save_all)
        self.horizontalLayout_16.addWidget(self.setup_save_button)
        self.setup_save_button.setText("Save")

        self.setup_nuke_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.setup_nuke_button.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.setup_nuke_button.clicked.connect(self.tactical_nuke_incoming)
        self.horizontalLayout_16.addWidget(self.setup_nuke_button)
        self.setup_nuke_button.setText("Clear ALL save data")

        self.setup_back_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.setup_back_button.setStyleSheet("background-color: rgb(161, 161, 161);")

        self.setup_back_button.clicked.connect(self.home_page)
        self.setup_back_button.setText("Back")

        self.horizontalLayout_16.addWidget(self.setup_back_button)

        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        self.setup_background_label = QtWidgets.QLabel(self.setup)
        self.setup_background_label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.setup_background_label.setMinimumSize(QtCore.QSize(800, 600))

        self.setup_background_label.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.tabWidget.addTab(self.setup, "")
        GPUMagician.setCentralWidget(self.centralwidget)

        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GPUMagician)

        self.home_background_label_2.setText(
            '<html><head/><body><p><img src=":/images/bg2k.png"/></p></body></html>'
        )
        self.home_background_label.setText(
            '<html><head/><body><p><img src=":/images/bg2k.png"/></p></body></html>'
        )
        self.setup_background_label.setText(
            '<html><head/><body><p><img src=":/images/bg2k.png"/></p></body></html>'
        )

        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)

    def login(self):
        website = self.setup_website_combo_2.currentText()
        if website == "-Website-":
            pass
        else:
            Ui_GPUMagician.website = self.setup_website_combo_2.currentText()
            Dialog = QtWidgets.QDialog()
            ui = Login()
            ui.setupUi(Dialog)
            Dialog.exec_()
            self.clear_layout(self.verticalLayout_6)
            self.draw_scrollarea()

    def add_item(self):
        if self.setup_website_combo_2.currentText() == "-Website-":
            pass
        else:
            Ui_GPUMagician.website = self.setup_website_combo_2.currentText()
            Dialog = QtWidgets.QDialog()
            ui = Add_Item()
            ui.setupUi(Dialog)
            Dialog.exec_()
            self.clear_layout(self.verticalLayout_6)
            self.draw_scrollarea()

    def edit_item(self, x, y):
        Ui_GPUMagician.website = self.setup_website_combo_2.currentText()
        Ui_GPUMagician.nick = y["nick"]
        Ui_GPUMagician.price = y["price"]
        Ui_GPUMagician.current_url = x
        Dialog = QtWidgets.QDialog()
        ui = Edit_Item()
        ui.setupUi(Dialog)
        Dialog.exec_()
        self.clear_layout(self.verticalLayout_6)
        self.draw_scrollarea()

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    self.clear_layout(child.layout())

    def website_changed(self):
        self.clear_layout(self.verticalLayout_6)
        self.draw_scrollarea()

    def home_page(self):
        self.tabWidget.setCurrentIndex(0)

    def worker_page(self):
        self.tabWidget.setCurrentIndex(1)

    def setup_page(self):
        self.tabWidget.setCurrentIndex(2)

    def delete_row(self, x):
        del user_websites[x]
        self.clear_layout(self.verticalLayout_6)
        self.draw_scrollarea()

    def tactical_nuke_incoming(self):
        user_login.clear()
        user_websites.clear()
        self.clear_layout(self.verticalLayout_6)
        self.draw_scrollarea()

    def draw_scrollarea(self):
        #!BUG all buttons in loop call the last x value | Fixed with closure
        for i, (x, y) in enumerate(user_websites.items()):
            self.setup_layout_6 = QtWidgets.QHBoxLayout()
            if y["website"] == self.setup_website_combo_2.currentText():

                self.setup_checkbox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
                self.setup_checkbox.setMinimumSize(QtCore.QSize(0, 50))
                self.setup_checkbox.setChecked(True)
                self.setup_checkbox.setText("Active")

                # Creates a label based on user provided nickname
                self.setup_nickname_label = QtWidgets.QLabel(
                    self.scrollAreaWidgetContents
                )
                sizePolicy = QtWidgets.QSizePolicy(
                    QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
                )
                sizePolicy.setHeightForWidth(
                    self.setup_nickname_label.sizePolicy().hasHeightForWidth()
                )
                self.setup_nickname_label.setSizePolicy(sizePolicy)
                self.setup_nickname_label.setMinimumSize(QtCore.QSize(0, 50))
                self.setup_nickname_label.setText(y["nick"])

                # Creates a label based on user provided price
                self.setup_price_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                sizePolicy = QtWidgets.QSizePolicy(
                    QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
                )
                sizePolicy.setHeightForWidth(
                    self.setup_price_label.sizePolicy().hasHeightForWidth()
                )
                self.setup_price_label.setSizePolicy(sizePolicy)
                self.setup_price_label.setText(f'${y["price"]}')

                # Allowes the user to edit the individual line
                sizePolicy = QtWidgets.QSizePolicy(
                    QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
                )
                self.setup_edit_button = QtWidgets.QPushButton(
                    self.scrollAreaWidgetContents
                )
                sizePolicy.setHeightForWidth(
                    self.setup_edit_button.sizePolicy().hasHeightForWidth()
                )
                self.setup_edit_button.setSizePolicy(sizePolicy)
                self.setup_edit_button.setStyleSheet(
                    "background-color: rgb(134, 194, 50);"
                )
                self.setup_edit_button.clicked.connect(partial(self.edit_item, x, y))
                self.setup_edit_button.setText("Edit")

                # Allowes for the removal of any specific line
                self.setup_delete_button = QtWidgets.QPushButton(
                    self.scrollAreaWidgetContents
                )
                sizePolicy = QtWidgets.QSizePolicy(
                    QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
                )
                sizePolicy.setHeightForWidth(
                    self.setup_delete_button.sizePolicy().hasHeightForWidth()
                )
                self.setup_delete_button.setSizePolicy(sizePolicy)
                self.setup_delete_button.setText("Delete")
                self.setup_delete_button.clicked.connect(partial(self.delete_row, x))

                # added to improve visual clarity while scrolling | alternates between red and orange
                if i % 2 == 0:
                    self.setup_delete_button.setStyleSheet(
                        "background-color: rgb(255, 30, 0);"
                    )
                else:
                    self.setup_delete_button.setStyleSheet(
                        "background-color: rgb(255, 85, 0);"
                    )
                spacerItem12 = QtWidgets.QSpacerItem(
                    40,
                    20,
                    QtWidgets.QSizePolicy.Expanding,
                    QtWidgets.QSizePolicy.Minimum,
                )

                #self.setup_layout_6.addWidget(self.setup_checkbox)
                self.setup_layout_6.addWidget(self.setup_nickname_label)
                self.setup_layout_6.addWidget(self.setup_price_label)
                self.setup_layout_6.addItem(spacerItem12)
                self.setup_layout_6.addWidget(self.setup_edit_button)
                self.setup_layout_6.addWidget(self.setup_delete_button)
                self.verticalLayout_6.addLayout(self.setup_layout_6)

    def save_all(self):
        config["items"] = self.setup_items_spinbox.value()

        with open("storage/user_websites.pickle", "wb") as handle:
            rick.dump(user_websites, handle, protocol=rick.HIGHEST_PROTOCOL)
        with open("storage/user_data.pickle", "wb") as handle:
            rick.dump(user_login, handle, protocol=rick.HIGHEST_PROTOCOL)
        with open("storage/user_config.pickle", "wb") as handle:
            rick.dump(config, handle, protocol=rick.HIGHEST_PROTOCOL)
        self.setup_save_button.setText("Saved")

    def debug(self):
        if self.worker_debug_check.isChecked():
            config["debug"] = True
        else:
            config["debug"] = False
        with open("storage/user_config.pickle", "wb") as handle:
            rick.dump(config, handle, protocol=rick.HIGHEST_PROTOCOL)

    def start_worker(self):
        if self.pushButton_2.isChecked():
            if not self.thread.isRunning():
                self.thread.start()
            else:
                self.worker.resume()
        else:  
            self.worker.stop()


class Worker(QObject):
    def __init__(self):
        super().__init__()

    def run(self):
        self.resume()
        Bot().check_availability()

    def resume(self):
        Bot.start_running(Bot)
    
    def stop(self):
        Bot.stop_running(Bot)
    
class Login(Ui_GPUMagician, object):
    def setupUi(self, Dialog):

        Dialog.setWindowIcon(QtGui.QIcon("login.png"))
        Dialog.setWindowTitle("Login")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background-color: #222629; color: white;")

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setStyleSheet("background-color: rgb(134, 194, 50);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save
        )
        self.buttonBox.accepted.connect(self.save_login)  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject)  # type: ignore

        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 231))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)

        self.login_username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.login_username.setPlaceholderText("Email")

        self.login_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.login_password.setPlaceholderText("Password")

        #self.login_CVV2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        #self.login_CVV2.setPlaceholderText("CVV2(card security number)")

        self.verticalLayout.addWidget(self.login_username)
        self.verticalLayout.addWidget(self.login_password)
        #self.verticalLayout.addWidget(self.login_CVV2)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Dialog = Dialog

    def save_login(self):
        user_login[Ui_GPUMagician.website] = {
            "username": self.login_username.text(),
            "password": self.login_password.text(),
            #"CVV2": self.login_CVV2.text(),
        }
        self.Dialog.close()


class Add_Item(object):
    def setupUi(self, Dialog):

        Dialog.setWindowIcon(QtGui.QIcon("plus.png"))
        Dialog.setWindowTitle("Add Item")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background-color: #222629; color: white;")

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setStyleSheet("background-color: rgb(134, 194, 50);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save
        )
        self.buttonBox.accepted.connect(self.add_item)  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject)  # type: ignore

        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 231))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)

        self.item_url = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.item_url.setPlaceholderText("Enter URL here")

        self.item_price = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.item_price.setPlaceholderText("Maximum Price (Before Taxes)")

        self.item_nick = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.item_nick.setPlaceholderText("Nick Name")

        self.verticalLayout.addWidget(self.item_url)
        self.verticalLayout.addWidget(self.item_price)
        self.verticalLayout.addWidget(self.item_nick)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Dialog = Dialog

    def add_item(self):
        user_websites[self.item_url.text()] = {
            "website": Ui_GPUMagician.website,
            "price": self.item_price.text(),
            "nick": self.item_nick.text(),
        }
        self.Dialog.close()


class Edit_Item(object):
    def setupUi(self, Dialog):

        Dialog.setWindowIcon(QtGui.QIcon("edit.png"))
        Dialog.setWindowTitle("Edit Item")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background-color: #222629; color: white;")

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setStyleSheet("background-color: rgb(134, 194, 50);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save
        )
        self.buttonBox.accepted.connect(self.edit_item)  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject)  # type: ignore

        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 231))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)

        self.item_url = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.item_url.setPlaceholderText("Enter URL here")
        self.item_url.setText(Ui_GPUMagician.current_url)

        self.item_price = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.item_price.setPlaceholderText("Maximum Price (Before Taxes)")
        self.item_price.setText(Ui_GPUMagician.price)

        self.item_nick = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.item_nick.setPlaceholderText("Nick Name")
        self.item_nick.setText(Ui_GPUMagician.nick)

        self.verticalLayout.addWidget(self.item_url)
        self.verticalLayout.addWidget(self.item_price)
        self.verticalLayout.addWidget(self.item_nick)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Dialog = Dialog

    def edit_item(self):
        user_websites[self.item_url.text()] = {
            "website": Ui_GPUMagician.website,
            "price": self.item_price.text(),
            "nick": self.item_nick.text(),
        }
        self.Dialog.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    GPUMagician = QtWidgets.QMainWindow()
    ui = Ui_GPUMagician()
    ui.setupUi(GPUMagician)
    GPUMagician.show()
    sys.exit(app.exec_())
