class Config:
    """
    General configuration parent class
    """
    pass


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
