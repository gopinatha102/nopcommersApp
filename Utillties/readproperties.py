import configparser

config=configparser.RawConfigParser()
config.read(r".\\Configurations\\config1.ini")


class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseUrl')
        return url

    @staticmethod
    def getuseremail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password