from func import *
from Authenticate import *
from settings import *

con_friday = sql.connect(host='localhost', user='root', password='krish4926', database='friday_allusers')
cursor_friday = con_friday.cursor()


cursor_friday.execute("SELECT name, address FROM websites")
websites = {name.lower(): address for name, address in cursor_friday.fetchall()}
current_user= activeuser()
uname = activeuname()


# UserAuth()
# print_hi_art()
# Greet()
while True:


    query = listen()

    matches = [website_name for website_name in websites if website_name in query.lower()]

    if matches:
        x = f"Opening websites: {', '.join(matches)}"
        print(x)
        history(current_user, query, x)
        for match in matches:
            webbrowser.open(websites[match])

    elif any(keyword in query for keyword in ["song", "music"]):

        speak("Which song would you like to listen")
        songquery = listen().lower()
        speak("From where would you like to listen? Youtube, Spotify, Or local storage")
        songlocationquery = listen().lower()
        y = f"Playing Song: {songquery}"
        history(current_user, query, y)
        if any(keyword in songlocationquery for keyword in ["youtube", "you tube", "utube", "u tube"]):
            speak(f"Playing {songquery} on youtube:")
            pywhatkit.playonyt(songquery)
        elif "spotify" in songlocationquery:
            speak(f"Playing {songquery} on Spotify:")
            webbrowser.open(f"https://open.spotify.com/search/{songquery}")

        elif any(keyword in songlocationquery for keyword in ["locals", "local", "pc", "laptop", "folder"]):
            speak("Please type in the path for your music file")
        else :
            print("Unable to find your song")


    elif any(keyword in query for keyword in ["sleep", "quit", "bye", "turn off", "goodbye", "turnoff", "good bye", "bi", "bye", "log off", "logoff", "shutdown", "shut down", "exit"]):
        speak("goodbye sir")
        exit()


    elif any(keyword in query for keyword in ["open settings", "settings", "open setting", "setting", "change setting", "change settings", "configure", "configurations"]):
        settings()
        print("setings done")
        z = "Settings changed succesfully"
        history(current_user, query,z)

    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        a = f"Sir, the time is {current_time}."
        history(current_user, query, a)
        speak(a)
    elif "create" in query:
        create_todo(current_user)
        history(current_user, query, "To-do created.")

    elif "show" in query:
        read_todos(current_user)

    elif "update" in query:
        update_todo(current_user)

    elif "delete" in query:
        delete_todo(current_user)












