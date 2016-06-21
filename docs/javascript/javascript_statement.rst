JavaScript Statements
=====================

Overview
--------

JavaScript does not have block scope and variables declared within a statement block
are not private to the block.

Variables are defined throughout the script or function in which they are declared.
Their declaration is “hoisted” up to the start of the script or function. Initialization,
however, occurs at the location of the var statement, and the value of the variable is
undefined before that point in the code.

Function declaration statements may appear in top-level JavaScript code, or they may
be nested within other functions. When nested, however, function declarations may
only appear at the top level of the function they are nested within. That is, function
definitions may not appear within if statements, while loops, or any other statements.

With var, only the variable declaration is hoisted, the variable initialization code
remains where you placed it. With function declaration statements, however, both the
function name and the function body are hoisted: all functions in a script or all nested
functions in a function are declared before any other code is run.

Like the var statement, function declaration statements create variables that cannot be
deleted.

Finally, note that a break statement, with or without a label, can not transfer control
across function boundaries. You cannot label a function definition statement, for ex-
ample, and then use that label inside the function.


Statements Structure
--------------------

statements::

    // Initialize an array a
    for(i = 0; i < a.length; a[i++] = 0) /* empty */ ;

    var f = function(x) { return x+1; }  // Expression assigned to a variable
    function f(x) { return x+1; }        // Function declaration statement

    if (expression) {
        statements
    }
    else if (expression) {
        statements
    }
    else {
        statements
    }

    // compare by "==="
    switch(expression) {
        case value1:
            statements
            break;
        case value2:
            statements
            break;
        default:
            statements
            break;
    }

    while (expression) {
        statements
    }

    do {
        statements
    } while (expression) ;  // Must always be terminated with a semicolon.

    for(initialize; test; increment) {
        statements
    }

    for (var p in o) {   // Enumerable properties in object
        statements
    }

    var o = {x:1, y:2, z:3}, a = [], i = 0;
    for (a[i++] in o) {  // Store properties of object into arrray
        statements
    }

    lablename: loop-statements {
        loop-statement {
            ...
            continue lablename;
            ...
            break lablename;
        }
    }

    throw new Error("x must not be negative");

    try {
        // Normally, this code runs from the top of the block to the bottom
        // without problems. But it can sometimes throw an exception,
        // either directly, with a throw statement, or indirectly, by calling
        // a method that throws an exception.
    }
    catch (e) {
        // The statements in this block are executed if, and only if, the try
        // block throws an exception. These statements can use the local variable
        // e to refer to the Error object or other value that was thrown.
        // This block may handle the exception somehow, may ignore the
        // exception by doing nothing, or may rethrow the exception with throw.
    }
    finally {
        // This block contains statements that are always executed, regardless of
        // what happens in the try block. They are executed whether the try
        // block terminates:
        //   1) normally, after reaching the bottom of the block
        //   2) because of a break, continue, or return statement
        //   3) with an exception that is handled by a catch clause above
        //   4) with an uncaught exception that is still propagating
    }

    if (o === undefined) debugger;

examples::

    var o = {one: 1, two: 2, three: 3};
    for (let p in o) console.log(p);            // indexes: one, two, three
    for each (let v in o) console.log(v)        // values: 1, 2, 3

    try {
        // more than one type of exception where
        throw 1;
    }
    catch(e if e instanceof ReferenceError) {
        //do something here
    }
    catch(e if e === "quit") {
        // do something here
    }
    catch(e){ //all other cases
        // do something here
    }
    finally {
        // do something here
    }


'use strict' Directive
----------------------
It can appear only at the start of a script or at the start of a function body, before
any real statements have appeared. It need not be the very first thing in the script
or function.

The differences between strict mode and non-strict mode are the following:

- The with statement is not allowed in strict mode.
- In strict mode, all variables must be declared: a ReferenceError is thrown if you
  assign a value to an identifier that is not a declared variable, function, function
  parameter, catch clause parameter, or property of the global object. (In non-strict
  mode, this implicitly declares a global variable by adding a new property to the
  global object.)
- In strict mode, functions invoked as functions (rather than as methods) have a
  this value of undefined . (In non-strict mode, functions invoked as functions are
  always passed the global object as their this value.) This difference can be used to
  determine whether an implementation supports strict mode:
  ``var hasStrictMode = (function() { "use strict"; return this===undefined}());``

- Also, in strict mode, when a function is invoked with call() or apply() , the this
  value is exactly the value passed as the first argument to call() or apply() . (In
  nonstrict mode, null and undefined values are replaced with the global object and
  non-object values are converted to objects.)
- In strict mode, assignments to nonwritable properties and attempts to create new
  properties on nonextensible objects throw a TypeError. (In non-strict mode, these
  attempts fail silently.)
- In strict mode, code passed to eval() cannot declare variables or define functions
  in the caller’s scope as it can in non-strict mode. Instead, variable and function
  definitions live in a new scope created for the eval() . This scope is discarded when
  the eval() returns.
- In strict mode, the arguments object (§8.3.2) in a function holds a static copy of
  the values passed to the function. In non-strict mode, the arguments object has
  “magical” behavior in which elements of the array and named function parameters
  both refer to the same value.
- In strict mode, a SyntaxError is thrown if the delete operator is followed by an
  unqualified identifier such as a variable, function, or function parameter. (In non-
  strict mode, such a delete expression does nothing and evaluates to false .)
- In strict mode, an attempt to delete a nonconfigurable property throws a
  TypeError. (In non-strict mode, the attempt fails and the delete expression eval-
  uates to false .)
- In strict mode, it is a syntax error for an object literal to define two or more prop-
  erties by the same name. (In non-strict mode, no error occurs.)
- In strict mode, it is a syntax error for a function declaration to have two or more
  parameters with the same name. (In non-strict mode, no error occurs.)
- In strict mode, octal integer literals (beginning with a 0 that is not followed by an
  0x) are not allowed. (In non-strict mode, some implementations allow octal literals.)
- In strict mode, the identifiers eval and arguments are treated like keywords, and
  you are not allowed to change their value. You cannot assign a value to these identifiers,
  declare them as variables, use them as function names, use them as function parameter
  names, or use them as the identifier of a catch block.
- In strict mode, the ability to examine the call stack is restricted. arguments.caller
  and arguments.callee both throw a TypeError within a strict mode function. Strict mode
  functions also have caller and arguments properties that throw TypeError when read.
  (Some implementations define these nonstandard properties on non-strict functions.)


