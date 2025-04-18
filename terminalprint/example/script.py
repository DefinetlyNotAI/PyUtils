import os

from tprint import TPrint, TPrintColors, separator

log_file = "tprint_demo_log.txt"

# Ensure clean state
if os.path.exists(log_file):
    os.remove(log_file)

colors = {
    'info': TPrintColors.WHITE,
    'warning': TPrintColors.YELLOW,
    'error': TPrintColors.RED,
    'debug': TPrintColors.CYAN,
    'critical': TPrintColors.BRIGHT_RED,
    'success': TPrintColors.BRIGHT_GREEN,
    'input': TPrintColors.WHITE
}

tprint = TPrint(
    color_scheme=colors,
    debug_mode=True,
    log_file=log_file,
    use_timestamps=True,
    purge_old_logs=True
)

# Full style and message types
separator("1. Initial Setup with Custom Color Scheme and All Flags Enabled")
tprint.info("Informational message", log=True, style=TPrintColors.BOLD)
tprint.warning("Warning message", log=True, style=TPrintColors.UNDERLINE)
tprint.error("Error message", log=True, style=TPrintColors.REVERSED)
tprint.success("Success achieved!", log=True, style=f"{TPrintColors.BOLD}{TPrintColors.UNDERLINE}")
tprint.critical("System has crashed!", log=True, style=TPrintColors.BRIGHT_RED)
tprint.debug("Debugging trace enabled!", log=True, style=TPrintColors.BOLD)

separator("2. Input Handling")
name = tprint.input("Enter your name")
tprint.info(f"Nice to meet you, {name}!", style=TPrintColors.BRIGHT_GREEN)

separator("3. Toggling Timestamp and Debug Mode Off")
tprint.set_timestamp_usage(False)
tprint.set_debug_mode(False)

tprint.info("This message has NO timestamp", log=True)
tprint.debug("This debug message SHOULD NOT appear", log=True)

separator("4. Resetting Log File and Logging OFF")
tprint.set_log_file(None)
tprint.info("This message won't be logged", log=False)

separator("5. Changing Color Scheme Dynamically")
tprint.set_color_scheme({'info': TPrintColors.CYAN})
tprint.info("Color changed to cyan")

separator("6. Manual Log Purging Check")
# Should not purge old logs this time
tprint.set_log_file(log_file)
tprint.set_purge_old_logs(False)
tprint.info("This message should append to existing log", log=True)

separator("7. Edge Case: Unknown Color Key (Should Raise Error)")
try:
    tprint.set_color_scheme({'nonexistent_level': TPrintColors.RED})
except ValueError as e:
    tprint.error(f"Caught expected exception: {e}")

separator("8. Mixed Styles and Complex Chaining")
tprint.success("Styled success", style=f"{TPrintColors.UNDERLINE}{TPrintColors.BRIGHT_GREEN}")
tprint.critical("Styled critical", style=f"{TPrintColors.REVERSED}{TPrintColors.BRIGHT_RED}")

separator("9. Final Debug Enable")
tprint.set_debug_mode(True)
tprint.debug("Debugging is back!")

separator("10. Log File Contents")
with open(log_file, 'r') as f:
    print(f"{TPrintColors.BRIGHT_BLACK}--- Log File Output ---\n{f.read()}{TPrintColors._RESET}")
