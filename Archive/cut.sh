#!/bin/bash

export FILE_NAME=trace.log

### Write the example file which we will use
cat << EOF > $FILE_NAME
03/22 08:51:01 INFO    :.main: *************** RSVP Agent started ***************
03/22 08:51:01 INFO    :...locate_configFile: Specified configuration file: /u/user10/rsvpd1.conf
03/22 08:51:01 INFO    :.main: Using log level 511
03/22 08:51:01 INFO    :..settcpimage: Get TCP images rc - EDC8112I Operation not supported on socket.
03/22 08:51:01 INFO    :..settcpimage: Associate with TCP/IP image name = TCPCS
03/22 08:51:02 INFO    :..reg_process: registering process with the system
03/22 08:51:02 INFO    :..reg_process: attempt OS/390 registration
03/22 08:51:02 INFO    :..reg_process: return from registration rc=0
03/22 08:51:03 TRACE   :...read_physical_netif: Home list entries returned = 7
03/22 08:51:03 INFO    :...read_physical_netif: index #0, interface VLINK1 has address 129.1.1.1, ifidx 0
03/22 08:51:03 INFO    :...read_physical_netif: index #1, interface TR1 has address 9.37.65.139, ifidx 1
03/22 08:51:03 INFO    :...read_physical_netif: index #2, interface LINK11 has address 9.67.100.1, ifidx 2
03/22 08:51:03 INFO    :...read_physical_netif: index #3, interface LINK12 has address 9.67.101.1, ifidx 3
03/22 08:51:03 INFO    :...read_physical_netif: index #4, interface CTCD0 has address 9.67.116.98, ifidx 4
03/22 08:51:03 INFO    :...read_physical_netif: index #5, interface CTCD2 has address 9.67.117.98, ifidx 5
03/22 08:51:04 INFO    :...read_physical_netif: index #6, interface LOOPBACK has address 127.0.0.1, ifidx 0
03/22 08:51:04 INFO    :....mailslot_create: creating mailslot for timer
03/22 08:51:04 INFO    :...mailbox_register: mailbox allocated for timer
03/22 08:51:04 INFO    :.....mailslot_create: creating mailslot for RSVP
03/22 08:51:04 INFO    :....mailbox_register: mailbox allocated for rsvp
03/22 08:51:06 INFO    :.....mailslot_create: creating mailslot for RSVP via UDP
03/22 08:51:06 WARNING :.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
03/22 08:51:05 INFO    :....mailbox_register: mailbox allocated for rsvp-udp
03/22 08:51:05 TRACE   :..entity_initialize: interface 129.1.1.1, entity for rsvp allocated and initialized
03/22 08:51:05 INFO    :.....mailslot_create: creating mailslot for RSVP
03/22 08:51:05 INFO    :....mailbox_register: mailbox allocated for rsvp
03/22 08:51:05 INFO    :.....mailslot_create: creating mailslot for RSVP via UDP
03/22 08:51:05 WARNING :.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
03/22 08:51:05 INFO    :....mailbox_register: mailbox allocated for rsvp-udp
03/22 08:51:05 TRACE   :..entity_initialize: interface 9.37.65.139, entity for rsvp allocated and initialized
03/22 08:51:05 INFO    :.....mailslot_create: creating mailslot for RSVP
03/22 08:51:06 INFO    :....mailbox_register: mailbox allocated for rsvp
03/22 08:51:06 INFO    :.....mailslot_create: creating mailslot for RSVP via UDP
03/22 08:51:06 WARNING :.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
03/22 08:51:06 INFO    :....mailbox_register: mailbox allocated for rsvp-udp
03/22 08:51:06 TRACE   :..entity_initialize: interface 9.67.100.1, entity for rsvp allocated and initialized
03/22 08:51:06 INFO    :.....mailslot_create: creating mailslot for RSVP
03/22 08:51:06 INFO    :....mailbox_register: mailbox allocated for rsvp
03/22 08:51:06 INFO    :.....mailslot_create: creating mailslot for RSVP via UDP
03/22 08:51:07 WARNING :.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
03/22 08:51:07 INFO    :....mailbox_register: mailbox allocated for rsvp-udp
03/22 08:51:07 TRACE   :..entity_initialize: interface 9.67.101.1, entity for rsvp allocated and initialized
03/22 08:51:07 INFO    :.....mailslot_create: creating mailslot for RSVP
03/22 08:51:07 INFO    :....mailbox_register: mailbox allocated for rsvp
03/22 08:51:07 INFO    :.....mailslot_create: creating mailslot for RSVP via UDP
03/22 08:51:08 INFO    :....mailbox_register: mailbox allocated for rsvp-udp
03/22 08:51:08 TRACE   :..entity_initialize: interface 9.67.116.98, entity for rsvp allocated and initialized
03/22 08:51:08 INFO    :.....mailslot_create: creating mailslot for RSVP
03/22 08:51:08 INFO    :....mailbox_register: mailbox allocated for rsvp
03/22 08:51:08 INFO    :.....mailslot_create: creating mailslot for RSVP via UDP
03/22 08:51:08 INFO    :....mailbox_register: mailbox allocated for rsvp-udp
03/22 08:51:08 TRACE   :..entity_initialize: interface 9.67.117.98, entity for rsvp allocated and initialized 
EOF


#### Cut examples:

# Extract only the 2nd & 3rd column (field) of each line time
cut -d " " -f 2,3 $FILE_NAME

# Extract only the log trace levels and remove duplications
cut -d " " -f 3 $FILE_NAME | sort | uniq

# Count the number of each log type
# INFO = 41
# TRACE = 7
# WARNING = 4

# Simple solution:
echo -e INFO = $(cut -d ' ' -f 3 $FILE_NAME | grep INFO | wc -l)
echo -e TRACE = $(cut -d ' ' -f 3 $FILE_NAME | grep TRACE | wc -l)
echo -e WARNING = $(cut -d ' ' -f 3 $FILE_NAME | grep WARNING | wc -l)

###
### Advanced solution using dynamic for loop:
###

### Extract the log levels
LOG_LEVEL=$(cut -d " " -f 3 $FILE_NAME | sort | uniq)

### Loop over each log level and count entries
for LEVEL in $LOG_LEVEL
do
    echo -e $LEVEL = $(cut -d ' ' -f 3 $FILE_NAME | grep $LEVEL | wc -l)
done


### Extract IP addresses
grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" $FILE_NAME | sort | uniq