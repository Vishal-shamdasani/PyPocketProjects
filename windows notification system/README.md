# Drink Water Reminder

This Python script sends desktop notifications to remind you to drink water periodically. It uses the `win10toast` library to display notifications on Windows systems.

## Features
- Allows you to specify the number of reminders.
- Sends desktop notifications with a custom message.
- Includes a time interval between reminders.

## Prerequisites

- Python 3.x installed on your system.
- `win10toast` library installed.

## Installation

1. Clone or download the script to your local machine.
2. Install the required library by running:
   ```bash
   pip install win10toast
   ```

## Usage

1. Run the script using Python:
   ```bash
   python windows_notification_system/drinking_water_reminder.py
   ```
2. Enter the number of reminders when prompted.
3. The script will display notifications and count down until all reminders are completed.

## Code Explanation

```python
from win10toast import ToastNotifier
import time

# Ask user for the number of reminders
occrence = int(input("no. "))

# Create a ToastNotifier instance
toast = ToastNotifier()

# Loop to send notifications
while occrence > 0:
    toast.show_toast(title="reminder", msg="drink water", duration=5)  # Display notification
    occrence -= 1  # Decrease the counter
    print(occrence)  # Print remaining reminders
    time.sleep(10)  # Wait 10 seconds before the next reminder
```

## Customization

- **Message**: Change the `msg` parameter in `toast.show_toast` to customize the notification message.
- **Interval**: Modify the `time.sleep(10)` line to adjust the time (in seconds) between notifications.
- **Duration**: Adjust the `duration` parameter in `toast.show_toast` to control how long the notification stays on the screen.

## Example Output

- When you run the script and enter `3` as the input, you'll receive 3 notifications at 10-second intervals reminding you to drink water.

## Note

- This script is designed for Windows systems only, as `win10toast` is a Windows-specific library.

## License

This project is open-source and available under the MIT License. Feel free to modify and use it as needed!
