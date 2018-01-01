
# ==============================================================================
# Copyright 2015 The Paragon Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

#=====================================================================================================

__main__ = '''
        The Paragon framework made in python. c++, prolog, fortran, and C.

        External Libraries are not mine, cubecorps, or owned representivavely of any individual
        associated with CubeCorps or the Paragon project currently. All respected rights are of the
        copyright owner.

                                        Simulated Artificially Intelligent Companion

                                            -= Author: Klaminite & Blue =-
                                          -= Project Name: The Paragon Project =-

        About:

        Simulates intelligence using external libraries and inside code to parse data,
        graph and predict the modeled equation. On top of the neural networks here, we also have an interface.


'''

#=====================================================================================================

__about__ = '''
****************************************************************************************************************************************
Simulates intelligence using external libraries and inside code to parse data,
graph and predict the modeled equation. Uses modern approaches and algorithms to attempt to
simulate intelligence, though partial, through data and mathematical applications.
****************************************************************************************************************************************
'''
#versions (release.update.patch)
__version__ = '1.0.0'

#if platform.system() == 'Windows':
#    print('Warning! It appears youre using a windows operating system! Switching to windows version now!')
#    subprocess.call('python3 WindowsBoot.py', shell=True)
#else:
print('Using native system: Continuing load;')
#========================
#   System wide Imports
#========================
from mpi4py import MPI
import numpy
import sys, os, urllib
#========================

'''
Initiliaze the system wide variables
here
'''

comm = MPI.COMM_WORLD
rank = comm.Get_rank()  #Applies computer ranking for the backend servers
null_error = '//NULL//ERROR'

class spn():
    '''
    This contains all the classes and functions that is utilized by the master node; also used as the "core" of the software.
    '''
    def main():
        #Start by loading all libraries
        sys.path.append('/PARAGON/BOOT/DRIVERS')
        print("\033[0;31m[System]" + "\033[0;32m | Importing all modules from system;")
        #===============================================================================================
        #import all of the needed files here, note they all are imported via importance.
        try:
            import os, subprocess, signal, time, datetime, random, Speech, protocols, pyaudio, json, nltk, scipy, math, textblob, webbrowser, keras
            import speech_recognition as sr
            from pygame import mixer
            import yahoo_finance as fc
            from time import strftime
            import requests, pywapi, feedparser
            import tensorflow as tf
            import numpy as np
            from multiprocessing import Process
            from keras.applications.resnet50 import ResNet50
            from keras.preprocessing import image
            from keras.applications.resnet50 import preprocess_input, decode_predictions
            import googlemaps as gmaps
        except ImportError:
            import os, subprocess, signal, time, datetime, random, Speech, pyaudio, json, nltk, scipy, math, textblob, webbrowser, keras
            import speech_recognition as sr
            from pygame import mixer
            import yahoo_finance as fc
            from time import strftime
            import requests, pywapi, feedparser
            import tensorflow as tf
            import numpy as np
            from multiprocessing import Process
            from keras.applications.resnet50 import ResNet50
            from keras.preprocessing import image
            from keras.applications.resnet50 import preprocess_input, decode_predictions
            import googlemaps as gmaps
            import include.funcs
            print("It appears as if you do not have all the packages!")
        #===============================================================================================
        '''
        Load all of the files needed for
        basic operation into memory
        '''
        import json
        print("\033[0;31m[System]" + "\033[0;32m Loading files into memory!")
        datafile = json.loads(open('/PARAGON/main/Data/Databases/Data/data.json').read())
        '''
        After this, we can safely start up the system.
        '''
        #Globals
        #sp.init_printing()
        n = 0
        print("[System] Running Version: " + __version__)

        #Start other processes within the script.
        #subprocess.call("ipython3 ./Paragon/Protocols/Pitch.py &", shell=True)
        #subprocess.call("ipython3 ./Paragon/Protocols/Pitch.py &", shell=True)
        '''
        If the webcam isn't already prioritized, then it needs to be set manually, prompting the
        user for a password if they aren't dropped to root.
        '''
        #Checks if there is an external camera, if so, it'll use it.
        '''if os.path.isdir("/dev/video1") == False:
            subprocess.call("python ./Paragon/Startups/Startup_Extern_Webcam", shell=True)
            subprocess.call("python ./Paragon/Protocols/vInter.py &", shell=True)
        else:
            subprocess.call("python ./Paragon/Protocols/vInter.py &", shell=True)
            '''
        print(__about__)
        print(__main__)
        print("//STRT//EVS//GO//VER//" + __version__)
        ct = strftime("%I:%M, %p")
        rand = ["Hello" + (datafile["Identity"][0]["nameFirst"]) + ", welcome back. The current time is" + repr(ct)] #go ahead and welcome whatever you set this to.
        Speech.say(rand,n,mixer)
        class start():
            '''
            The main class, other classes might be related to this or not, really
            classes are just used in this program as a case around any other systems or infrastructures.
            '''
            def Interface():
                '''
                The audio version, and the primary version of the interface.
                '''
                doss = os.getcwd()
                i=0
                n=0
                while (i<1):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        audio = r.adjust_for_ambient_noise(source)
                        n = (n+1)
                        audio = r.listen(source)
                    '''
                    This uses the driver that is installed on the system
                    '''
                    try:
                        s = (r.recognize_google(audio))
                        print(s)
                        message = (s.lower())
                        # Paragon's main interface.
                        '''
                        Most of where this started was from a rather small github repo, in which I ammased this MONSTER code.
                        '''
                        if ('wikipedia') in message:
                            message = message.replace("wikipedia", "")
                            message = message.replace(" ", "_")
                            message = message.capitalize()
                            proxies = {
                            }
                            headers = {
                                "User-Agent": "Definitions/1.0"
                            }
                            params = {
                                'action':'query',
                                'prop':'extracts',
                                'format':'json',
                                'exintro':1,
                                'explaintext':1,
                                'generator':'search',
                                'gsrseParagonh':message,
                                'gsrlimit':1,
                                'continue':''
                            }
                            r = requests.get('http://en.wikipedia.org/w/api.php',
                                             params=params,
                                             headers=headers,
                                             proxies=proxies)
                            json1 = r.json1()
                            result = list(json1["query"]["pages"].items())[0][1]["extract"]
                            print(result)
                            rand = [(result) + '.']
                            Chrome = ("google-chrome %s")
                            webbrowser.get(Chrome)
                            webbrowser.open('https://en.wikipedia.org/wiki/' + message, new=2, autoraise=True)
                            Speech.say(rand,n,mixer)

                        if ('goodbye') in message:
                            rand = ['Goodbye ' + (datafile["Identity"][0]["pronouns"]), 'Paragon powering off']
                            Speech.say(rand,n,mixer)
                            break
                        if ('evening') in message:
                            rand = ['Good evening ' + (datafile["Identity"][0]["pronouns"])]
                            Speech.say(rand,n,mixer)

                        if ('morning') in message:
                            mTime = time.strftime('%B:%d:%Y')
                            rand = ['Good morning ' + (datafile["Identity"][0]["pronouns"]) + ', I grabbed the news for,' + mTime]
                            Chrome = ("google-chrome %s")
                            Speech.say(rand,n,mixer)
                            webbrowser.get(Chrome)
                            webbrowser.open('https://www.sciencenews.org/topic/math-technology', new=2, autoraise=True)
                            print ('')
                        if message == ('Paragon'):
                            rand = ['Yes' + (datafile["Identity"][0]["pronouns"]) + 'What can I, do for you ' + (datafile["Identity"][0]["pronouns"])]
                            Speech.say(rand,n,mixer)
                        if ('are we connected') in message:
                            REMOTE_SERVER = "www.google.com"
                            Speech.wifi()
                            rand = ['We are connected' + (datafile["Identity"][0]["pronouns"])]
                            Speech.say(rand,n,mixer)
                        if ('.com') in message :
                            rand = ['Opening' + message + (datafile["Identity"][0]["pronouns"])]
                            Chrome = ("google-chrome %s")
                            Speech.say(rand,n,mixer)
                            webbrowser.get(Chrome).open('http://www.'+message)
                        if ('.net') in message :
                            rand = ['Opening' + message + (datafile["Identity"][0]["pronouns"])]
                            Chrome = ("google-chrome %s")
                            Speech.say(rand,n,mixer)
                            webbrowser.get(Chrome).open('http://www.'+message)
                        if ('.org') in message :
                            rand = ['Opening' + message]
                            Chrome = ("google-chrome %s")
                            Speech.say(rand,n,mixer)
                            webbrowser.get(Chrome).open('http://www.'+ message)
                        if ('what is the time') in message or ('what time is it') in message or ('can you get me the current time') in message or ('can you tell me the time') in message:
                            lTime = time.strftime('%I:%M')
                            rand = ['the time is,' + lTime + (datafile["Identity"][0]["pronouns"])]
                            Speech.say(rand,n,mixer)
                        if ('what day is it') in message or ('what is the date') in message or ('date please') in message:
                            tDate = time.strftime('%B:%d:%Y')
                            rand = ['Today is,' + tDate + (datafile["Identity"][0]["pronouns"])]
                            Speech.say(rand,n,mixer)
                        if ('Paragon can you get me the weather') in message or ('can you get the weather') in message or ('Paragon weather please') in message or ('weather please') in message:
                            noaa_result = pywapi.get_weather_from_noaa('KPWT')
                            rand = ["I've fetched the weather for you." + "It is currently" + noaa_result['weather'] + '\n' + 'Current Temperature is: ' + noaa_result['temp_f'] +  'Degrees.'+ '\n' + 'Information grabbed from' + noaa_result['location']]
                            Speech.say(rand,n,mixer)
                        if ('can you get the news') in message or ('get the news please') in message or ('Paragon get the news please') in message:
                            rand = ['Fetching todays headlines' + (datafile["Identity"][0]["pronouns"]) + 'please wait.']
                            Speech.say(rand,n,mixer)
                            time.sleep(5)
                            d = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/Science.xml')
                            rand = [d.feed['title'] + d.feed['description']]
                            Speech.say(rand,n,mixer)
                        if ('night mode') in message:
                            rand = ['Ok,' + (datafile["Identity"][0]["pronouns"]) + 'turning on your nightmode settings.']
                            Speech.say(rand,n,mixer)
                            subprocess.call("xbacklight -time 5000 -set 5", shell=True)
                            time.sleep(4)
                            rand = ['Ok' + (datafile["Identity"][0]["pronouns"]) + 'night mode is active.']
                            Speech.say(rand,n,mixer)
                        if ('day mode') in message:
                            rand = ['Ok,' + (datafile["Identity"][0]["pronouns"]) + 'turning on your daytime settings.']
                            Speech.say(rand,n,mixer)
                            subprocess.call("xbacklight -time 5000 -set 100", shell=True)
                            time.sleep(3)
                            rand = ['Ok' + (datafile["Identity"][0]["pronouns"]) + 'daytime mode is now active.']
                            Speech.say(rand,n,mixer)
                        if ('sleep') in message:
                            subprocess.call("xbacklight -time 5000 -set 0", shell=True)
                        if ('where is') in message:
                            rand = ['Searching for' + message + ', please wait.']
                            LocSrch_Message = message.replace("where is", "")
                            Chrome = ("google-chrome %s")
                            Speech.say(rand,n,mixer)
                            webbrowser.get(Chrome).open('http://www.'+ message)
                        if ('what is a') in message or ("what is an") or ("what is") in message:
                            from nltk.corpus import wordnet as Word
                            if "an" in message:
                                message = message.replace("an ","")
                            if "a" in message:
                                message = message.replace("a ","")
                            message = message.replace(" ", "_")
                            spoken_def = Word.synset(message + '.n.1')
                            colist = str(len(spoken_def))
                            rand = [(datafile["Identity"][0]["pronouns"]) + 'there are ' + colist + 'entries, reading the first one: ' + spoken_def.defintion()]
                            webbrowser.get(Chrome)
                            webbrowser.open("http://www.dictionary.com/browse/" + message)
                        if ('medical') in message:
                            #Searches the entire medical dictionary for a term of definition
                            term = message.replace("medical","")
                            import nltk.corpus
                            medical = open('./Data/Databases/Medical_Dictionary.txt')
                            #Converts the text file into an actual corpus, the reason it isn't converted or loaded above,
                            #is because it would consume to many resources if it were constantly loaded.
                            text = medical.read()
                            text1 = text.split()
                            conc_term = nltk.corpus.nltk.Text(text1)
                            med_term = conc_term.concordance(term)
                            rand = [med_term]
                            Speech.say(rand,n,mixer)
                        if ('stock opening') in message:
                            message = message.replace("stock opening", "")
                            #Search the stock database for the given company name
                            df[df['Name'].str.contains(message)]
                            #Further break down the stock table, and find the first hit.
                            TableDi = x.iloc[-1]['Symbol']
                            #Now it's easy sailing.
                            TableConv = stocks.Share(TableDi)
                            rand = ['The opening value of' + message + 'is: ' + TableConv.get_open()]
                            Speech.say(rand,n,mixer)
                        if ('stock price') in message:
                            message = message.replace("stock price", "")
                            #Saearh the stock database for the given company name
                            df[df['Name'].str.contains(message)]
                            #Further break down the stock table, and find the first hit.
                            TableDi = x.iloc[-1]['Symbol']
                            #Now it's easy sailing. x2
                            TableConv = stocks.Share(TableDi)
                            rand = ['The price value of' + message + 'is: ' + TableConv.get_price()]
                            Speech.say(rand,n,mixer)
                        if ('tweet') in message:
                            message.replace('tweet','')

                        if ('paper') in message:
                            name = message.replace("search for papers on", "")
                            embed_prot.search(name)

                        else:
                            temporal_save1 = open("/PARAGON/BOOT/DRIVERS/VOCAL/temp1", "r+") #temp1 -> train.en
                            temporal_save1.write(message)
                            temporal_save1.close()
                            #save the message before giving a response, this way we don't lose data.
                            print(null_error)

                    #exceptions
                    except (KeyboardInterrupt,SystemExit):
                        print("Goodbye, Paragon powering down now")
                        break
                    except sr.UnknownValueError:
                        print("error")
                    except sr.RequestError as e:
                        print("\033[0;31m[System] |Warning! Connection Warning!|")
        if __name__ == '__main__':
            start.Interface()


#========================
#   System wide Imports
#========================
#distributing jobs that can be done simply here.
#mathematically intense jobs that require repetition will be done in c++, anything one off or neccesary to be called quickly in console will be done here.

import numpy
import sys, os, urllib
try:
    from mpi4py import MPI
    if rank == 0:
    #Node 1 and the linguistics
        import apt
        cache = apt.Cache()
        if cache['mpich'].is_installed:
            print('Mpich installed')
            spn.main()
    if rank == 2:
    #Node 2 and the mathmatical node.
    #===========================
        try:
            import theano as th
            import sympy as sp
            import numpy as np
        except ImportError:
            print("\033[0;31m[System] |Warning! Import Warning!| System failed to import a library!")
        if rank == 3:

            print("none")
        if rank == 4:
            print("none")
        else:
            #Continue the program as if nothing really happens
            if __name__ == '__main__':
                 spn.main()
except ImportError:
    print("Not configured for cluster computing; continuing with single computer computing.")
    if __name__ == '__main__':
        spn.main()
            

