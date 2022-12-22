from rich.console import Console
from database import *
import os
import subprocess

console = Console()
end = " \n-> "

#Set up
def getting_started():
    #ask for habits
    input = console.input("[magenta][i]What habits do you want to keep track of? Separate with commas!" + end)
    
    habits = input.split(", ")

    #verify habits are correct
    console.print(habits)
    verify = console.input("[magenta][i]Are these the habits you want to keep track of? (y/n)" + end)
    verify = check(verify)

    if(verify.lower() == "n" or verify.lower() == "no"):
        getting_started()
    else:
        #reformat for database
        habits = [(x,) for x in habits]

        #ask about notifications
        notify = console.input("[magenta][i]Great! Lets get started. Do you wanted to be notified? (y/n)" + end)
        notify = check(notify)

        if(notify.lower() == "n" or notify.lower() == "no"):
            notify = 0
        else:
            notify = 1

        return habits, notify

#Checking on input
def check(verify):
    yorno = "[magenta][i]Please input [/]'n'[i] for no or [/]'y'[i] for yes. \n-> "
    while(verify.lower() != 'y' and verify.lower() != 'yes' and verify.lower() != 'n' and verify.lower() != 'no'):
        verify = console.input(yorno)
    return verify

def routine():
    if(get_notif()):
        notify()

    habits = get_habits()

    console.print("[green][b]Did you do the following? (y/n)")
    
    streak = True

    for habit in habits:
        res = console.input(f"[magenta][i]{habit}{end}")
        res = check(res)

        if(res.lower() == "yes" or res.lower() == "y"):
            console.print("[green][b]Good job! Super proud!")

        else:
            streak = False
            console.print("[green][b]Dang :( Next time, bud!")

    if(streak == False):
        prev_diff = (get_date() - date.today()).days
        restart = update_restart()
        console.print(f"[green][b]You broke your streak of {prev_diff} days. You have restarted {restart} times. :(")

        today = date.today()
        update_date(today)

    cur_diff = (get_date() - date.today()).days
    console.print(f"[green][b]Your current streak is {cur_diff} days <3 <3")

#notifies - works only on mac i think 
def notify():
    CMD = '''
    on run argv
    display notification (item 2 of argv) with title (item 1 of argv)
    end run
    '''
    
    title = "Habit Tracker <3"
    text = "hey! remember to update your habit tracker for today so you don't lose your streak!"

    subprocess.call(['osascript', '-e', CMD, title, text])

#final call
def controller():
    if not verify_table():
        habits, notify = getting_started()

        try:
            create_table()
            insert_habits(habits)
            insert_notif(notify)

            today = date.today()
            insert_date(today)

        except Exception as e:
            os.remove("database.db")
            console.print("[magenta][i]Something went wrong! Here's the error message:")
            print(e)

    
    routine()

if __name__ == "__main__":
    controller()