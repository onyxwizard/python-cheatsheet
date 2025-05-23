# data_processing/utils/utils.py

def _log_data(message):
    """Private function to log messages internally."""
    print(f"[INTERNAL] {message}")

def process_data(data):
    """Public function to process data."""
    _log_data("Processing started")
    return [x * 2 for x in data]

def validate_input(data):
    """Public function to validate input."""
    if not isinstance(data, list):
        raise ValueError("Input must be a list.")
    return True

__all__ = ['process_data', 'validate_input']