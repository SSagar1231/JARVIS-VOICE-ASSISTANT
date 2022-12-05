from multiprocessing.connection import Listener
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
import pyjokes
# import playsound
import random
from speech import talk


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say('hello my name is Jarvis how may i help you')
engine.runAndWait()
engine.connectrunAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listenpip.install.SpeechRecognitionr.listen(source)
            command = Listener.recognize_google(voice)
            command = command.lower()
            if 'Jarvis' in command:
                command = command.replace('Jarvis', '')
                print(command)
    # except:
    #     pass
    except sr.UnknownValueError:
            print("Oops! Didn't catch that")
    return command
    

def run_Jarvis():
    command = take_command()
    print(command)
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'how are you' in command:
        greet = command.replace('how are you', '')
        
        list_of_greet = ["I am good, how can i help you?","Better then yesterday, any work for me","Great, today is nice day. How can i help you?","Nice, i am learning new things to help you better."]
        # print("the given list is :",list1)
        random_index = random.randrange(len(list_of_greet))
        # print(random_index)
        pick =  list_of_greet[random_index]
        

        print(pick)
        talk(pick)

    elif 'what is' in command:
        question = command.replace('what is', '')
        info = wikipedia.summary(question, 1)
        print(info)
        talk(info)

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    
    elif "search for" in command:
        search_term = command.replace("search for", '')
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        talk(f'Here is what I found for {search_term} on google')
    
    elif "where is" in command:
        search_dir = command.replace("where is", '')
        url = f"https://www.google.com/maps/place/{search_dir}"
        webbrowser.get().open(url)
        # talk(f'Here is what I found for {search_term} on google')
    
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    
    elif 'google translate' in command:
        trans = command.replace("google transalate", '')
        url = f"https://translate.google.co.in/?sl=auto&tl=mr{trans}"
        talk()
    

    elif 'send message' in command:
        message = command.replace("send message", '')
        pywhatkit.sendwhatmsg('+919527961203',"Hello user, this message is generated by Pratik. Through Python Script",15,54)

    else:
        talk('Please say the command again.')

if __name__ == "__main__":
    while True:
        run_Jarvis()
