Python Design Patterns
======================

| https://github.com/faif/python-patterns
|

Creational Patterns:

======================= =========================================================================================
Pattern                 Description
======================= =========================================================================================
abstract_factory        use a generic function with specific factories
borg                    a singleton with shared-state among instances
builder                 instead of using multiple constructors, builder object
                        receives parameters and returns constructed objects
factory_method          delegate a specialized function/method to create instances
lazy_evaluation         lazily-evaluated property pattern in Python
pool                    preinstantiate and maintain a group of instances of the same type
prototype               use a factory and clones of a prototype for new instances
                        (if instantiation is expensive)
======================= =========================================================================================


Structural Patterns:

======================= =========================================================================================
Pattern                 Description
======================= =========================================================================================
3-tier                  data<->business logic<->presentation separation (strict relationships)
adapter                 adapt one interface to another using a white-list
bridge                  a client-provider middleman to soften interface changes
composite               encapsulate and provide access to a number of different objects
decorator               wrap functionality with other functionality in order to affect outputs
facade                  use one class as an API to a number of others
flyweight               transparently reuse existing instances of objects with similar/identical state
front_controller        single handler requests coming to the application
mvc                     model<->view<->controller (non-strict relationships)
proxy                   an object funnels operations to something else
======================= =========================================================================================


Behavioral Patterns:

======================= =========================================================================================
Pattern                 Description
======================= =========================================================================================
chain                   apply a chain of successive handlers to try and process the data
catalog                 general methods will call different specialized methods based on construction parameter
chaining_method         continue callback next object method
command                 bundle a command and arguments to call later
mediator                an object that knows how to connect other objects and act as a proxy
memento                 generate an opaque token that can be used to go back to a previous state
observer                provide a callback for notification of events/changes to data
publish_subscribe       a source syndicates events/data to 0+ registered listeners
registry                keep track of all subclasses of a given class
specification           business rules can be recombined by chaining the business rules together
                        using boolean logic
state                   logic is organized into a discrete number of potential states
                        and the next state that can be transitioned to
strategy                selectable operations over the same data
template                an object imposes a structure but takes pluggable components
visitor                 invoke a callback for all items of a collection
======================= =========================================================================================


Singleton
---------

| http://blog.csdn.net/ghostfromheaven/article/details/7671853
| http://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons-in-python/31887#31887

Examples::

    # Method 1: only __new__() once
    class Singleton(object):
        def __new__(cls,*args,**kwargs):
            if not hasattr(cls,'_inst'):
                cls._inst=super(Singleton,cls).__new__(cls,*args,**kwargs)
            return cls._inst

    # Method 2: share the __dict__
    class Borg(object):
        _shared_state={}
        def __new__(cls,*args,**kwargs):
            obj=super(Borg,cls).__new__(cls,*args,**kwargs)
            obj.__dict__=cls._shared_state
            return obj


.. note::
    The pythonic way is to define a module if you want to use singleton class.
