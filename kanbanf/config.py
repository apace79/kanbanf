# config.py


class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    SCHEMA = 'schema.sql'


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True
    DATABASE = 'instance/dev.db'


class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    DATABASE = 'instance/test.db'


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DATABASE = 'instance/prod.db'


def add_config(app, instance):
    configs = {'dev': DevelopmentConfig,
               'test': TestingConfig,
               'prod': ProductionConfig
               }

    app.config.from_object(configs[instance])
