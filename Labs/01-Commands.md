# Basic Commands


---

## File & Directory Management


| Command | Explanation |
|:---|:---|
| `ls` | [List directory contents](#01-ls---list-directory-contents) |
| `cd` | [Change directory](#02-cd---change-directory) |
| `pwd` | [Print working directory](#03-pwd---print-working-directory) |
| `mkdir` | [Make directory](#04-mkdir---make-directory) |
| `touch` | [Create empty files or update timestamps](#05-touch---create-empty-files-or-update-timestamps) |
| `cp` | [Copy files and directories](#06-cp---copy-files-and-directories) |
| `mv` | [Move or rename files](#07-mv---move-or-rename-files) |
| `rm` | [Remove files or directories](#08-rm---remove-files-or-directories) |


---


### 01. ls - List directory contents

* <a href="https://man7.org/linux/man-pages/man1/ls.1.html" target="_blank">man Page</a>

The `ls` command lists the contents of a directory. By default, it lists the files in the current directory sorted alphabetically.

#### Common Flags

| Command&nbsp;Flag | Description                                                                                                           |
|:-------------|:----------------------------------------------------------------------------------------------------------------------|
| `-l`         | **Long listing format**. Shows file details: permissions, owner, size, modification time.                             |
| `-a`         | **All files**. Shows hidden files (those starting with `.`), such as `.bashrc` or `.git`.                             |
| `-h`         | **Human-readable**. When used with `-l`, prints sizes in human-readable format (e.g., 1K, 234M, 2G) instead of bytes. |
| `-R`         | **Recursive**. Lists files in the current directory and all subdirectories recursively.                               |
| `-t`         | **Sort by time**. Shows the most recently modified files first.                                                       |
| `-r`         | **Reverse**. Reverses the sort order.                                                                                 |

#### Examples


**1. List all files in long format with human-readable sizes**

```sh
ls -lah
```

**Output Explanation:**
```text
drwxr-xr-x  5 user staff  160B Dec 11 10:00 .
drwxr-xr-x 10 user staff  320B Dec 10 14:30 ..
-rw-r--r--  1 user staff  220B Dec 11 09:00 .bashrc
-rw-r--r--  1 user staff  1.2K Dec 11 10:00 file.txt
```
- `drwxr-xr-x`: Directory permissions.
- `user staff`: Owner and Group.
- `1.2K`: File size.
- `.bashrc`: Hidden file shown due to `-a`.


**2. List files sorted by modification time (newest first)**

```sh
ls -lt
```


**3. List files in reverse alphabetical order**

```sh
ls -r
```

#### Questions

- What does the `ls` command do by default?
- Which flag would you use to see hidden files (starting with `.`)?
- How can you list files in long format with human-readable sizes?


---


### 02. cd - Change directory

* <a href="https://man7.org/linux/man-pages/man1/cd.1p.html" target="_blank">man Page</a>

The `cd` command changes the current working directory of the shell.

#### Common Usage

| Path              | Description                                                                |
|:------------------|:---------------------------------------------------------------------------|
| `cd /path/to/dir` | **Absolute path**. Changes to the directory specified from the root.       |
| `cd dir`          | **Relative path**. Changes to a subdirectory inside the current directory. |
| `cd ..`           | **Parent directory**. Moves up one level in the directory tree.            |
| `cd ~` or `cd`    | **Home directory**. Moves to the current user's home directory.            |
| `cd -`            | **Previous directory**. Switches back to the last directory you were in.   |

#### Examples


**1. Navigate to a system directory**

```sh
cd /var/log
```


**2. Move up two levels**

```sh
cd ../..
```


**3. Toggle between two directories**

```sh
cd -
```
*Output:* Prints the path of the directory you returned to.


**4. Change to the home directory**

```sh
cd ~
```

#### Questions

- What command changes the current directory?
- How do you go to the parent directory?
- What does `cd -` do?


---


### 03. pwd - Print working directory

* <a href="https://man7.org/linux/man-pages/man1/pwd.1.html" target="_blank">man Page</a>

The `pwd` command prints the full absolute path of the current working directory.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-L` | **Logical**. Displays the logical current working directory, including symbolic links (default). |
| `-P` | **Physical**. Displays the physical current working directory, resolving all symbolic links. |

#### Examples


**1. Check where you are**

```sh
pwd
```

**Output:**
```text
/Users/username/projects/UnixLabs
```


**2. Show the physical path (resolving symlinks)**

```sh
pwd -P
```

#### Questions

- What does `pwd` stand for?
- What is the difference between `pwd -L` and `pwd -P`?


---


### 04. mkdir - Make directory

* <a href="https://man7.org/linux/man-pages/man1/mkdir.1.html" target="_blank">man Page</a>

The `mkdir` command creates new directories.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-p` | **Parents**. No error if existing, make parent directories as needed. Useful for creating nested structures. |
| `-v` | **Verbose**. Print a message for each created directory. |
| `-m` | **Mode**. Set file mode (permissions) for the new directory (e.g., `-m 755`). |

#### Examples


**1. Create a directory structure**

```sh
mkdir -p project/{src,bin,logs}
```
*Explanation:* Creates `project` folder and `src`, `bin`, `logs` inside it.


**2. Create a directory with specific permissions**

```sh
mkdir -m 700 private_folder
```
*Explanation:* Creates a folder that only the owner can read, write, and execute.


**3. Create multiple directories at once**

```sh
mkdir dir1 dir2 dir3
```

#### Questions

- What does `mkdir` do?
- Which flag allows creating parent directories if they don't exist?
- How can you set permissions when creating a directory?


---


### 05. touch - Create empty files or update timestamps

* <a href="https://man7.org/linux/man-pages/man1/touch.1.html" target="_blank">man Page</a>

The `touch` command is used to create an empty file if it doesn't exist. If the file exists, it updates the access and modification timestamps to the current time.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-a` | **Access time**. Change only the access time. |
| `-m` | **Modification time**. Change only the modification time. |
| `-c` | **No create**. Do not create any files if they don't exist. |
| `-t` | **Time**. Use specified time instead of current time (format: [[CC]YY]MMDDhhmm[.ss]). |

#### Examples


**1. Create a new file**

```sh
touch newfile.txt
```


**2. Update timestamp of an existing file**

```sh
touch existingfile.txt
```
*Explanation:* Useful to trigger build systems that rely on file modification times.


**3. Create multiple files at once**

```sh
touch file1.txt file2.txt file3.txt
```

#### Questions

- What does `touch` do if the file doesn't exist?
- What happens if you run `touch` on an existing file?
- Which flag changes only the access time?


---
## System & Process Management

| Command | Explanation |
|:---|:---|
| `ps` | [Report a snapshot of the current processes](#16-ps---report-a-snapshot-of-the-current-processes) |
| `kill` | [Terminate a process](#17-kill---terminate-a-process) |
| `top` | [Display Linux processes](#18-top---display-linux-processes) |
| `df` | [Report file system disk space usage](#19-df---report-file-system-disk-space-usage) |
| `du` | [Estimate file space usage](#20-du---estimate-file-space-usage) |


---


### 06. cp - Copy files and directories

* <a href="https://man7.org/linux/man-pages/man1/cp.1.html" target="_blank">man Page</a>

The `cp` command copies files and directories from a source to a destination.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-r` or `-R` | **Recursive**. Copy directories and their contents recursively. |
| `-i` | **Interactive**. Prompt before overwriting an existing file. |
| `-v` | **Verbose**. Explain what is being done. |
| `-u` | **Update**. Copy only when the SOURCE file is newer than the destination file or when the destination file is missing. |
| `-p` | **Preserve**. Preserve mode, ownership, and timestamps. |

#### Examples


**1. Copy a file to another directory**

```sh
cp file.txt /backup/
```


**2. Copy a directory recursively**

```sh
cp -r src/ src_backup/
```


**3. Safe copy (prompt before overwrite)**

```sh
cp -i important.txt /data/
```
*Output:* `cp: overwrite '/data/important.txt'?`


**4. Copy and preserve attributes**

```sh
cp -p original.txt copy.txt
```

#### Questions

- What is the purpose of the `cp` command?
- Which flag do you use to copy directories recursively?
- What does the `-i` flag do?


---


### 07. mv - Move or rename files

* <a href="https://man7.org/linux/man-pages/man1/mv.1.html" target="_blank">man Page</a>

The `mv` command moves files or directories from one place to another. It is also used to rename files.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-i` | **Interactive**. Prompt before overwriting. |
| `-u` | **Update**. Move only when the SOURCE file is newer than the destination file. |
| `-v` | **Verbose**. Explain what is being done. |
| `-n` | **No clobber**. Do not overwrite an existing file. |

#### Examples


**1. Rename a file**

```sh
mv old_name.txt new_name.txt
```


**2. Move files to a directory**

```sh
mv *.log /var/log/myapp/
```


**3. Move a directory**

```sh
mv myfolder /new/location/
```

#### Questions

- How does `mv` differ from `cp`?
- What happens if you use `mv` to move a file to a different name in the same directory?
- Which flag prevents overwriting existing files?


---


### 08. rm - Remove files or directories

* <a href="https://man7.org/linux/man-pages/man1/rm.1.html" target="_blank">man Page</a>

The `rm` command removes (deletes) files and directories. **Warning:** Deleted files are usually not recoverable.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-r` or `-R` | **Recursive**. Remove directories and their contents recursively. |
| `-f` | **Force**. Ignore nonexistent files and arguments, never prompt. |
| `-i` | **Interactive**. Prompt before every removal. |
| `-v` | **Verbose**. Explain what is being done. |

#### Examples


**1. Remove a single file**

```sh
rm file.txt
```


**2. Remove a directory and all its contents (Use with caution)**

```sh
rm -rf my_dir
```


**3. Interactive removal**

```sh
rm -i *.txt
```
*Output:* `rm: remove regular file 'file1.txt'?`


**4. Remove files forcefully without prompts**

```sh
rm -f temp*.log
```

#### Questions

- Why is the `rm` command dangerous?
- Which flag removes directories recursively?
- What does `-f` do?



---

## Text Processing


| Command | Explanation |
|:---|:---|
| `cat` | [Concatenate and display files](#09-cat---concatenate-and-display-files) |
| `head` | [Output the first part of files](#10-head---output-the-first-part-of-files) |
| `tail` | [Output the last part of files](#11-tail---output-the-last-part-of-files) |
| `grep` | [Print lines matching a pattern](#12-grep---print-lines-matching-a-pattern) |
| `wc` | [Print newline, word, and byte counts](#13-wc---print-newline-word-and-byte-counts) |
| `sort` | [Sort lines of text files](#14-sort---sort-lines-of-text-files) |
| `uniq` | [Report or omit repeated lines](#15-uniq---report-or-omit-repeated-lines) |
| `less` | [Opposite of more](#16-less---opposite-of-more) |


---


### 09. cat - Concatenate and display files

* <a href="https://man7.org/linux/man-pages/man1/cat.1.html" target="_blank">man Page</a>

The `cat` command reads data from the file and outputs its content. It is often used to combine files.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-n` | **Number**. Number all output lines. |
| `-b` | **Number non-blank**. Number nonempty output lines, overrides `-n`. |
| `-s` | **Squeeze blank**. Suppress repeated empty output lines. |
| `-E` | **Show ends**. Display `$` at the end of each line. |

#### Examples


**1. Display file content**

```sh
cat /etc/hostname
```


**2. Concatenate multiple files**

```sh
cat part1.txt part2.txt > full_document.txt
```


**3. Create a file from terminal input (Press Ctrl+D to save)**

```sh
cat > notes.txt
```


**4. Number all lines in a file**

```sh
cat -n file.txt
```

#### Questions

- What does `cat` stand for?
- How can you use `cat` to create a new file?
- Which flag numbers the output lines?


---


### 10. head - Output the first part of files

* <a href="https://man7.org/linux/man-pages/man1/head.1.html" target="_blank">man Page</a>

The `head` command outputs the first part of files. By default, it shows the first 10 lines.

#### Common Flags

| Command Flag | Description                                                     |
|:-------------|:----------------------------------------------------------------|
| `-n NUM`     | **Lines**. Print the first `NUM` lines instead of the first 10. |
| `-c NUM`     | **Bytes**. Print the first `NUM` bytes of each file.            |
| `-q`         | **Quiet**. Never print headers giving file names.               |

#### Examples


**1. Show the first 5 lines of a file**

```sh
head -n 5 /var/log/syslog
```


**2. View the top of a script to check the shebang**

```sh
head -n 1 script.sh
```
*Output:* `#!/bin/bash`


**3. Show the first 10 bytes of a file**

```sh
head -c 10 file.txt
```

#### Questions

- What is the default number of lines `head` displays?
- How do you display the first 20 lines of a file?
- What does `-c` do?


---


### 11. tail - Output the last part of files

* <a href="https://man7.org/linux/man-pages/man1/tail.1.html" target="_blank">man Page</a>

The `tail` command outputs the last part of files. By default, it shows the last 10 lines. It is extremely useful for monitoring logs.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-n NUM` | **Lines**. Output the last `NUM` lines, instead of the last 10. |
| `-f` | **Follow**. Output appended data as the file grows. Useful for watching log files in real-time. |
| `-c NUM` | **Bytes**. Output the last `NUM` bytes. |

#### Examples


**1. Show the last 20 lines of a log file**

```sh
tail -n 20 error.log
```


**2. Monitor a log file in real-time**

```sh
tail -f /var/log/nginx/access.log
```
*Explanation:* The command will stay running and print new lines as they are written to the file. Press `Ctrl+C` to stop.


**3. Show the last 50 bytes of a file**

```sh
tail -c 50 file.txt
```

#### Questions

- What is `tail -f` used for?
- How do you display the last 50 lines?
- What is the difference between `head` and `tail`?


---


### 12. grep - Print lines matching a pattern

* <a href="https://man7.org/linux/man-pages/man1/grep.1.html" target="_blank">man Page</a>

The `grep` command searches for patterns (strings or regular expressions) in files and prints the matching lines.

#### Common Flags

| Command Flag | Description                                                                                                                                   |
|:-------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| `-i`         | **Ignore case**. Ignore case distinctions in patterns and data.                                                                               |
| `-r` or `-R` | **Recursive**. Read all files under each directory, recursively.                                                                              |
| `-v`         | **Invert match**. Select non-matching lines.                                                                                                  |
| `-n`         | **Line number**. Prefix each line of output with the 1-based line number.                                                                     |
| `-l`         | **Files with matches**. Suppress normal output; instead print the name of each input file from which output would normally have been printed. |
| `-c`         | **Count**. Suppress normal output; instead print a count of matching lines.                                                                   |

#### Examples


**1. Search for a string in a file**

```sh
grep "error" application.log
```


**2. Search recursively for a string in the current directory**

```sh
grep -r "TODO" .
```


**3. Count occurrences of a word**

```sh
grep -c "localhost" /etc/hosts
```


**4. Search case-insensitively**

```sh
grep -i "Error" file.txt
```

#### Questions

- What does `grep` do?
- Which flag searches recursively?
- How do you invert the match?


---


### 13. wc - Print newline, word, and byte counts

* <a href="https://man7.org/linux/man-pages/man1/wc.1.html" target="_blank">man Page</a>

The `wc` command prints newline, word, and byte counts for each file.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-l` | **Lines**. Print the newline counts. |
| `-w` | **Words**. Print the word counts. |
| `-c` | **Bytes**. Print the byte counts. |

#### Examples

**1. Count lines in a file**

```sh
wc -l file.txt
```

**2. Count words**

```sh
wc -w file.txt
```

**3. Count everything**

```sh
wc file.txt
```

#### Questions

- What does `wc` stand for?
- How do you count only lines?
- What are the three default counts `wc` displays?


---


### 14. sort - Sort lines of text files

* <a href="https://man7.org/linux/man-pages/man1/sort.1.html" target="_blank">man Page</a>

The `sort` command sorts lines of text files.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-r` | **Reverse**. Reverse the result of comparisons. |
| `-n` | **Numeric**. Compare according to string numerical value. |
| `-u` | **Unique**. Output only the first of an equal run. |

#### Examples

**1. Sort a file alphabetically**

```sh
sort names.txt
```

**2. Sort numbers**

```sh
sort -n numbers.txt
```

**3. Sort in reverse order**

```sh
sort -r names.txt
```

#### Questions

- How do you sort numerically?
- How do you reverse the sort order?
- Which flag removes duplicates?


---


### 15. uniq - Report or omit repeated lines

* <a href="https://man7.org/linux/man-pages/man1/uniq.1.html" target="_blank">man Page</a>

The `uniq` command reports or omits repeated lines. Note: `uniq` does not detect repeated lines unless they are adjacent.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-c` | **Count**. Prefix lines by the number of occurrences. |
| `-d` | **Repeated**. Only print duplicate lines, one for each group. |
| `-u` | **Unique**. Only print unique lines. |

#### Examples

**1. Remove adjacent duplicates**

```sh
sort file.txt | uniq
```

**2. Count occurrences**

```sh
sort file.txt | uniq -c
```

**3. Show only duplicates**

```sh
sort file.txt | uniq -d
```

#### Questions

- Why do you often use `sort` before `uniq`?
- How do you count occurrences of lines?
- Which flag shows only duplicate lines?


---


### 16. less - Opposite of more

* <a href="https://man7.org/linux/man-pages/man1/less.1.html" target="_blank">man Page</a>

The `less` command is a program similar to `more`, but it allows backward movement in the file as well as forward movement.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-N` | **Line numbers**. Show line numbers. |
| `-S` | **Chop long lines**. Causes lines longer than the screen width to be chopped rather than wrapped. |
| `+F` | **Follow**. Scroll forward, and keep trying to read when the end of file is reached (like tail -f). |

#### Examples

**1. View a file**

```sh
less file.txt
```

**2. View with line numbers**

```sh
less -N file.txt
```

**3. Search inside less**

```sh
/search_term (inside the viewer)
```

#### Questions

- How do you quit `less`?
- How do you search forward in `less`?
- What is the advantage of `less` over `cat`?


---
## User & Permissions


| Command | Explanation |
|:---|:---|
| `chmod` | [Change file mode bits](#17-chmod---change-file-mode-bits) |
| `chown` | [Change file owner and group](#18-chown---change-file-owner-and-group) |
| `sudo` | [Execute a command as another user](#19-sudo---execute-a-command-as-another-user) |
| `whoami` | [Print effective userid](#20-whoami---print-effective-userid) |


---


### 17. chmod - Change file mode bits

* <a href="https://man7.org/linux/man-pages/man1/chmod.1.html" target="_blank">man Page</a>

The `chmod` command changes the file mode bits (permissions) of a file or directory. Permissions define who can read, write, or execute a file.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-R` | **Recursive**. Change files and directories recursively. |
| `-v` | **Verbose**. Output a diagnostic for every file processed. |
| `-c` | **Changes**. Like verbose but report only when a change is made. |

#### Permission Modes

**Symbolic Modes**

| Category | Symbol | Description |
| :--- | :--- | :--- |
| **Who** | `u` | User |
| | `g` | Group |
| | `o` | Others |
| | `a` | All |
| **Operator** | `+` | Add |
| | `-` | Remove |
| | `=` | Set |
| **Permission** | `r` | Read |
| | `w` | Write |
| | `x` | Execute |

**Octal Modes**

| Value | Permission |
| :--- | :--- |
| `4` | Read |
| `2` | Write |
| `1` | Execute |

#### Examples


**1. Make a script executable for the owner**

```sh
chmod u+x script.sh
```


**2. Set permissions to 755 (rwxr-xr-x)**

```sh
chmod 755 script.sh
```
*Explanation:* Owner has full access (7), Group and Others can read and execute (5).


**3. Remove write permission for others**

```sh
chmod o-w file.txt
```


**4. Add execute permission for group**

```sh
chmod g+x file.sh
```

#### Questions

- What does `chmod` do?
- Explain the octal permission 755.
- How do you make a file executable?


---


### 18. chown - Change file owner and group

* <a href="https://man7.org/linux/man-pages/man1/chown.1.html" target="_blank">man Page</a>

The `chown` command changes the user and/or group ownership of a given file.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-R` | **Recursive**. Operate on files and directories recursively. |
| `-v` | **Verbose**. Output a diagnostic for every file processed. |
| `-c` | **Changes**. Like verbose but report only when a change is made. |

#### Examples


**1. Change owner of a file**

```sh
chown alice file.txt
```


**2. Change owner and group**

```sh
chown bob:developers project/
```


**3. Change ownership recursively**

```sh
chown -R www-data:www-data /var/www/html
```


**4. Change only the group**

```sh
chown :staff file.txt
```

#### Questions

- What is the difference between `chown` and `chmod`?
- Which flag changes ownership recursively?
- How do you change both owner and group?


---


### 19. sudo - Execute a command as another user

* <a href="https://man7.org/linux/man-pages/man8/sudo.8.html" target="_blank">man Page</a>

The `sudo` command allows a permitted user to execute a command as the superuser or another user.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-u user` | **User**. Run command as specified user. |
| `-i` | **Login**. Run the shell specified by the target user's password database entry as a login shell. |
| `-l` | **List**. List user's privileges or check a specific command. |

#### Examples

**1. Run command as root**

```sh
sudo apt update
```

**2. Switch to root user**

```sh
sudo -i
```

**3. Run command as another user**

```sh
sudo -u postgres psql
```

#### Questions

- What does `sudo` stand for?
- How do you switch to the root user environment?
- How do you run a command as a specific user?


---


### 20. whoami - Print effective userid

* <a href="https://man7.org/linux/man-pages/man1/whoami.1.html" target="_blank">man Page</a>

The `whoami` command prints the user name associated with the current effective user ID.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `--help` | **Help**. Display this help and exit. |
| `--version` | **Version**. Output version information and exit. |

#### Examples

**1. Check current user**

```sh
whoami
```

#### Questions

- What does `whoami` print?
- Is `whoami` the same as `id -un`?
- When is `whoami` useful?



---

## System Information & Management


| Command | Explanation |
|:---|:---|
| `man` | [An interface to the system reference manuals](#21-man---an-interface-to-the-system-reference-manuals) |
| `ps` | [Report a snapshot of the current processes](#22-ps---report-a-snapshot-of-the-current-processes) |
| `kill` | [Terminate a process](#23-kill---terminate-a-process) |
| `top` | [Display Linux processes](#24-top---display-linux-processes) |
| `df` | [Report file system disk space usage](#25-df---report-file-system-disk-space-usage) |
| `du` | [Estimate file space usage](#26-du---estimate-file-space-usage) |


---


### 21. man - An interface to the system reference manuals

* <a href="https://man7.org/linux/man-pages/man1/man.1.html" target="_blank">man Page</a>

The `man` command displays the user manual of any command that we can run on the terminal.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-k` | **Apropos**. Search the short descriptions and manual page names for the keyword. |
| `-f` | **Whatis**. Display short description from the manual page. |
| `-w` | **Where**. Print the location of the manual page file. |

#### Examples


**1. Read the manual for `ls`**

```sh
man ls
```
*Navigation:* Use arrow keys to scroll, `q` to quit.


**2. Search for commands related to "copy"**

```sh
man -k copy
```


**3. Get a short description of a command**

```sh
man -f ls
```

#### Questions

- What does `man` do?
- How do you search for manual pages?
- What key do you press to quit the man page viewer?


---


### 22. ps - Report a snapshot of the current processes

* <a href="https://man7.org/linux/man-pages/man1/ps.1.html" target="_blank">man Page</a>

The `ps` command displays information about a selection of the active processes.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-e` | **Every**. Select all processes. |
| `-f` | **Full**. Do full-format listing. |
| `-u user` | **User**. Select by effective user ID (EUID) or name. |
| `aux` | **BSD Style**. `a` (all users), `u` (user oriented), `x` (no terminal). |

#### Examples

**1. View all running processes**

```sh
ps -ef
```

**2. View processes for a specific user**

```sh
ps -u root
```

**3. View processes with CPU/Memory usage (BSD style)**

```sh
ps aux
```

#### Questions

- What does `ps` stand for?
- Which flag selects all processes?
- How do you view processes for a specific user?


---


### 23. kill - Terminate a process

* <a href="https://man7.org/linux/man-pages/man1/kill.1.html" target="_blank">man Page</a>

The `kill` command sends a signal to a process. The default signal is TERM (terminate).

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-9` | **SIGKILL**. Force kill the process immediately. |
| `-l` | **List**. List all available signal names. |
| `-s SIG` | **Signal**. Send a specific signal. |

#### Examples

**1. Terminate a process by PID**

```sh
kill 1234
```

**2. Force kill a process**

```sh
kill -9 1234
```

**3. List available signals**

```sh
kill -l
```

#### Questions

- What is the default signal sent by `kill`?
- Which signal forces a process to stop immediately?
- How do you list available signals?


---


### 24. top - Display Linux processes

* <a href="https://man7.org/linux/man-pages/man1/top.1.html" target="_blank">man Page</a>

The `top` command provides a dynamic real-time view of a running system.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-d SECS` | **Delay**. Specifies the delay between screen updates. |
| `-u user` | **User**. Monitor only processes for a given user. |
| `-p PID` | **PID**. Monitor only processes with specified process IDs. |

#### Examples

**1. Start top**

```sh
top
```

**2. Monitor a specific user**

```sh
top -u username
```

**3. Refresh every 5 seconds**

```sh
top -d 5
```

#### Questions

- What does `top` display?
- How do you filter processes by user in `top`?
- How do you change the update interval?


---


### 25. df - Report file system disk space usage

* <a href="https://man7.org/linux/man-pages/man1/df.1.html" target="_blank">man Page</a>

The `df` command displays the amount of disk space available on the file system containing each file name argument.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-h` | **Human-readable**. Print sizes in powers of 1024 (e.g., 1023M). |
| `-T` | **Type**. Print file system type. |
| `-i` | **Inodes**. List inode information instead of block usage. |

#### Examples

**1. Check disk space usage**

```sh
df
```

**2. Human readable format**

```sh
df -h
```

**3. Show file system type**

```sh
df -Th
```

#### Questions

- What does `df` report?
- Which flag shows sizes in human-readable format?
- How do you see the file system type?


---


### 26. du - Estimate file space usage

* <a href="https://man7.org/linux/man-pages/man1/du.1.html" target="_blank">man Page</a>

The `du` command estimates file space usage.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-h` | **Human-readable**. Print sizes in human readable format (e.g., 1K 234M 2G). |
| `-s` | **Summarize**. Display only a total for each argument. |
| `-c` | **Total**. Produce a grand total. |

#### Examples

**1. Check size of current directory**

```sh
du -h .
```

**2. Summary of a directory**

```sh
du -sh /var/log
```

**3. Check size of specific files**

```sh
du -h file1.txt file2.txt
```

#### Questions

- What is the difference between `df` and `du`?
- How do you get a summary of a directory's size?
- Which flag gives a grand total?


---
## Advanced Search

| Command | Explanation |
|:---|:---|
| `find` | [Search for files in a directory hierarchy](#21-find---search-for-files-in-a-directory-hierarchy) |



---

### 27. find - Search for files in a directory hierarchy

* <a href="https://man7.org/linux/man-pages/man1/find.1.html" target="_blank">man Page</a>

The `find` command searches for files in a directory hierarchy.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-name pattern` | **Name**. Base of file name (the path with the leading directories removed) matches shell pattern pattern. |
| `-type c` | **Type**. File is of type c: f (regular file), d (directory). |
| `-exec command ;` | **Execute**. Execute command; true if 0 status is returned. |
| `-mtime n` | **Modification time**. File's data was last modified n*24 hours ago. |

#### Examples

**1. Find files by name**

```sh
find . -name "*.txt"
```

**2. Find directories only**

```sh
find /var -type d
```

**3. Find and delete files (Be careful)**

```sh
find . -name "temp*" -delete
```

#### Questions

- How do you find files by name?
- How do you find only directories?
- What does `-mtime` do?


---
## Networking


| Command | Explanation |
|:---|:---|
| `ping` | [Send ICMP ECHO_REQUEST to network hosts](#28-ping---send-icmp-echo_request-to-network-hosts) |
| `curl` | [Transfer a URL](#29-curl---transfer-a-url) |


---


### 28. ping - Send ICMP ECHO_REQUEST to network hosts

* <a href="https://man7.org/linux/man-pages/man8/ping.8.html" target="_blank">man Page</a>

The `ping` command uses the ICMP protocol's mandatory ECHO_REQUEST datagram to elicit an ICMP ECHO_RESPONSE from a host or gateway.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-c count` | **Count**. Stop after sending count ECHO_REQUEST packets. |
| `-i interval` | **Interval**. Wait interval seconds between sending each packet. |
| `-t ttl` | **TTL**. Set the IP Time to Live. |

#### Examples

**1. Ping a host**

```sh
ping google.com
```

**2. Ping 5 times**

```sh
ping -c 5 google.com
```

**3. Ping with specific interval**

```sh
ping -i 0.5 google.com
```

#### Questions

- What protocol does `ping` use?
- How do you limit the number of pings?
- What does TTL stand for?


---


### 29. curl - Transfer a URL

* <a href="https://man7.org/linux/man-pages/man1/curl.1.html" target="_blank">man Page</a>

The `curl` command is a tool to transfer data from or to a server.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-O` | **Remote name**. Write output to a local file named like the remote file we get. |
| `-I` | **Head**. Fetch the HTTP-header only. |
| `-L` | **Location**. Follow redirects. |
| `-d data` | **Data**. Sends the specified data in a POST request. |

#### Examples

**1. Download a file**

```sh
curl -O https://example.com/file.zip
```

**2. Check headers**

```sh
curl -I https://google.com
```

**3. Follow redirects**

```sh
curl -L https://google.com
```

#### Questions

- What does `curl` do?
- How do you save the output to a file with the same name?
- Which flag follows redirects?


---
## Archives


| Command | Explanation |
|:---|:---|
| `tar` | [An archiving utility](#30-tar---an-archiving-utility) |
| `zip` | [Package and compress (archive) files](#31-zip---package-and-compress-(archive)-files) |
| `unzip` | [List, test and extract compressed files in a ZIP archive](#32-unzip---list-test-and-extract-compressed-files-in-a-zip-archive) |


---


### 30. tar - An archiving utility

* <a href="https://man7.org/linux/man-pages/man1/tar.1.html" target="_blank">man Page</a>

The `tar` command is an archiving utility used to store and extract files from an archive file known as a tarball.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-c` | **Create**. Create a new archive. |
| `-x` | **Extract**. Extract files from an archive. |
| `-v` | **Verbose**. Verbosely list files processed. |
| `-f` | **File**. Use archive file or device ARCHIVE. |
| `-z` | **Gzip**. Filter the archive through gzip. |

#### Examples

**1. Create a tar.gz archive**

```sh
tar -czvf archive.tar.gz /path/to/dir
```

**2. Extract a tar.gz archive**

```sh
tar -xzvf archive.tar.gz
```

**3. List contents of an archive**

```sh
tar -tvf archive.tar.gz
```

#### Questions

- What does `tar` stand for?
- Which flag creates a new archive?
- How do you compress the archive with gzip?


---


### 31. zip - Package and compress (archive) files

* <a href="https://man7.org/linux/man-pages/man1/zip.1.html" target="_blank">man Page</a>

The `zip` command is a compression and file packaging utility.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-r` | **Recursive**. Travel the directory structure recursively. |
| `-e` | **Encrypt**. Encrypt the contents of the zip archive. |
| `-d` | **Delete**. Delete entries from the zip archive. |

#### Examples

**1. Zip a directory**

```sh
zip -r archive.zip directory/
```

**2. Zip multiple files**

```sh
zip archive.zip file1.txt file2.txt
```

**3. Password protect zip**

```sh
zip -e secure.zip file.txt
```

#### Questions

- How do you zip a directory recursively?
- How do you password protect a zip file?
- What is the difference between `tar` and `zip`?


---


### 32. unzip - List, test and extract compressed files in a ZIP archive

* <a href="https://man7.org/linux/man-pages/man1/unzip.1.html" target="_blank">man Page</a>

The `unzip` command will list, test, or extract files from a ZIP archive.

#### Common Flags

| Command Flag | Description |
| :--- | :--- |
| `-l` | **List**. List archive files (short format). |
| `-t` | **Test**. Test archive files. |
| `-d dir` | **Directory**. An optional directory to which to extract files. |

#### Examples

**1. Unzip a file**

```sh
unzip archive.zip
```

**2. List contents without extracting**

```sh
unzip -l archive.zip
```

**3. Extract to specific directory**

```sh
unzip archive.zip -d /path/to/dest
```

#### Questions

- How do you list contents of a zip file?
- How do you extract to a specific directory?
- What does `unzip -t` do?


---
