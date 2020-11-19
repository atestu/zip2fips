#!/usr/bin/env python

import json

zip2fips = json.load(open('zip2fips.json'))
fips_map = {}

for (zipcode, fips_details) in zip2fips.items():
	if fips_details['fips'] in fips_map:
		fips_map[fips_details['fips']]['zipcodes'].append(zipcode)
	else:
		fips_map[fips_details['fips']] = {
			'state': fips_details['state'],
			'county': fips_details['county'],
			'zipcodes': [zipcode]
		}

print(json.dumps(fips_map))
