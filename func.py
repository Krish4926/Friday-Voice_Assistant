import speech_recognition as sr
import pyttsx3
import sys
import datetime
import os
import pywhatkit
import random
import webbrowser
import mysql.connector as sql
import time
import smtplib
import random
from prettytable import PrettyTable
import mysql.connector as sql

con_func = sql.connect(host='localhost', user='root', password='krish4926', database='friday_allusers')
cursor_func = con_func.cursor()

def activeuser():
    cursor_func.execute('''
    SELECT username
    FROM usage_reg
    ORDER BY log_time DESC
    LIMIT 1
    ''')
    latest_username_data = cursor_func.fetchone()
    loginusername = latest_username_data[0]
    return loginusername

def activeuname():
    cursor_func.execute('''
    SELECT name
    FROM usage_reg
    ORDER BY log_time DESC
    LIMIT 1
    ''')
    latest_uname_data = cursor_func.fetchone()
    loginusern = latest_uname_data[0]
    return loginusern



current_user = activeuser()
current_uname = activeuname()




#Default settings-----------

def current_defaults() :
    cursor_func.execute('''
        SELECT * FROM friday_config
        ORDER BY id DESC
        LIMIT 1
    ''')
    latest_config = cursor_func.fetchone()
    default_id, default_speech_rate, default_email, default_password, default_volume = latest_config
    return default_speech_rate, default_email, default_password, default_volume


default_rate, default_sendersemail, default_senderspassword, default_volume = current_defaults()


def slowprint(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()
def clear():
    # os.system('cls')
    return None

def print_hi_art():
    hi_art = """
███   ███   ███    
███   ███   
███   ███   ███
███▄▄▄███   ███
█████████   ███
███▀▀▀███   ███
███   ███   ███
███   ███   ███
███   ███   ███     
            
"""
    print(hi_art )
    
def mail(to, content) :

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(default_sendersemail, default_senderspassword)
    server.sendmail(default_sendersemail, default_senderspassword, to, content)
    server.close()


def listen():
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio_data = recognizer.listen(source)
        try:
            recognized_text = recognizer.recognize_google(audio_data)
            print(f"You said: {recognized_text.lower()}")
            return recognized_text.lower()  # Return the recognized text

        except sr.UnknownValueError as ee:
            print("Sorry, I couldn't understand.")
            return ""  
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")
            return ""








def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('volume', default_volume)
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', default_rate)
    print(text)
    engine.say(text)
    engine.runAndWait()

def Greet(uname="krish") :
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if 5 <= hour < 12:
        greeting = "Good morning!"
    elif 12 <= hour < 17:
        greeting = "Good afternoon!"
    elif 17 <= hour < 21:
        greeting = "Good evening!"
    else:
        greeting = "Good night!"
    speak(f"{greeting} {uname}!, how can i help you today?")


def create_todo(current_username):
    speak("What task would you like to add to your to-do list?")
    todo_text = listen().lower()
    insert_query = "INSERT INTO todos (username, todo_text) VALUES (%s, %s)"
    cursor_func.execute(insert_query, (current_username, todo_text))
    con_func.commit()
    speak(f"To-do added: {todo_text}")


def read_todos(current_username):
    select_query = f"SELECT * FROM todos "
    cursor_func.execute(select_query)
    result = cursor_func.fetchall()
    if result:
        for row in result:
            status = "Done" if row[4] else "Not Done"
            print(f"To-do {row[1]}: {row[2]} ({status}), Created on: {row[3]}")
    else:
        speak("You have no to-dos.")



def update_todo(current_username):
    read_todos(current_username)
    speak("Which to-do would you like to update? Please provide the to-do number.")
    todo_number = int(listen())
    speak("Is the to-do done? Yes or no?")
    is_done = listen().lower() == "yes"
    update_query = f"UPDATE todos SET completed = {is_done} WHERE id = {todo_number}"
    cursor_func.execute(update_query)
    con_func.commit()
    speak("To-do updated successfully.")

def delete_todo(current_username):
    read_todos(current_username)
    speak("Which to-do would you like to delete? Please provide the to-do number.")
    todo_number = int(listen())
    delete_query = f"DELETE FROM todos WHERE id = {todo_number}"
    cursor_func.execute(delete_query)
    con_func.commit()
    speak("To-do deleted successfully.")









