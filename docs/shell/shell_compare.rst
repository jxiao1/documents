Shell Test And Compoare
=======================

**File test**::

    -b 	File is block special device (for files like /dev/hda1)
    -c 	File is character special (for files like /dev/tty)
    -d 	File is a directory
    -e 	File exists
    -f 	File is a regular file
    -g 	File has its set-group-ID bit set
    -h 	File is a symbolic link (same as -L)
    -G 	File is owned by the effective group ID
    -k 	File has its sticky bit set
    -L 	File is a symbolic link (same as -h)
    -O 	File is owned by the effective user ID
    -p 	File is a named pipe
    -r 	File is readable
    -s 	File has a size greater than zero
    -S 	File is a socket
    -u 	File has its set-user-ID bit set
    -w 	File is writable
    -x 	File is executable


**Variable Test**::

    -lt 	< 		Less than
    -le 	<= 		Less than or equal to
    -gt 	> 		Greater than
    -ge 	>= 		Greater than or equal to
    -eq 	=, == 		Equal to
    -ne 	!= 		Not equal to

    -n "$var"               Variable is not empty
    -z "$var"               Varibale is empty


**Examples**::

    if [ -r $FILE -a -w $FILE ]
    if [ -z "$V1" -o -z "${V2:=YIKES}" ]
    if [[ "${MYFILENAME}" == *.jpg ]]
    if [[ "$FN" == *.@(jpg|jpeg) ]]
    if [[ "$CDTRACK" =~ "([[:alpha:][:blank:]]*)- ([[:digit:]]*) - (.*)$" ]]

