#Source: https://stackoverflow.com/questions/57447541/ask-about-this-error-type-error-cant-mix-string-and-bytes-in-path-components
class threading_one(QThread, QMessageBox):
    signal = pyqtSignal()
    count_pro = pyqtSignal(int)
    cha_name = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)

    def progress_count(self, total, recvd, ratio, rate, eta):
        read_data = recvd
        if total > 0:
            download_percentage = read_data * 100 / total
            self.count_pro.emit(download_percentage)
            if download_percentage >= 100:
                self.signal.emit()

    def run(self):

        video = pafy.new(self.url)
        stream = video.getbest(preftype='mp4')
        self.cha_name.emit(video.title)
        stream.download(filepath=self.save, callback=self.progress_count)
        self.signal.emit()


class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.Handel_Screen()
        self.Handel_Button()

    def Handel_Screen(self):
        self.setWindowTitle("Test Download Program")

    def Handel_Button(self):
        self.pushButton.clicked.connect(self.download_video)
        self.pushButton_2.clicked.connect(self.Browse_Location)

        self.down_single = threading_one()
        self.down_single.signal.connect(self.finish)
        self.down_single.count_pro.connect(self.chang_progressBar)
        self.down_single.cha_name.connect(self.change_name_video)

    def chang_progressBar(self, value):
        self.progressBar.setValue(value)

    def finish(self):
        QMessageBox.information(self, "Complete Download ...", "Your Download is Complete ...")
        self.lineEdit.clear()
        self.progressBar.setValue(0)
        self.pushButton.setEnabled(True)

    def Browse_Location(self):
        save_lacation = QFileDialog.getExistingDirectory(self, 'Select Location')
        self.label.setText(save_lacation)

    def change_name_video(self, title):
        self.label_2.setText(title)

    def download_video(self):
        self.down_single.url = self.lineEdit.text()
        self.down_single.save = self.label.text()

        if self.lineEdit.text() == "":
            QMessageBox.warning(self, " From System ! ", " Please put valid URL first  !! ")
            return
        self.pushButton.setEnabled(False)
        self.down_single.start()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()