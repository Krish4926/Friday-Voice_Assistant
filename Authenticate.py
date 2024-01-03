from func import *
import sys
import time
con_auth = sql.connect(host='localhost', user='root', password='krish4926', database='friday_allusers')
cursor_auth = con_auth.cursor()




def signup():
    speak("Please fill in the details. Type 'exit' at any time to quit.")
    while True:
        username = input("Enter your username: ")
        if username.lower() == 'exit':
            sys.exit("User opted to exit the signup process.")
        email_id = input("Enter your email: ")
        cursor_auth.execute('''
            SELECT 1 FROM users WHERE username = %s OR email_id = %s
        ''', (username, email_id))
        duplicate_entry = cursor_auth.fetchone()
        if duplicate_entry:
            print("Error: Username or email already exists. Please choose a different one.")
            continue
        uname = input("Enter your full name: ")
        while True:
            password = input("Enter your password: ")
            repeat_password = input("Repeat your password: ")
            if password == repeat_password:
                break
            else:
                print("Passwords do not match. Please try again.")
        mobile_no = input("Enter your mobile number: ")

        log_time = time.strftime('%Y-%m-%d %H:%M:%S') 

        cursor_auth.execute('''
            INSERT INTO users (username, email_id, name, password, mobile_no)
            VALUES (%s, %s, %s, %s, %s)
        ''', (username, email_id, uname, password, mobile_no))

        cursor_auth.execute('''
            INSERT INTO usage_reg (username, name, log_time)
            VALUES (%s, %s, %s)
        ''', (username, uname, log_time)) 
        con_auth.commit()
        speak("You have been signed up to your account")
        time.sleep(1)
        break

def login():
    login_successful = True
    while login_successful:
        login_input = input("Enter your username/email/mobile_no (type 'exit' to quit): ")
        if login_input.lower() == 'exit':
            sys.exit("User opted to exit the login process.")
        password_input = input("Enter your password: ")
        cursor_auth.execute('''
            SELECT * FROM users
            WHERE username = %s OR email_id = %s OR mobile_no = %s
        ''', (login_input, login_input, login_input))
        user_data = cursor_auth.fetchone()
        if user_data and user_data[3] == password_input:
            speak("Login successful!")

            log_time = time.strftime('%Y-%m-%d %H:%M:%S')  # Define log_time

            cursor_auth.execute('''
                INSERT INTO usage_reg (username, name, log_time)
                VALUES (%s, %s, %s)
            ''', (user_data[0], user_data[2], log_time))
            
            con_auth.commit()

            time.sleep(2)
            clear()
            login_successful = False
            print("You are logged in.")
            return
        else:
            speak("Login failed. Invalid username/email/mobile_no or password.")
            time.sleep(1)

def UserAuth():
    speak("Would you like to Signup or Login as an Existing User?")
    authdata = listen()
    if any(keyword in authdata.lower() for keyword in ["login", "old user", "not a new user", "not new user", "signin", "sign in", "log in"]):
        login()
    elif any(keyword in authdata.lower() for keyword in ["signup", "new user", "sign me up", "logup", "sign up", "log up"]):
        signup()


def activeuser():
    cursor_auth.execute('''
    SELECT username
    FROM usage_reg
    ORDER BY log_time DESC
    LIMIT 1
    ''')
    latest_username_data = cursor_auth.fetchone()
    loginusername = latest_username_data[0]
    return loginusername

def activeuname():
    cursor_auth.execute('''
    SELECT name
    FROM usage_reg
    ORDER BY log_time DESC
    LIMIT 1
    ''')
    latest_uname_data = cursor_auth.fetchone()
    loginusern = latest_uname_data[0]
    return loginusern



