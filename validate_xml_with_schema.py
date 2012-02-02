"""
A quick utility to validate an XML doc against a schema

Ben Adida
ben.adida@childrens
2009-06-26

python validate_xml_with_schema.py schema.xsd doc.xml
"""

import sys, StringIO
from lxml import etree

SCHEMA_FILE_NAME = sys.argv[1]
XML_FILE_NAME = sys.argv[2]

schema_file = open(SCHEMA_FILE_NAME, "r")
xml_file = open(XML_FILE_NAME, "r")

schema = etree.XMLSchema(etree.parse(schema_file))
doc = etree.parse(xml_file)

output = 'Validating %s against %s...   '%(XML_FILE_NAME, SCHEMA_FILE_NAME)
if schema.validate(doc):
    output += "ok"
else:
    log = schema.error_log
    error = log.last_error
    output += str(error)
print output
