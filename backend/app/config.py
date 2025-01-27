import os
from dotenv import load_dotenv

# Load environment variables from a .env file if it exists
load_dotenv()

class Config:
    """Base configuration with default values for environment variables."""
    # General Configurations
    DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1', 't']
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
    ENV = os.getenv('FLASK_ENV', 'production')
    
    # Database Configurations
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///default.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False').lower() in ['true', '1', 't']

    # JWT Configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 3600))  # default 1 hour

    # Redis Configurations
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')

    # Other API Configurations
    EXTERNAL_API_KEY = os.getenv('EXTERNAL_API_KEY', 'your_external_api_key')

    # Celery Configuration
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')

    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'app.log')

class DevelopmentConfig(Config):
    """Development configuration, enabling debug mode and using a local database."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL', 'sqlite:///dev.db')
    LOG_LEVEL = 'DEBUG'

class TestingConfig(Config):
    """Testing configuration, optimized for test environments."""
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', 'sqlite:///test.db')
    LOG_LEVEL = 'DEBUG'

class ProductionConfig(Config):
    """Production configuration with optimizations for security and performance."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/prod_db')
    LOG_LEVEL = 'WARNING'

# Configuration map to choose the right config based on FLASK_ENV or other env settings
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': Config
}

# Choose the config based on the FLASK_ENV variable
def get_config():
    """
    Get the appropriate configuration class based on the FLASK_ENV environment variable.

    Returns:
        Config: The configuration class for the current environment.
    """
    env = os.getenv('FLASK_ENV', 'default').lower()
    return config.get(env, Config)

# Example usage of the configuration
if __name__ == "__main__":
    current_config = get_config()
    print(f"Using configuration: {current_config.__name__}")
    print(f"Debug mode: {current_config.DEBUG}")
    print(f"Database URI: {current_config.SQLALCHEMY_DATABASE_URI}")
    print(f"Celery Broker URL: {current_config.CELERY_BROKER_URL}")
    print(f"Log Level: {current_config.LOG_LEVEL}")
