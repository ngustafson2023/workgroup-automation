# workgroup-automation
##Assign the brothers of Chi Phi Fraternity to workgroups for cleaning the chapter house.

To run the script, enter `python3 main.py` in Terminal. The assignments will be printed in the console, where you can confirm, regenerate, swap two assignments, or manually edit an assignment. Once confirmed, the assignments will be saved to a Excel spreadsheet in `./Sheets/`.

`main.py`: specifies the classes participating in the round of workgroups (can comment out a class to remove them from consideration if needed; e.g. `#Brothers.freshmen`)

`brothers.py`: specifies the brothers particpating in each class (can comment out specific brothers to remove them from consideration if needed; e.g. `#Brother('Mattew Nay', 3, 3)`)

`workgroups.py`: specifies the workgroups to be completed (can comment out specific workgroups to remove them from consideration if needed; e.g. `#Workgroup('Library', 1, 1)`)

`assign.py`: contains the algorithm for assigning brothers to workgroups
