#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'dusanklinec'


import unittest
from jbossply import jbossparser


test_simple = """{
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
}"""


class SimpleTest(unittest.TestCase):
    """Simple test from the readme"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simple(self):
        parser = jbossparser.JbossParser()
        result = parser.parse(test_simple)
        expected = {u'outcome': u'success', u'result': {
            u'rule-3': {
                u'pattern': u'^/pki/?$',
                u'flags': u'L,QSA,R',
                u'condition': None,
                u'substitution': u'/ejbca/adminweb'},
            u'rule-1': {
                 u'pattern': u'^/$',
                 u'flags': u'L,QSA,R',
                 u'condition': None,
                 u'substitution': u'/ejbca'
            }}}

        self.assertEqual(expected, result, "Result does not match")

if __name__ == "__main__":
    unittest.main()  # pragma: no cover


