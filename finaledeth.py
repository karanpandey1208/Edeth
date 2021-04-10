import datetime
import os
import pyjokes
import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import wikipedia
import pyautogui as ui  
from googlesearch import search 
from time import sleep
from playsound import playsound




engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Login():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")
    elif hour>=18 and hour<21:
        speak("Good Evening sir!")
    else:
        speak("Good NIght sir!")    
    
    

def logout():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning"+ name)
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon"+ name)
    elif (hour >= 18 and hour < 20):
        speak("Good Evening"+ name)
    else:
        speak("Good Night.. Sweet Dreams"+ name)



def reciver():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listeming....")
        r.energy_threshold = 300
        r.pause_threshold = 0.6
        r.non_speaking_duration = 0.3
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')    
        print("user said: ",query)

    except Exception as e:
         print(e)
         print("Parden please......")
         return"None"
    return query


def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {Time}")

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def screenCapture():
    myScreenshot = ui.screenshot()
    myScreenshot.save(r'C:\\PYTHON\\screenshot.png')

if __name__ =="__main__":
    print("-------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------")
    print("                                                                                                             ")
    print("                      _____      _______      ______     _________     _      _                              ")
    print("                     ! ____!    ! !   \ \    !  ____!   !___   ___!   ! !    ! !                             ")
    print("                     ! |__      ! !    ! !   ! !__          ! !       ! !____! !                             ")
    print("                     !  __!     ! !    ! !   !  __!         ! !       !  ____  !                             ")
    print("                     ! |___     ! !    ! !   ! |____        ! !       ! !    ! !                             ")
    print("                     !_____!    !_!___/_/    !______!       !_!       !_!    !_!                             ")
    print("                                                                                                             ")
    print("-------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------<<<<<Creator= KARAN PANDEY>>>>>------")
    
    
    
    Login()
    
    speak("I am edeth, please tell your name")   
    name = reciver().lower()
    name = name.replace("my name is", " ")
    speak('Hello' + name)
    print('Speak :- ( Hello  ,mycode, Hey or Activate ) to Wakeup the EDETH.')
    while(True):
            query = reciver().lower()
                
            if('Edeth' in query or 'activate' in query 
            or 'my code' in query or 'hey ' in query or 'hello' in query or 'hyy' in query or 'hey' in query or 'activate edeth' in query or 'mycode' in query ):
                speak('ACTIVATED')
                
                
                query = reciver().lower()
                
                if ('open code' in query or 'vs code' in query
                    or 'visual studio' in query):
                    speak("opening visual stdio code")
                    codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)
    

                elif ('open word' in query or 'ms word' in query 
                     or 'microsoft word' in query):
                    speak("opening microsoft word")
                    codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                    os.startfile(codePath)
                
                elif ('open PowerPoint' in query or 'ms PowerPoint' in query 
                     or 'Microsoft PowerPoint' in query or 'power' in query):
                    speak("opening microsoft powerpoint")
                    codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                    os.startfile(codePath)
    
                elif ('open excel' in query or 'ms excel' in query 
                     or 'microsoft excel' in query or 'xl' in query):
                    speak("opening microsoft excel")
                    codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                    os.startfile(codePath)
    
                elif ('open access' in query or 'ms access' in query 
                     or 'microsoft access' in query):
                    speak("opening microsoft access")
                    codePath = "C:\\Program Files\Microsoft Office\\root\\Office16\\MSACCESS.EXE"
                    os.startfile(codePath)
    
    

                elif ('open spotify' in query ):
                    speak("opening spotify")
                    codePath = "C:\\Users\\Admin\\AppData\\Roaming\\Spotify\\Spotify.exe"
                    spotify = os.startfile(codePath)
                    sleep(2)
                    ui.press('space')
                    continue

                elif 'close spotify' in query:
                    os.system("taskkill /f /im Spotify.exe")
                    continue            

                elif ('wikipedia' in query or 'who' in query
                    or 'when' in query or 'where' in query):
                    try:
                        speak("searching...")
                        query = query.replace("wikipedia", " ")
                        query = query.replace("search", " ")
                        query = query.replace("when", " ")
                        query = query.replace("where", " ")
                        query = query.replace("who", " ")
                        query = query.replace("is", " ")
                        result = wikipedia.summary(query, sentences=2)
                        speak("According to wikipedia")
                        print(result)
                        speak(result)
                    except Exception:
                        speak("Sorry i am to search your query")
                
                elif ('what is' in query or "how much is" in query 
                    or 'joke' in query):
                    try:
                        speak("searching...")
                        query=query.replace("what is", " ")
                        query=query.replace("how much is", " ")
                        app_id="XWVQYR-3REARW7W5A"
                        client = wa.Client('XWVQYR-3REARW7W5A')
                        res = client.query(query)
                        answer = next(res.results).text
                        print(answer)
                        speak(answer)
                    except Exception:
                        speak("Sorry i an unable to search your query")    


                elif 'google' in query:
                    try:
                        speak("opening google")
                        wb.open("www.google.com")
                    except Exception:
                        speak("Sorry i an unable to search your query")

                elif 'youtube' in query:
                    try:
                        speak("opening youtube")
                        wb.open("www.youtube.com")    
                    except Exception:
                        speak("Sorry i an unable to search your query")
                
                elif ('stackoverflow' in query or 'stack over flow' in query):
                    try:
                        speak("opening stack over flow")
                        wb.open("stackoverflow.com")    
                    except Exception:
                        speak("Sorry i an unable to search your query")                        
                
                elif ('github' in query or 'git hub' in query):
                    try:    
                        speak("opening github")
                        wb.open("github.com")
                    except Exception:
                        speak("Sorry i an unable to search your query")
                
                elif ('whatsapp' in query or 'whatsapp' in query
                    or 'whats app' in query):
                    try:    
                        speak("opening whatsapp web")
                        wb.open("web.whatsapp.com")
                    except Exception:
                        speak("Sorry i an unable to search your query") 
                
                elif 'instagram' in query:
                    try:
                        speak("opening instagram")
                        wb.open("instagram.com")
                    except Exception:
                        speak("Sorry i an unable to search your query")
                
                elif ("create a reminder list" in query or "reminder" in query):
                    speak("What is the reminder?")
                    data = reciver()
                    speak("You said to remember that" + data)
                    reminder_file = open("edeth reminder.txt", 'a')
                    reminder_file.write('\n')
                    reminder_file.write(data)
                    reminder_file.close()
                
                elif 'search' in query:
                    try:
                        speak("Searching...")
                        query = query.replace("search"," ")
                        search(query, tld="co.in", num=10, stop=10, pause=2)
                        wb.open("https://google.com/search?q=%s" % query)
                    except Exception:
                        speak("Sorry i an unable to search your query") 

                elif 'close browser' in query:
                    os.system("taskkill /f /im msedge.exe")
                    continue

                elif 'time' in query:
                    time()
                    speak("Thank you")

                elif 'date' in query:
                    date()
                    speak("thank you")
                    continue
                
                elif ("screenshot" in query):
                    screenCapture()
                    speak("Done!")
                    continue

                elif ("tell me a joke" in query or "joke" in query):
                    jokes()

                elif 'restart' in query or 'restart the pc' in query:
                    speak("do you want to restart this p.c.")
                    speak("if you want then say yes!")
                    q = reciver()
                    if "yes" in q:
                        logout()
                        speak("Restarting your p.c...")
                        os.system("shutdown /r /t 1")  
                        break
                    else:
                        speak("ok sir")
    
                elif 'shutdown' in query or 'shut down' in query:
                    speak("do you want to shutdown this p. c.")
                    speak("if you want then say yes!")
                    q = reciver()
                    if "yes" in q:
                        logout()
                        speak("Shutting down your p.c...")
                        os.system("shutdown /s /t 1")  
                        break
                    else:
                        speak("ok sir")
                elif ('i am done' in query or 'bye edeth' in query
                                or 'go offline edeth' in query or 'bye' in query or 'go offline' in query or 'thats enough' in query
                                or 'see you edeth' in query or 'nothing' in query or 'logout' in query or 'log out' in query):
                    logout()
                    break
                
