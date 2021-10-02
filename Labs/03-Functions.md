# Bash Functions

<!-- inPage TOC start -->

---
## Lab Highlights:
- [Lab Highlights:](#lab-highlights)
- [01. Basic Function Structure](#01-basic-function-structure)
- [02. Passing Arguments to Functions](#02-passing-arguments-to-functions)
- [03. Returning Values from Functions](#03-returning-values-from-functions)
- [04. Local vs Global Variables](#04-local-vs-global-variables)
- [05. Functions with Checks (If/Else)](#05-functions-with-checks-ifelse)
- [06. Functions with Loops](#06-functions-with-loops)
- [07. Nested Functions](#07-nested-functions)

---

## Prefix: Understanding Bash Functions

* Functions in Bash are `reusable blocks of code` that perform a specific task. 
* They help organize scripts, reduce redundancy, and improve readability.
* Functions can accept `arguments` and can `return values` (via output or exit status).
* Functions are defined once and can be called multiple times throughout a script.
* Functions can also have `local` variables that do not interfere with global variables.
* Functions can include `control structures` like loops and conditionals.
* They can be `nested`, meaning one function can call another.
* Functions enhance modularity, making scripts easier to maintain and debug.
* They are essential for writing efficient and effective Bash scripts.

---

**Defining a Function:**
You can define a function in two ways:

1. **Using the `function` keyword:**
   ```bash
   function my_func {
       # commands
   }
   ```

2. **Using just the name and parentheses (Standard):**
   ```bash
   my_func() {
       # commands
   }
   ```

**Calling a Function:**

   * To call a function, simply write its name as if it were a command. You **do not** use parentheses when calling it.
      ```bash
      my_func arg1 arg2
      ```

---

## 01. Basic Function Structure

* This script demonstrates the simplest way to define and call a function.
* It defines a function named `greet` that prints a welcome message.
* The function is then called at the end of the script.

      ```sh
      #!/bin/bash

      # Define the function
      function greet() {
          echo "Hello! Welcome to Bash Functions."
      }

      # Call the function
      echo "Calling the function..."
      greet
      echo "Function execution finished."
      ```

    **What we're doing:**   

      * Creating a reusable block of code to print a message.  

    **How the script does it:**   

      * The `function greet() { ... }` block defines the function.
      * The code inside the curly braces `{}` is not executed until the function is called.
      * `greet` triggers the execution of the commands inside the function.

---

## 02. Passing Arguments to Functions

* Functions can accept arguments just like scripts.
* Inside a function, `$1`, `$2`, etc., refer to the arguments passed **to the function**, not the script.
* `$#` holds the number of arguments passed to the function.

      ```sh
      #!/bin/bash

      # Function to add two numbers
      add_numbers() {
          sum=$(( $1 + $2 ))
          echo "The sum of $1 and $2 is: $sum"
      }

      # Call the function with arguments
      add_numbers 10 20
      add_numbers 50 100
      ```

    **What we're doing:**   

      * Passing data into a function to perform a calculation.  

    **How the script does it:**   

      * `add_numbers 10 20` calls the function with `10` as `$1` and `20` as `$2`.
      * `sum=$(( $1 + $2 ))` performs arithmetic expansion to calculate the total.
      * The function is reused with different values (`50` and `100`).

---

## 03. Returning Values from Functions

* Unlike other programming languages, Bash functions do not return values using a `return` statement in the traditional sense.
* `return` in Bash is used to set the **exit status** (0-255) of the function (0 usually means success).
* To "return" a string or result, you typically `echo` the value and capture it using command substitution `$()`.

      ```sh
      #!/bin/bash

      # Function that 'returns' a value by echoing it
      get_current_date() {
          formatted_date=$(date +"%Y-%m-%d")
          echo "$formatted_date"
      }

      # Function that uses 'return' for status
      check_file_exists() {
          if [ -f "$1" ]; then
              return 0 # Success (True)
          else
              return 1 # Failure (False)
          fi
      }

      # Capture the output
      today=$(get_current_date)
      echo "Today's date is: $today"

      # Check status
      if check_file_exists "/etc/passwd"; then
          echo "File exists!"
      else
          echo "File not found."
      fi
      ```

    **What we're doing:**   

      * Retrieving data from a function and checking success/failure status.  

    **How the script does it:**   

      * `get_current_date` prints the date to stdout. `today=$(get_current_date)` captures that output into a variable.
      * `check_file_exists` uses `return 0` or `return 1`. The `if` statement checks this exit code directly.

---

## 04. Local vs Global Variables

* By default, all variables in Bash are **global**, even if defined inside a function.
* Use the `local` keyword to restrict a variable's scope to the function. This prevents overwriting variables outside the function.

      ```sh
      #!/bin/bash

      global_var="I am global"

      test_scope() {
          local local_var="I am local"
          global_var="I have been changed inside function"
          echo "Inside function: $local_var"
          echo "Inside function: $global_var"
      }

      echo "Before function: $global_var"
      test_scope
      echo "After function: $global_var"
      # echo "After function: $local_var" # This would be empty/undefined
      ```

    **What we're doing:**   

      * Understanding variable scope to write safer scripts.  

    **How the script does it:**   

      * `local local_var` ensures `local_var` only exists within `test_scope`.
      * `global_var` is modified inside the function, and that change persists after the function finishes because it wasn't declared `local`.

---

## 05. Functions with Checks (If/Else)

* This script uses conditional logic inside a function to validate input.
* It checks if a user is root or a regular user.

      ```sh
      #!/bin/bash

      check_user() {
          user_id=$(id -u)
          
          if [ "$user_id" -eq 0 ]; then
              echo "You are running as ROOT."
          else
              echo "You are running as a regular user (ID: $user_id)."
          fi
      }

      # Call the function
      check_user
      ```

    **What we're doing:**   

      * Encapsulating logic to check the current user's permissions.  

    **How the script does it:**   

      * `id -u` gets the user ID. Root is always `0`.
      * The `if` statement checks if the ID equals 0 and prints the appropriate message.

---

## 06. Functions with Loops

* Functions can contain loops to process lists of items.
* This example defines a function that takes multiple filenames as arguments and checks each one.

      ```sh
      #!/bin/bash

      process_files() {
          echo "Processing $# files..."
          
          # Loop through all arguments passed to the function
          for file in "$@"; do
              if [ -e "$file" ]; then
                  echo "  [OK] $file exists."
              else
                  echo "  [XX] $file missing."
              fi
          done
      }

      # Call function with a list of files
      process_files /etc/hosts /etc/passwd /tmp/missing_file.txt
      ```

    **What we're doing:**   

      * Batch processing items passed as arguments to a function.  

    **How the script does it:**   

      * `"$@"` represents all arguments passed to the function.
      * The `for` loop iterates over each file.
      * `[ -e "$file" ]` checks if the file exists.

---

## 07. Nested Functions

* You can define functions inside other functions, or call functions from within functions.
* This helps break down complex tasks into smaller steps.

      ```sh
      #!/bin/bash

      log_msg() {
          echo "[$(date +%T)] $1"
      }

      backup_file() {
          local file="$1"
          log_msg "Starting backup for $file"
          
          if [ -f "$file" ]; then
              cp "$file" "${file}.bak"
              log_msg "Backup created: ${file}.bak"
          else
              log_msg "Error: File $file not found"
          fi
      }

      # Main script logic
      backup_file "data.txt"
      ```

    **What we're doing:**   

      * Using a helper function (`log_msg`) inside another function (`backup_file`) to standardize output.  

    **How the script does it:**   

      * `log_msg` handles the formatting of log messages with a timestamp.
      * `backup_file` calls `log_msg` instead of using raw `echo`, keeping the code clean and consistent.
