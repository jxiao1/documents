Shell Variables
===============

**Internal Variables**::

    $SHELL                  Current shell name, such as "/bin/bash"
    $PPID                   Parent PID
    $UID                    User ID, specially, root UID is zero
    $RANDOM                 Return a random number
    $IFS                    shell separator character, default value is "\ "
    $PATH                   System path
    $PWD                    Current directory
    $HOME                   Home directory
    $SECONDS                time from it begin to run
    $LINENO                 Current line number
    $FUNCNAME               Current function name
    $BASH_LINENO            Line number where this function is called

    $$                      Current PID
    $!                      PID of the last process which running in the background
    $#                      Number of parameters
    $?                      Command or script return value
    $0                      Script or function name which is called.
    $1                      Ther first parameter, $N means the Nth parameter
    $*                      all parameters
    “$*”                    "$1 $2 $3 ..."
    “$@”                    "$1" "$2" "$3" ...
　　

**Wildcard Variables**::

    [[:alnum:]]             all number characters
    [[:digit:]]             all number characters
    [[:xdigit:]]            all hex number characters
    [[:alpha:]]             all letter characters
    [[:lower:]]             all lower letter characters
    [[:upper:]]             all upper letter characters
    [[:punct:]]             all punctuation characters
    [[:graph:]]             all nonblank characters
    [[:space:]]             all space characters
    [[:blank:]]             all blank characters, such as whitespace and tab
    [[:cntrl:]]             all control characters
    [[:print:]]             all printable characters


**Wildcard Variables**::

    $variable              variable value
    ${variable}            variable value, separate name from the following letters
    ${variable:n:m}        part of variable string, start at n, lenght is m
    ${variable:n}          part of variable string, from the n to the end
    ${#variable}           length of the variable string

    ${variable:?message}   If the variable exists and is not NULL, returen it,
                           otherwise output the message and exit the script.
    ${variable:=word}      If the variable exists and is not NULL, returen it,
                           otherwise set the variable to word and return the word.
    ${variable:-word}      If the variable exists and is not NULL, returen it,
                           otherwise return ther word, variable is not changed.
    ${variable:+word}      If the variable exists and is not NULL, return the word,
                           otherwise return NULL.

    ${variable%.*}         From right to left, match ".*", then remove this part.
                           e.g. if variable="file-v1.0.txt", then return "file-v1.0"
    ${variable%%.*}        From right to left, match ".*" as long as possible, then
                           remove this part. e.g. if variable="file-v1.0.txt",
                           then return "file-v1"
    ${variable#*.}         From left to right, match "*.", then remove this part,
                           e.g. if variable="file-v1.0.txt", then return "0.txt"
    ${variable##*.}        From left to right, match "*." as long as possible, then
                           remove this part. e.g. if variable="file-v1.0.txt",
                           then return ".txt"
    ${variable/patt/str}   Replace pattern matching part with string.
    ${variable//patt/str}  Replace pattern matching part (as long as possible) with string.


**Variables expression**::

    let result=no1+no2
    let i++
    result=$[ $no1 +  $no2 ]
    result=$(($no1 +  $no2))
    result=`expr 3+4`
    result=$(expr $no1 + 5)

