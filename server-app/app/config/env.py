import os

def get_environment():
    """Returns the current environment (defaults to 'development' if not set)."""
    return os.getenv('ENVIRONMENT', 'development')

def get_base_url():
    """Returns the base URL based on the current environment."""
    environment = get_environment()

    if environment == 'production':
        return os.getenv('BASE_URL', 'https://dummyurl:3000')
    elif environment == 'develop':
        return os.getenv('BASE_URL', 'http://localhost:3001')
    else:
        return os.getenv('BASE_URL', 'http://localhost:3000')
