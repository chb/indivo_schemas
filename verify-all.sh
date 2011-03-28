#!/bin/bash
python validate_xml_with_schema.py allergy.xsd allergy.xml
python validate_xml_with_schema.py contact.xsd contact.xml
python validate_xml_with_schema.py demographics.xsd demographics.xml
python validate_xml_with_schema.py hospital-api-metadata.xsd hospital-api-metadata.xml
python validate_xml_with_schema.py immunization.xsd immunization.xml
python validate_xml_with_schema.py lab.xsd lab.xml
python validate_xml_with_schema.py medication.xsd medication.xml
python validate_xml_with_schema.py metadata.xsd metadata.xml
python validate_xml_with_schema.py problem.xsd problem.xml
python validate_xml_with_schema.py procedure.xsd procedure.xml
python validate_xml_with_schema.py vitals.xsd vitals.xml

