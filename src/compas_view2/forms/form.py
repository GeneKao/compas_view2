from PySide2 import QtWidgets
from PySide2 import QtGui


class Form(QtWidgets.QDialog):

    def __init__(self, title):
        super().__init__(f=QtGui.Qt.WindowTitleHint | QtGui.Qt.WindowSystemMenuHint)
        self.setWindowTitle('Add Sphere')
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        # inputs
        inputs = self.inputs()
        # buttons
        buttons = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addLayout(inputs)
        layout.addWidget(buttons)

    def inputs(self):
        raise NotImplementedError 

    # def accept(self):
    #     return super().accept()

    # def reject(self):
    #     return super().reject()