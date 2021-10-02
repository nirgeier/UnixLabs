# Vim Cheat Sheet

<!-- inPage TOC start -->

---
## Cheat Sheet Highlights:
- [What is Vim?](#what-is-vim)
- [Installation](#installation)
- [Modes](#modes)
- [Most Common Commands](#most-common-commands)
- [File Operations](#file-operations)
- [Cursor Movement](#cursor-movement)
- [Editing Text](#editing-text)
- [Search & Replace](#search--replace)
- [Visual Mode](#visual-mode)
- [Advanced Navigation (Marks & Scrolling)](#advanced-navigation-marks--scrolling)
- [Multiple Windows & Tabs](#multiple-windows--tabs)
- [Macros](#macros)
- [Ex Commands & Ranges](#ex-commands--ranges)
- [Global Commands](#global-commands)
- [Vim Options (Settings)](#vim-options-settings)

---

## What is Vim?

**Vim** (Vi IMproved) is a highly configurable text editor built to enable efficient text editing. It is an improved version of the `vi` editor distributed with most UNIX systems.

Vim is known for being:
*   **Modal**: It has different modes for inserting text, navigating, and executing commands.
*   **Keyboard-centric**: Almost everything can be done without a mouse.
*   **Ubiquitous**: Available on almost every Linux/Unix system.

---

## Installation

Most Linux distributions come with `vi` installed by default, but it might be the lightweight version. To get the full `vim` experience:

| OS | Command |
| :--- | :--- |
| **Ubuntu / Debian** | `sudo apt update && sudo apt install vim` |
| **CentOS / RHEL** | `sudo yum install vim` |
| **Fedora** | `sudo dnf install vim` |
| **macOS** | `brew install vim` (or use built-in `vi`) |
| **Arch Linux** | `sudo pacman -S vim` |

---

## Modes

Vim has several modes. Understanding them is key to using Vim.

| Mode | Description | How to access |
| :--- | :--- | :--- |
| **Normal** | The default mode for navigation and manipulation. | Press `Esc` |
| **Insert** | For typing text. | Press `i`, `a`, `o` |
| **Visual** | For selecting blocks of text. | Press `v`, `V`, `Ctrl+v` |
| **Command** | For saving, quitting, and settings. | Press `:` in Normal mode |

---

## Most Common Commands

These are the absolute essentials you need to survive in Vim.

| Command | Action |
| :--- | :--- |
| `i` | Switch to **Insert Mode** (start typing) |
| `Esc` | Switch to **Normal Mode** (exit insert mode) |
| `:w` | **Save** the file |
| `:q` | **Quit** Vim |
| `:wq` | **Save and Quit** |
| `:q!` | **Force Quit** (discard changes) |
| `u` | **Undo** last change |
| `Ctrl + r` | **Redo** |

---

## File Operations

Commands for managing the file itself (saving, quitting, opening).

| Command | Action |
| :--- | :--- |
| `:w` | Save changes |
| `:w <filename>` | Save as a new file |
| `:q` | Quit (fails if there are unsaved changes) |
| `:q!` | Quit and discard unsaved changes |
| `:wq` or `ZZ` | Save and quit |
| `:e <filename>` | Open a file for editing |
| `:sav <filename>` | Save file as `<filename>` and continue editing it |

---

## Cursor Movement

Navigate through the file quickly without leaving the keyboard.

### Basic Movement
| Command | Action |
| :--- | :--- |
| `h` | Move Left |
| `j` | Move Down |
| `k` | Move Up |
| `l` | Move Right |

### Line & File Navigation
| Command | Action |
| :--- | :--- |
| `0` (zero) | Jump to **start** of the line |
| `$` | Jump to **end** of the line |
| `gg` | Jump to **first line** of the file |
| `G` | Jump to **last line** of the file |
| `:n` | Jump to line number `n` (e.g., `:10`) |
| `nG` | Jump to line number `n` |

### Word Movement
| Command | Action |
| :--- | :--- |
| `w` | Jump forward to start of next **word** |
| `b` | Jump backward to start of previous **word** |
| `e` | Jump forward to **end** of word |

---

## Editing Text

Commands to manipulate text (delete, copy, paste, change).

### Inserting Text
| Command | Action |
| :--- | :--- |
| `i` | Insert before cursor |
| `I` | Insert at beginning of line |
| `a` | Append after cursor |
| `A` | Append at end of line |
| `o` | Open new line **below** and insert |
| `O` | Open new line **above** and insert |

### Deleting & Changing
| Command | Action |
| :--- | :--- |
| `x` | Delete character under cursor |
| `dw` | Delete word |
| `dd` | Delete **entire line** |
| `D` | Delete from cursor to end of line |
| `r` | Replace single character |
| `cw` | Change word (delete word and enter insert mode) |
| `cc` | Change entire line |

### Copy & Paste
| Command | Action |
| :--- | :--- |
| `yy` | **Yank** (copy) current line |
| `yw` | Yank word |
| `p` | **Paste** after cursor |
| `P` | Paste before cursor |

---

## Search & Replace

Find text and replace it efficiently.

| Command | Action |
| :--- | :--- |
| `/pattern` | Search **forward** for `pattern` |
| `?pattern` | Search **backward** for `pattern` |
| `n` | Jump to **next** match (in same direction) |
| `N` | Jump to **previous** match (in reverse direction) |
| `*` | Search **forward** for word under cursor |
| `#` | Search **backward** for word under cursor |
| `:%s/old/new/g` | Replace **all** occurrences of `old` with `new` in file |
| `:%s/old/new/gc` | Replace all with **confirmation** |
| `:noh` | **Clear** search highlights |

---

## Visual Mode

Select text to perform actions on specific blocks.

| Command | Action |
| :--- | :--- |
| `v` | Start character-wise visual mode |
| `V` | Start line-wise visual mode |
| `Ctrl + v` | Start block-wise visual mode |
| `d` | Delete selection |
| `y` | Yank (copy) selection |
| `>` | Indent selection |
| `<` | Un-indent selection |

---

## Advanced Navigation (Marks & Scrolling)

Move around the file faster.

### Scrolling
| Command | Action |
| :--- | :--- |
| `Ctrl + u` | Scroll **Up** half a page |
| `Ctrl + d` | Scroll **Down** half a page |
| `Ctrl + f` | Scroll **Forward** one full page |
| `Ctrl + b` | Scroll **Backward** one full page |

### Marks
| Command | Action |
| :--- | :--- |
| `ma` | Set mark **a** at current cursor location |
| `'a` | Jump to line of mark **a** |
| `` `a `` | Jump to exact position (line & column) of mark **a** |
| `''` | Jump back to the line you were on before the last jump |

---

## Multiple Windows & Tabs

Work on multiple files or parts of a file simultaneously.

### Split Windows
| Command | Action |
| :--- | :--- |
| `:sp` | Split window **horizontally** |
| `:vsp` | Split window **vertically** |
| `Ctrl + w` then `w` | Switch between windows |
| `Ctrl + w` then `q` | Close current window |

### Tabs
| Command | Action |
| :--- | :--- |
| `:tabnew` | Open a new tab |
| `:tabn` or `gt` | Go to **next** tab |
| `:tabp` or `gT` | Go to **previous** tab |

---

## Macros

Record and replay complex sequences of commands.

| Command | Action |
| :--- | :--- |
| `qa` | Start recording macro into register **a** |
| `q` | Stop recording |
| `@a` | Play back macro **a** |
| `@@` | Replay the last executed macro |

---

## Ex Commands & Ranges

Ex commands allow you to execute commands on specific lines or ranges.

| Command | Action |
| :--- | :--- |
| `:10,20d` | Delete lines 10 through 20 |
| `:%d` | Delete **all** lines in the file |
| `:.,$d` | Delete from current line (`.`) to end of file (`$`) |
| `:1,10w newfile.txt` | Write lines 1 to 10 to `newfile.txt` |
| `:5r file.txt` | Read `file.txt` and insert it after line 5 |
| `:%s/foo/bar/g` | Substitute `foo` with `bar` in the entire file (`%`) |
| `:5,10s/foo/bar/g` | Substitute `foo` with `bar` in lines 5-10 |

---

## Global Commands

The `:g` (global) command executes a command on all lines that match a pattern.
Syntax: `:g/pattern/command`

| Command | Action |
| :--- | :--- |
| `:g/pattern/d` | Delete all lines matching `pattern` |
| `:g!/pattern/d` or `:v/pattern/d` | Delete all lines **NOT** matching `pattern` |
| `:g/^$/d` | Delete all empty lines |
| `:g/error/p` | Print all lines containing "error" |
| `:g/pattern/m$` | Move all matching lines to the end of the file |
| `:g/pattern/t$` | Copy (transfer) all matching lines to the end of the file |

---

## Vim Options (Settings)

Customize Vim's behavior on the fly. These can also be added to your `~/.vimrc` file.

### Display Options
| Command | Description |
| :--- | :--- |
| `:set number` | Show line numbers |
| `:set nonumber` | Hide line numbers |
| `:set relativenumber` | Show relative line numbers |
| `:set wrap` | Enable line wrapping |
| `:set nowrap` | Disable line wrapping |
| `:syntax on` | Enable syntax highlighting |

### Search Options
| Command | Description |
| :--- | :--- |
| `:set hlsearch` | Highlight search results |
| `:set nohlsearch` | Disable search highlighting |
| `:set incsearch` | Show matches as you type |
| `:set ignorecase` | Ignore case when searching |
| `:set smartcase` | Ignore case unless uppercase letters are used |

### Indentation & Tabs
| Command | Description |
| :--- | :--- |
| `:set autoindent` | Copy indentation from previous line |
| `:set expandtab` | Use spaces instead of tabs |
| `:set tabstop=4` | Set tab width to 4 spaces |
| `:set shiftwidth=4` | Set indentation width to 4 spaces |

### Other Useful Settings
| Command | Description |
| :--- | :--- |
| `:set mouse=a` | Enable mouse support |
| `:set clipboard=unnamedplus` | Use system clipboard |
| `:set paste` | Enable paste mode (prevents auto-indenting when pasting) |
| `:set nopaste` | Disable paste mode |
