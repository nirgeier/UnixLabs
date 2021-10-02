#!/bin/bash

function Greet() {
  str="Hello $name"
  echo $str
}

echo "-> what's your name?"
read name

val=$(Greet)
echo -e "-> $val"