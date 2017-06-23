import time
import sys

run = input("Start? > ")
mins = 0
# Only run if the user types in "start"
if run == "start":
    # Loop until we reach 20 minutes running
    while mins != 2:
        print(">>>>>>>>>>>>>>>>>>>>> %f", mins)
        # Sleep for a minute
        time.sleep(10)
        # Increment the minute total
        mins += 1
    # Bring up the dialog box here
    print('wake up')