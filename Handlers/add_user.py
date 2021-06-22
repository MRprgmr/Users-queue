from PyQt5.QtWidgets import QDialog, QMessageBox

from Resources import Designs as ds
from models import User


class add_dialog(QDialog, ds.add_user.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.buttons_events()

    def buttons_events(self):
        self.ok.pressed.connect(self.save)
        self.cancel.pressed.connect(self.close)

    def save(self):
        if self.name_edit.text() == "" or len(self.phone_edit.text()) != 16 or self.age_edit.value() == 0:
            return None
        else:
            try:
                User.create(Name=self.name_edit.text(), PhoneNumber=self.phone_edit.text().replace('-', ''),
                            Course=self.course_name.currentText(),
                            Age=self.age_edit.value())
                self.accept()
            except Exception as er:
                QMessageBox.about(self, "Unable to add user", str(er))

    def exec_(self):
        self.name_edit.clear()
        self.phone_edit.clear()
        self.age_edit.setValue(0)
        super(add_dialog, self).exec_()
