#!/usr/bin/env python

import json
import re

statecodes = json.load(open('state_fips.json'))
zipmap = {}

for i in range(1,11):
    zfile = open('zipctys/zipcty%d' % i)
    zfile.readline() # skip first line
    for l in zfile:
		# FROM https://wonder.cdc.gov/wonder/sci_data/codes/fips/type_txt/cntyxref.asp
		# RECORD LAYOUT

		#  Field Description

		#   FIELD
		#   SEQUENCE                                          RELATIVE
		#                 FIELD                    LOGICAL    POSITION
		#   NUMBER        DESCRIPTION              LENGTH     FROM THRU    CONTENT NOTES


		#      1          ZIP CODE                   05         01    as

		#      2          UPDATE KEY NO              10         06    15

		#      3              ZIP ADD ON LOW NO
		#                        ZIP SECTOR NO       02         16    17
		#                        ZIP SEGMENT NO      02         18    19

		#      4             ZIP ADD ON HIGH NO
		#                        ZIP SECTOR NO       02         20    21
		#                        ZIP SEGMENT NO      02         22    23

		#      5          STATE ABBREV               02         24    25

		#      6          COUNTY NO                  03         26    28

		#      7          COUNTY NAME                25         29    53
        m = re.match(r"(?P<zip>.{5}).{18}(?P<state>..)(?P<fips>...)(?P<county>.{25})", l)
        if m:
            r = m.groupdict()
            zipmap[r['zip']] = {
            	'fips': statecodes[r['state']] + r['fips'],
            	'county': r['county'].strip().capitalize(),
            	'state': r['state']
            }

print(json.dumps(zipmap))
