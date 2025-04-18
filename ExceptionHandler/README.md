# Exception Handler

A Python-based exception handling utility that provides customizable exception messages,
formatting, and behavior. 

This project allows developers to handle exceptions with enhanced readability and flexibility.
It is designed to be easy to use and integrate into existing projects, 
providing a consistent way to manage exceptions across your codebase.

## Features

- **Customizable Exception Handling**: Configure global and local exception handling settings.
- **Traceback and Line Number**: Optionally include traceback and line numbers in exception messages.
- **Timestamp Support**: Add timestamps to exception messages with customizable formats.
- **Color and Format Customization**: Customize colors and text formats for exception messages, tracebacks, and timestamps.
- **Global and Local Settings**: Override global settings with local configurations for specific exceptions.
- **Script Exit Control**: Control whether the script exits after handling an exception.
- **Return or Print Messages**: Choose to return exception messages as strings or print them directly.

## Installation

Clone the repository and ensure you have Python installed.
Recommended to use Python 3.11 or higher.

```bash
git clone https://github.com/DefinetlyNotAI/ExceptionHandler.git
cd ExceptionHandler
```

## Usage

### Initialize the Handler

```python
from exception import Handler, Colors, Format

# Initialize the Handler with custom settings - These are global settings
# NOTE: return_string_rather_than_print has priority over exit_script both locally and globally!
handler = Handler(
    show_line=True,  # Show the line number where the exception occurred
    trace=True,  # Include the traceback in the output
    use_timestamp=True,  # Add a timestamp to the exception message
    exit_script=True,  # Exit the script after handling the exception
    return_string_rather_than_print=True
    # Return the message instead of printing it,
    # if True it will override/ignore exit_script
)

# Customize the formatter
# NOTE: Specific settings always the defaults,
#       example if message_color is set it will override the main_color for the message part,
handler.formatter(
    main_color=Colors.RED,  # Set the main color to red
    message_color=Colors.YELLOW,  # Set the message color to yellow
    trace_color=Colors.CYAN,  # Set the traceback color to cyan
    timestamps_color=Colors.GREEN,  # Set the timestamp color to green
    main_format=Format.BOLD,  # Set the main format to bold
    message_format=Format.UNDERLINE,  # Underline the message text
    trace_format=Format.DIM,  # Dim the traceback text
    timestamps_format=Format.BLINK,  # Blink the timestamp text
    datetime_format="%d-%m-%Y %H:%M:%S"  # Customize the datetime format
)
```

### Example Function

```python
# Bare Minimum
from exception import Handler

handler = Handler()  # Use default settings

def divide_numbers(a, b):
    try:
        return a / b
    except Exception as e:
        # Note: You can just use handler.exception() or handler.exception(msg=e) to rely on global settings
        handler.exception(
            # These are local settings, if they are different from the global, they take priority
            # so they will override the global settings only for this case.
            msg=e,  # Detailed exception message, can be a custom string
            exit_script=True,  # Exit the script after handling the exception
            quit_code=1,  # Exit code to use when exiting the script, defaults to 1
            return_string_rather_than_print=False  # Return the message instead of printing it
            # NOTE: If return_string_rather_than_print is set to True globally,
            #       and you want to locally quit for this singular case,
            #       then you HAVE TO explicitly set it to False here.
        )

divide_numbers(10, 0)
```

## Customization

- **Global Settings**: Set during `Handler` initialization.
- **Local Settings**: Override global settings in the `exception` method.
- **Formatter**: Customize colors and formats using the `formatter` method.

Check the [`example.py`](example.py) file for a proper example.

### Override priority

- Local settings take precedence over global settings.
  - If both global and local settings are provided, the local settings will override the global ones.
  - To use the global settings, simply call `handler.exception()`/`handler.exception(msg=e)`.
    - Any settings you want to override for this specific use case can be passed as arguments.
- `return_string_rather_than_print` has priority over `exit_script` both locally and globally.
  - If `return_string_rather_than_print` is set to `True` globally, and you want to locally quit for this singular case, then you HAVE TO explicitly set it to `False` in the local settings.

### Modify Colors, Format or Messages

If you want to modify the DataType for format's or colors ANSI, you can do so by modifying the `Format` and `Colors` classes in the [`exception.py`](colors.py) file.

If you want to add/remove Messages from the dictionary, you can do so by modifying the `Messages` class in the [`messages.py`](messages.py) file.

## Dependencies

- Datetime

## License

This project is licensed under the MIT License. See the [`LICENSE`](../LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
