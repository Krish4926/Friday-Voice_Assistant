from func import *
from Authenticate import *
from prettytable import PrettyTable



con_setting = sql.connect(host='localhost', user='root', password='krish4926', database='friday_allusers')
cursor_setting = con_setting.cursor()

current_user= activeuser() #for username
uname = activeuname() #for name

def settings(login_user):
    settingsloop = True

    while settingsloop:
        speak("What would you like to access?")
        print("""
            1) Admin Controls
            2) Friday Settings
            3) Users History
            4) Account Centre
            5) Exit
        """)

        query1 = listen()

        if any(keyword in query1.lower() for keyword in ["nothing", "exit", "close", "5", "five"]):
            settingsloop = False
        elif any(keyword in query1.lower() for keyword in ["1", "one", "admin", "admin controls", "admin settings", "admin setting", "admin control"]):
            admin_controls(login_user)  # Pass login_user to admin_controls
        elif any(keyword in query1.lower() for keyword in ["2", "two", "setting", "settings"]):
            friday_settings()
        elif any(keyword in query1.lower() for keyword in ["3", "three", "history"]):
            users_history()
        elif any(keyword in query1.lower() for keyword in ["4", "four", "profile","account","center","centre"]):
            profile()




#----------------------------------Admin Controls-------------------------------------

def admin_controls(login_user):
    cursor_setting.execute('''
        SELECT role FROM users
        WHERE username = %s
    ''', (login_user,))
    user_role = cursor_setting.fetchone()

    if user_role and user_role[0] == 'admin':
        speak("Welcome Admin!")
        speak("Performing admin actions...")

        while True:
            speak("Admin Controls opened! ")
            print("""
                Admin Controls:
                1) View User List
                2) Grant Admin Access
                3) Revoke Admin Access
                4) View All User History
                5) Exit Admin Controls
            """)
            query2 = listen()

            if any(keyword in query2.lower() for keyword in ["1", "one", "user list", "list", "first"]):
                view_user_list()
            elif any(keyword in query2.lower() for keyword in ["2", "two", "grant", "allow", "second", "give"]):
                grant_admin_access()
            elif any(keyword in query2.lower() for keyword in ["3", "three", "revoke", "remove", "third"]):
                revoke_admin_access()
            elif any(keyword in query2.lower() for keyword in ["4", "four", "view all", "user history", "all users", "fourth"]):
                view_all_user_history()
            elif any(keyword in query2.lower() for keyword in ["5", "five", "exit", "close", "bye", "fifth"]):
                speak("Exiting Admin Controls.")
                break
            else:
                speak("Invalid choice. Please enter a valid option.")

    else:
        speak("You do not have permission to access admin controls. Please log in as an admin.")
        admin_login_successful = False
        while not admin_login_successful:
            admin_username = input("Enter admin username: ")
            admin_password = input("Enter admin password: ")
            cursor_setting.execute('''
                SELECT 1 FROM users
                WHERE username = %s AND password = %s AND role = 'admin'
            ''', (admin_username, admin_password))
            is_admin = cursor_setting.fetchone()

            if is_admin:
                cursor_setting.execute('''
                        SELECT * FROM users
                        WHERE username = %s
                    ''', (admin_username,))
                user_data = cursor_setting.fetchone()
                print(user_data[2],user_data[0])
                log_time = time.strftime('%Y-%m-%d %H:%M:%S')
                cursor_setting.execute('''
                        INSERT INTO usage_reg (id, username, name, log_time)
                        VALUES (NULL, %s, %s, %s)
                    ''', (user_data[0], user_data[2], log_time))
                con_setting.commit()
                speak("Admin login successful!")
                login_user = admin_username
                admin_login_successful = True
                print("Performing admin actions...")
                while True:
                    speak("Admin Controls opened! ")
                    print("""
                        Admin Controls:
                        1) View User List
                        2) Grant Admin Access
                        3) Revoke Admin Access
                        4) View All User History
                        5) Exit Admin Controls
                    """)
                    query2 = listen()

                    if any(keyword in query2.lower() for keyword in ["1", "one", "user list", "list", "first"]):
                        view_user_list()
                    elif any(keyword in query2.lower() for keyword in ["2", "two", "grant", "allow", "second", "give"]):
                        grant_admin_access()
                    elif any(keyword in query2.lower() for keyword in ["3", "three", "revoke", "remove", "third"]):
                        revoke_admin_access()
                    elif any(keyword in query2.lower() for keyword in ["4", "four", "view all", "user history", "all users", "fourth"]):
                        view_all_user_history()
                    elif any(keyword in query2.lower() for keyword in ["5", "five", "exit", "close", "bye", "fifth"]):
                        speak("Exiting Admin Controls.")
                        break
                    else:
                        speak("Invalid choice. Please enter a valid option.")

            else:
                speak("Invalid admin credentials. What else can I do for you?")
                break


def view_user_list():
    speak("Displaying the User List.")
    cursor_setting.execute('''
        SELECT * FROM users
    ''')
    user_list_data = cursor_setting.fetchall()
    if not user_list_data:
        speak("No users found.")
    else:
        table = PrettyTable()
        table.field_names = ["Username", "Email ID", "Name", "Password", "Mobile Number", "Role"]
        for user_data in user_list_data:
            table.add_row([user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5]])
        print(table)
    speak("End of User List.")

def display_users_table():
    cursor_setting.execute('''
        SELECT name, username, role FROM users
    ''')
    user_list_data = cursor_setting.fetchall()
    table = PrettyTable()
    table.field_names = ["Name", "Username", "Role"]
    for user_data in user_list_data:
        table.add_row([user_data[0], user_data[1], user_data[2]])
    print(table)

def grant_admin_access():
    display_users_table()
    speak("Enter the username or name to grant admin access: ")
    username_to_grant = input("Username/Name: ")
    cursor_setting.execute('''
        SELECT name, username, role FROM users
        WHERE name = %s OR username = %s
    ''', (username_to_grant, username_to_grant))
    user_data = cursor_setting.fetchone()

    if user_data:
        name, username, role = user_data
        if role == 'admin':
            print(f"{name} ({username}) already has admin access.")
        else:
            cursor_setting.execute('''
                UPDATE users
                SET role = 'admin'
                WHERE username = %s
            ''', (username,))
            con_setting.commit()
            print(f"Admin access granted to {name} ({username}).")
    else:
        print(f"No user found with the name/username: {username_to_grant}.")

def revoke_admin_access():
    display_users_table()
    speak("Enter the username or name to revoke admin access: ")
    username_to_revoke = input("Username/Name: ")
    cursor_setting.execute('''
        SELECT name, username, role FROM users
        WHERE name = %s OR username = %s
    ''', (username_to_revoke, username_to_revoke))
    user_data = cursor_setting.fetchone()

    if user_data:
        name, username, role = user_data
        if role == 'guest':
            print(f"{name} ({username}) already doesn't have admin access.")
        else:
            cursor_setting.execute('''
                UPDATE users
                SET role = 'guest'
                WHERE username = %s
            ''', (username,))
            con_setting.commit()
            print(f"Admin access revoked from {name} ({username}).")
    else:
        print(f"No user found with the name/username: {username_to_revoke}.")

def history(username, user_input, friday_output):
    table_name = f"{username}_history"
    cursor_setting.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_input TEXT,
            friday_output TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor_setting.execute(f'''
        INSERT INTO {table_name} (user_input, friday_output)
        VALUES (%s, %s)
    ''', (user_input, friday_output))
    con_setting.commit()


# ------------------------------------------Friday Settings--------------------------------------------

def friday_settings():
    print("Friday Settings")

    while True:
        print("""
            1) Change Speech Rate
            2) Change Default Email Address (Used for Emailing Services)
            3) Adjust Volume
            4) Back to Main Menu
        """)

        query2 = listen()

        if any(keyword in query2.lower() for keyword in ["nothing", "exit", "close", "4", "four"]):
            print("Exiting Friday Settings.")
            break
        elif any(keyword in query2.lower() for keyword in ["1", "one", "speech rate", "change speech rate"]):
            change_speech_rate()
        elif any(keyword in query2.lower() for keyword in ["2", "two", "default email", "change email"]):
            change_default_email()
        elif any(keyword in query2.lower() for keyword in ["3", "three", "volume", "adjust volume"]):
            adjust_volume()
        else:
            print("Invalid choice. Please enter a valid option.")


def change_default_email():
    speak("Enter your new default email address: ")
    new_default_email = input("Email: ")

    speak("Enter your new default password: ")
    new_default_password = input("Password: ")

    speak(f"Confirm changes: New email: {new_default_email}, New password: {new_default_password}. Is that correct?")
    confirmation = listen()

    if any(keyword in confirmation for keyword in ["yes", "confirm"]):
        cursor_func.execute('''
            UPDATE friday_config
            SET default_email = %s, default_password = %s
            ORDER BY id DESC
            LIMIT 1
        ''', (new_default_email, new_default_password))
        con_func.commit()

        speak("Changes confirmed. Default email and password updated successfully.")
    else:
        speak("Changes not confirmed. Default email and password remain unchanged.")

def change_speech_rate():
    speak("What is the new rate? ")
    print("""Default: 130
High: 150
Slow: 100""")      
          
    user_input = listen().lower()
    rate_mapping = {"default": "130", "fast": "150", "slow": "100"}
    if user_input.isdigit():
        new_rate = user_input
    elif user_input in rate_mapping:
        new_rate = rate_mapping[user_input]
    else:
        speak("Invalid input. Please provide a numeric value or choose from the allowed terms.")
        return
    cursor_func.execute('''
        UPDATE friday_config
        SET default_speech_rate = %s
        ORDER BY id DESC
        LIMIT 1
    ''', (new_rate,))
    con_func.commit()
    speak(f"Speech rate updated to {new_rate}.")

def adjust_volume():
    speak("What is the new volume level? Please say a number between 0 and 100.")
    new_volume = listen()

    try:
        new_volume = int(new_volume)
        if 0 <= new_volume <= 100:
            new_volume_range = new_volume/100
            cursor_func.execute('''
                UPDATE friday_config
                SET default_volume = %s
                ORDER BY id DESC
                LIMIT 1
            ''', (new_volume_range,))
            con_func.commit()
            speak(f"Volume level updated to {new_volume}.")
        else:
            speak("Please provide a valid volume level between 0 and 100.")
    except ValueError:
        speak("Sorry, I couldn't understand the volume level. Please provide a valid number.")






#---------------------------------------------------------------------------------------------


def users_history():
    print("Users History")
    table_name = f"{current_user}_history"
    cursor_setting.execute(f"SELECT * FROM {table_name}")
    history_data = cursor_setting.fetchall()
    table = PrettyTable()
    table.field_names = ["ID", "User Input", "Friday Output", "Timestamp"]
    for entry in history_data:
        table.add_row(entry)
    print("Displaying Users History:")
    print(table)
    print("""
        1) Delete All History
        2) Delete History in a Range
        3) Delete Single History by ID
        4) Back to Main Menu
    """)

    action_choice = listen()
    print("Action Choice:", action_choice)  # Add this line


    if any(keyword in action_choice.lower() for keyword in ["nothing", "exit", "close", "4", "four"]):
        print("Exiting Users History.")
    elif any(keyword in action_choice.lower() for keyword in ["1", "delete all", "delete all history"]):
        delete_all_history()
    elif any(keyword in action_choice.lower() for keyword in ["2", "delete range", "delete history range"]):
        delete_history_range()
    elif any(keyword in action_choice.lower() for keyword in ["3", "delete single", "delete history single"]):
        delete_single_history()
    else:
        print("Invalid choice. Please enter a valid option.")
    con_setting.commit()


def delete_all_history():
    table_name = f"{current_user}_history"
    cursor_setting.execute(f"DELETE FROM {table_name}")
    con_setting.commit()

def delete_history_range():
    table_name = f"{current_user}_history"
    speak("Enter the range of history entries to delete (start ID and end ID):")
    start_id = input("Start ID: ")
    end_id = input("End ID: ")
    cursor_setting.execute(f"DELETE FROM {table_name} WHERE id BETWEEN %s AND %s", (start_id, end_id))
    con_setting.commit()
    speak(f"History entries from ID {start_id} to {end_id} deleted successfully.")

def delete_single_history():
    table_name = f"{current_user}_history"
    speak("Enter the ID of the history entry to delete:")
    entry_id = input("Entry ID: ")
    cursor_setting.execute(f"DELETE FROM {table_name} WHERE id = %s", (entry_id,))
    con_setting.commit()
    speak(f"History entry with ID {entry_id} deleted successfully.")










#----------------------------------------------------------------------------------------------

def view_profile():
    table_name = "users"
    cursor_setting.execute(f"SELECT * FROM {table_name} WHERE username = %s", (current_user,))
    user_data = cursor_setting.fetchone()

    if user_data:
        table = PrettyTable()
        table.field_names = ["Username", "Email", "Name", "Mobile Number", "Role"]
        table.add_row(user_data[:-1])  # Exclude the "Role" field from user_data
        print("Your Profile:")
        print(table)
    else:
        print("User not found. Please check your credentials.")

def update_profile():
    speak("What would you like to change?")
    print("1) Name\n2) Email\n3) Mobile Number\n4) Password\n5) Back to Main Menu")
    
    choice = listen()
    
    if any(keyword in choice.lower() for keyword in ["1", "name"]):
        new_name = input("Enter your new name: ")
        cursor_setting.execute(f"UPDATE users SET name = %s WHERE username = %s", (new_name, current_user))
        speak("Name updated successfully.")
    elif any(keyword in choice.lower() for keyword in ["2", "email"]):
        new_email = input("Enter your new email: ")
        cursor_setting.execute(f"SELECT * FROM users WHERE email_id = %s", (new_email,))
        existing_user = cursor_setting.fetchone()
        if existing_user:
            speak("Email already exists. Please choose a different email.")
        else:
            cursor_setting.execute(f"UPDATE users SET email_id = %s WHERE username = %s", (new_email, current_user))
            speak("Email updated successfully.")
    elif any(keyword in choice.lower() for keyword in ["3", "mobile"]):
        new_mobile = input("Enter your new mobile number: ")
        cursor_setting.execute(f"SELECT * FROM users WHERE mobile_no = %s", (new_mobile,))
        existing_user = cursor_setting.fetchone()
        if existing_user:
            speak("Mobile number already exists. Please choose a different number.")
        else:
            cursor_setting.execute(f"UPDATE users SET mobile_no = %s WHERE username = %s", (new_mobile, current_user))
            speak("Mobile number updated successfully.")
    elif any(keyword in choice.lower() for keyword in ["4", "password"]):
        new_password = input("Enter your new password: ")
        cursor_setting.execute(f"UPDATE users SET password = %s WHERE username = %s", (new_password, current_user))
        speak("Password updated successfully.")
    elif any(keyword in choice.lower() for keyword in ["5", "back"]):
        speak("Returning to Main Menu.")
    else:
        speak("Invalid choice. Please enter a valid option.")

def delete_account():
    speak("Are you sure you want to delete your account? (confirm/no): ")
    confirm = listen()
    
    if any(keyword in confirm.lower() for keyword in ["yes", "confirm"]):
        cursor_setting.execute("DELETE FROM users WHERE username = %s", (current_user,))
        con_setting.commit()
        speak("Account deleted successfully. Goodbye!")
        exit()
    else:
        speak("Account deletion canceled.")

def profile():
    speak("Profile Options:")
    print("1) View Profile\n2) Update Profile\n3) Delete Account\n4) Back to Main Menu")
    
    
    choice = listen()
    
    if any(keyword in choice.lower() for keyword in ["1", "view"]):
        view_profile()
    elif any(keyword in choice.lower() for keyword in ["2", "update"]):
        update_profile()
    elif any(keyword in choice.lower() for keyword in ["3", "delete"]):
        delete_account()
    elif any(keyword in choice.lower() for keyword in ["4", "back"]):
        speak("Returning to Main Menu.")
    else:
        speak("Invalid choice. Please enter a valid option.")

#------------------------------------------------------------------------------------------------

def view_all_user_history():
    print("Viewing All User History")

    # Get a list of all user tables in the database
    cursor_setting.execute("SHOW TABLES LIKE '%_history'")
    user_tables = [table[0] for table in cursor_setting.fetchall()]

    if not user_tables:
        print("No user history tables found.")
        return

    # Display user history from all user tables
    for table_name in user_tables:
        cursor_setting.execute(f'''
            SELECT * FROM {table_name}
        ''')
        user_history_data = cursor_setting.fetchall()

        if user_history_data:
            # Display user history in a tabular format using PrettyTable
            table = PrettyTable()
            table.field_names = ["ID", "User Input", "Friday Output", "Timestamp"]
            for history_entry in user_history_data:
                table.add_row([history_entry[0], history_entry[1], history_entry[2], history_entry[3]])
            print(f"\nUser History for {table_name}:")
            print(table)


