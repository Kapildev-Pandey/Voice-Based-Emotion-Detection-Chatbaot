
from keras.models import Sequential
from keras.losses import categorical_crossentropy
from keras.optimizers import SGD
from keras.layers import Dense,Dropout,Input,Embedding
import nltk
from numpy import argmax
import numpy as np
import re
from keras.models import load_model
import pandas as pd
import warnings
import pyttsx3
warnings.filterwarnings("ignore")
print('Loading packages...')

print("Happpy Or Sad")
print('Loading Model..........')
model_name=input()
if model_name=='Happy':
    excel_model=pd.read_excel('{}.xlsx'.format(model_name),engine='openpyxl',sheet_name='{}'.format(model_name))
    model1 = load_model('{}_model.h5'.format(model_name))
    print("Bot :","You look very happy KSilver. How was your day? Is anything interesting happened today?")
    pyttsx3.speak("You look very happy KSilver. How was your day? Is anything interesting happened today?")
else:
    excel_model=pd.read_excel('Happy.xlsx'.format(model_name),engine='openpyxl',sheet_name='{}'.format(model_name))
    model1 = load_model('{}_model.h5'.format(model_name))
    print("Bot :","You lack the prettiest thing in your face KSilver")
    pyttsx3.speak("You lack the prettiest thing in your face KSilver")
    

total_words=int(excel_model.iloc[0,1])
#print(total_words)
word2idx=eval(excel_model.iloc[1,1])
max_sequence_len=int(excel_model.iloc[2,1])
classes= eval(excel_model.iloc[3,1])



import pyttsx3
import speech_recognition as SRG 
import time
 
store = SRG.Recognizer()
with SRG.Microphone() as s:
    while True:
        print("Speak...")
        try:
            audio_input = store.record(s, duration=15)
            text_output = store.recognize_google(audio_input)
            sentence = text_output
            print("Me: ",sentence)
            if sentence=='bye':
                print("Bye !! Take care yourself :)")
                pyttsx3.speak("Bye Take care yourself")
                break
            else:

                tok=nltk.word_tokenize(sentence.lower())
                b=[]
                for i in range(len(tok)):
                    for j in range(total_words):
                        if tok[i]==list(word2idx.items())[j][0]:
                            b.append(list(word2idx.items())[j][1])

                for i in range(len(tok)):
                        if len(b)!=max_sequence_len:
                            zero=max_sequence_len-len(b)
                            for j in range(zero):
                                b.append(0)

                prediction= model1.predict(np.array([b]))
                print('BOT: ',classes[argmax(prediction)])
                pyttsx3.speak(classes[argmax(prediction)])
                
        except:
            print("Couldn't process the audio input.")



