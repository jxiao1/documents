JavaScript Regular Expressions
==============================

Just as string literals are specified as characters within quotation marks,
regular expression literals are specified as characters within a pair of slash ( / ) characters.

::

    var pattern = /s$/;
    var pattern = new RegExp("s$");
    var pattern = new RegExp("\\d{5}", "g");

    // RegExp can create regular expression dynamically in runtime
    var something;               // Maybe some thing from user.
    var pattern = new RegExp(something)


Regular-expression literal characters
-------------------------------------
::

    =============== ================================================================
    Character       Matches 
    =============== ================================================================
    Alphanumeric    character Itself
    \0              The NUL character (\u0000)
    \t              Tab (\u0009 )
    \n              Newline ( \u000A )
    \v              Vertical tab ( \u000B )
    \f              Form feed ( \u000C )
    \r              Carriage return ( \u000D )
    \xnn            The hexadecimal number; \x0A == \n
    \uxxxx          The hexadecimal number Unicode; \u0009 == \t
    \cX             The control character ^X ; \cJ == \n
    =============== ================================================================


Regular expression character classes
------------------------------------
::

    =============== ================================================================
    Character       Matches 
    =============== ================================================================
    [...]           Any one character between the brackets.
    [^...]          Any one character not between the brackets.
    .               Any character except newline or another Unicode line terminator.
    \w              Any ASCII word character.
    \W              Any character that is not an ASCII word character.
    \s              Any Unicode whitespace character.
    \S              Any character that is not Unicode whitespace.
    \d              Any ASCII digit. Equivalent to [0-9] .
    \D              Any character other than an ASCII digit. Equivalent to [^0-9] .
    [\b]            A literal backspace (special case).
    =============== ================================================================


Regular expression repetition characters
----------------------------------------
::

    =============== ================================================================
    Character       Meaning 
    =============== ================================================================
    {n, m}          Match previous item at least n times but no more than m times.
    {n,}            Match the previous item n or more times.
    {n}             Match exactly n occurrences of the previous item.
    ?               Match zero or one occurrences of the previous item. {0,1}
    +               Match one or more occurrences of the previous item. {1,}
    *               Match zero or more occurrences of the previous item. {0,}
    =============== ================================================================

.. note::
    The repetition characters listed above table match as many times as possible
    while still allowing any following parts of the regular expression to match.
    We say that this repetition is “greedy.”

    It is also possible to specify that repetition should be done in a nongreedy
    way. Simply follow the repetition character or characters with a question
    mark: ?? , +? or even {1,5}? .

    Match of /a+?b/ in 'aaab' still return 'aaab' because start at first 'a'.


Regular expression alternation, grouping, and reference characters
------------------------------------------------------------------
::

    =============== ================================================================
    Character       Meaning 
    =============== ================================================================
    |               Alternation. Match either the subexpression to the left or
                    the subexpression to the right.
    (...)           Grouping. Group items into a single unit that can be used with
                    * , + , ? , | , and so on. Also remember the characters
                    that match this group for use with later references.
    (?:...)         Grouping only. Group items into a single unit, but do not
                    remember the characters that match this group.
    \n              Match the same characters that were matched when group number n
                    was first matched. 
                    Groups are subexpressions within (possibly nested) parentheses.
                    Group numbers are assigned by counting left parentheses from
                    left to right. Groups formed with (?: are not numbered.
    =============== ================================================================

Examples::

    /ab|cd|ef/          // matches “ab” or “cd” or “ef”.
    /\d{3}|[a-z]{4}/    // matches either three digits or four lowercase letters.


    /java(script)?/     // matches “java” followed by the optional “script”.
    /(ab|cd)+|ef/       // matches either the string “ef” or one or more
                        // repetitions of either of the strings “ab” or “cd”.

    /([Jj]ava([Ss]cript)?)\sis\s(fun\w*)/    // ([Ss]cript) is referred to as \2        
    /(['"][^'"]*\1)                          // matches '.*' or ".*"


Regular-expression anchor characters
------------------------------------
::

    =============== ================================================================
    Character       Meaning 
    =============== ================================================================
    ^               Match beginning of string. (or line in multiline searches)
    $               Match the end of string. (end of a line in multiline searches)
    \b              Match a word boundary. (Note: [\b] matches backspace.)
    \B              Match a position that is not a word boundary.
    (?=p)           A positive lookahead assertion.
                    Require that the following characters match the pattern p,
                    but do not include those characters in the match.
    (?!p)           A negative lookahead assertion.
                    Require that the following characters don't match the pattern p.
    =============== ================================================================

Examples::

    /\B[Ss]cript/       // Matches "JavaScript" and "postscript", but not "script".

    /[Jj]ava([Ss]cript)?(?=\:)/         // Matches the word "JavaScript" in
                        "JavaScript: The Definitive Guide", but it does not match
                        "Java" in "Java in a Nutshell".

    /Java(?!Script)/    // Matches "Java" in "JaveBeans" but null in "JavaScript"


Regular-expression flags
------------------------
::

    =============== ================================================================
    Character       Meaning 
    =============== ================================================================
    i               Perform case-insensitive matching.
    g               Perform a global match—that is, find all matches.
    m               Multiline mode. ^/$ matche beginning/end of line or string.
    =============== ================================================================

Examples::

    /java$/im   // Matches “java” as well as “Java\nis fun”


RegExp Properties
-----------------

**source**:
Read-only string that contains the text of the regular expression.

**global**:
Read-only boolean value that specifies whether the regular expression has the g flag.

**ignoreCase**:
Read-only boolean value that specifies whether the regular expression has the i flag.

**multiline**:
Read-only boolean value that specifies whether the regular expression has the m flag.

**lastIndex**:
Read/write integer. For patterns with the g flag, it stores the position in the string
at which the next search is to begin. It is used by the exec() and test() methods


RegExp Methods
--------------

**exec()**::

    var pattern = /Java/g;
    var text = "JavaScript is more fun than Java!";
    var result;
    while((result = pattern.exec(text)) != null) {
        alert("Matched '" + result[0] + "'" +
        " at position " + result.index +
        "; next search begins at " + pattern.lastIndex);
    }

**test()**::

    var pattern = /java/i;
    pattern.test("JavaScript"); // Returns true
