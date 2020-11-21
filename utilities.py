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

    @staticmethod
    def list_files(startpath):
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))