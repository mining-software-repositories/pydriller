import datetime
from check_commits import CheckCommits
import numpy as np
from os import path
import matplotlib.pyplot as plt
from utilities import Util
from threading import Thread
import json

def processing(repository, name):
    try:
        # Class that represents a repository analysis
        analysis = CheckCommits(repository, name)

        print("SysRepo Analysis - v: 1.0.0", datetime.datetime.now())
        print("Repository: ", repository)

        before1 = datetime.datetime.now()
        print("Started on: ", before1)
        print("Please wait...")

        frequencyOfEachFile = None

        try: 
            print("Processing the frequency of each file in commits...")
            frequencyOfEachFile = analysis.counterWithFrequencyOfFile()
            print(frequencyOfEachFile)
        except:
            print("Error in analysis.counterWithFrequencyOfFile()")

        try: 
            # Save frequencyOfEachFile in a json file
            singleName = name + ".json"
            path = "json/"
            name = path + name + ".json"
            with open(name, 'w', encoding="utf-8") as jsonFile:
                json.dump(frequencyOfEachFile, jsonFile)
            print("The file {} was saved with success!".format( singleName ))
        except: 
            print( "Error when try to save the json file")

        print( "Processing word cloud...")
        T1 = Thread(target=analysis.generateWordCloud(), args=())
        T2 = Thread(target=Util.showProgressBar(1, 10), args=())
        T1.start()
        T2.start()
        T2.join()
        T1.join()

        after =  datetime.datetime.now()
        print("The wordcloud was generated with success!")
        print("Finished on: ", after)
    except:
        print("Something wrong!")
    finally:
        print("Finished processing!")

repository = "https://github.com/topicos-sistemas-distribuidos/systagram.git"
name = "systagram"

processing(repository, name)