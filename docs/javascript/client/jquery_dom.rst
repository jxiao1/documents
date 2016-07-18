jQuery DOM Manipulation
=======================

DOM Intraduction
----------------

DOM Core functions: element.getAttribute("src")
HTML-DOM attributes: element.src
CSS-DOM attributes of style:  element.style.color = "red"


jQuery DOM
----------

https://api.jquery.com/category/manipulation/

Examples::

    var $li_1 = $("<li>apple</li>")   // create a new li element
    $("ul").append($li_1)             // append it into document

    $("ul").append("<li>apple</li>")  // append element directly

    $("ul li:eq(2)").text()           // the text value of the second li in ul

    $("p").attr("title")              // get the title attribute
    $("p").attr("title", "New title") // set the title attribute 

    $("p").css("color")               // get the css style attribute value
    $("p").css("color", "red")        // set the css style attribute value
