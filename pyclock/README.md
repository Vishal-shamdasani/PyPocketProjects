# Tkinter Clock Application

This is a simple digital clock application built using Python's `Tkinter` library. It displays the current time in **HH:MM:SS AM/PM** format and updates every second.

## Features

- Displays the current time with a sleek, digital-style font.
- Uses a **black background** with a **lime green foreground** for a visually appealing design.
- Automatically updates the displayed time every second.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.x

## Installation

1. Clone or download this repository.
2. Make sure Python is installed on your system.
3. Open a terminal or command prompt and navigate to the directory where the script is located.

## How to Run

Run the following command to start the clock:

```bash
python clock.py
```

## Code Overview

### Libraries Used

- **Tkinter**: Used to create the graphical user interface.
- **time.strftime**: Retrieves the current time in the desired format.

### Main Components

- **Root Window**: The main application window.
- **Label**: Displays the time with a customizable font and color.
- **`time()` Function**: Updates the time on the clock every second using the `after()` method.

### Customization

You can customize the application by changing the following:

- Font style and size in `Label()`.
- Background and foreground colors in `Label()`.
- Time format in the `strftime()` function (e.g., change to 24-hour format).

## Example Screenshot

*Screenshot not included. Run the program to see the clock in action!*

---

Enjoy your digital clock application! 😊
