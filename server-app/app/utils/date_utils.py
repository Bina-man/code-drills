from datetime import datetime, timedelta
import pytz

def extract_report_date(report_date_str: str) -> dict:
    """
    Extracts and processes the report date from a string.
    
    Args:
    - report_date_str (str): The report date string, e.g., "As at 26 August 2024".
    
    Returns:
    - dict: A dictionary containing the original date string and the processed datetime object.
    """
    try:
        # Extract the date portion from the string
        date_str = report_date_str.replace("As at ", "")
        # Parse the date string into a datetime object
        report_date = datetime.strptime(date_str, "%d %B %Y")
        
        return {
            "report_date_extracted": report_date,  # Processed datetime object
            "report_date_original": report_date_str  # Original string
        }
    except ValueError as e:
        return {"error": f"Date parsing error: {str(e)}"}

def format_date(date: datetime, format_str: str = "%d %B %Y") -> str:
    """
    Formats a datetime object into a string.
    
    Args:
    - date (datetime): The datetime object to format.
    - format_str (str): The format string (default is "%d %B %Y").
    
    Returns:
    - str: The formatted date string.
    """
    return date.strftime(format_str)

def calculate_date_difference(date1: datetime, date2: datetime) -> int:
    """
    Calculates the difference in days between two dates.
    
    Args:
    - date1 (datetime): The first date.
    - date2 (datetime): The second date.
    
    Returns:
    - int: The difference in days between the two dates.
    """
    return (date2 - date1).days

def add_days_to_date(date: datetime, days: int) -> datetime:
    """
    Adds a number of days to a date.
    
    Args:
    - date (datetime): The original date.
    - days (int): The number of days to add.
    
    Returns:
    - datetime: The new date after adding the days.
    """
    return date + timedelta(days=days)

def validate_date_string(date_str: str, format_str: str = "%d %B %Y") -> bool:
    """
    Validates whether a string is a valid date according to the specified format.
    
    Args:
    - date_str (str): The date string to validate.
    - format_str (str): The format string to validate against (default is "%d %B %Y").
    
    Returns:
    - bool: True if valid, False otherwise.
    """
    try:
        datetime.strptime(date_str, format_str)
        return True
    except ValueError:
        return False

def convert_timezone(date: datetime, from_tz: str, to_tz: str) -> datetime:
    """
    Converts a datetime object from one time zone to another.
    
    Args:
    - date (datetime): The original datetime object.
    - from_tz (str): The time zone of the original date.
    - to_tz (str): The target time zone.
    
    Returns:
    - datetime: The datetime object in the target time zone.
    """
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)

    # Localize the date to the original time zone
    localized_date = from_zone.localize(date)
    
    # Convert to the target time zone
    return localized_date.astimezone(to_zone)

def is_weekend(date: datetime) -> bool:
    """
    Checks if a given date falls on a weekend.
    
    Args:
    - date (datetime): The date to check.
    
    Returns:
    - bool: True if the date is a Saturday or Sunday, False otherwise.
    """
    return date.weekday() >= 5

def get_current_datetime_in_timezone(timezone: str) -> datetime:
    """
    Gets the current datetime in a specific time zone.
    
    Args:
    - timezone (str): The time zone to get the current datetime in.
    
    Returns:
    - datetime: The current datetime in the specified time zone.
    """
    tz = pytz.timezone(timezone)
    return datetime.now(tz)
