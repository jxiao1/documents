JavaScript Function
===================

Overview
--------

Function names are often verbs or phrases that begin with verbs. It is a common con-
vention to begin function names with a lowercase letter. When a name includes multiple
words, one convention is to separate words with underscores like_this() ; another
convention is to begin all words after the first with an uppercase letter likeThis() .

Function declaration statements are “hoisted” to the top of the enclosing script or the
enclosing function, so that functions declared may be invoked from code that appears before
they are defined. However, this is not true for functions defined as expressions,
variable declarations are hoisted, variables are not hoisted, so functions defined with
expressions cannot be invoked before they are defined.

If the return statement does not have an associated expression, it returns the undefined value.
If a function does not contain a return statement, it return the undefined value to the caller.

Function declaration statements are not true statements, and the ECMAScript specification
only allows them as top-level statements. They can appear in global code, or within other functions,
but they cannot appear inside of loops, conditionals, or try/catch/finally or with statements.
Note that this restriction applies only to functions declared as statements.
Function definition expressions may appear anywhere in your JavaScript code.
(But firefox allows define function in if statement)

In JavaScript, however, functions are not only syntax but also values, which means they
can be assigned to variables, stored in the properties of objects or the elements of arrays,
passed as arguments to functions, and so on.


Defining/Invoking Functions
---------------------------

**declaration statement/definiton expression**::

    function functionName(arg1, arg2[, argN, ...]) {
        //statements
        return [value]  //optional
    }

    // Function expressions can include names, which is useful for recursion.
    var f = function fact(x) { if (x <= 1) return 1; else return x*fact(x-1); };

    // Function expressions are sometimes defined and immediately invoked:
    var tensquared = (function(x) {return x*x;}(10));

**Invoked ways**::
    /* JavaScript functions can be invoked in four ways:
    - as functions,
    - as methods,
    - as constructors,
    - indirectly through their call() and apply() methods.
    */
    
    var total = distance(0,0,2,1) + distance(2,1,3,5);

    o.m(x, y);  // m is method of object o

    var o = new Object();
    var o = new Object;     //only when the constructor function has no args.

    f.call(o, x, y)   // f is not method of o, but want use o as invocation context.

**method chaining**::

    // If object methods always return 'this' (the object itself)
    shape.setX(100).setY(100).setSize(50).setOutline("red").setFill("blue").draw();


Constructor Invocation
----------------------
If a function or method invocation is preceded by the keyword new , then it is a
constructor invocation. Constructor invocations differ from regular function and
method invocations in their handling of arguments, invocation context, and return value.

You can always omit a pair of empty parentheses in a constructor invocation.
If a constructor has no parameters, then JavaScript constructor invocation syntax allows
the argument list and parentheses to be omitted entirely.

A constructor invocation creates a new, empty object that inherits from the prototype
property of the constructor. Constructor functions are intended to initialize objects
and this newly created object is used as the invocation context, so the constructor function
can refer to it with the this keyword. 

Constructor functions do not normally use the return keyword. They typically initialize
the new object and then return it. If a constructor explicitly used the return statement
to return an object, then that object becomes the value of the invocation expression.
But if the constructor uses return with no value, or if it returns a primitive value,
that return value is ignored and the new object is used as the value of the invocation.


Function Arguments and Parameters
---------------------------------
JavaScript function definitions do not specify an expected type for the function pa-
rameters, and function invocations do not do any type checking on the argument values
you pass. In fact, JavaScript function invocations do not even check the number of
arguments being passed.

**Optional Parameters**

When a function is invoked with fewer arguments than declared parameters,
the additional parameters are set to the undefined value::

    function getPropertyNames(o, /* optional */ a) {
        a = a || []; // If undefined, use a new array
        for(var property in o) a.push(property);
        return a;
    }

.. note::
    When designing functions with optional arguments, you should be sure to
    put the optional ones at the end of the argument list.
    The comment "optional" in the function definition to emphasize the fact that
    the parameter is optional.

**Variable-Length Argument Lists**

When a function is invoked with more argument values than declared parameter,
names, the additional arguments cannot be read by names, but the Arguments object
"arguments" refers to all the arguments. "arguments" is not a array, but it happens
to have number indexes.

::

    function max(initialValue, /* numbers ... */) {
        var max = initialValue;   //or arguments[0] 
    
        // Loop through the arguments, looking for other arguments.
        for(var i = 1; i < arguments.length; i++) {
            if (arguments[i] > max) max = arguments[i];
        }
        return max;
    }

There are also "callee" and "caller" properties in Arguments object:
- arguments.callee refers to this currently running function.
- arguments.caller refers to the function that called this one.

**Using Object Properties As Arguments**

When a function has more than three parameters, it becomes difficult for the programmer
who invokes the function to remember the correct order in which to pass arguments.

::
    function easycopy(args) {
        if (isArray(args.from) && isArray(args.to)) {
            arraycopy(args.from,
                args.from_start || 0, // Note default value provided
                args.to,
                args.to_start || 0,
                args.length);
        }
        else throw new Error("argument from and to must be array!");
    }
    // Here is how you might invoke easycopy():
    var a = [1,2,3,4], b = [];
    easycopy({from: a, to: b, length: 4});
    

Properties of Function
----------------------

**length**
Function itself also has length, you can access it like this:
"functionName.length" or "arguments.callee.length"

**prototype**
Will be used when invoked as constructor.


**Defining Your Own Function Properties**
Function is a specialized kind of object, which means that functions can have properties.
Sometimes, it is better to store the information in a property of the Function object
instead of cluttering up the name space by defining a global variable.

::

    // Compute factorials and cache results as properties of the function itself.
    function factorial(n) {
        if (isFinite(n) && n>0 && n==Math.round(n)) {   // Finite, positive ints only
            if (!(n in factorial))                      // If no cached result
                factorial[n] = n * factorial(n-1);      // Compute and cache it
            return factorial[n];                        // Return the cached result
        }
        else return NaN;                                // If input was bad
    }
    factorial[1] = 1;                   // Initialize the cache to hold this base case.


Functions As Namespaces
-----------------------

Sometimes, it's useful to define a function simply to act as a temporary namespace
in which you can define variables without polluting the global namespace.

::

    var some = (function() { // function as module or namespace
        // Module code goes here.
        return somethings
    }());       // end the function literal and invoke it now.


this
----
Note that this is a keyword, not a variable or property name. JavaScript syntax does
not allow you to assign a value to this .

For function invocation in ECMAScript 3 and nonstrict ECMAScript 5, the invocation context
(the this value) is the global object. In strict mode, however, the invocation context is undefined .

Functions written to be invoked as functions do not typically use the this keyword at all.
It can be used, however, to determine whether strict mode is in effect::

    // Define and invoke a function to determine if we're in strict mode.
    var strict = (function() { return !this; }());

When a function is invoked on or through an object, that object is the invocation
context or this value for the function.

Unlike variables, the this keyword does not have a scope, and nested functions do not
inherit the this value of their caller. If a nested function is invoked as a method, its
this value is the object it was invoked on. If a nested function is invoked as a function
then its this value will be either the global object (non-strict mode) or undefined (strict
mode). It is a common mistake to assume that a nested function invoked as a function
can use this to obtain the invocation context of the outer function. If you want to access
the this value of the outer function, you need to store that value into a variable that is
in scope for the inner function. It is common to use the variable self for this purpose.
For example::

    var o = {
        m: function() {
            var self = this;                // Save the this value in a variable.
            console.log(this === o);        // true, if called by o.m()

            function f() {                  // A nested function f
                console.log(this === o);    // false, this is global object or undefined.
                console.log(self === o);    // true, self is the this of outer function.
            }

            f();
        }
    };
    o.m();

Note that the new object is always set as the invocation context even if the constructor invocation
looks like a method invocation. For example::

    // o.m() is used as constructor, o is not used as the invocation context, it's p.
    p = new o.m()


closure
-------

Like most modern programming languages, JavaScript uses lexical scoping. This means
that functions are executed using the variable scope that was in effect when they were
defined, not the variable scope that is in effect when they are invoked. In order to
implement lexical scoping, the internal state of a JavaScript function object must include
not only the code of the function but also a reference to the current scope chain.
This is an old term that refers to the fact that the function’s variables have bindings
in the scope chain and that therefore the function is “closed over” its variables.

This combination of a function object and a scope (a set of variable bindings) in which
the function’s variables are resolved is called a closure in the computer science literature.

Technically, all JavaScript functions are closures: they are objects, and they have a scope
chain associated with them.

Closures become interesting when they are invoked under a different scope chain than the one
that was in effect when they were defined. This happens most commonly when a nested function
object is returned from the function within which it was defined.
common in JavaScript programming.

In C language, function’s local variables are defined on a CPU stack, then they would indeed
cease to exist when the function returned. But JavaScript described it as a list of objects.

Each time a JavaScript function is invoked, a new object is created to hold the local variables
for that invocation, and that object is added to the scope chain. When the function returns,
that variable binding object is removed from the scope chain. If there were no nested functions,
there are no more references to the binding object and it gets garbage collected.
If there were nested functions defined, then each of those functions has a reference to
the scope chain, and that scope chain refers to the variable binding object.

If those nested functions objects remained within their outer function, however, then they
themselves will be garbage collected, along with the variable binding object they referred to.
But if the function defines a nested function and returns it or stores it into a property somewhere,
then there will be an external reference to the nested function. It won’t be garbage collected,
and the variable binding object it refers to won’t be garbage collected either.

Example 1::

    var scope = "global scope";         // A global variable
    function checkscope() {
        var scope = "local scope";      // A local variable
        function f() { return scope; }
        return f;
    }

    /* Remember the fundamental rule of lexical scoping: JavaScript functions are executed
    using the scope chain that was in effect when they were defined. */
    checkscope()();                     // It should return "local scope" here.
 

Example 2::

    // Function declarations are hoisted so we can do this assignment here.
    uniqueInteger.counter = 0;

    // This function returns a different integer each time it is called.
    function uniqueInteger() {
        return uniqueInteger.counter++; // Increment and return counter property
    }

    /* The above version has one problem, uniqueInteger.counter can be changed out of function. 
       So, rewrite the uniqueInteger() function using closures.
    */
    var uniqueInteger = (function() {                   // Define and invoke immediately
                            var counter = 0;            // Private state of function below
                            return function() { return counter++; };
                        }());                // no way to access counter after function return

Example 3::

    /* Two or more nested functions to be defined within the same outer function
       will share the same scope chain.
    */
    function counter(n) {
        return {
            count: function() { return n++; },
            reset: function() { n = 0; }
        };
    }
    var c = counter(0), d = counter(0); // two counters with two copies of scope chains
    c.count()                           // => 0
    d.count()                           // => 0: they count independently
    c.reset()                           // reset() and count() methods share state
    c.count()                           // => 0: because we reset c
    d.count()                           // => 1: d was not reset

.. note::
    As what mentioned above, nested functions in closure function will not share 'this'
    and 'arguments' of the outer function, except that we save them by other variables.
