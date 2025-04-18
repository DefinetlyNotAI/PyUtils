# TPrint - A Python Logging and Printing Library

## Overview

`TPrint` is a Python library that provides enhanced console printing with customizable colors, text styles, and logging features. It allows you to print messages to the console in different log levels (info, warning, error, debug, etc.), style them with ANSI color codes, and optionally log them to a file. It also supports timestamped logging and dynamic color scheme updates.

## Features

- Customizable color scheme for different log levels.
- Support for printing and logging messages with various levels: **info**, **warning**, **error**, **debug**, **critical**, and **success**.
- Optionally log messages to a file with timestamps.
- Support for input prompts with colored text.
- Adjustable debug mode for conditional logging.
- Support for text styles: bold, underline, and reversed.
- Easy-to-use API with dynamic configuration changes.

## Installation

This library does require installation of dependencies. You can install it using `pip`.

```bash
pip install -r requirements.txt
```

## Usage

You can check specific usages below, but I advise check the [example script](example/script.py) provided in the `examples` folder.

### Importing the Classes

```python
from tprint import TPrint, TPrintColors
```

### Basic Usage

```python
from tprint import TPrint, TPrintColors

# Initialize TPrint
tprint = TPrint(debug_mode=True, use_timestamps=True, log_file="app.log")

# Print messages with various log levels
tprint.info("This is an info message.")
tprint.warning("This is a warning message.", log=True)
tprint.error("This is an error message.", style=TPrintColors.BOLD)
tprint.debug("This is a debug message.")  # Only prints in debug mode
tprint.success("This is a success message.")
tprint.critical("This is a critical message.")

# Get user input with colored prompt
user_input = tprint.input("Please enter a value")
```

### Customizing the Color Scheme

You can customize the color scheme by passing a dictionary to the `TPrint` constructor or by updating it dynamically.

```python
from tprint import TPrint, TPrintColors

custom_colors = {
    'info': TPrintColors.CYAN,
    'warning': TPrintColors.BRIGHT_YELLOW,
    'error': TPrintColors.BRIGHT_RED,
}

tprint = TPrint(
    color_scheme=custom_colors,
)

tprint.set_color_scheme(custom_colors)
tprint.info("This message uses the custom info color.")
```

### Dynamic Settings

You can dynamically update the following settings:

- **Color Scheme**: `set_color_scheme(color_scheme)`
- **Debug Mode**: `set_debug_mode(debug_mode)`
- **Timestamp Usage**: `set_timestamp_usage(use_timestamps)`
- **Log File**: `set_log_file(log_file)`
- **Purge Old Logs**: `set_purge_old_logs(purge_old_logs)`

```python
from tprint import TPrint

tprint = TPrint()

tprint.set_debug_mode(False)  # Disable debug mode
tprint.set_timestamp_usage(False)  # Disable timestamp in logs
```

### Separator Function

You can print a styled separator with a title using the `separator` function:

```python
from tprint import separator

separator("Section Title")
```

### Example Output

```bash
[*][2025-04-07 12:30:15] This is an info message.
[!][2025-04-07 12:30:16] This is a warning message.
[x][2025-04-07 12:30:17] This is an error message.
[-][2025-04-07 12:30:18] This is a debug message.
[✓][2025-04-07 12:30:19] This is a success message.
[x][2025-04-07 12:30:20] This is a critical message.
```

### Logging

Messages can be logged to a file by enabling the `log_file` parameter when initializing `TPrint`. A timestamp will automatically be added to each log entry:

```python
from tprint import TPrint

tprint = TPrint(log_file="log.txt")
tprint.info("This message will be logged to a file.")
```

## Configuration Options

- **`color_scheme`**: A dictionary that allows you to specify custom colors for log levels. Default values are provided.
- **`debug_mode`**: Boolean flag to enable or disable debug mode.
- **`log_file`**: Path to the log file where messages will be logged (or `None` to disable logging).
- **`use_timestamps`**: Boolean flag to enable or disable timestamps in logs.
- **`purge_old_logs`**: Boolean flag to enable or disable old log purging.

## Example

```python
from tprint import TPrint

# Initialize with default settings
tprint = TPrint(debug_mode=True, use_timestamps=True, log_file="application.log")

# Print different types of messages
tprint.info("Information message")
tprint.warning("Warning message", log=True)
tprint.error("Error message")
tprint.success("Success message")
tprint.debug("Debug message")  # This will only print if debug_mode is True
tprint.critical("Critical message")

# Input prompt
name = tprint.input("What is your name?")
tprint.success(f"Hello, {name}!")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Notes

- This library uses ANSI escape sequences to color the output text in the terminal.
- Special thanks to the Python community for making such powerful and flexible libraries.
