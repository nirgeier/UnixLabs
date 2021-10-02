## Basic scripts

## 01. echo

```sh
#!/bin/bash

# Prints the string “Hello World” to the standard output
echo "Hello World"
```

## 02. Receive Input from User
```sh
#!/bin/bash

echo -n "Enter Something:"
read something

echo "You Entered: $something"
```

## 03. The If Statement
```sh
#!/bin/bash

echo -n "Enter a number: "
read num

if [[ $num -gt 10 ]]
then
echo "Number is greater than 10."
fi
```

## 04. Using the AND Operator
```sh
#!/bin/bash

echo -n "Enter Number:"
read num

if [[ ( $num -lt 10 ) && ( $num%2 -eq 0 ) ]]; then
echo "Even Number"
else
echo "Odd Number"
fi
```

## 05. Using the OR Operator

```sh
#!/bin/bash

echo -n "Enter Number:"
read num

if [[ ( $num -lt 10 ) && ( $num%2 -eq 0 ) ]]; then
echo "Even Number"
else
echo "Odd Number"
fi
```

## 06. Switch statement {switch,case,esac}
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

## 07. Command Line Arguments
```sh
#!/bin/bash
echo "Total arguments : $#"
echo "First Argument = $1"
echo "Second Argument = $2"
```

## 08. #!/bin/bash
- The below example shows how to get command-line arguments with their names.

```sh
#!/bin/bash

for arg in "$@"
do
index=$(echo $arg | cut -f1 -d=)
val=$(echo $arg | cut -f2 -d=)
case $index in
X) x=$val;;
Y) y=$val;;
*)
esac
done
((result=x+y))
echo "X+Y=$result"
```

## 09. Slicing Strings
```sh
#!/bin/bash
Str="Learn Bash Commands from UbuntuPit"
subStr=${Str:0:20}
echo $subStr
```

## 10. Extracting Substrings Using Cut
```sh
#!/bin/bash
Str="Learn Bash Commands from UbuntuPit"
#subStr=${Str:0:20}

subStr=$(echo $Str| cut -d ' ' -f 1-3)
echo $subStr
```

## 11. Test File Existence
```sh
#!/bin/bash
filename=$1
if [ -f "$filename" ]; then
echo "File exists"
else
echo "File does not exist"
fi
```