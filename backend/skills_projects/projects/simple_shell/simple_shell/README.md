so in here i'll keep the most important notes i came too from searching on how to build a shell
first of all..
shells are the outer layer of operating system , its true idea " responsibility " is taking orders " commands "
from a user and asking the operating system " kernel " to do it , returning the output to the user 
so its kinda of interface between the user and the kernel " os " , we can specify these steps on 4 fundmentals
1- READ - its always the first thing shell do , the shell start with reading the input of user translating it first
2- EVALUATE - its really a tricky step , the shell start evaluating the command , all the inputs shall go into a process
considering multiple steps , if its a specified command , it shall execute it
if its not a specified command , it shall send an error message
if its a command with unknown flags , comments it shall process it trying to figure where the problem is , sending 
the right specified error message to the user so he can edit the command or whatever, just like an extra help for him
3-PRINT - so to be accurate the past step dont send the input to user , yet it process it , then after finishing the
process the shell shall print all the " BUFFER " output as its third step
4-LOOP - repeat , the shell shall keep executing till the EXIt is written as input , so it keep looping in the past 3 steps
one time over another in infinite loop till it takes exit as input 
these was the 4 basic steps for a SHELL , there are lot of details among every part of them , i'll explain them more now
===========================================================================================================================
so basically the shell is an executable program that running in terminal " the environment " without stopping
shell is the most close part of the operating system to the user , kernel is far away from our hands to deal with
shell interact with kernel with system calls " they're functions that kernel understands " every library function
is built on system calls , they're the base of programming , they're the way into input output devices " CPU , RAM ,.. "
so shell is delivering these system calls into the kernel to execute , getting back the wanted output
but its not right for normal users to use system calls , so they implemented a large library of functions to use
these functions with their flags are built in executable files inside the system files , so in bash "LINUX" for example
there is a bash file with lot of files around that holds all the informations about the whole bash scripts in binary
and the shell runs the needed file to execute specific command whenever you call it, thats a quick turtorial upon it
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
you need to learn about system calls to build your own shell , making executable file that execute more files while he is working
this can be handled with execve , fork , wait funcs
you need also to handle the input , so you need to take the input as argument , start to cutting it into pieces and search inside
for the flags , commands , comments , strings , whatever you want to implement
so this  can be done with strtok , getline funcs with ARGS ofcourse the famous argc, argv will help recieving different inputs
----------------------------------------------------------------------------------------------------------------------------
with an infinite loop you can make the shell working till argv[0] = exit
with some extra CONDITIONING you can make the shell exit with arguments like status - Exit with 98 -
with an simple printf you can make the shell display the current env , displaying "$" or even displaying a ^_^: in the starty
you can handle the "EXIT" with splitting " tokenize " the arguments provided and comparing it with exit , status , every args to handle
you can also handle the path thing by providing Av1 as the path to search within , like if the system files are all in the 
bin/bash , provide it as the argv[0] so it'll seek for it and the argv[1] will be the command so if the user written ls it will be 
executed
with this you can also handle all the args provided by the same way , all you need is to provide the conditions needed for this
******************************************************************************************************************************
you can do your own string manipulation for more extra controlling , you can manipulate data with linked list for sure
