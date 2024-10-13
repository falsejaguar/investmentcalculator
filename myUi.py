# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLCDNumber, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(883, 747)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 185, 97, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(14, 84, 10, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(170, 170, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush3)
        brush4 = QBrush(QColor(252, 180, 98, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush5 = QBrush(QColor(200, 243, 100, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush5)
        brush6 = QBrush(QColor(37, 40, 182, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush6)
        brush7 = QBrush(QColor(170, 170, 0, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        brush8 = QBrush(QColor(110, 113, 115, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        brush9 = QBrush(QColor(101, 103, 104, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        brush10 = QBrush(QColor(114, 118, 121, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush11 = QBrush(QColor(40, 44, 48, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush6)
        brush12 = QBrush(QColor(252, 252, 252, 128))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        MainWindow.setPalette(palette)
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        icon = QIcon()
        iconThemeName = u"computer"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(0.950000000000000)
        MainWindow.setStyleSheet(u"QWidget#centralwidget {\n"
"    background-color: #000000; /* Black background */\n"
"}\n"
"\n"
"QMainWindow {\n"
"    background-color: #000000; /* Black background */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #2E7D32; /* Dark green background */\n"
"    border: 3px solid #FFD700; /* Gold border */\n"
"    border-radius: 15px; /* Rounded corners */\n"
"    font-family: \"Math Jax_AMS\"; /* Built-in font */\n"
"    font-size: 19px; /* Font size */\n"
"    padding: 9px; /* Padding around the text */\n"
"    color: #de7a63; /* White text */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2E7D32, stop:1 #1B5E20); /* Gradient on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #004D40; /* Darker green on press */\n"
"    border: 3px solid #C0C0C0; /* Silver border on press */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A0A0A0; /* Grey background when disabled */\n"
"    border: 3px soli"
                        "d #A0A0A0; /* Grey border when disabled */\n"
"    color: #ffffff; /* White text when disabled */\n"
"}\n"
"\n"
"QRadioButton {\n"
"    font-family: \"Courier New\"; /* Built-in font */\n"
"    font-size: 16px; /* Font size */\n"
"    color: #de7a63; /* Light grey text */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    border: 2px solid #FFD700; /* Gold border */\n"
"    background-color: #2E7D32; /* Dark green */\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    border: 2px solid #FFD700; /* Gold border */\n"
"    background-color: #FFD700; /* Gold background */\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 2px solid #FFD700; /* Gold border */\n"
"    background-color: #a3b8c8; /* Dark green background */\n"
"    color: white; /* White text */\n"
"    font-family: \"Courier New\"; /* Built-in font */\n"
"    font-size: 16px; /* Font size */\n"
"    paddin"
                        "g: 5px; /* Padding */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #FFD700; /* Gold border */\n"
"    background-color: #00ffff; /* Darker green on hover */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #FFD700; /* Gold border */\n"
"    background-color: #7fb5b0; /* Slightly lighter green on focus */\n"
"}\n"
"QLCDNumber {\n"
"    background-color: #000000; /* Black background */\n"
"    color: #00FF00; /* Bright green text */\n"
"    border: 2px solid #FFD700; /* Gold border for consistency */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    padding: 5px; /* Padding around the display */\n"
"}\n"
"\n"
"QCheckBox {\n"
"    padding: 6px;\n"
"	border: 2px solid #fef65b; /* Black border */\n"
"    border-radius: 4px; \n"
"	color: #de7a63;\n"
"	background-color: #05313d;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #2196F3;\n"
"}\n"
"\n"
"QCh"
                        "eckBox::indicator:unchecked {\n"
"    background-color: #ccc;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dailyRadioButton = QRadioButton(self.centralwidget)
        self.dailyRadioButton.setObjectName(u"dailyRadioButton")
        self.dailyRadioButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.dailyRadioButton, 0, Qt.AlignHCenter)

        self.monthlyRadioButton = QRadioButton(self.centralwidget)
        self.monthlyRadioButton.setObjectName(u"monthlyRadioButton")
        self.monthlyRadioButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.monthlyRadioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.monthlyRadioButton, 0, Qt.AlignHCenter)

        self.quarterlyRadioButton = QRadioButton(self.centralwidget)
        self.quarterlyRadioButton.setObjectName(u"quarterlyRadioButton")
        self.quarterlyRadioButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.quarterlyRadioButton, 0, Qt.AlignHCenter)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"font: 29pt \"Winks\";")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(132)
        self.gridLayout_2.setVerticalSpacing(2)
        self.gridLayout_2.setContentsMargins(70, 2, 70, 2)
        self.yr6 = QLCDNumber(self.centralwidget)
        self.yr6.setObjectName(u"yr6")
        self.yr6.setDigitCount(8)
        self.yr6.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.yr6, 7, 1, 1, 1, Qt.AlignLeft)

        self.yr1 = QLCDNumber(self.centralwidget)
        self.yr1.setObjectName(u"yr1")
        self.yr1.setSmallDecimalPoint(False)
        self.yr1.setDigitCount(8)
        self.yr1.setSegmentStyle(QLCDNumber.Flat)
        self.yr1.setProperty(u"value", 0.000000000000000)

        self.gridLayout_2.addWidget(self.yr1, 0, 1, 1, 1, Qt.AlignLeft)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 10, 0, 1, 1, Qt.AlignRight)

        self.yr3 = QLCDNumber(self.centralwidget)
        self.yr3.setObjectName(u"yr3")
        self.yr3.setDigitCount(8)
        self.yr3.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.yr3, 3, 1, 1, 1, Qt.AlignLeft)

        self.yr11 = QLCDNumber(self.centralwidget)
        self.yr11.setObjectName(u"yr11")
        self.yr11.setDigitCount(8)
        self.yr11.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.yr11, 12, 1, 1, 1, Qt.AlignLeft)

        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 9, 0, 1, 1, Qt.AlignRight)

        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 8, 0, 1, 1, Qt.AlignRight)

        self.yr5 = QLCDNumber(self.centralwidget)
        self.yr5.setObjectName(u"yr5")
        self.yr5.setDigitCount(8)
        self.yr5.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.yr5, 6, 1, 1, 1, Qt.AlignLeft)

        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 6, 0, 1, 1, Qt.AlignRight)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1, Qt.AlignRight)

        self.yr10 = QLCDNumber(self.centralwidget)
        self.yr10.setObjectName(u"yr10")
        self.yr10.setDigitCount(8)
        self.yr10.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.yr10, 11, 1, 1, 1, Qt.AlignLeft)

        self.yr8 = QLCDNumber(self.centralwidget)
        self.yr8.setObjectName(u"yr8")
        self.yr8.setDigitCount(8)
        self.yr8.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.yr8, 9, 1, 1, 1, Qt.AlignLeft)

        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 7, 0, 1, 1, Qt.AlignRight)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 11, 0, 1, 1, Qt.AlignRight)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 12, 0, 1, 1, Qt.AlignRight)

        self.yr7 = QLCDNumber(self.centralwidget)
        self.yr7.setObjectName(u"yr7")
        self.yr7.setDigitCount(8)
        self.yr7.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.yr7, 8, 1, 1, 1, Qt.AlignLeft)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 5, 0, 1, 1, Qt.AlignRight)

        self.yr4 = QLCDNumber(self.centralwidget)
        self.yr4.setObjectName(u"yr4")
        self.yr4.setDigitCount(8)
        self.yr4.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.yr4, 5, 1, 1, 1, Qt.AlignLeft)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1, Qt.AlignRight)

        self.yr9 = QLCDNumber(self.centralwidget)
        self.yr9.setObjectName(u"yr9")
        self.yr9.setDigitCount(8)
        self.yr9.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.yr9, 10, 1, 1, 1, Qt.AlignLeft)

        self.yr2 = QLCDNumber(self.centralwidget)
        self.yr2.setObjectName(u"yr2")
        self.yr2.setDigitCount(8)
        self.yr2.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.yr2, 1, 1, 1, 1, Qt.AlignLeft)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1, Qt.AlignRight)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.l_additionLabel = QLabel(self.centralwidget)
        self.l_additionLabel.setObjectName(u"l_additionLabel")

        self.verticalLayout_3.addWidget(self.l_additionLabel)

        self.l_cagrLabel = QLabel(self.centralwidget)
        self.l_cagrLabel.setObjectName(u"l_cagrLabel")

        self.verticalLayout_3.addWidget(self.l_cagrLabel)

        self.l_apLabel = QLabel(self.centralwidget)
        self.l_apLabel.setObjectName(u"l_apLabel")

        self.verticalLayout_3.addWidget(self.l_apLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.inAmount = QLineEdit(self.centralwidget)
        self.inAmount.setObjectName(u"inAmount")

        self.verticalLayout_2.addWidget(self.inAmount)

        self.intRate = QLineEdit(self.centralwidget)
        self.intRate.setObjectName(u"intRate")

        self.verticalLayout_2.addWidget(self.intRate)

        self.adAmount = QLineEdit(self.centralwidget)
        self.adAmount.setObjectName(u"adAmount")

        self.verticalLayout_2.addWidget(self.adAmount)

        self.divCagr = QLineEdit(self.centralwidget)
        self.divCagr.setObjectName(u"divCagr")

        self.verticalLayout_2.addWidget(self.divCagr)

        self.estAp = QLineEdit(self.centralwidget)
        self.estAp.setObjectName(u"estAp")

        self.verticalLayout_2.addWidget(self.estAp)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(225, 32, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.goButton = QPushButton(self.centralwidget)
        self.goButton.setObjectName(u"goButton")
        self.goButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.goButton, 2, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.checkBox, 3, 0, 1, 1, Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 883, 34))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Investment Calculator", None))
        self.dailyRadioButton.setText(QCoreApplication.translate("MainWindow", u"Daily", None))
        self.monthlyRadioButton.setText(QCoreApplication.translate("MainWindow", u"Monthly", None))
        self.quarterlyRadioButton.setText(QCoreApplication.translate("MainWindow", u"Quarterly", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Investment Calculator", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Year Nine", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Year Eight", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Year Seven", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Year Five", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Year Two", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Year Six", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Year Ten", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Year Eleven", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Year Four", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Year Three", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Year One", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Initial Investment Amount: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Interest Rate (%)", None))
        self.l_additionLabel.setText(QCoreApplication.translate("MainWindow", u"Additional Contributions Per Month: ", None))
        self.l_cagrLabel.setText(QCoreApplication.translate("MainWindow", u"Dividend CAGR (%): ", None))
        self.l_apLabel.setText(QCoreApplication.translate("MainWindow", u"Estimated Unit Appreciation Per Year (%): ", None))
        self.inAmount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.intRate.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.adAmount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.divCagr.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.estAp.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.goButton.setText(QCoreApplication.translate("MainWindow", u"Go!", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Advanced", None))
    # retranslateUi

