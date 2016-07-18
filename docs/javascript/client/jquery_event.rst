jQuery Events
=============

https://api.jquery.com/category/events/

.ready() and .load()

While JavaScript provides the load event for executing code when a page is rendered,
this event does not get triggered until all assets such as images have been completely received.

In most cases, the script can be run as soon as the DOM hierarchy has been fully constructed.
The handler passed to .ready() is guaranteed to be executed after the DOM is ready, so this is
usually the best place to attach all other event handlers and run other jQuery code.
When using scripts that rely on the value of CSS style properties, it's important to reference
external stylesheets or embed style elements before referencing the scripts.

In cases where code relies on loaded assets (for example, if the dimensions of an image are required),
the code should be placed in a handler for the load event instead.

.ready() allows to register multi handlers and call function handlers in turn. For example::

        .ready(function() {
            func1()
        })


        .ready(function() {
            func2()
        })


All three of the following syntaxes are equivalent::

    $(document).ready( handler )
    $().ready(handler) (this is not recommended)
    $(handler)


Bind Event
----------

Use the bind API function: ``bind(eventType [, eventData ], handler)``

List of Event Types:
https://www.w3.org/TR/DOM-Level-3-Events/#event-types-list

Or use the predefined simple API::

    $(...).click(handler)       // equal to bind("click", handler)
    $(...).mouseover(handler)   // equal to bind("mouseover", handler)
    ...

Or if you want to bind multi events at one time::

    $("div").bind("mouseover", "mouseout", function() {
        $(this).toggleClass("over")
    });

Or bind handler only execute once::

    one(eventType [, eventData ], handler)


Unbind Event
------------

Use the unbind API function: ``unbind([eventType]) //no type means unbind all``

Or remove special named handler::

    $("#btn").bind("click", handler_1 = function() { ...})
        .bind("click", handler_2 = function() { ...})
        .bind("click", handler_3 = function() { ...});
    $("#btn").unbind("click", handler_3).unbind("click", handler_2);


Or remove the events in special namespace::

    
    $("#btn").bind("click.plugin", handler_1 = function() { ...})
        .bind("mouseover.plugin", handler_2 = function() { ...})
        .bind("dbclick", handler_3 = function() { ...});
    $("#btn").unbind(".plugin";


Trigger Event
-------------

For example, trigger click event manually, but not by click the button::

    $("#btn").trigger("click")

Or even you can trigger a self-defined event::

    $("$btn").bin("clickme", function(event){
        alert(event.data.message)
    });
    $("#btn").trigger("clickme", {message: "You clicked me!"})

The trigger() function will also result in the bowers default behaviors,
for example, get the focus. So, if you only want to trigger the handler::

    $("#btn").triggerHandler("clickme")


Or you can trigger event with special name space::

    $("#mydiv").bind("click", function() { ...});
    $("#mydiv").bind("click,plugin", function() { ...});

    $("#mydiv").trigger("click")   //trigger both click and click.plugin events.
    $("#mydiv").trigger("click!")  //trigger click only, but not click.plugin event.

    
Event Attributes
----------------

https://api.jquery.com/category/events/event-object/

- event.type                      Describes the nature of the event. (e.g. "click")
- event.data                      Refer to eventDate.
- event.target                    The DOM element that initiated the event.
- event.relatedTarget             The other DOM element involved in the event, if any. (e.g. mouseover from where)
- event.isDefaultPrevented()      Whether isDefaultPrevented() is called.
- event.isPropagationStopped()    Wheether event.isPropagationStopped() is called.
- event.metaKey                   Indicates whether the META key was pressed when the event fired.
- event.pageX                     The mouse position relative to the left edge of the document.
- event.pageY                     The mouse position relative to the top edge of the document.
- event.result                    The last value returned by an event handler that was triggered by this event.
- event.timeStamp                 The time when the event is triggered.
- event.which                     For key or mouse events, indicates the specific key or button that was pressed.


jQuery self-defined events
--------------------------

    hover(mouseover-handler, mouseout-handler)
    hover(mouseout-handler)

    toggle(handler1, hander2, ..)  // call handlerN in turn when click the element.


Event Propagation
-----------------

If you click the child element, this means the parent is also be clicked.
Then the onclick event of child and parent will be triggered in turn.

To stop this event propagation like this::

    $("span").bind("click", function(event){
        // do something...
        event.stopPropagation();        // or: return false;
    })


Prevent Default Behavior
------------------------

There are some default behaviors to some elements, for example, when click
submit input element, the form will be submitted, when click the href element,
the page will jump to the new address.

To stop this kind of default behavior like this::

    $("#sub").bind("click", function(event){
        // validate the form values...
        event.preventDefault();         // or: return false;
    })
