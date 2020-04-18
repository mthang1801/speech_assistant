import speech_recognition as sr
import time
import webbrowser
from time import ctime
import playsound
from gtts import gTTS
import os
import random
#Init speech recognition
r = sr.Recognizer();

def record_audio(ask = False) : 
  if ask : 
    alexis_speak(ask)
  with sr.Microphone() as source : 
    #Listen from microphone 
    audio = r.listen(source);
    voice_data = "";
    try :
      #write audio to text_speech
      voice_data = r.recognize_google(audio);      
    except sr.UnknownValueError : 
      alexis_speak("Sorry, I didn't get that");
    except sr.RequestError : 
      alexis_speak("Sorry, my speech service is down");
    return voice_data;

def alexis_speak(audio_string) : 
  tts = gTTS(text=audio_string,lang="en");
  r = random.randint(1,100000);  
  audio_file = "audio-" + str(r) + ".mp3";
  tts.save(audio_file);
  playsound.playsound(audio_file);
  print(audio_string);
  os.remove(audio_file);

def respond(voice_data) :
  if "what is your name" in voice_data or "what's your name" in voice_data or "who are you" in voice_data: 
    alexis_speak("My name is Alexis");
  if "what time is it" in voice_data : 
    alexis_speak(ctime())
  if "search" in voice_data : 
    search = record_audio("What do you want to search for?");
    url = "https://google.com/search?q=" + search 
    webbrowser.get().open(url);
    alexis_speak("Here is what I found for " + search);
  if "find location" in voice_data : 
    location = record_audio("What is the location?");
    url = "https://google.nl/maps/place/" + location + "/&amp;"
    webbrowser.get().open(url);
    alexis_speak("Here is the location I found " + location);
  if "stop" in voice_data or "exit" in voice_data:
    alexis_speak("Good bye");
    exit();
    
time.sleep(1);
alexis_speak("How can I help you?");
while 1: 
  voice_data = record_audio();
  print(voice_data)
  respond(voice_data);
  

  