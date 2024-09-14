# Persian Calendar

Welcome to the Persian Calendar project! This application provides a user-friendly interface to display and interact with a Persian calendar, leveraging PyQt5 for a graphical user interface.

## Features

- **Persian Date Display:** Shows the current Persian month and year with navigation capabilities.
- **Monthly Navigation:** Navigate through previous and next months using the provided buttons.
- **Date Selection:** Click on a date to view and manage appointments.
- **Appointment Management:** Add and view appointments for selected dates.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- PyQt5
- `persiantools` library

You can install the required libraries using pip:

```bash
pip install PyQt5 persiantools
```



## Getting Started

1. **Clone the Repository:**
    

```bash
    git clone https://github.com/Morteza-Abbaszadeh/PyVault.git
```


    
2. **Navigate to the Project Folder:**
  
```bash
cd PyVault/PersianCalendar
```

3.  **Usage**

To use the `CalendarApp` class, you need to import it into your Python script. The class provides functionalities to interact with the Persian calendar, including getting today's date, setting a specific date, and managing events.

Example

```python 
import sys
from PyQt5.QtWidgets import QApplication
from your_module import CalendarApp  # فرض بر این است که کلاس CalendarApp در فایل `your_module.py` قرار دارد

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calendar = CalendarApp()
    calendar.show()
    
    # دریافت تاریخ امروز
    today_date = calendar.get_today_date()
    print(f"Today: {today_date.strftime('%Y-%m-%d')}")
    
    # تنظیم تاریخ خاص
    calendar.set_date(1403, 6, 15)
    print(f"Date set to: {calendar.get_selected_date_info().strftime('%Y-%m-%d')}")
    
    # افزودن رویداد
    calendar.add_event('1403-06-15', 'Meeting with team')
    
    # حذف رویداد
    calendar.remove_event('1403-06-15', event_id=1)

    sys.exit(app.exec_())

```



## How It Works

- **Main Window:** The main window displays the current month and year, with buttons to navigate to the previous and next months.
- **Calendar Display:** The calendar is displayed in a grid format with Persian month names. Each cell represents a day of the month.
- **Date Selection:** Clicking on a date will open a dialog window where you can manage appointments for that date.
- **Appointment Management:** In the dialog window, you can add appointments by specifying the time, description, and national ID. Appointments are saved and displayed in the same dialog.

## Code Overview

- **`persian_calendar.py`:** Contains the main application code, including the `CalendarApp` class for the calendar interface and the `DatePageWindow` class for managing appointments.
- **`styles.py`:** Includes styling information for the buttons used in the application.













## Contributing

If you have suggestions for improvements or new features, feel free to submit an issue or a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License. For more details, please see the LICENSE file.

## Contact

For any questions or inquiries, you can reach out to me at [morteza.at1996@gmail.com].

Thank you for using the Persian Calendar application!





