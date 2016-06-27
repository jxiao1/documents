JavaScript Basic
================
http://www.w3school.com.cn/b.asp
http://www.w3school.com.cn/js/index_pro.asp
https://developer.mozilla.org/en-US/docs/Web/JavaScript

JavaScript Overview
-------------------

- JavaScript programs are written using the Unicode character set.
- JavaScript is a case-sensitive language. (However, HTML is not case-sensitive.)
- JavaScript ignores spaces that appear between tokens in programs and ignores line breaks.
- JavaScript supports two styles of comments, the same as C language.
- JavaScript uses the semicolon ( ; ) to separate statements (see Chapter 5) from each other.
- JavaScript identifier names must match "^[a-zA-z_$][a-zA-z0-9_$]*"
- JavaScript interpreter performs automatic garbage collection for memory management.
- JavaScript is an object-oriented language.
- JavaScript variables are untyped, you can assign a value of any type to a variable.
- All numbers in JavaScript are represented as floating-point values.
- JavaScript numbers can approximate 0.1 very closely, but cannot be represented exactly.
- JavaScript code behaves as if all variable declarations in a function (but not any
  associated assignments) are “hoisted” to the top of the function.


JavaScript Reserved Words
-------------------------

JavaScript reserves a number of identifiers as the keywords of the language itself. You
cannot use these words as identifiers in your programs::

    break       case        catch       continue    debugger    default
    delete      do          else        false       finally     for
    function    if          in          instanceof  new         null
    return      switch      this        throw       true        try
    typeof      var         void        while       with

JavaScript also reserves certain keywords that are not currently used by the language
but which might be used in future versions. ECMAScript 5 reserves the following words::

    class       const       enum        export      extends     import      super

The following words are legal in ordinary JavaScript code, but reserved in strict mode::

    implements  interface   let         package     private     protected
    public      static      yield

Strict mode also imposes restrictions on the use of the following identifiers. They are
not fully reserved, but they are not allowed as variable, function, or parameter names::

    arguments   eval

ECMAScript 3 reserved all the keywords of the Java language, and although this has been
relaxed in ECMAScript 5, you should still avoid all of these identifiers if you plan
to run your code under an ECMAScript 3 implementation of JavaScript::

    abstract    boolean     byte        char        class       const
    double      enum        export      extends     final       float
    goto        implements  import      int         interface   long
    native      package     private     protected   public      short
    static      super     synchronized  throws      transient   volatile

JavaScript predefines a number of global variables and functions, and you should avoid
using their names for your own variables and functions::

    arguments           Array               Boolean             Date
    decodeURI           decodeURIComponent  encodeURI           encodeURIComponent
    Error               eval                EvalError           Function
    Infinity            isFinite            isNaN               JSON
    Math                NaN                 Number              Object
    parseFloat          parseInt            RangeError          ReferenceError
    RegExp              String              SyntaxError         TypeError
    undefined           URIError
