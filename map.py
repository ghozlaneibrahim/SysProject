import folium
from folium.map import Tooltip
import os
import json
import func
import sys
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWidgets import QPushButton, QMessageBox
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QVBoxLayout
from PyQt5.uic import loadUi
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MainWindow(QDialog):
    global filePathArray
    global noCordination
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
        loadUi('gui3.ui', self)
        self.choseBtn1.clicked.connect(self.browsefiles1)
        self.choseBtn2.clicked.connect(self.browsefiles2)
        self.choseBtn3.clicked.connect(self.browsefiles3)
        self.showMapBtn.clicked.connect(self.showmap)

        btn = QPushButton("button1")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.frame_2)
        self.webEngineView.setGeometry(QtCore.QRect(0, 0, 1450, 900))
        self.loadFirstPage()

    def browsefiles1(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', 'Images (*.png, *.xmp *.jpg)')
        global fileAddrss1
        fileAddrss1 = fname[0]
        self.line1.setText(fname[0])
        print(fileAddrss1)
        filePathArray[0] = fileAddrss1

    def browsefiles2(self):
        global fileAddrss2
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', 'Images (*.png, *.xmp *.jpg)')
        fileAddrss2 = fname[0]
        self.line2.setText(fname[0])
        print(fileAddrss2)
        filePathArray[1] = fileAddrss2

    def browsefiles3(self):
        global fileAddrss3
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', 'Images (*.png, *.xmp *.jpg)')
        fileAddrss3 = fname[0]
        self.line3.setText(fname[0])
        print(fileAddrss3)
        filePathArray[2] = fileAddrss3

    def showmap(self):
        print("maaap")
        if '' in filePathArray:
            QMessageBox.about(self, "Warning", "You have to select 3 images!")
        else:
            CreateMap(filePathArray)


            if(noCordination!=(-1)):
                print(noCordination)
                if (noCordination==0):
                    QMessageBox.about(self, "Warning", "the image 1 does not have location coordinates!")

                elif(noCordination==1):
                    QMessageBox.about(self, "Warning", "the image 2 does not have location coordinates!")

                elif(noCordination==2):
                    QMessageBox.about(self, "Warning", "the image 3 does not have location coordinates!")




            self.loadPage()


    def loadFirstPage(self):
        with open(r'C:\Users\alouane\PycharmProjects\SysProject\map1.html', 'r') as f:
            html = f.read()
            self.webEngineView.setHtml(html)

    def loadPage(self):

        with open(r'C:\Users\alouane\PycharmProjects\SysProject\map.html', 'r') as f:
            html = f.read()
            self.webEngineView.setHtml(html)


def CreateMap(Photos_path_name_array):
    global noCordination
    noCordination = -1
    style2 = {"fillColor": "#228B22", "color": "#eedcdd"}
    # create map object
    locations = [func.image_coordinates(Photos_path_name_array[i]) for i in range(3)]



    nb=0
    new_locations = []
    images_index_without_exif = []
    for i in locations:
        new_locations.append(i)
        nb=+1
        if int(i.longitude) == 0 and int(i.latitude) == 0:
            images_index_without_exif.append(locations.index(i))
            new_locations.remove(i)
            noCordination=locations.index(i)

    locations = new_locations

    for i in images_index_without_exif:
        print('Image {} does not have Location coordinates'.format(i + 1))

    Sphotos = [Photos_path_name_array[i] for i in range(3)]

    location = func.Location()
    location.latitude, location.longitude = 36.731141399722226, 3.183093799722222
    # hna yakhdm map
    m = folium.Map(
        location=[location.latitude, location.longitude],
        tiles="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
        zoom_size=20,
        zoom_start=6,
        max_zoom=11,
        min_zoom=6,
        attr="My Data Attribution",
    )
    if locations:
        f = open(r'C:\Users\alouane\PycharmProjects\SysProject\Shape.json')

        data = json.loads(f.read())
        citiesCord = data["features"][0]["geometry"]["coordinates"][0]
        for i in range(0, len(locations)):
            if locations[i] != "":
                data["features"][0]["geometry"]["coordinates"][0].append(
                    [locations[i].longitude, locations[i].latitude]
                )
        i = 1
        for cityCord in citiesCord:
            folium.GeoJson(data, style_function=lambda x: style2).add_to(m)

            folium.Marker(
                [cityCord[1], cityCord[0]],
                popup="<b>Name : </b> photo{} <br> <b> location </b> {} , {} <br> <img src={} height=200 width=290>".format(
                    i, locations[i - 1].longitude, locations[i - 1].latitude, Sphotos[i - 1]),
                icon=folium.Icon(color="red"),
            ).add_to(m)
            i += 1

    # Generate map

    return m.save(r'C:\Users\alouane\PycharmProjects\SysProject\map.html')



noCordination=-1
fileAddrss1 = ""
fileAddrss2 = ""
fileAddrss3 = ""
# CreateEmptyMap()
filePathArray = ['', '', '']
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1500)
widget.setFixedHeight(900)
widget.show()
sys.exit(app.exec_())
