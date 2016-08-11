Markdown
========

Specification
-------------
| http://daringfireball.net/projects/markdown/syntax
|
| http://wowubuntu.com/markdown/index.html
|

Full Examples (zh_CN)
---------------------
| https://gitcafe.com/riku/Markdown-Syntax-CN/blob/master/syntax.md
| https://pandao.github.io/editor.md/examples/full.html
|

Difference between md and rst
-----------------------------
| http://fasiondog.cn/archives/698.html
|

Online Editor
-------------
| http://mahua.jser.me/
| https://maxiang.io/
| http://dillinger.io/
|

Markdown to HTML
----------------

#. Download `markdown-browser-0.6.0-beta1.tgz <https://github.com/evilstreak/markdown-js/releases>`_

#. Test it like this::

    tar -xvf markdown-browser-0.6.0-beta1.tgz
    cd markdown-browser-0.6.0-beta1
    vi test.html && firefox test.html

   test.html::

    <!DOCTYPE html>
    <html>
    <head>
    <link href="http://cdn.bootcss.com/bootstrap/3.3.1/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body style="padding:30px">
    <textarea id="text-input" oninput="this.editor.update()">Type **Markdown** here.</textarea>
    <div id="preview"> </div>
    <script src="markdown.js"></script>
    <script>
    function Editor(input, preview) {
        this.update = function () {
            preview.innerHTML = markdown.toHTML(input.value);
        };
        input.editor = this;
        this.update();
    }
    var $ = function (id) { return document.getElementById(id); };
    new Editor($("text-input"), $("preview"));
    </script>
    </body>
    </html>

