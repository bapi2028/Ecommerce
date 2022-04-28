import inspect
import logging

class LogGen:
    @staticmethod
    # def loggen():
    #     logging.basicConfig(filename=".\\Logs\\automation.log",
    #                         format='%(asctime)s - %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    #     logger = logging.getLogger()
    #     logger.setLevel(logging.INFO)
    #     return logger

    def loggen(logLevel=logging.DEBUG):
        Logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(Logger_name)
        logger.setLevel(logLevel)
        fh = logging.FileHandler("automationNew.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s : %(message)s",
                                          datefmt="%d/%m/%Y %I:%M:%S %p ")
        fh.setFormatter(formatter)
        logger.addHandler(fh)