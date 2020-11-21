import os
from time import sleep
from tqdm import tqdm

class Util:

    @staticmethod
    def createEmptyFile(path):
        with open(path, 'a') as file:
            os.utime(path, None)
        return file

    @staticmethod
    def showProgressBar(time, step):
        for i in tqdm(range(step)):
            sleep(time)