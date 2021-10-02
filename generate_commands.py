
import os

commands_data = [
    {
        "category": "System & Process Management",
        "commands": [
            {
                "name": "ps",
                "desc": "Report a snapshot of the current processes",
                "man_section": "1",
                "long_desc": "The `ps` command displays information about a selection of the active processes.",
                "flags": [
                    ("-e", "**Every**. Select all processes."),
                    ("-f", "**Full**. Do full-format listing."),
                    ("-u user", "**User**. Select by effective user ID (EUID) or name."),
                    ("aux", "**BSD Style**. `a` (all users), `u` (user oriented), `x` (no terminal).")
                ],
                "examples": [
                    ("1. View all running processes", "ps -ef"),
                    ("2. View processes for a specific user", "ps -u root"),
                    ("3. View processes with CPU/Memory usage (BSD style)", "ps aux")
                ],
                "questions": [
                    "What does `ps` stand for?",
                    "Which flag selects all processes?",
                    "How do you view processes for a specific user?"
                ]
            },
            {
                "name": "kill",
                "desc": "Terminate a process",
                "man_section": "1",
                "long_desc": "The `kill` command sends a signal to a process. The default signal is TERM (terminate).",
                "flags": [
                    ("-9", "**SIGKILL**. Force kill the process immediately."),
                    ("-l", "**List**. List all available signal names."),
                    ("-s SIG", "**Signal**. Send a specific signal.")
                ],
                "examples": [
                    ("1. Terminate a process by PID", "kill 1234"),
                    ("2. Force kill a process", "kill -9 1234"),
                    ("3. List available signals", "kill -l")
                ],
                "questions": [
                    "What is the default signal sent by `kill`?",
                    "Which signal forces a process to stop immediately?",
                    "How do you list available signals?"
                ]
            },
            {
                "name": "top",
                "desc": "Display Linux processes",
                "man_section": "1",
                "long_desc": "The `top` command provides a dynamic real-time view of a running system.",
                "flags": [
                    ("-d SECS", "**Delay**. Specifies the delay between screen updates."),
                    ("-u user", "**User**. Monitor only processes for a given user."),
                    ("-p PID", "**PID**. Monitor only processes with specified process IDs.")
                ],
                "examples": [
                    ("1. Start top", "top"),
                    ("2. Monitor a specific user", "top -u username"),
                    ("3. Refresh every 5 seconds", "top -d 5")
                ],
                "questions": [
                    "What does `top` display?",
                    "How do you filter processes by user in `top`?",
                    "How do you change the update interval?"
                ]
            },
            {
                "name": "df",
                "desc": "Report file system disk space usage",
                "man_section": "1",
                "long_desc": "The `df` command displays the amount of disk space available on the file system containing each file name argument.",
                "flags": [
                    ("-h", "**Human-readable**. Print sizes in powers of 1024 (e.g., 1023M)."),
                    ("-T", "**Type**. Print file system type."),
                    ("-i", "**Inodes**. List inode information instead of block usage.")
                ],
                "examples": [
                    ("1. Check disk space usage", "df"),
                    ("2. Human readable format", "df -h"),
                    ("3. Show file system type", "df -Th")
                ],
                "questions": [
                    "What does `df` report?",
                    "Which flag shows sizes in human-readable format?",
                    "How do you see the file system type?"
                ]
            },
            {
                "name": "du",
                "desc": "Estimate file space usage",
                "man_section": "1",
                "long_desc": "The `du` command estimates file space usage.",
                "flags": [
                    ("-h", "**Human-readable**. Print sizes in human readable format (e.g., 1K 234M 2G)."),
                    ("-s", "**Summarize**. Display only a total for each argument."),
                    ("-c", "**Total**. Produce a grand total.")
                ],
                "examples": [
                    ("1. Check size of current directory", "du -h ."),
                    ("2. Summary of a directory", "du -sh /var/log"),
                    ("3. Check size of specific files", "du -h file1.txt file2.txt")
                ],
                "questions": [
                    "What is the difference between `df` and `du`?",
                    "How do you get a summary of a directory's size?",
                    "Which flag gives a grand total?"
                ]
            }
        ]
    },
    {
        "category": "Advanced Search",
        "commands": [
            {
                "name": "find",
                "desc": "Search for files in a directory hierarchy",
                "man_section": "1",
                "long_desc": "The `find` command searches for files in a directory hierarchy.",
                "flags": [
                    ("-name pattern", "**Name**. Base of file name (the path with the leading directories removed) matches shell pattern pattern."),
                    ("-type c", "**Type**. File is of type c: f (regular file), d (directory)."),
                    ("-exec command ;", "**Execute**. Execute command; true if 0 status is returned."),
                    ("-mtime n", "**Modification time**. File's data was last modified n*24 hours ago.")
                ],
                "examples": [
                    ("1. Find files by name", "find . -name \"*.txt\""),
                    ("2. Find directories only", "find /var -type d"),
                    ("3. Find and delete files (Be careful)", "find . -name \"temp*\" -delete")
                ],
                "questions": [
                    "How do you find files by name?",
                    "How do you find only directories?",
                    "What does `-mtime` do?"
                ]
            }
        ]
    },
    {
        "category": "Text Processing",
        "commands": [
            {
                "name": "wc",
                "desc": "Print newline, word, and byte counts",
                "man_section": "1",
                "long_desc": "The `wc` command prints newline, word, and byte counts for each file.",
                "flags": [
                    ("-l", "**Lines**. Print the newline counts."),
                    ("-w", "**Words**. Print the word counts."),
                    ("-c", "**Bytes**. Print the byte counts.")
                ],
                "examples": [
                    ("1. Count lines in a file", "wc -l file.txt"),
                    ("2. Count words", "wc -w file.txt"),
                    ("3. Count everything", "wc file.txt")
                ],
                "questions": [
                    "What does `wc` stand for?",
                    "How do you count only lines?",
                    "What are the three default counts `wc` displays?"
                ]
            },
            {
                "name": "sort",
                "desc": "Sort lines of text files",
                "man_section": "1",
                "long_desc": "The `sort` command sorts lines of text files.",
                "flags": [
                    ("-r", "**Reverse**. Reverse the result of comparisons."),
                    ("-n", "**Numeric**. Compare according to string numerical value."),
                    ("-u", "**Unique**. Output only the first of an equal run.")
                ],
                "examples": [
                    ("1. Sort a file alphabetically", "sort names.txt"),
                    ("2. Sort numbers", "sort -n numbers.txt"),
                    ("3. Sort in reverse order", "sort -r names.txt")
                ],
                "questions": [
                    "How do you sort numerically?",
                    "How do you reverse the sort order?",
                    "Which flag removes duplicates?"
                ]
            },
            {
                "name": "uniq",
                "desc": "Report or omit repeated lines",
                "man_section": "1",
                "long_desc": "The `uniq` command reports or omits repeated lines. Note: `uniq` does not detect repeated lines unless they are adjacent.",
                "flags": [
                    ("-c", "**Count**. Prefix lines by the number of occurrences."),
                    ("-d", "**Repeated**. Only print duplicate lines, one for each group."),
                    ("-u", "**Unique**. Only print unique lines.")
                ],
                "examples": [
                    ("1. Remove adjacent duplicates", "sort file.txt | uniq"),
                    ("2. Count occurrences", "sort file.txt | uniq -c"),
                    ("3. Show only duplicates", "sort file.txt | uniq -d")
                ],
                "questions": [
                    "Why do you often use `sort` before `uniq`?",
                    "How do you count occurrences of lines?",
                    "Which flag shows only duplicate lines?"
                ]
            },
            {
                "name": "less",
                "desc": "Opposite of more",
                "man_section": "1",
                "long_desc": "The `less` command is a program similar to `more`, but it allows backward movement in the file as well as forward movement.",
                "flags": [
                    ("-N", "**Line numbers**. Show line numbers."),
                    ("-S", "**Chop long lines**. Causes lines longer than the screen width to be chopped rather than wrapped."),
                    ("+F", "**Follow**. Scroll forward, and keep trying to read when the end of file is reached (like tail -f).")
                ],
                "examples": [
                    ("1. View a file", "less file.txt"),
                    ("2. View with line numbers", "less -N file.txt"),
                    ("3. Search inside less", "/search_term (inside the viewer)")
                ],
                "questions": [
                    "How do you quit `less`?",
                    "How do you search forward in `less`?",
                    "What is the advantage of `less` over `cat`?"
                ]
            }
        ]
    },
    {
        "category": "Networking",
        "commands": [
            {
                "name": "ping",
                "desc": "Send ICMP ECHO_REQUEST to network hosts",
                "man_section": "8",
                "long_desc": "The `ping` command uses the ICMP protocol's mandatory ECHO_REQUEST datagram to elicit an ICMP ECHO_RESPONSE from a host or gateway.",
                "flags": [
                    ("-c count", "**Count**. Stop after sending count ECHO_REQUEST packets."),
                    ("-i interval", "**Interval**. Wait interval seconds between sending each packet."),
                    ("-t ttl", "**TTL**. Set the IP Time to Live.")
                ],
                "examples": [
                    ("1. Ping a host", "ping google.com"),
                    ("2. Ping 5 times", "ping -c 5 google.com"),
                    ("3. Ping with specific interval", "ping -i 0.5 google.com")
                ],
                "questions": [
                    "What protocol does `ping` use?",
                    "How do you limit the number of pings?",
                    "What does TTL stand for?"
                ]
            },
            {
                "name": "curl",
                "desc": "Transfer a URL",
                "man_section": "1",
                "long_desc": "The `curl` command is a tool to transfer data from or to a server.",
                "flags": [
                    ("-O", "**Remote name**. Write output to a local file named like the remote file we get."),
                    ("-I", "**Head**. Fetch the HTTP-header only."),
                    ("-L", "**Location**. Follow redirects."),
                    ("-d data", "**Data**. Sends the specified data in a POST request.")
                ],
                "examples": [
                    ("1. Download a file", "curl -O https://example.com/file.zip"),
                    ("2. Check headers", "curl -I https://google.com"),
                    ("3. Follow redirects", "curl -L https://google.com")
                ],
                "questions": [
                    "What does `curl` do?",
                    "How do you save the output to a file with the same name?",
                    "Which flag follows redirects?"
                ]
            }
        ]
    },
    {
        "category": "Archives",
        "commands": [
            {
                "name": "tar",
                "desc": "An archiving utility",
                "man_section": "1",
                "long_desc": "The `tar` command is an archiving utility used to store and extract files from an archive file known as a tarball.",
                "flags": [
                    ("-c", "**Create**. Create a new archive."),
                    ("-x", "**Extract**. Extract files from an archive."),
                    ("-v", "**Verbose**. Verbosely list files processed."),
                    ("-f", "**File**. Use archive file or device ARCHIVE."),
                    ("-z", "**Gzip**. Filter the archive through gzip.")
                ],
                "examples": [
                    ("1. Create a tar.gz archive", "tar -czvf archive.tar.gz /path/to/dir"),
                    ("2. Extract a tar.gz archive", "tar -xzvf archive.tar.gz"),
                    ("3. List contents of an archive", "tar -tvf archive.tar.gz")
                ],
                "questions": [
                    "What does `tar` stand for?",
                    "Which flag creates a new archive?",
                    "How do you compress the archive with gzip?"
                ]
            },
            {
                "name": "zip",
                "desc": "Package and compress (archive) files",
                "man_section": "1",
                "long_desc": "The `zip` command is a compression and file packaging utility.",
                "flags": [
                    ("-r", "**Recursive**. Travel the directory structure recursively."),
                    ("-e", "**Encrypt**. Encrypt the contents of the zip archive."),
                    ("-d", "**Delete**. Delete entries from the zip archive.")
                ],
                "examples": [
                    ("1. Zip a directory", "zip -r archive.zip directory/"),
                    ("2. Zip multiple files", "zip archive.zip file1.txt file2.txt"),
                    ("3. Password protect zip", "zip -e secure.zip file.txt")
                ],
                "questions": [
                    "How do you zip a directory recursively?",
                    "How do you password protect a zip file?",
                    "What is the difference between `tar` and `zip`?"
                ]
            },
            {
                "name": "unzip",
                "desc": "List, test and extract compressed files in a ZIP archive",
                "man_section": "1",
                "long_desc": "The `unzip` command will list, test, or extract files from a ZIP archive.",
                "flags": [
                    ("-l", "**List**. List archive files (short format)."),
                    ("-t", "**Test**. Test archive files."),
                    ("-d dir", "**Directory**. An optional directory to which to extract files.")
                ],
                "examples": [
                    ("1. Unzip a file", "unzip archive.zip"),
                    ("2. List contents without extracting", "unzip -l archive.zip"),
                    ("3. Extract to specific directory", "unzip archive.zip -d /path/to/dest")
                ],
                "questions": [
                    "How do you list contents of a zip file?",
                    "How do you extract to a specific directory?",
                    "What does `unzip -t` do?"
                ]
            }
        ]
    },
    {
        "category": "User & Permissions",
        "commands": [
            {
                "name": "sudo",
                "desc": "Execute a command as another user",
                "man_section": "8",
                "long_desc": "The `sudo` command allows a permitted user to execute a command as the superuser or another user.",
                "flags": [
                    ("-u user", "**User**. Run command as specified user."),
                    ("-i", "**Login**. Run the shell specified by the target user's password database entry as a login shell."),
                    ("-l", "**List**. List user's privileges or check a specific command.")
                ],
                "examples": [
                    ("1. Run command as root", "sudo apt update"),
                    ("2. Switch to root user", "sudo -i"),
                    ("3. Run command as another user", "sudo -u postgres psql")
                ],
                "questions": [
                    "What does `sudo` stand for?",
                    "How do you switch to the root user environment?",
                    "How do you run a command as a specific user?"
                ]
            },
            {
                "name": "whoami",
                "desc": "Print effective userid",
                "man_section": "1",
                "long_desc": "The `whoami` command prints the user name associated with the current effective user ID.",
                "flags": [
                    ("--help", "**Help**. Display this help and exit."),
                    ("--version", "**Version**. Output version information and exit.")
                ],
                "examples": [
                    ("1. Check current user", "whoami")
                ],
                "questions": [
                    "What does `whoami` print?",
                    "Is `whoami` the same as `id -un`?",
                    "When is `whoami` useful?"
                ]
            }
        ]
    }
]

start_index = 16
output_lines = []

for category_data in commands_data:
    category = category_data["category"]
    commands = category_data["commands"]
    
    output_lines.append("\n---\n")
    output_lines.append(f"# {category}\n\n")
    
    # Category Table of Contents
    output_lines.append("| Command | Explanation |\n")
    output_lines.append("|:---|:---|\n")
    
    for cmd in commands:
        idx = start_index + commands.index(cmd)
        name = cmd["name"]
        desc = cmd["desc"]
        man_section = cmd["man_section"]
        
        header_text = f"{idx:02d}. {name} - {desc}"
        slug = header_text.lower().replace(" ", "-").replace(".", "").replace(",", "")
        
        output_lines.append(f"| `{name}` | [{desc}](#{slug}) |\n")

    output_lines.append("\n")

    for cmd in commands:
        idx = start_index
        start_index += 1
        name = cmd["name"]
        desc = cmd["desc"]
        man_section = cmd["man_section"]
        long_desc = cmd["long_desc"]
        flags = cmd["flags"]
        examples = cmd["examples"]
        questions = cmd["questions"]
        
        man_url = f"https://man7.org/linux/man-pages/man{man_section}/{name}.{man_section}.html"
        
        output_lines.append("---\n\n")
        output_lines.append(f"## {idx:02d}. {name} - {desc}\n")
        output_lines.append(f"* <a href=\"{man_url}\" target=\"_blank\">man Page</a>\n\n")
        output_lines.append(f"{long_desc}\n\n")
        
        output_lines.append("#### Common Flags\n\n")
        output_lines.append("| Command Flag | Description |\n")
        output_lines.append("| :--- | :--- |\n")
        for flag, flag_desc in flags:
            output_lines.append(f"| `{flag}` | {flag_desc} |\n")
        output_lines.append("\n")
        
        output_lines.append("#### Examples\n\n")
        for ex_title, ex_code in examples:
            output_lines.append(f"!!! note \"{ex_title}\"\n\n")
            output_lines.append(f"    ```sh\n")
            output_lines.append(f"    {ex_code}\n")
            output_lines.append(f"    ```\n\n")
            
        output_lines.append("#### Questions\n\n")
        for q in questions:
            output_lines.append(f"- {q}\n")
        output_lines.append("\n")

with open("Labs/01-Commands.md", "a") as f:
    f.writelines(output_lines)
