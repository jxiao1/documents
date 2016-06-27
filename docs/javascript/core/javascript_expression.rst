JavaScript Expression
=====================

Operator Overview
-----------------

The following operators re arranged in order from high precedence to low
precedence, with horizontal lines separating groups of operators at the
same precedence level::

    ============ ============================ ==== ==== ==================
    Operator     Operation                    A    N    Types
    ============ ============================ ==== ==== ==================
    ++           Pre- or post-increment       R    1       lval -> num
    --           Pre- or post-decrement       R    1       lval -> num
    -            Negate number                R    1        num -> num
    +            Convert to number            R    1        num -> num
    ~            Invert bits                  R    1        int -> int
    !            Invert boolean value         R    1       bool -> bool
    delete       Remove a property            R    1       lval -> bool
    typeof       Determine type of operand    R    1        any -> str
    void         Return undefined value       R    1        any -> undef
    ----------------------------------------------------------------------
    * / %        Multiply, divide, remainder  L    2    num,num -> num
    ----------------------------------------------------------------------
    +  -         Add, subtract                L    2    num,num -> num
    +            Concatenate strings          L    2    str,str -> str
    ----------------------------------------------------------------------
    <<           Shift left                   L    2    int,int -> int
    >>           Shift right with sign        L    2    int,int -> int
    >>>          Shift right with zero        L    2    int,int -> int
    ----------------------------------------------------------------------
    < <= > >=    Compare in numeric order     L    2    num,num -> bool
    < <= > >=    Compare in alphabetic order  L    2    str,str -> bool
    instanceof   Test object class            L    2    obj,func-> bool
    in           Test whether property exists L    2    str,obj -> bool
    ----------------------------------------------------------------------
    ==           Test for equality            L    2    any,any -> bool
    !=           Test for inequality          L    2    any,any -> bool
    ===          Test for strict equality     L    2    any,any -> bool
    !==          Test for strict inequality   L    2    any,any -> bool
    ----------------------------------------------------------------------
    &            Compute bitwise AND          L    2    int,int -> int
    ----------------------------------------------------------------------
    ^            Compute bitwise XOR          L    2    int,int -> int
    ----------------------------------------------------------------------
    |            Compute bitwise OR           L    2    int,int -> int
    ----------------------------------------------------------------------
    &&           Compute logical AND          L    2    any,any -> any
    ----------------------------------------------------------------------
    ||           Compute logical OR           L    2    any,any -> any
    ----------------------------------------------------------------------
    ?:           Choose 2nd or 3rd operand    R    3    bool,any,any->any
    ----------------------------------------------------------------------
    =            Variable or property assign  R    2    lval,any-> any
    *= /= %= +=  Operate and assign           R    2    lval,any-> any
    -= &= ^= |=  Operate and assign           R    2    lval,any-> any
    <<= >>= >>>= Operate and assign           R    2    lval,any-> any
    ----------------------------------------------------------------------
    ,            Discard 1st, return 2nd      L    2    any,any -> any
    ============ ============================ ==== ==== ==================


.. note::
    | + prefer to convert number to string
    | < <= > >= prefer to convert string to number
    | compare NaN with anything will return false
    | var v = a || b || 2, common way to provide defualt values.
    | Global variables are properties of the global object, so they can be deleted


=== and ==
----------
The strict equality operator === evaluates its operands, and then compares the two
values as follows, performing no type conversion:

* If the two values have different types, they are not equal.
* If both values are null or both values are undefined , they are equal.
* If both values are the boolean value(true or false), they are equal.
* If one or even both values is NaN , they are not equal. 
* If both values are numbers and have the same value, they are equal.
* If one value is 0 and the other is -0 , they are also equal.
* If both values are strings and have same content, they are equal.
* If both values refer to the same object, array, or function, they are equal.
* If they refer to different object instances, they are not equal.

The equality operator == is like the strict equality operator, but it is less strict:

* If the two values have the same type, test them for strict equality as described above.
  If they are strictly equal, they are equal. If they are not strictly equal, they are not equal.
* If the two values do not have the same type, the == operator attempts some
  type conversions and tries the comparison again:

    - If one value is null and the other is undefined , they are equal.
    - If one value is a number and the other is a string, convert the string to a number
      and try the comparison again, using the converted value.
    - If either value is true , convert it to 1 and try the comparison again.
    - If either value is false , convert it to 0 and try the comparison again.
    - If one value is an object and the other is a number or string, convert the object
      to a primitive value and try the comparison again. (toString/valueOf)
    - Any other combinations of values are not equal.


typeof
------
::

    ======================= ===========
    x                       typeof x
    ======================= ===========
    undefined               "undefined"
    null                    "object"
    true or false           "boolean"
    any number or NaN       "number"
    any string              "string"
    any function            "function"
    any native object       "object"
    ======================= ===========
