JavaScript Array
================

Overview
--------

JavaScript arrays are a specialized form of JavaScript object, and array indexes are really
little more than property names that happen to be integers. What is special about arrays is
that when you use property names that are non-negative integers less than 2^32 , the array
automatically maintains the value of the length property for you. (JavaScript arrays are
zero-based and use 32-bit indexes.)

JavaScript arrays are untyped: an array element may be of any type, and different
elements of the same array may be of different types.

Array elements may even be objects or other arrays, which allows you to create
complex data structures, such as arrays of objects and arrays of arrays.

JavaScript arrays are dynamic: they grow or shrink as needed and there is no need to declare
a fixed size for the array when you create it or to reallocate it when the size changes.

JavaScript arrays may be sparse: the elements need not have contiguous indexes and
there may be gaps.

Every JavaScript array has a length property. For nonsparse arrays, this property specifies
the number of elements in the array. For sparse arrays, length is larger than the index of
all elements.


Array Operators
---------------

**Creating Arrays**
::

    var empty = [];                     // An array with no elements
    var primes = [2, 3, 5, 7, 11];      // An array with 5 numeric elements
    var misc = [ 1.1, true, "a", ];     // 3 elements of various types + trailing comma
    var b = [[1,{x:1, y:2}], [2, {x:3, y:4}]];

    var base = 1024;
    var table = [base, base+1, base+2, base+3];

    var count = [1,,3];         // An array with 3 elements, the middle one undefined.
    var undefs = [,,];          // Normal array with 2 elements, both undefined.
    var a = new Array(10)       // Sparse array, length is 10, indexs/elements are all undefined
    var a = new Array(5, 4, 3, 2, 1, "testing, testing"); // array with these elements


**Reading and Writing Array Elements**
::

    var a = ["world"];
    var value = a[0];
    a[1] = 3.14;
    i = 2;
    a[i] = 3;
    a[i + 1] = "hello";

    a[-1.23] = true;            // Invalid index number, this creates a property named "-1.23"
    a["1000"] = 0;              // Valid index string, this the 1001st element of the array
    a[1.000]                    // Valid index float, same as a[1]

**Adding and Deleting Array Elements**
::

    a = []
    a[0] = "zero";              // a = ["zero"]
    a.push("one")               // Add a value at the end. a = ["zero", "one"]
    a.push("two", "three")      // Add two more values. a = ["zero", "one", "two", "three"]

    delete a[2]                 // Delete will not change lenght, lenght is still 4        
    a.length = 2                // Delete elements, a = ["zero", "one"]

**Iterating Arrays**
::

    for(var i = 0, len = a.length ; i < len; i++) {
        if (!a[i]) continue;                // Skip null, undefined, and nonexistent elements
        if (a[i] === undefined) continue;   // Skip undefined + nonexistent elements
        if (!(i in a)) continue ;           // Skip nonexistent elements
        // loop body here
    }

**Array Type**
::

    Array.isArray([])           // => true
    Array.isArray({})           // => false
    Array.isArray{""}           // => false


Array Methods
-------------

**join()**::

    var a = [1, 2, 3];          // Create a new array with these three elements
    a.join();                   // => "1,2,3"
    a.join(" ");                // => "1 2 3"
    var b = new Array(10);      // An array of length 10 with no elements
    b.join('-')                 // => '---------': a string of 9 hyphens

**reverse()**::

    a.reverse()                 // a is now [3,2,1]

**sort**::
    
    /* Always in dictionary order by default. Numbers will also be converted to string
       If an array contains undefined elements, they are sorted to the end of the array.
    */
    ["one", "two", undefined, "four"].sort()    // => ["four", "one", "two", undefined]
    [11, 444, 2].sort();                            // => [11, 2, 444]
    [11, 444, 2].sort(function(a,b) {return a-b;}); // => [2, 11, 444]

**concat()**::

    /* concat() will always create new array, but not to change the original array.
       If any of these arguments is itself an array, then it is the array elements that
       are concatenated, not the array itself.
    */
    var a = [1,2,3];
    a.concat(4, 5)              // return new array [1, 2, 3, 4, 5]
    a.concat([4,5]);            // return new array [1, 2, 3, 4, 5]
    a.concat(4, [5,[6,7]])      // return new array [1, 2, 3, 4, 5, [6,7]]

**slice()**::

    var a = [1,2,3,4,5];
    a.slice(0,3);               // Returns [1,2,3]
    a.slice(3);                 // Returns [4,5]
    a.slice(1,-1);              // Returns [2,3,4]
    a.slice(-3,-2);             // Returns [3]

**splice()**::

    /* Unlike slice() and concat() , splice() modifies the array on which it is invoked.
       Unlike concat() , splice() inserts arrays themselves, not the elements of them.
    */
    var a = [1,2,3,4,5,6,7,8];
    a.splice(4);                // Returns [5,6,7,8]; a is [1,2,3,4]
    a.splice(1,2);              // Returns [2,3]; a is [1,4]

    var a = [1,2,3,4,5];
    a.splice(2,0,'a','b');      // Returns []; a is [1,2,'a','b',3,4,5]
    a.splice(2,2,[1,2],3);      // Returns ['a','b']; a is [1,2,[1,2],3,3,4,5]

**push()/pop()**::

    /* The push() method appends one or more new elements to the end of an array and
       returns the new length of the array. The pop() method ddeletes the last element
       of an array, decrements the array length, and returns the value that it removed.
       Note that both methods modify the array in place rather than produce a new array.
    */
    var stack = [];
    stack.push("one", "two");   // stack = ["one", "two"], return 2
    stack.pop();                // stack = ["one"], return "two"
    stack.push([2, 3]);         // stack = ["one", [2, 3]], return 2
    stack.pop();                // stack = ["one"], return [2, 3]

**unshift()/shift()**::

    /* The unshift() and shift() methods behave much like push() and pop() , except that
       they insert and remove elements from the beginning of an array.
    */
    var a = [1, 2];
    a.unshift(0);               // a = [0, 1, 2], return 3
    a.shift()                   // a = [1, 2], return 0
    a.unshift(3, [4, 5])        // a = [3, [4, 5], 1, 2], return 4

**toString()/toLocalString()**::

    [1,2,3].toString()          // => '1,2,3'
    ["a", "b", "c"].toString()  // => 'a,b,c'
    [1, [2,'c']].toString()     // => '1,2,c'

.. note::
    The following methods are defined in ECMAScript 5

**forEach()**::

    /*  function arguments: value[, index, array-itself]
    */
    var data = [1,2,3,4,5];
    var sum = 0;
    data.forEach(function(value) { sum += value; });
    sum                         // => 15
    data.forEach(function(v, i, a) { a[i] = v + 1; });
    data                        // => [2,3,4,5,6]

**map()**::

    /* Returns an new array containing the values returned by specified function.
       The same function arguments as forEach(), neet return in function.
    */
    a = [1, 2, 3];
    b = a.map(function(x) { return x*x; });             // b = [1, 4, 9]

**filter()**::

    /* Unlike map(), filter method will skips missing elements in sparse arrays
    */
    a = [5, 4, 3, 2, 1];
    b = a.filter(function(x) { return x < 3 });         // b = [2, 1]

    var dense = sparse.filter(function() { return true; }); // return dense array

**reduce()/reduceRight()**::

    /* //first time with initial value
       function(firstElement, initialValue[, index=0, arrayitself])

       // first time without initial value
       function(firstElement, secondElement[, index=1, arrayitself])

       // other times when reducing
       function(lastReturnValue, nextElement[, index, arrayitself])

       reduceRight() works just like reduce() , except that it processes the array from
       highest index to lowest (right-to-left), rather than from lowest to highest.
    */
    var a = [1,2,3,4,5]
    var sum = a.reduce(function(x,y) { return x+y }, 0);     // Sum of values
    var product = a.reduce(function(x,y) { return x*y }, 1); // Product of values
    var max = a.reduce(function(x,y) { return (x>y)?x:y; }); // Largest value

    function extend(o, p) {
        for (prop in p) {
            o[prop] = p[prop];
        }
        return o;
    }
    var a = [{x:1, a:1}, {y:2, a:2}, {z:3, a:3}];
    var unionLeft = {}
    var unionRight = {}                 // Please note the different value to a
    a.reduce(extend, unionLeft)         // unionLeft = {x:1, a:3, y:2, z:3}
    a.reduceRight(extend, unionRight)   // unionRight = {z:3, a:1, y:2, x:1}

**every()/some()**::

    /* Both every() and some() stop iterating array elements as soon as they know
       what value to return.
       every() returns true and some returns false when invoked on an empty array.
    */
    a = [1,2,3,4,5];
    a.every(function(x) { return x < 10; })         // => true: all values < 10.
    a.every(function(x) { return x % 2 === 0; })    // => false: not all values even.
    a.some(function(x) { return x % 2 === 0; })     // => true: a has some even numbers.

**indexOf()/lastIndexOf()**::

    /* indexOf() and lastIndexOf() search an array for an element with a specified value,
       and return the index of the first such element found, or –1 if none is found.
    */

    a = [0,1,2,1,0];
    a.indexOf(1)                        // => 1: a[1] is 1
    a.lastIndexOf(1)                    // => 3: a[3] is 1
    a.indexOf(3)                        // => -1: no element has value 3
    a.indexOf(1,1)                      // => 3: a[3] is 1, begin the search at 1
