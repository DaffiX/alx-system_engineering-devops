#Processes and signals
___________________________________________________________________________________________

How to use Process Identification Numbers and Signals in Linux Bellow are the commands that I used: ps, pgrep, pkill, pkill, exit, and trap.
Tasks 📃
0. What is my PID

0-what-is-my-pid: Bash script that displays its own PID.
1. List your processes

1-list_your_processes: Bash script that displays a list of currently running processes.
Shows all processes for all users, including those not featuring a TTY.
Processes are displayed in a user-oriented hierarchy.
2. Show your Bash PID

2-show_your_bash_pid: Bash script that displays lines containing the bash keyword based on the script defined in 1-list_your_processes.
3. Show your Bash PID made easy

3-show_your_bash_pid_made_easy: Bash script that displays the PID along with the process name of processes who name contains the word bash.
4. To infinity and beyond

4-to_infinity_and_beyond: Bash script that displays To infinity and beyond indefinitely with a sleep 2 in between each iteration.
5. Kill me now

5-kill_me_now: Bash script that kills the 4-to_infinity_and_beyond process using kill.
6. Kill me now made easy

6-kill_me_now_made_easy: Bash script that kills the 4-to_infinity_and_beyond process using pkill.
7. Highlander

7-highlander: Bash script that displays To infinity and beyond indefinitely with a sleep 2 in between each iteration.
Displays I am invincible!!! upon receiving a SIGTERM signal.
8. Beheaded process

8-beheaded_process: Bash script that kills the process 7-highlander.
