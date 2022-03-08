#import logging


#class LogGen():
   # @staticmethod
   # def loggen():


 #      logging.basicConfig(filename=r"C:\\Users\\PAVAN KUMARA\\PycharmProjects\\nopcommerceApp\Logs\\text.log"

#     logger=logging.getLogger()
#      logger.setLevel(logging.INFO)
#       return logger

import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\Logs\\automation1.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger

