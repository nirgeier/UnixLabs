# Basic Bash scripting

<!-- inPage TOC start -->

---
## Lab Highlights:
- [Lab Highlights:](#lab-highlights)
- [01. echo](#01-echo)
- [02. Receive Input from User](#02-receive-input-from-user)
- [03. The If Statement](#03-the-if-statement)
- [04. Using the AND Operator](#04-using-the-and-operator)
- [05. Using the OR Operator](#05-using-the-or-operator)
- [06. Switch statement {switch,case,esac}](#06-switch-statement-switchcaseesac)
- [07. Command Line Arguments](#07-command-line-arguments)
- [08. #!/bin/bash](#08-binbash)
- [09. Slicing Strings](#09-slicing-strings)
- [10. Extracting Substrings Using Cut](#10-extracting-substrings-using-cut)
- [11. Test File Existence](#11-test-file-existence)

---

## 01. echo

* This script demonstrates the basic use of the `echo` command in Bash scripting.
* The `echo` command is used to output text to the standard output (usually the terminal).
* Here, we're simply printing the string "Hello World" to the screen.
      ```sh
      #!/bin/bash
  
      # Prints the string "Hello World" to the standard output
      echo "Hello World"
      ```

    **What we're doing:**   

      * Displaying a simple message to the user.  

    **How the script does it:**   

      * The `echo` command takes the string argument and outputs it followed by a newline. 
      * The shebang `#!/bin/bash` tells the system to interpret this script with Bash.

---

## 02. Receive Input from User

* This script shows how to receive input from the user using the `read` command.
* It prompts the user to enter something and then echoes back what they entered.
      ```sh
      #!/bin/bash
  
      echo -n "Enter Something:"
      read something
  
      echo "You Entered: $something"
      ```
    **What we're doing:**   
      * Interacting with the user by taking input and displaying it back.  

    **How the script does it:**   

      * The `echo -n` prints the prompt without a newline, so the cursor stays on the same line.
      * The `read` command waits for user input and stores it in the variable `something`.
      * Then, `echo` displays the variable's value using `$something`.


---

## 03. The If Statement

* This script introduces conditional logic using the `if` statement.
* It checks if a number entered by the user is greater than 10 and prints a message accordingly.

      ```sh
      #!/bin/bash
  
      echo -n "Enter a number: "
      read num
  
      if [[ $num -gt 10 ]]
      then
        echo "Number is greater than 10."
      fi
      ```

    **What we're doing:**   

      * Making a decision based on user input.  

    **How the script does it:**   

      * The `if` statement evaluates the condition `[[ $num -gt 10 ]]`, which uses double brackets for arithmetic comparison.
      * `-gt` means "greater than". 
      * If true, it executes the `then` block.
      * The `fi` closes the if statement.

---

## 04. Using the AND Operator

* This script demonstrates the use of the logical AND operator (`&&`) in an if statement.
* It checks if a number is less than 10 AND even, then classifies it as even or odd.

      ```sh
      #!/bin/bash
  
      echo -n "Enter Number:"
      read num
  
      if [[ ( $num -lt 10 ) && ( $num%2 -eq 0 ) ]]; 
      then
        echo "Even Number"
      else
        echo "Odd Number"
      fi
      ```

    **What we're doing:**   

      * Checking multiple conditions simultaneously.  

    **How the script does it:**   

      * The condition uses `&&` to combine two tests: `$num -lt 10` (less than 10) and `$num%2 -eq 0` (even).
      * The `%` operator is used to check for evenness (remainder 0 when divided by 2).
      * The `-lt` operator checks if the number is less than 10.
      * The `-eq` operator checks for equality.
      * If both are true, it prints "Even Number"; otherwise, "Odd Number".
      * Note: The logic seems incorrect as it only checks evenness if less than 10, but the else covers all other cases.


---

## 05. Using the OR Operator

* This script is similar to the previous one but demonstrates the OR operator (`||`).
* It checks if a number is less than 10 OR even.

      ```sh
      #!/bin/bash
  
      echo -n "Enter Number:"
      read num
  
      if [[ ( $num -lt 10 ) || ( $num%2 -eq 0 ) ]]; 
      then
        echo "Number is less than 10 OR Even"
      else
        echo "Number is greater than 10 AND Odd"
      fi
      ```

    **What we're doing:**   

      * Checking if at least one of the conditions is true.  

    **How the script does it:**   

      * The condition uses `||` to combine two tests.
      * If either `$num -lt 10` is true OR `$num%2 -eq 0` is true, it executes the `then` block.


---

## 06. Switch statement {switch,case,esac}

* This script uses a `case` statement (switch-case equivalent in Bash) to match the input number against specific values and print corresponding messages.

      ```sh
      #!/bin/bash
  
      echo -n "Enter a number: "
      read num
  
      case $num in
        100)
          echo "Hundred!!" ;;
        200)
          echo "Double Hundred!!" ;;
        *)
          echo "Neither 100 nor 200" ;;
      esac
      ```

    **What we're doing:**   

      * Handling multiple possible values for a variable with specific actions.  

    **How the script does it:**   

      * The `case` statement matches `$num` against patterns: `100`, `200`, or `*` (default).
      * Each match ends with `;;`.
      * The `esac` closes the case block.
      * The `100` and `200` cases print specific messages, while the `*` case handles all other inputs.
      * The user is prompted to enter a number, which is then evaluated by the case statement.

---

## 07. Command Line Arguments

* This script demonstrates how to access command-line arguments passed to the script.
* Run the script like `./script.sh arg1 arg2`.
* It prints the total number of arguments and the first two arguments.
* The special variable `$#` holds the number of arguments, while `$1`, `$2`, etc., access individual arguments.  
    ```sh
    #!/bin/bash
    echo "Total arguments : $#"
    echo "First Argument = $1"
    echo "Second Argument = $2"
    ```

    **What we're doing:**   

      * Displaying information about arguments provided when running the script.  

    **How the script does it:**   

      * `$#` gives the number of arguments.
      * `$1`, `$2`, etc., access the first, second, etc., arguments.
      * When run as `./script.sh arg1 arg2`, it outputs:
        ```bash 
        Total arguments : 2
        First Argument = arg1
        Second Argument = arg2
        ```
---

## 08. #!/bin/bash

* This script shows how to parse named command-line arguments (like X=5 Y=10) and perform operations on them.

      ```sh
      #!/bin/bash
  
      for arg in "$@"
      do
        # This splits each argument on '=' and assigns values accordingly
        index=$(echo $arg | cut -f1 -d=)

        # Then we extract the value part
        val=$(echo $arg | cut -f2 -d=)

        # Look at the index and assign to variables
        case $index in
          X) 
            x=$val;;
          Y) 
            y=$val;;
          *)
        esac
      done
      
      # Sum the values of X and Y
      ((result=x+y))

      # Print the result
      echo "X+Y=$result"
      ```

    **What we're doing:**   

      * Parsing named arguments and calculating their sum.  

    **How the script does it:**   

      * Loops through all arguments (`$@`), 
        * splits each on `=` using `cut`, 
        * assigns values to variables `x` and `y` based on the index, 
        * then performs arithmetic addition with `((result=x+y))`.
      * Run as `./script.sh X=5 Y=10`.


---

## 09. Slicing Strings

* This script demonstrates string slicing in Bash, extracting a substring from a given string.

      ```sh
      #!/bin/bash

      Str="Learn Bash Commands from UbuntuPit"
      
      # Substring from position 0 to 20 (starting at 0 not 1)
      subStr=${Str:0:20}
      echo $subStr
      ```

    **What we're doing:**   

      * Extracting a portion of a string.  

    **How the script does it:**   

      * Uses parameter expansion `${Str:0:20}` to get 20 characters starting from position 0.
      * The result is "Learn Bash Commands".
      * `Str:` indicates the starting index, and `20` is the length of the substring.
      * The output is printed using `echo`.
      * Note: String indexing starts at 0 in Bash (Not from 1 !!!).
  
---

## 10. Extracting Substrings Using Cut

* This script shows how to extract substrings using the `cut` command, which is useful for parsing delimited text.

      ```sh
      #!/bin/bash
      Str="Learn Bash Commands from UbuntuPit"
      
      # Previous example was: subStr=${Str:0:20}

      # Now using cut to get first three words (words are space delimited)
      # The -d ' ' specifies space as the delimiter
      # The -f 1-3 specifies fields 1 to 3
      subStr=$(echo $Str| cut -d ' ' -f 1-3)
      echo $subStr
      ```

    **What we're doing:**   

      * Extracting specific fields from a string based on delimiters.  

    **How the script does it:**   

      * Pipes the string to `cut`, which uses space (`-d ' '`) as delimiter and selects fields 1 through 3 (`-f 1-3`).
      * The output is "Learn Bash Commands".
      * Run as `./script.sh`.
      ```bash
      # Printing the output
      Learn Bash Commands
      ```

---

## 11. Test File Existence

* This script checks if a file exists using conditional statements and file test operators.
* It takes a filename as a command-line argument and verifies its existence.
* The `-f` operator checks if the file exists and is a regular file.

      ```sh
      #!/bin/bash
      filename=$1
      if [ -f "$filename" ]; then
        echo "File exists"
      else
        echo "File does not exist"
      fi
      ```

    **What we're doing:**   

      * Verifying the existence of a file provided as an argument.  

    **How the script does it:**   

      * Uses the `-f` test operator in an `if` statement to check if the file exists and is a regular file.
      * `$1` is the first command-line argument.
      * Run as `./script.sh myfile.txt`.
      ```bash
      # If myfile.txt exists:
      File exists 
      # If myfile.txt does not exist:
      File does not exist
      ```
---

## 12. Working with Variables 

* This script introduces the concept of variables and demonstrates input from the user.
* It captures the user's name and the current date, then displays a personalized greeting.
* It uses command substitution to get the current date.
* Variables are accessed by prefixing their names with a dollar sign (`$`).
* `$(...)` is used for command substitution to assign the output of a command to a variable.

      ```sh
      #!/bin/bash

      # Define a variable named 'TODAY' and assign it the output of the 'date' command.
      # $(...) is a command substitution, which executes the command inside and
      # uses its output as the value for the variable.
      TODAY=$(date +"%A, %B %d, %Y")

      # Prompt the user for their name.
      echo "Hello! What is your name?"

      # 'read' is used to capture user input and store it in the variable 'USER_NAME'.
      read USER_NAME

      # Use the variables in the output.
      # To access a variable's value, you prefix its name with a dollar sign ($).
      echo "Welcome, $USER_NAME!"
      echo "Today is $TODAY."
      echo "Have a great day!"
      ```

    **What we're doing:**

      * Introducing variables, user input, and command substitution.

          | Format Specifier | Description                                     | Example Output (for the current date) |
          |:-----------------|:------------------------------------------------|:--------------------------------------|
          | %A               | Full weekday name.                              | Saturday                              |
          | ","              | A literal comma and a space.                    | ", "                                  |
          | %B               | Full month name.                                | December                              |
          | %d               | Day of the month as a two-digit number (01-31). | 13                                    |
          | ","              | A literal comma and a space.                    | ", "                                  |
          | %Y               | Full year (four digits).                        | 2025                                  |

    **How the script does it:**

      * **Variables**: Storing data (e.g., `USER_NAME`, `TODAY`).
      * **Variable Access**: Retrieving the value using the dollar sign (`$VARIABLE_NAME`).
      * **Command Substitution (`$(...)`)**: Running a command and using its result as data.
      * **read**: Capturing input typed by the user.
      * **echo**: Displaying messages that include variable values.
  
---

## 13. File ReaRename (Loop)

* This script introduces the `for` loop, which is used to iterate over a list of items and perform an action on each one.
* The script renames multiple files by appending "_processed" to their names.
* It checks if each file exists before renaming it to avoid errors.
* Positional parameters (`$@`) are used to access all arguments passed to the script.
* String manipulation techniques are used to construct the new filenames.
* The `mv` command is used to rename the files.
* Run the script like `./script.sh file1.txt file2.txt`.
* The script processes each file provided as an argument.
  
      ```sh
      #!/bin/bash

      # Check if any arguments were provided.
      # This ensures the script is used correctly.
      # Its assumes the user will provide filenames as arguments.
      # Its a check to prevent errors if no files are given.
      if [ "$#" -eq 0 ]; then
          echo "Usage: $0 <file1> <file2> ..."
          echo "Provide one or more filenames to add '_processed' to their name."
          exit 1
      fi

      # The 'for' loop iterates over all positional arguments ($@ means all arguments).
      for FILENAME in "$@"; do
          # Check if the file actually exists before trying to rename it.
          if [ -f "$FILENAME" ]; then
              NEW_FILENAME="${FILENAME%.*}_processed.${FILENAME##*.}"
              
              # 'mv' command is used to move/rename files.
              mv "$FILENAME" "$NEW_FILENAME"
              
              echo "Renamed: '$FILENAME' -> '$NEW_FILENAME'"
          else
              echo "Skipping: File '$FILENAME' not found."
          fi
      done

      echo "Batch renaming complete."
      ```

    **What we're doing:**

      * Iterating over a list of files and renaming them.

    **How the script does it:**

      * **for loop**: Repeating a set of commands for every item in a list.
      * **Positional Parameters (`$@`)**: Represents all arguments passed to the script.
      * **File Test Operator (`-f`)**: Checks if a path exists and is a regular file.
      * **String Manipulation (Parameter Expansion)**:
        * `${FILENAME%.*}`: Removes the shortest match of `.*` (the extension) from the end.
        * `${FILENAME##*.}`: Removes the longest match of `*` (the filename/path) from the beginning, leaving the extension.
      * **mv**: The command used for moving/renaming files.