# Bash Loops

<!-- inPage TOC start -->

---
## Lab Highlights:
- [Lab Highlights:](#lab-highlights)
- [01. Using for loop to read items in a list](#01-using-for-loop-to-read-items-in-a-list)
- [02. Using for loop to read an array](#02-using-for-loop-to-read-an-array)
- [03. Using for loop to read a list of string values with spaces](#03-using-for-loop-to-read-a-list-of-string-values-with-spaces)
- [04. Using for loop in {START..END..INCREMENT} range](#04-using-for-loop-in-startendincrement-range)
- [05. Using for loop in {START..END..INCREMENT} range going backward](#05-using-for-loop-in-startendincrement-range-going-backward)
- [06. Using for loop with 3 parts and condition counter](#06-using-for-loop-with-3-parts-and-condition-counter)
- [07. Using for loop with 3 parts and multiple conditions and actions with comma](#07-using-for-loop-with-3-parts-and-multiple-conditions-and-actions-with-comma)
- [08. Using Infinite for loop](#08-using-infinite-for-loop)
- [09. Using for loop with conditional break and continue](#09-using-for-loop-with-conditional-break-and-continue)
- [10. Using for loop to read filenames by `globbing`](#10-using-for-loop-to-read-filenames-by-globbing)
- [11. Using for loop to read output from find command](#11-using-for-loop-to-read-output-from-find-command)
- [12. Using for loop to read filenames of a directory recursively](#12-using-for-loop-to-read-filenames-of-a-directory-recursively)
- [13. Using for loop to read filenames of a directory recursively with the condition](#13-using-for-loop-to-read-filenames-of-a-directory-recursively-with-the-condition)
- [14. Running the loop until the file exists](#14-running-the-loop-until-the-file-exists)
- [15. Using for loop based on the output of package list command](#15-using-for-loop-based-on-the-output-of-package-list-command)
- [16. Using for loop to read lines of a file](#16-using-for-loop-to-read-lines-of-a-file)
- [17. Using for loop to read lines of a file with conditional match](#17-using-for-loop-to-read-lines-of-a-file-with-conditional-match)
- [18. Using while loop with a counter](#18-using-while-loop-with-a-counter)
- [19. Using while loop with user input and quit when selecting exit from the menu](#19-using-while-loop-with-user-input-and-quit-when-selecting-exit-from-the-menu)
- [20. Combining while loops with `getopts`](#20-combining-while-loops-with-getopts)
- [21. Using until loop with a counter](#21-using-until-loop-with-a-counter)
- [22. Terminate until loop based on user input](#22-terminate-until-loop-based-on-user-input)
- [23. Using nested while loops](#23-using-nested-while-loops)
- [24. Using until loop to sleep/wait for background task started in script](#24-using-until-loop-to-sleepwait-for-background-task-started-in-script)
- [25. Using while loop to read pid from ps output that is not terminated](#25-using-while-loop-to-read-pid-from-ps-output-that-is-not-terminated)
- [26. Searching any string in a file using loop and exit](#26-searching-any-string-in-a-file-using-loop-and-exit)
- [27. Combine bash with curl to evaluate data from URL](#27-combine-bash-with-curl-to-evaluate-data-from-url)
- [28. Reading data from a port sent by netcat using while loop](#28-reading-data-from-a-port-sent-by-netcat-using-while-loop)
- [29. ping URL using a loop](#29-ping-url-using-a-loop)
- [30. Running top in batch mode using a loop and record output](#30-running-top-in-batch-mode-using-a-loop-and-record-output)

---

<!-- inPage TOC end -->

## 01. Using for loop to read items in a list
- The most simple use of `for` loop is to read a list of string or numeric data. 
- The list of numeric data is iterated by using for-in loop in the following example. 
- Here, four numbers will be read in the variable, `$n` in each step of the loop and printed. 
- Create a bash file with the following script and run from the terminal.

```sh
#!/bin/bash
# for-in loop to read a list of numbers
for n in 1 2 3 4 5
do
  # Print each number
  echo "The number is $n"
done
```

## 02. Using for loop to read an array
- Any array variable contains a list of data that can be iterated very easily by using for-in loop. 
- The following example shows the use of for-in loop to read an array of string data. 
- Here, each array value will fetch in the variable, `$language` and print a message based on language in each iteration.

```sh
#!/bin/bash
# Define an array of languages
languages=("Bash PERL Python PHP")

# Iterate through the array
for language in $languages
do
  # Check if the language is PHP
  if [ $language == 'PHP' ]
  then
    echo "$language is a web programming language"
  else
    echo "$language is a scripting language"
  fi
done
```

## 03. Using for loop to read a list of string values with spaces
- When a list of a string is read by for-in loop and any string value contains space then the values split into words based on space if the string value is not quoted with a single or double quotation. 
- The following example shows how a list of string values with space can be read by for-in loop. 
- Here, one value of the list contains space and it is printed with the space in the output.

```sh
#!/bin/bash
#for-in loop to read list of strings with space
for os in "Ubuntu [Space]" "Linux Mint" "Fedora" "CentOS"
do
  #Print each string
  echo "Operating System - $os"
done
```

## 04. Using for loop in {START..END..INCREMENT} range
- Another use of for-in loop is to read range array. 
- In the following example, a for loop is used to read a range of data from 10 to 30 which is incremented by 5 in each step. 
- Next, the script will print those numbers in the range that are divisible by 10.

```sh
#!/bin/bash
# Read a range using for loop
for num in {10..30..5}
do
  # Check the number is divisible by 10 or not
  if (( $num%10==0 ))
  then
    echo "$num is divisible by 10"
  fi
done
```

## 05. Using for loop in {START..END..INCREMENT} range going backward
- The range of data can be read backward by using for-in loop where the starting value of the range is greater than the ending value of the range. 
- In the following example, the range will start from 50 and end to 30. 
- The value of `$num` will be decremented by 10 in each step of the loop.
-  The script will print those numbers from the range that are divisible by 5 and 10.

```sh
#!/bin/bash
echo "The following numbers are divisible by 5 and 10"
# Read a range using for loop
for num in {50..30..10}
do
  # Check the number is divisible by 5 and 10 or not
  if (( $num%5==0 && $num%10==0 ))
  then
    echo -n "$num "
  fi
done
echo "Done"
```

## 06. Using for loop with 3 parts and condition counter
- Bash supports for loop with three parts like other standard programming languages. 
  - The `first part` contains initialization. 
  - The `second part `contains the termination condition.
  - The `third part` contains increment or decrement operation. 
- This loop is mainly used when the number of iteration is previously defined. 
- In the following example, for loop will iterate for 50 times and calculate the sum of 1 to 50. 
- The result of the summation will print as output.

```sh
#!/bin/bash
# Initialize the variable
sum=0
# Loop will iterate for 50 times
for (( n=1; n<=50; n++ ))
do
  # Add the sum value with the next value of n
  ((sum=$sum+$n))
done
# Print the result
echo "The sum of 1 to 50 is $sum"
```

## 07. Using for loop with 3 parts and multiple conditions and actions with comma
- For loop with three parts can be defined with multiple initializations, `termination` `conditions` and `actions`. 
- The following example shows the use of this type of loop.  
  - Here, `$x` and `$y` variables are initialized by `5` and `25`. 
  - The loop will continue until the value of `$x` is less than or equal to 20 and the value of `$y` is greater than `5`. 
  - The value of `$x` will increment by `5` and the value of `$y` will decrement by `5` in each iteration of the loop. 
- The current value of `$x` and `$y` in each step will print as output.

```sh
#!/bin/bash
# Loop will iterate based on two conditions
for (( x=5,y=25; x<=20 && y>5; x+=5,y-=5 ))
do
  echo "The current value of x=$x and y=$y"
done
```

## 08. Using Infinite for loop
- When any loop is defined without any termination condition then the loop works as an `infinite loop`. 
- The following example shows the use of infinite for loop that does not contain any initialization, termination and action parts. 
- This type of for loop is defined by double semicolon `(; ;)`. 
- The following script will continue the loop until the user types `quit` as input. 
- The script will print any number from 1 to 20 that will take as input otherwise it will print **The number is out of range**

```sh
#!/bin/bash
# Declare infinite loop
for (( ; ; ))
do
  # Take a input
  echo "Enter a number between 1 to 20"
  read n
  # Set the termination condition of the loop
  if [ $n == "quit" ]
  then
    echo "Program terminated"
    exit 0
  fi
  # Check the number range
  if (( $n < 1 || $n > 20 ))
  then
    echo "The number is out of range"
  else
    echo "The number is $n"
  fi
done
```

## 09. Using for loop with conditional break and continue
- `continue` statement is used to omit some part(s) of the loop based on any condition and `break` statement is used to terminate the loop based on any condition.  
- The following example shows the uses of these statements in a for loop. 
- Here, the loop is used to read a list of string data and each value in the list is stored in the variable, `$food`. 
  - When the value of `$food` is `Soup` then it will continue the loop without printing the value. 
  - When the value of `$food` is `Pasta` then it will terminate the loop. 
  - When `$food` contains any value other than `Soup` and `Pasta` then it will print the value. 
  
- So, the script will print two values from the list as output.

```sh
#!/bin/bash
# Declare a loop with a list
for food in Pizza Soup Burger Pasta Noodles
do
  # Set condition for continue
  if [ $food == 'Soup' ]
  then
    continue
    # Set condition for break
  elif [ $food == 'Pasta' ]
  then
    break
  else
    echo "$food is my favorite"
  fi
done

# Output:
# Here, two values are omitted from the list. 
#       `Soup` is not printed for the continue statement and 
#       `Pasta` is not printed for break statement.
```

## 10. Using for loop to read filenames by `globbing`
- Filenames or the particular content of a file can be searched by using `globbing`. 
- It uses different types of wildcard characters for matching any filename or searching content in the file. 
- All files with txt extension of the current location are searched printed by the following example. 
- When you will run the script then all matching filenames will be printed without newline as output.

```sh
#!/bin/bash
# Loop will search all text files and store each filename in $file
for file in "*.txt";
do
  # Print the filename
  echo $file;
done
```

## 11. Using for loop to read output from find command
- `find` command is used for different purposes in bash. 
- In the following example, `find` command is used to read all text filenames from the current location. 
- `-name` option to use for case-sensitive search. 
- So, the script will print those filenames of the current location that have the `.txt` extension with any name. 
- `IFS` variable is used to define the newline as field separator and print the value of `$file` in each line.

```sh
#!/bin/bash
# Set field separator
IFS=$'\n';
# Read the files of a directory
for file in $(find -name "*.txt"); do
  echo $file
done
# Unset field separator
unset IFS;
```

## 12. Using for loop to read filenames of a directory recursively
- `find` command can be used to read all files and sub-folders of a particular directory. 
- The following example shows the use of `find` command to read all filenames and directories under `mydir` directory. 
- `IFS` variable is used to print the value of `$filename` with `newline` like the previous example.

```sh
#!/bin/bash
# Set field separator
IFS=$'\n';
# Read the files of a directory
for filename in $(find "mydir")
do
  echo "$filename"
done
# Unset field separator
unset IFS;
```

## 13. Using for loop to read filenames of a directory recursively with the condition
- `for` loop with `find` command can be used to print some particular filenames of a directory based on any condition. 
- `find` command is used with a condition in the following example. It will search only text filenames of mydir directory.  
- Here, `-iname` option is used with `find` command for case insensitive search. 
- That means all files with the extension `txt` or `TXT` will be matched and printed as output.  
- Here, IFS variable is used to print the value of `$filename` with `newline` like the previous example.

```sh
#!/bin/bash
# Set field separator
IFS=$'\n';

# Read all text files of a directory
for filename in $(find mydir -iname '*.txt'); do
  echo "$filename"
done
# Unset field separator
unset IFS;
```

## 14. Running the loop until the file exists
Any filename exists or not is checked in the following example by using infinite for loop. In this script, a filename will take as input in each iteration of the loop and test the filename is exists in the current location or not. If the filename exists then the script will print “File exists” and continue the loop otherwise it will terminate the loop by printing the message, `File does not exist`.

```sh
#!/bin/bash
# Define infinite loop
for(( ; ; ))
do

  # Input a filename
  echo "Enter a file name"
  read file

  # Check the file exists or not
  if [ ! -f $file ]
  then

    echo "Filename does not exist"
    exit 0
  else
    echo "File exists"
  fi
done
```

## 15. Using for loop based on the output of package list command
- The information about the installed packages in the system can be retrieved by the command `apt list – -installed`. 
- `for` loop is used in the following example to read the installed package information from the package list command and print each package information in each line. 
- IFS variable is used here to print the value of `$line` with `newline` like the previous example.

```sh
# Set field separator
IFS=$'\n';
# Read file line by line
for line in $(apt list --installed)
do
  echo "$line"
done

# Unset field separator
unset IFS;
```

## 16. Using for loop to read lines of a file
- There are many ways to read a file in bash. 
- `cat` command is used in the following example to read the file, `temp.txt`. 
- Each line of the file will store in the variable, `$line` and print the line in each iteration of for loop. 
- IFS variable is used here to print the value of `$line` with `newline` like the previous example.

```sh
#!/bin/bash
# Set field separator
IFS=$'\n';

# Read file line by line
for line in $(cat temp.txt)
do
  echo "$line"
done
# Unset field separator
unset IFS;
```

## 17. Using for loop to read lines of a file with conditional match
- If you want to print particular lines from a file only then you have to add inside the loop that is used to read the file. 
- The following example prints the formatted output of each line of `weekday.txt` file based on a condition. 
- If any line of the file contains the value, `Sunday` then it will print `holiday` message otherwise it will print `working day` message.

```sh
# Read the file
for line in $(cat weekday.txt)
do

  #Compare the value with a string data
  if [ $line == "Sunday" ]
  then
    echo "$line is a holiday"
  else
    echo "$line is a working day"
  fi
done
```

## 18. Using while loop with a counter
- `$counter` variable is used any loop to control the iteration of the loop. 
- The following example shows the use of while loop with the counter. 
- Here, `$counter` is initialized to 1 and while loop will iterate `5` times and print the value of `$counter` in each iteration.  
- `$counter` is incremented by 1 in each step to reach the termination condition of the loop.

```sh
#!/bin/bash
# Initialize counter
counter=1

# Iterate the loop for 5 times
while [ $counter -le 5 ]
do
  echo "Counter value = $counter"
  ((counter++))
done
```

## 19. Using while loop with user input and quit when selecting exit from the menu
- `while` loop is used in the following example to display a menu of 5 options. 
- The first four options are used to perform four arithmetic operations based on the user's input and the last option is used to quit from the script.  
- The menu will appear after providing two numbers as input. 
  - If the user selects `1` then the input numbers will be added. 
  - If the user selects `2` then the second input number will be subtracted from the first input number.  
  - If the user selects `3` then the input numbers will be multiplied.
  - if the user selects `4` then the first input number will be divided by the second input number.

```sh
#!/bin/bash
# Take two numbers
echo "Enter a number"
read n1
echo "Enter a number"
read n2

# Declare an infinite loop
while true
do

  # Display the menu
  echo "1. Addition"
  echo "2. Subtraction"
  echo "3. Multiplication"
  echo "4. Division"
  echo "5. Exit"
  echo -n "Select any number from [1-5]:"
  read input

  # Perform the operation based on the selected value
  if [[ "$input" -eq "1" ]]
  then
    ((result=n1+n2))
  elif [[ "$input" -eq "2" ]]
  then
    ((result=n1-n2))
  elif [[ "$input" -eq "3" ]]
  then
    ((result=$n1*$n2))
  elif [[ "$input" -eq "4" ]]
  then
    ((result=$n1/$n2))
  elif [[ "$input" -eq "5" ]]
  then
    exit 0
  else
    echo "Invalid input"
  fi
  echo "The result is $result"
done
```

## 20. Combining while loops with `getopts`
- `getopts` is a built-in function of bash that is used to read arguments and options in the bash script. 
- The following example shows the use of getopts function that is used in a while loop. 
- Here, three option values are used with getopts. 
- These are `a`, `r`  and `c`. 
- Three different messages will be printed for these options.

```sh
#!/bin/bash
 
# Read the option and store in a variable
while getopts "arc" option; do
  # Check the option value
  case ${option} in
  a ) #option a
    echo "Process is aborted"
  ;;
  r ) #option r
    echo "Process is restarted"
  ;;
  c ) #option c
    echo "Process is continuing"
  ;;
  \? ) #invalid option
    echo "Use: [-a] or [-r] or [-c]"
  ;;
  esac
done
```

## 21. Using until loop with a counter
- Until loop can be used with a counter like while loop that is shown before. 
- The following example shows the use of until loop with a counter. 
- Here, `$counter` variable is used to control the iteration of the loop that is initialized to `1`. 
- The until loop will continue until the value of `$counter` to `5`. 
- So, the loop will iterate for `6` times and print the value `$counter` in each step. 
- `$counter` will be decrement by `1` in each step to reach the termination condition of the loop.

```sh
#!/bin/bash
# Initialize the counter
counter=10

# Iterate the loop for 6 times
until [ $counter -lt 5 ]
do
  echo "The current value of counter = $counter"
  ((counter--))
done
```

## 22. Terminate until loop based on user input
- Any loop terminates based on a particular condition. How until loop can be terminated based on user input, is shown in the following example.  
- According to the termination condition, the loop will terminate when the value of `$number` is greater than `50`. 
- The value of `$number` is not incremented inside the loop. 
- So., the loop will continue to take input from the user until a number of more than `50` is taken as input.

```sh
#!/bin/bash
# Initialize  number
number=0
# Set the pattern for numeric data
pattern='^[0-9]+$'
# Set the termination condition
until [ $number -gt 50 ]
do
  echo -n "Enter a number : "
  read number
  # Check the input value is number or not
  if ! [[ $number =~ $pattern ]]
  then
    echo "error: Not a number"
    number=0
  else
    echo "You have entered $number"
  fi
done
```

## 23. Using nested while loops
- When a loop is declared inside another loop then it is called an infinite loop. 
- The following example shows the use of nested while loop. 
- Here, the first while loop will iterate for 2 times and the second while loop inside the first loop will iterate for three times. 
- The total iteration of the loops are 2×3=6 times. 
- `$i` and `$j` variables are used to control the iteration of these loops and the values of these variables in each step are printed as output.

```sh
#!/bin/bash
 
# Initialize i and j
i=1
j=1
# Set termination condition for i
while [ $i -le 2 ]
do
  # Set termination condition for j
  while [ $j -le 3 ]
  do
    # Print the current value of i and j
    printf "i=%d, j=%d\n" $i $j
    ((j++))
  done
  j=1
  ((i++))
done
```

## 24. Using until loop to sleep/wait for background task started in script
- Any process can be run in the background by using `&` symbol. 
- How a process can be run in the background using until loop and terminate the loop based on the time specified in sleep command is shown in this example.  
- Here, `$cnt` variable is used to terminate the loop.  
- The loop will start the background process and write the output in a text file named `output.txt` for `1 second`. 
- After that, the termination condition of the loop will check and it will return false. 
- Next, the script will print a message, `Sleeping…` and exit from the script after 3 seconds.

```sh
#!/bin/bash
# Initialize counter
cnt=1
# Set termination condition
until [ $cnt -ge 1000 ]
do
  echo "Background process is running";
  # Wait for 1 second
  sleep 1;
  ((cnt++))
done > output.txt &
# Wait for 3 seconds
echo "Sleeping..."
sleep 3
```

## 25. Using while loop to read pid from ps output that is not terminated
- `ps` command is used to get information about all running processes of the system. 
- It provides detail information on any running process such as user id, PID, cpu usage, memory usage, etc. 
- The following example shows how a while loop can be used to read the running process information related to `apache`. 
- Here, IFS variable is used to print the PID of each process with a newline. 
- Next, it will wait for the user to press any key to exit from the script.

```sh
#!/bin/bash
# Set field separator
IFS=' '
while [ true ]
do
  # Retrieve all running process id of apache
  pid=`ps -ef | grep "apache" | awk ' {print $2 " process is running ..." }'`
  echo $pid
  # Wait for 1 second
  sleep 1
  # Press any key to terminate the loop
  echo "Press any key to terminate"
  if read -r -N 1 ; then
    break
  fi
done
# Unset field separator
unset IFS
```

## 26. Searching any string in a file using loop and exit
- Create a file named `month.txt` with the following content to test the bash script given below.
- `while` loop is used in the following example to read `month.txt` file line by line. 
- If any line contains the value, `June` then it will print `Enjoy summer vacation` and terminate from the script otherwise it will print the value of `$line`.
- Here, `June` exists in the file `month.txt` and it terminates the loop. So, month names after `June` line will not read by the loop.

```sh
#!/bin/bash

# Set the filename to read
filename="month.txt"

# month.txt
cat << EOF >> $filename
January
February
March
April
May
June
July
August
September
October
November
December
EOF

# Read file line by line
while IFS= read -r line
do
  # Check the value of line is equal to June
  # Terminate the program if the condition is true
  if [[ "$line" == "June" ]];
  then
    echo "Enjoy Summer vacation"
    exit 0
  else
    echo $line
  fi
done < $filename
```

## 27. Combine bash with curl to evaluate data from URL
- Data can be transferred to or from any network server in bash by using `curl` command with any supported protocol like HTTP, FTP, TELNET, etc.
- It is a command-line tool. How `curl` command can be used to evaluate data from URL using for loop is shown in the following example. 
- Here, for loop will read a list of url and pass each URL value in the curl and print the data received from the URL.

```sh
#!/bin/bash
# Read each URL from the list
for url in "yahoo.com" "youtube.com"
do

  # Print HTTP response code for each URL
  echo $url; curl -v -m 5 -s $1 "$url" | grep HTTP/1.1;
done
```

## 28. Reading data from a port sent by netcat using while loop
- `netcat` command is used to read and write data over the network using tcp or udp protocol. 
- `nc` command is used in bash to run `netcat` command. 
- The following example shows the use of `nc` command in while loop.  
- Here, the script will try to connect with the port 1234 using nc command and it will print a message in the other terminal if it can connect. 
- You have to open another terminal window or tab to run the command, `nc localhost 1234` to make a connection.  
- After establishing the connection, any message can be transferred from one terminal to another terminal.

```sh
#!/bin/bash
echo "Listening on port 1234 ..."
# Read the message passed by netcat at port 1234
while read text
do
  # Terminate the loop if the received message is "quit"
  if [ "$text" == 'quit' ]; then
    echo "Bye"
    break
  else
    echo "$text"
  fi
# Print message when the port is connected
done < <((printf "Welcome.\r\nType some message :") | nc -l 1234)
```

- Next, open another terminal and run the following command to communicate with the first terminal.

```sh
$ nc localhost 1234

# It will show a welcome message in the second terminal. 
# If the user types something in the second terminal then it will be displayed in the first terminal. 
# When the user will type `quit` in the second terminal then the script will terminate by displaying a message, `Bye` in the first terminal.
```

## 29. ping URL using a loop
- You can find out any website is live or not by executing `ping` command with the URL of the site. 
- `ping` command is used with `google.com` in the following example to check the Internet connection is working or not. 
- While loop will iterate 5 times in the script and try to ping google.com. 
- If the server responds then it will print “The Internet is working” and terminate the loop. 
- If the loop iterates 5 times and does not get any server response then it will print “No Internet connection”.

```sh
#!/bin/bash
# Set the counter
count=5
while [[ $count -ne 0 ]]
do

  # Try to ping google.com
  ping -c 1 google.com
  c=$?

  # Check the status code
  if [[ $c -eq 0 ]]
  then
    echo "The Internet is working"
  exit 0
  fi
  # Decrement the counter
  ((count--))
done
echo "No Internet connection"
```

## 30. Running top in batch mode using a loop and record output
- `top` command is a Linux administrative tool that is used to examine the usage of system resources, manage different tasks and monitor running processes. 
- How you can run `top` command in batch mode using for loop and store the records in a text file is shown in the following example. 
- Here, `-b` option is used to start the `top` command in batch mode and `-p` option is used to set the process id that you want to monitor. 
- The output of the `top` command will be stored in `output.txt` file.

```sh
#!/bin/bash
# Loop will iterate for 5 times and execute top command
for ((i=0; i<5; i++))
do
  top -b -p 2875 -n1 | tail -1 >> output.txt
done

# Run the following command to view the script output.
cat output.txt
```
