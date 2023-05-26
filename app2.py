import sys 
from PyQt5.QtWidgets import *

class CalendarApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calendar App")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.calendar_widget = QCalendarWidget(self)
        self.calendar_widget.setGridVisible(True)  # Tampilkan tampilan grid pada kalender

        self.selected_date_label = QLabel(self)

        self.calendar_widget.clicked.connect(self.calendar_clicked)

        layout.addWidget(self.calendar_widget)
        layout.addWidget(self.selected_date_label)

    def calendar_clicked(self, date):
        self.selected_date_label.setText(f"Selected Date: {date.toString('yyyy-MM-dd')}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calendar_app = CalendarApp()
    calendar_app.show()
    sys.exit(app.exec())
