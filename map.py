import folium
from folium.map import Tooltip
import os
import json
import func
import sys
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWidgets import QPushButton, QMessageBox
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog,QVBoxLayout
from PyQt5.uic import loadUi
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MainWindow(QDialog):
    def setupUi(self, Dialog):
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame_2)
        self.calendarWidget.setGeometry(QtCore.QRect(170, 190, 392, 236))
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame_2)
        self.calendarWidget.setGeometry(QtCore.QRect(170, 190, 392, 236))
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout.addWidget(self.frame_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("gui3.ui", self)
        self.choseBtn1.clicked.connect(self.browsefiles1)
        self.choseBtn2.clicked.connect(self.browsefiles2)
        self.choseBtn3.clicked.connect(self.browsefiles3)
        self.showMapBtn.clicked.connect(self.showmap)

        btn = QPushButton("button1")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.frame_2)
        self.webEngineView.setGeometry(QtCore.QRect(0, 0, 1450, 900))

    def browsefiles1(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', 'Images (*.png, *.xmp *.jpg)')
        global fileAddrss1
        fileAddrss1 = fname[0]
        self.line1.setText(fname[0])
        print(fileAddrss1)

    def browsefiles2(self):
        global fileAddrss2
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', 'Images (*.png, *.xmp *.jpg)')
        fileAddrss2 = fname[0]
        self.line2.setText(fname[0])
        print(fileAddrss2)

    def browsefiles3(self):
        global fileAddrss3
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', 'Images (*.png, *.xmp *.jpg)')
        fileAddrss3 = fname[0]
        self.line3.setText(fname[0])
        print(fileAddrss3)

    def showmap(self):
        print("maaap")
        if (fileAddrss1 == "") or (fileAddrss2 == "") or (fileAddrss3 == ""):
            QMessageBox.about(self, "Warning", "You have to select 3 images!")
        else:
            self.loadPage()

    def loadPage(self):

        with open('map.html', 'r') as f:
            html = f.read()
            self.webEngineView.setHtml(html)






def CreateMap(Photos_path_name_array):
    ## fog hadi ndiro win lazm user ymed les images w  7na njbdo les cites
    style2 = {"fillColor": "#228B22", "color": "#eedcdd"}
    # create map object
    locations = [func.image_coordinates(Photos_path_name_array[i]) for i in range(2,5)]

    Sphotos=[Photos_path_name_array[i] for i in range (1,5)]




    location = locations[0]
    # hna yakhdm map
    m = folium.Map(
        location=[location.latitude, location.longitude],
        tiles="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
        zoom_size=20,
        zoom_start = 10,
        attr="My Data Attribution",
    )


    f = open("Shape.json")



    data = json.loads(f.read())
    citiesCord = data["features"][0]["geometry"]["coordinates"][0]
    for i in range(0, len(locations)):
        if locations[i] != "" :
            data["features"][0]["geometry"]["coordinates"][0].append(
                [locations[i].longitude, locations[i].latitude]
            )
    i =1
    for cityCord in citiesCord:

        folium.GeoJson(data, style_function=lambda x: style2).add_to(m)

        folium.Marker(
            [cityCord[1], cityCord[0]],
            popup="<b>Name : </b> photo{} <br> <b> location </b> {} , {} <br> <img src={} height=200 width=290>".format(i,locations[i-1].longitude, locations[i-1].latitude,Sphotos[i-1]),
            icon=folium.Icon(color="red"),
        ).add_to(m)
        i+=1

        

    # Genereate map
   
    return m.save("map.html")

# w hna t7t ydir surface w yrsom tmnkii7 hadak w nchlh nkono kmlna

fileAddrss1=""
fileAddrss2=""
fileAddrss3=""

app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1500)
widget.setFixedHeight(900)
widget.show()
sys.exit(app.exec_())



