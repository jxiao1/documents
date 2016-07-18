jQuery Animate Effects
======================

https://api.jquery.com/category/effects/

- The multi CSS style in one animate function will be apply at the same time
- The animation chains apply the changes in turn
- The animation on all the element happen at the same time.
- The complete call back function will always happens when current animate is done.


Basics
------

::

    // "fast"=200ms, default is "normal"=400ms,  and "slow"=600ms

    .show()
    .show( [duration|"fast"|"slow" ] [, complete ] )

    .hide()
    .hide( [duration|"fast"|"slow" ] [, complete ] )

    .toggle()

Others
------

::

    fadeIn()/fadeOut()/fadeTo()/fadeToggle()
    slideUp()/slideDown()/slideToggle()


Custom
------

Perform a custom animation of a set of CSS properties::

    .animate()


Stop
----

Stop the currently-running animation::

    this.stop(true, [true])


Check
-----

Check the current element is animated status::

    .is(":animated")


Delay
-----

Delay between two animations::

    .delay(duration)


