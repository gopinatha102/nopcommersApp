import logging


class LogGen():

    @staticmethod
    def loggen():

        logging.basicConfig(filename=r"C:\\Users\\PAVAN KUMARA\\PycharmProjects\\nopcommerceApp\\Logs\\text.log",
                           format='%(asctime)s: %(levelname)s: %(message)s',
                           datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.basicConfig(filename="./text.log")


        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

