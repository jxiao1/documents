JavaScript Objects
==================

JavaScript’s fundamental datatype is the object. An object is an unordered collection
of properties, each of which has a name and a value.


Overview
--------

JavaScript objects are dynamic(properties can usually be added and deleted), but they
can be used to simulate the static objects and “structs” of statically typed languages.

The most common things to do with objects are create them and to set, query, delete,
test, and enumerate their properties.

In addition to its properties, every object has three associated object attributes:
- An object’s prototype is a reference to another object from which properties are inherited.
- An object’s class is a string that categorizes the type of an object.
- An object’s extensible flag specifies whether new properties may be added to the object.

Finally, here are some terms we’ll use to distinguish among three broad categories of
JavaScript objects and two types of properties:

Types of objects:

- A native object is an object or class of objects defined by the ECMAScript specification.
  Arrays, functions, dates, and regular expressions (for example) are native objects.
- A host object is an object defined by the host environment (such as a web browser)
  within which the JavaScript interpreter is embedded. The HTMLElement objects
  that represent the structure of a web page in client-side JavaScript are host objects.
  Host objects may also be native objects, as when the host environment defines
  methods that are normal JavaScript Function objects.
- A user-defined object is any object created by the execution of JavaScript code.

Types of properties:

- An own property is a property defined directly on an object.
- An inherited property is a property defined by an object’s prototype object.


property attributes
-------------------

- The writable attribute specifies whether the value of the property can be set.
- The enumerable attribute specifies whether the property name is returned by a for/in loop.
- The configurable attribute specifies whether the property can be deleted and
  whether its attributes can be altered.

::

    // Returns {value: 1, writable:true, enumerable:true, configurable:true}
    Object.getOwnPropertyDescriptor({x:1}, "x");

    // Now query the octet property of the random object defined above.
    // Returns { get: /*func*/, set:undefined, enumerable:true, configurable:true}
    Object.getOwnPropertyDescriptor(random, "octet");

    // Returns undefined for inherited properties and properties that don't exist.
    Object.getOwnPropertyDescriptor({}, "x");        // undefined, no such property
    Object.getOwnPropertyDescriptor({}, "toString"); // undefined, inherited
    
    // Does not have to include all four attributes at the same time.
    Object.defineProperty(o, "x", { value : 1,
                                    writable: true,
                                    enumerable: false,
                                    configurable: true});

    var p = Object.defineProperties({}, {
        x: { value: 1, writable: true, enumerable:true, configurable:true },
        y: { value: 1, writable: true, enumerable:true, configurable:true },
        r: {
            get: function() { return Math.sqrt(this.x*this.x + this.y*this.y) },
            enumerable:true,
            configurable:true
        }
    });

.. note::
    Here are the complete rules. Calls to Object.defineProperty() or
    Object.defineProperties() that attempt to violate them throw TypeError:

    - If an object is not extensible, you can edit its existing own properties, but you
      cannot add new properties to it.
    - If a property is not configurable, you cannot change its configurable or enumerable
      attributes.
    - If an accessor property is not configurable, you cannot change its getter or setter
      method, and you cannot change it to a data property.
    - If a data property is not configurable, you cannot change it to an accessor property.
    - If a data property is not configurable, you cannot change its writable attribute from
      false to true , but you can change it from true to false .
    - If a data property is not configurable and not writable, you cannot change its value.
      You can change the value of a property that is configurable but nonwritable. (making
      it writable, then changing the value, then converting it back to nonwritable).


Objects Operators
-----------------

**Creating Objects**
::

    var point = {x:0, y:0};
    var o = Object.create(Object.prototype)
    var o = new Object();
    var a = new Arrays();
    var d = new Date();
    var r = new RegExp();

**Querying and Setting Properties**

The fact that inheritance occurs when querying properties but not when setting them
is a key feature because it allows us to selectively override inherited properties.

Property assignment examines the prototype chain to determine whether the assignment is allowed.
If o inherits a read-only property named x , for example, then the assignment is not allowed.

It is not an error to query a property that does not exist, undefined will be return.
It is an error, however, to attempt to query a property of an object that does not exist.

An attempt to set a property p of an object o fails in these circumstances:

- o has an own property p that is read-only: it is not possible to set read-only prop-
  erties. (See the defineProperty() method, however, for an exception that allows
  configurable read-only properties to be set.)
- o has an inherited property p that is read-only: it is not possible to hide an inherited
  read-only property with an own property of the same name.
- o does not have an own property p ; o does not inherit a property p with a setter
  method, and o ’s extensible attribute is false . If p does not already exist on o ,
  and if there is no setter method to call, then p must be added to o . But if o is not
  extensible, then no new properties can be defined on it.

::

    /* If an object has properties whose name is a reserved
    word, you must use square bracket notation to access them */

    var author = book.author;           // Get the "author" property of the book.
    var name = author.surname;          // Get the "surname" property of the author.
    var title = book["main title"];     // Get the "main title" property of the book.
    book.edition = 6;                   // Create an "edition" property of book.
    book["main title"] = "ECMAScript";  // Set the "main title" property.

    var len = book && book.subtitile && book.subtitle.length; // May doesn't exist

**Deleting Properties**

The delete operator only deletes own properties, not inherited ones.
The delete operator does not remove properties that have a configurable attribute of false .

::

    delete book.author;                 // The book object now has no author property.
    delete book["main title"];          // Now it doesn't have "main title", either.

**Testing Properties**
::

    var o = { x: 1 }
    "x" in o;                           // true: o has an own property "x"
    "y" in o;                           // false: o doesn't have a property "y"
    "toString" in o;                    // true: o inherits a toString property

    o.hasOwnProperty("x");              // true: o has an own property x
    o.hasOwnProperty("y");              // false: o doesn't have a property y
    o.hasOwnProperty("toString");       // false: toString is an inherited property

    /* Only is property is an own property and its enumerable attribute is true */
    o.propertyIsEnumerable("x");        // true: o has an own enumerable property x
    Object.prototype.propertyIsEnumerable("toString"); // false: not enumerable
    
    o.x !== undefined  // It's equal to 'in' execpt property is explicitly set to undefined 
    if (o.x) o.x *=2 ; // If exist and is not undefined, null, false, "", 0, NaN

**Enumerating Properties**
::

    for(p in o) {
        if (!o.hasOwnProperty(p)) continue;
    }
    for(p in o) {
        if (typeof o[p] === "function") continue; // Skip methods
    }

    Object.keys()  // returns an array of the names of the enumerable own properties
    Object.getOwnPropertyNames()  // returns the names of all the own properties

**Property Getters and Setters**
::

    var p = {
        x: 1.0,
        y: 1.0,

        // r is a read-write accessor property with getter and setter.
        get r() {
            return Math.sqrt(this.x*this.x + this.y*this.y);
        },  // Don't forget to put a comma after accessor methods.
        set r(newvalue) {
            var oldvalue = Math.sqrt(this.x*this.x + this.y*this.y);
            var ratio = newvalue/oldvalue;
            this.x *= ratio;
            this.y *= ratio;
        }
    };


Object Attributes
-----------------

Every object has associated prototype, class, and extensible attributes.

**The prototype Attribute**

::

    var p = {x:1};
    var o = Object.create(p);
    p.isPrototypeOf(o)                  // => true: o inherits from p
    Object.prototype.isPrototypeOf(o)   // => true: p inherits from Object.prototype
    
    Object.getPrototypeOf(o) ;          // => Object { x=1}

**The class Attribute**

::

    function classof(o) {
        if (o === null) return "Null";
        if (o === undefined) return "Undefined";
        return Object.prototype.toString.call(o).slice(8,-1);
    }
    classof(null)                       // => "Null"
    classof(1)                          // => "Number"
    classof("")                         // => "String"
    classof(false)                      // => "Boolean"
    classof({})                         // => "Object"
    classof([])                         // => "Array"
    classof(/./)                        // => "Regexp"
    classof(new Date())                 // => "Date"
    classof(window)                     // => "Window" (a client-side host object)
    function f() {};
    classof(new f());                   // => "Object"

**The extensible Attribute**
::

    var p = {x:1};
    Object.isExtensible(p)              // true
    Object.preventExtensions(p)         // make object nonextensible
    Object.isExtensible(p)              // false
    p.y = 1                             // will not report error, but y is not added
    p.y                                 // undefined
    Object.seal(p)                      // object nonextensible, and all the own properties nonconfigurable.
    Object.isSealed(p)                  // true
    delete p.x                          // return false means cannot delete it
    p.x                                 // still exist with value 1
    Object.freeze(p)                    // besides seal, all data properties will be read only.
    Object.isFrozen()                   // true


Object Methods
--------------

::

    var o = {x:1, y:1};
    s = o.toString() ;                  // "[object object]"
    s = JSON.stringify(o)               // "{"x":1, "y":1}"
    p = JSON.parse(s)                   // p is the deepcopy of o

    p = new Number(3)
    p.valueOf()                         // 3
