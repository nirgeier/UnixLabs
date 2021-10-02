#!/bin/bash

### Write the example file which we will use
cat << EOF > file.txt
Student-Id	Name		Major			Grade
1		    John		Biology		    78
2		    George		Literature		82
3		    Paul		Music			94
4		    Ringo		Music			89 
EOF

# Print out the example file
#cat file.txt


#### AWK examples:
# Print the whole file
awk '{print $0}' file.txt

# Print the 2nd and 3rd columns with tab between each row
awk '{print $2 "\t" $3}' file.txt

# Print out all student whos majos is music (the whole line)
awk '/Music/ {print $0}' file.txt

# Counting and Printing Matched Pattern
awk '/Music/{++counter} END {print "Counter = " , counter}' file.txt