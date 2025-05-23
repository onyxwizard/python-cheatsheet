# data_processing/cleaner/cleaner.py

def _remove_duplicates(data):
    """Internal function to remove duplicates."""
    print("Removing duplicates...")
    return list(set(data))

def clean_data(data):
    """Public function to clean data."""
    print("Cleaning data...")
    return _remove_duplicates(data)

__all__ = [clean_data]