Python Template Libraries
=========================

jinja2
------

::

    from jinja2 import Environment, PackageLoader

    def template_render(name, args):
        env = Environment(loader=PackageLoader('myApp', 'templates'))
        template = env.get_template(name)
        return template.render(args=args)


mako
----

| http://www.makotemplates.org/
| http://docs.makotemplates.org/en/latest/
|
