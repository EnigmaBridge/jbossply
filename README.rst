JBoss CLI output parser
=======================

This simple python library is a JBoss output lexer & parser based on `PLY <http://www.dabeaz.com/ply/>`__
(yet another implementation of lex and yacc for Python).

JBoss CLI server has output that closely resembles JSON, but it is not 100% JSON so it is difficult
to parse it with ordinary tools. With this library you can process JBoss output and parse it as JSON.

Example

.. code:: python

    from jbossply.jbossparser import JbossParser
    test3 = """{
        "outcome" => "success",
        "result" => {
            "rule-1" => {
                "flags" => "L,QSA,R",
                "pattern" => "^/$",
                "substitution" => "/ejbca",
                "condition" => undefined
            },
            "rule-3" => {
                "flags" => "L,QSA,R",
                "pattern" => "^/pki/?$",
                "substitution" => "/ejbca/adminweb",
                "condition" => undefined
            }
        }
    }
    """

    parser = JbossParser()
    print(parser.parse(test3))

Which gives output

::

    {u'outcome': u'success', u'result': {u'rule-3': {u'pattern': u'^/pki/?$', u'flags': u'L,QSA,R', u'condition': None, u'substitution': u'/ejbca/adminweb'}, u'rule-1': {u'pattern': u'^/$', u'flags': u'L,QSA,R', u'condition': None, u'substitution': u'/ejbca'}}}


You may want to cache parser tables, then create `JbossParser` like this:

.. code:: python

    parser = jbossparser.JbossParser(write_tables=True, outputdir='/tmp/table-dir')


Command line usage
------------------

After installed with pip you may use also the command line helper `jboss2json`.

::

    $ cat jboss-output.txt | jboss2json
    {"outcome": "success", "result": {"rule-3": {"pattern": "^/pki/?$", "flags": "L,QSA,R", "condition": null, "substitution": "/ejbca/adminweb"}, "rule-1": {"pattern": "^/$", "flags": "L,QSA,R", "condition": null, "substitution": "/ejbca"}}}


Installation
------------

You can install this package using pip:

::

    pip install jbossply



Credits
-------

The code is based on @vsajip repository `json-ply <https://github.com/vsajip/json-ply>`__


