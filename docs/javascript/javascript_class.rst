JavaScript Classes
==================

Define Class by Constructors/Prototype
--------------------------------------

The prototype object is fundamental to the identity of a class: two objects are instances
of the same class if and only if they inherit from the same prototype object.

The constructor function that initializes the state of a new object is not fundamental:
two constructor functions may have prototype properties that point to the same prototype object.
Then both constructors can be used to create instances of the same class.

::

    function Range(from, to) {
        // Store the start and end points (state) of this new range object.
        // These are noninherited properties that are unique to this object.
        this.from = from;
        this.to = to;
    }

    // Extend the predefined Range.prototype object so we don't overwrite
    // the automatically created Range.prototype.constructor property.
    // All Range objects inherit from this object.
    // Note that the property name must be "prototype" for this to work.
    Range.prototype.includes = function(x) {
        return this.from<=x && x<=this.to;
    };
    Range.prototype.foreach = function(f) {
        for(var x = Math.ceil(this.from); x <= this.to; x++) f(x);
    };
    Range.prototype.toString = function() {
        return "(" + this.from + "..." + this.to + ")";
    };

    // Here are example uses of a range object
    var r = new Range(1,3);             // Create a range object
    r.includes(2);                      // => true: 2 is in the range
    r.foreach(console.log);             // => "1 2 3"
    r.toString();                       // => "(1...3)"

Java-Style Classes in JavaScript
--------------------------------

**Constructor object**:
The constructor function (an object) defines a name for a JavaScript class.

Properties you add to this constructor object serve as class fields and class
methods (depending on whether the property values are functions or not).
But these properties of constructor are not inheritable.

**Prototype object**:
The properties of this object are inherited by all instances of the class,
and properties whose values are functions behave like instance methods of the class.

**Instance object**:
Each instance of a class is an object in its own right, and properties defined directly
on an instance are not shared by any other instances. Nonfunction properties defined on
instances behave as the instance fields of the class.


Augmenting Classes
------------------

JavaScript’s prototype-based inheritance mechanism is dynamic: an object inherits
properties from its prototype, even if the prototype changes after the object is created.
This means that we can augment JavaScript classes simply by adding new methods to
their prototype objects.


