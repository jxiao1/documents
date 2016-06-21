JavaScript Types and Variables
==============================

Examples::

    const pi = 3.1415926;  // const value cannot be changed
    var a = 'test';
    var b = 'test';
    a == b ;           // true, Primitive type only compare value

    var a = {x: 1};
    var a = {x: 1};
    a == b             // false

    c = a;
    c.x = 2;
    a.x;               // => 2, object is reference type
    a === c;           // true

    // 'let' defines block level values in loop or function.
    for (let i=1; i<len; i++) { ...} 

    [x, y] = [1, 2]                                // x=1, y=2
    [x, y] = [y, x]                                // switch x and y
    [a, b, c] = [1, 2]                             // a=1, b=2, c=undefined
    [a, [b, c]] = [1, [2,3], 4]                    // a=1, b=2, c=3
    {r: red, g:green, b:blue} = {r:0, g:255, b:0}; // red=0, green=255, blue=0

    var data=[1, 2, -3];
    var squares = [x*x for each (x in data) if (x>=0)] // squares = [1, 4]


Primitive/Object Type
---------------------

**Primitive Type:**

- number
- string
- boolean
- null
- undefined

**Object Type:**

- object/class
- array
- function
- date
- regexp
- error


Mutable/Immutable Type
----------------------

**Mutable Type:**

- object
- array

**Immutable Type:**

- number
- string
- boolean
- null
- undefined


Number
------
::

    0 === -0       # true
    (0.3 - 0.2) == (0.2 -0.1) # False

    Math.pow(2,53)          // => 9007199254740992: 2 to the power 53
    Math.round(.6)          // => 1.0: round to the nearest integer
    Math.ceil(.6)           // => 1.0: round up to an integer
    Math.floor(.6)          // => 0.0: round down to an integer
    Math.abs(-5)            // => 5: absolute value
    Math.max(x,y,z)         // Return the largest argument
    Math.min(x,y,z)         // Return the smallest argument
    Math.random()           // Pseudo-random number x where 0 <= x < 1.0
    Math.PI                 // π: circumference of a circle / diameter
    Math.E                  // e: The base of the natural logarithm
    Math.sqrt(3)            // The square root of 3
    Math.pow(3, 1/3)        // The cube root of 3
    Math.sin(0)             // Trigonometry: also Math.cos, Math.atan, etc.
    Math.log(10)            // Natural logarithm of 10
    Math.log(100)/Math.LN10 // Base 10 logarithm of 100
    Math.log(512)/Math.LN2  // Base 2 logarithm of 512
    Math.exp(3)             // Math.E cubed


Date
----
::

    var then = new Date(2010, 0, 1);  // The 1st day of the 1st month of 2010
    var later = new Date(2010, 0, 1, 17, 10, 30);
    var now = new Date();       // The current date and time
    var elapsed = now - then;   // Date subtraction: interval in milliseconds
    later.getFullYear()         // => 2010
    later.getMonth()            // => 0: zero-based months
    later.getDate()             // => 1: one-based days
    later.getDay()              // => 5: day of week. 0 is Sunday 5 is Friday.
    later.getHours()            // => 17: 5pm, local time
    later.getUTCHours()         // -> hours in UTC time; depends on timezone
    later.toString()            // => "Fri Jan 01 2010 17:10:30 GMT-0800 (PST)"
    later.toUTCString()         // => "Sat, 02 Jan 2010 01:10:30 GMT"
    later.toLocaleDateString()  // => "01/01/2010"
    later.toLocaleTimeString()  // => "05:10:30 PM"
    later.toISOString()         // => "2010-01-02T01:10:30.000Z"; ES5 only


String
------
http://www.w3school.com.cn/jsref/jsref_obj_string.asp

In ECMAScript 3, string literals must be written on a single line.
In ECMAScript 5, however, you can break a string literal across multiple lines
by ending each line but the last with a backslash ( \ ).
In ECMAScript 5, strings can be treated like read-only arrays, and you
can access individual characters from a string using square brackets.

Basic Functions::

    var s = "Hello, " + "world";
    s.charAt(0)                 // => "h": the first character.
    s.charAt(s.length-1)        // => "d": the last character.
    s.substring(1,4)            // => "ell": the 2nd, 3rd and 4th
    s.slice(1,4)                // => "ell": same thing
    s.slice(-3)                 // => "rld": last 3 characters
    s.indexOf("l")              // => 2: position of first letter
    s.lastIndexOf("l")          // => 10: position of last letter
    s.indexOf("l", 3)           // => 3: position of first "l" at or after 3
    s.split(", ")               // => ["hello", "world"] split into substrings
    s.replace("h", "H")         // => "Hello, world": replaces all instances
    s.toUpperCase()             // => "HELLO, WORLD"
    s[0]                        // => "h"
    s[s.length-1]               // => "d"
    s.search(/world/);          // => 7, first position
    s.match(/l+/g)              // => ["ll", "l"], 'g' means return all matches
    
Advance Usage::

    "1, 2, 3, 4, 5".split(/\s*,\s*/);   // Returns ["1","2","3","4","5"]

    var s = 'My name is "John"' ;       // $1 refer to the first matches
    s.replace(/"([^'"]*)"/g, "'$1'")    // => My name is 'John'

    "1 plus 2 equals 3".match(/\d+/g)   // returns ["1", "2", "3"]
    "1 plus 2 equals 3".match(/\d+/)    // returns ["1"]
    "1 plus 2 equals 3".match(/(\d+)/g) // returns ["1", "2", "3"]
    "1 plus 2 equals 3".match(/(\d+)/)  // returns ["1", "1"], the first matches and content in "()" in turn

    var url_pattern = /(\w+):\/\/([\w.]+)\/(\S*)/;
    var text = "Visit my blog at http://www.example.com/~david";
    var result = text.match(url_pattern);
    if (result != null) {
        var fullurl = result[0];    // Contains "http://www.example.com/~david"
        var protocol = result[1];   // Contains "http"
        var host = result[2];       // Contains "www.example.com"
        var path = result[3];       // Contains "~david"
    }
    

Boolean
-------

All other values, including all objects (and arrays) convert to, and work like, true.
Except the following false values::

    undefined    null    0    -0    NaN    ""

    null == undefined  // true
    0 == false         // true
    "0" == 0           // true

.. note::
    null is a language keyword and undefined is a predefined global variable.
    You might consider undefined to represent a system-level, unexpected, or
    error-like absence of value and null to represent program-level, normal,
    or expected absence of value.


Type Conversions
----------------
::

    10 + " objects"    // "10 objects"
    "7" * "4"          // 28
    1 - ""             // 1
    1 - "x"            // NaN

    Number("3")        // 3
    String(false)      // "false"
    Boolean([])        // true
    Object(3)          // new Number(3)

    x + ""             // equal to String(x)
    +x                 // qeual to Number(x)
    !!x                // equal to Boolean(x)

    var n = 17;
    n.toString(2)      // "10001"
    n.toString(16)     // "11"

    var n = 123456.789
    n.toFixed(0)       // 123457
    n.toFixed(2)       // 123456.79
    n.toFixed(5)       // 123456.78900
    n.toExponential(1) // "1.2e+5"
    n.toPrecision(4)   // "1.235e+5"

    parseInt("3 blind mice")     //3
    parseFloat(" 3.14 meters")   // 3.14
    parseInt("0xFF")             //255
    parseInt(".1")               // NaN
    parseInt("0.1")              // 0
    parseFloat(".1")             // 0.1
    parseFloat("$12.34")         // NaN
    parseInt("11", 2)            // 3
    parseInt("11", 16)           // 17

    [1,2,3].toString()           // "1,2,3"

    
Special Global Number Variables
-------------------------------

**Infinity**

* Number.POSITITVE_INFINITY
* 1/0
* Number.MAX_VALUE + 1

**-Infinity**

* Number.NEGATIVE_INFINITY
* -1/0
* -Number.MAX_VALUE - 1

**NaN**

* 0/0

.. Note:: 
    | isNaN(x)       # true if x != x, that means x is NaN 
    | isFinite(x)    # true if x is not NaN, Infinity, -Infinity
