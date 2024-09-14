import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QPushButton, QMessageBox
from persiantools.jdatetime import JalaliDate
from PyQt5 import QtGui, QtCore

class CalendarApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Persian Calendar")
        self.setFixedSize(750, 750)
        self.currentYear = None
        self.currentMonth = None
        self.currentDay = None

        self.month_names = {
            1: "فروردین",
            2: "اردیبهشت",
            3: "خرداد",
            4: "تیر",
            5: "مرداد",
            6: "شهریور",
            7: "مهر",
            8: "آبان",
            9: "آذر",
            10: "دی",
            11: "بهمن",
            12: "اسفند",
        }

        self.events = {}  # Dictionary to store events

        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        frame = QWidget()
        frame.setStyleSheet("background-color: #c2f0c2; border-radius: 15px;")

        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)

        self.prevMonthButton = QPushButton('ماه قبل')
        self.prevMonthButton.setStyleSheet("border: none; padding: 10px;")
        button_layout.addWidget(self.prevMonthButton)

        self.monthYearLabel = QLabel()
        self.monthYearLabel.setStyleSheet("""
            background-color: #008000;
            border-radius: 10px;
            padding: 10px 20px;
            font-family: "Arial";
            font-size: 16px;
            color: white;
        """)
        self.monthYearLabel.setAlignment(QtCore.Qt.AlignCenter)
        button_layout.addWidget(self.monthYearLabel)

        self.nextMonthButton = QPushButton('ماه بعد')
        self.nextMonthButton.setStyleSheet("border: none; padding: 10px;")
        button_layout.addWidget(self.nextMonthButton)

        frame.setLayout(button_layout)
        main_layout.addWidget(frame)

        self.prevMonthButton.clicked.connect(self.showPreviousMonth)
        self.nextMonthButton.clicked.connect(self.showNextMonth)

        self.tableWidget = QTableWidget()
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['شنبه', 'یک‌شنبه', 'دوشنبه', 'سه‌شنبه', 'چهارشنبه', 'پنج‌شنبه', 'جمعه'])
        self.tableWidget.verticalHeader().setVisible(False)

        cell_size = 100
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHeight(i, cell_size)
            for j in range(self.tableWidget.columnCount()):
                self.tableWidget.setColumnWidth(j, cell_size)
                cell_label = QLabel()
                cell_label.setAlignment(QtCore.Qt.AlignCenter)
                cell_label.setStyleSheet("border: 1px solid black; border-radius: 50%;")
                self.tableWidget.setCellWidget(i, j, cell_label)

        main_layout.addWidget(self.tableWidget)
        self.updateCalendar()

        self.setLayout(main_layout)
        self.tableWidget.itemClicked.connect(self.get_selected_date)

    def updateCalendar(self):
        if self.currentYear is None or self.currentMonth is None:
            today = JalaliDate.today()
            self.currentYear = today.year
            self.currentMonth = today.month
            self.currentDay = today.day

        first_day_of_month = JalaliDate(self.currentYear, self.currentMonth, 1)
        day_of_week_of_first_day = first_day_of_month.weekday()
        days_in_month = first_day_of_month.days_in_month(year=self.currentYear, month=self.currentMonth)

        self.tableWidget.clearContents()

        persian_month = self.month_names[self.currentMonth]
        self.monthYearLabel.setText(f'{persian_month} {first_day_of_month.year}')

        row = 0
        col = day_of_week_of_first_day

        for d in range(1, days_in_month + 1):
            item = QTableWidgetItem(str(d))
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(row, col, item)

            if d == self.currentDay:
                item.setBackground(QtGui.QColor(200, 200, 255))
                item.setForeground(QtGui.QColor("blue"))

            col += 1
            if col == 7:
                col = 0
                row += 1

    def showPreviousMonth(self):
        self.currentMonth -= 1
        if self.currentMonth == 0:
            self.currentMonth = 12
            self.currentYear -= 1
        self.updateCalendar()

    def showNextMonth(self):
        self.currentMonth += 1
        if self.currentMonth == 13:
            self.currentMonth = 1
            self.currentYear += 1
        self.updateCalendar()

    def get_selected_date(self, item):
        selected_day = int(item.text())
        selected_date = JalaliDate(self.currentYear, self.currentMonth, selected_day)
        QMessageBox.information(self, "Selected Date", f"Selected Date: {selected_date.strftime('%Y-%m-%d')}")

    # Additional methods for functionality
    def get_today_date(self):
        return JalaliDate.today()

    def set_date(self, year, month, day):
        if 1 <= month <= 12 and 1 <= day <= JalaliDate(year, month, 1).days_in_month(year, month):
            self.currentYear = year
            self.currentMonth = month
            self.currentDay = day
            self.updateCalendar()
        else:
            QMessageBox.warning(self, "Invalid Date", "The provided date is invalid.")

    def get_selected_date_info(self):
        if self.currentYear and self.currentMonth and self.currentDay:
            return JalaliDate(self.currentYear, self.currentMonth, self.currentDay)
        else:
            QMessageBox.warning(self, "No Date Selected", "No date has been selected.")
            return None

    def add_event(self, date, event_description):
        """Add an event to the dictionary."""
        if date in self.events:
            self.events[date].append(event_description)
        else:
            self.events[date] = [event_description]
        QMessageBox.information(self, "Event Added", f"Event added on {date}: {event_description}")

    def remove_event(self, date, event_description):
        """Remove an event from the dictionary."""
        if date in self.events:
            if event_description in self.events[date]:
                self.events[date].remove(event_description)
                if not self.events[date]:
                    del self.events[date]
                QMessageBox.information(self, "Event Removed", f"Event removed from {date}: {event_description}")
            else:
                QMessageBox.warning(self, "Event Not Found", f"No such event found on {date}.")
        else:
            QMessageBox.warning(self, "Date Not Found", f"No events found for {date}.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalendarApp()
    ex.show()
    sys.exit(app.exec_())
