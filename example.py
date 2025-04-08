from exception.handler import Handler
from exception.colors import Colors, Format

# ALL BOOLEAN SETTINGS ARE FALSE BY DEFAULT,
# THE DEFAULT PRINT FUNCTION IS 'print()',
# THE DEFAULT COLOR IS WHITE, DEFAULT FORMAT IS NORMAL.

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


# Example function to demonstrate exception handling
def divide_numbers(a, b):
    try:
        return a / b
    except Exception as e:
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


# Trigger an exception
divide_numbers(10, 0)
print("Hello")  # This line will not be executed if exit_script is True
