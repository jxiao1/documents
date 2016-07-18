jQuery Quick Start
==================

Learn jQuery:    https://learn.jquery.com/using-jquery-core/
Download jQuery: https://jquery.com/


Hello World Example
-------------------
::

    <!DOCTYPE html>
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>helloworld</title>
    <script src="js/jquery-3.1.0.js" type="text/javascript"></script>
    <script type="text/javascript">
        $(document).ready(function(){
            alert("Hello World!");
        });
    </script>
    </head>

    <body>
    </body>
    </html>



DOM and jQuery Objects
----------------------

Get jQuery or DOM object::

    var $foo = $("#foo")
    var foo = document.getElementByID("foo")

Convert jQuery object to DOM object::

    var foo = $foo.get(0)
    var foo = $foo[0]

Convert DOM object to jQuery object::

    var $foo = $(foo)

Difference between jQuery and DOM object::

    var string = $foo.html()          // jQeury API
    var string = foo.innerHTML        // DOM attribute

    if ($("#cr").is(":checked")) ...  // jQuery API
    if ($("#cr")[0].checked) ...      // DOM attribute


Naming Conflict
---------------

Avoid to use '$' mixed with others::

    jQuery.noConflict();            // Reserve "$" to other libs like prototype.
    jQuery(function() {             // Only use full name jQuery() later.
        jQuery("p").click(function() {
            alert(jQuery(this).text());
        })
    })              

    var $j = jQuery.noConflict();   // use $j as the alias to jQuery object
    $j(function() {                 // Then we can use $j instead of $ or jQuery
        $j("p").click(function() {
            alert($j(this).text());
        })
    })              

    jQuery(function($) {            // Still use $ in callback function
        $("p").click(function() {   // and other callback function in it.
            alert($(this).text);
        })
    })


Coding Style
------------

**indentation**::

    // one line for not more than 3 operations
    $("li").show().unbind("click")

    // one element one line
    $(this).addClass("current")
        .next().show()
        .parent().siblings().children("a").removeclass("current")
        .next().hide();

    // indentation for children
    $(this).addClass("highlight")
        .children("li").show().end()
    .siblings().removeClass("highlight")
        .children("li").hide();


**comments**:

- Add comment for complex lines
