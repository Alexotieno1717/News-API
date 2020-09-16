class Config:
    """
    General configuration parent class
    """
    pass
    api_key = 'a493e30f11b147d0ba67b15ca60c5e4c'
    SECRET_KEY = '1234567890'


class ProdConfig(Config):
    """
    Production
    """
    pass


class DevConfig(Config):
    """
    development
    """

    DEBUG = True
