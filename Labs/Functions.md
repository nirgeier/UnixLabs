## Functions

## 01. Functions
- Here we’ve added two numbers just like before. 
- But here, we’ve done the work using a function called Add. 
- So whenever you need to add again, you can just call this function instead of writing that section again.

```sh
#!/bin/bash
function Add()
{
echo -n "Enter a Number: "
read x
echo -n "Enter another Number: "
read y
echo "Adiition is: $(( x+y ))"
}

Add
```

## 02. Functions with return values
```sh
#!/bin/bash

function Greet() {
  str="Hello $name"
  # Echo the input to the user
  echo $str
}

# Print the question 
echo "-> what's your name?"

# Read the answer
read name

# print teh name
val=$(Greet)

echo -e "-> $val"
```