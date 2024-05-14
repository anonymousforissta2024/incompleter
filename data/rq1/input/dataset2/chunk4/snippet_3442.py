#Source: https://stackoverflow.com/questions/76945050/qml-and-pyside6-typeerror-cannot-read-property-x-of-null
from pathlib import Path

from PySide6.QtCore import QObject, QStringListModel
from PySide6.QtQml import QQmlApplicationEngine

from date_range_dialog import DateRangeDialog


class DialogManager(QObject):
    _engine: QQmlApplicationEngine

    def __init__(self):
        QObject.__init__(self)
        self._engine = QQmlApplicationEngine()

    def loadDialog(
            self,
            name: str,
            width: float,
            height: float,
            startDates: list[str],
            endDates: list[str]
    ):
        dialog = DateRangeDialog()
        dialog.width = width
        dialog.height = height
        dialog.startDateModel = QStringListModel(startDates)
        dialog.endDateModel = QStringListModel(endDates)

        self._setRootContext(dialog)
        self._loadQmlFile(name)

        root = self._getQQmlEngineRoot()
        try: 
            root.outputDateRange.connect(dialog.outputDateRange)
        except AttributeError as e:
            print(e)

    def _setRootContext(self, dialog: DateRangeDialog):
        self._engine.rootContext().setContextProperty("dialog", dialog)

    def _loadQmlFile(self, qmlName: str) -> None:
        qmlFile = Path(__file__).parent / f"{qmlName}.qml"
        self._engine.load(qmlFile)

    def _getQQmlEngineRoot(self) -> QObject:
        if not self._engine.rootObjects():
            raise AttributeError("Root objects for QQmlApplicationEngine not found")

        root = QObject()
        for rootObject in self._engine.rootObjects():
            if rootObject.inherits("QWindow"): 
                root = rootObject
                break

        return root
       