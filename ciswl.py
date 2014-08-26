#!/usr/bin/python
# -*- coding: utf-8 -*-
# (c) 2014, Phil Eichinger, phil@zankapfel.net
# License: GPLv2
#
# Custom Idle Screen White List
# Use Team Eureka's whitelist but with a custom idle screen URL
# "Fo ciswl my chrizzle"
from __future__ import print_function
import json
import sys
import urllib2
import cgi;
#import cgitb; cgitb.enable()

try: 
  if( sys.argv[1] == "-d"):
    debug = True
  else:
    debug = False
except:
  debug = False

eureka_wl = "http://pwl.team-eureka.com/applist.php"
idle_appid = "00000000-0000-0000-0000-000000000000"
f = cgi.FieldStorage()

try:
  idle_url = f["url"].value
except:
  idle_url = "https://www.google.at"

try:
  if(f["debug"].value == "1"):
    debug = True
except:
  pass

print("Content-Type: text/html")
if( not debug ):
  print("Pragma: public")
  print("Expires: 0")
  print("Cache-Control: must-revalidate, post-check=0, pre-check=0")
  print("Cache-Control: public")
  print("Content-Description: File Transfer")
  print("Content-Disposition: attachment; filename='apps.conf'")
  print("Content-Transfer-Encoding: binary")
print()
print()
print()

u = urllib2.urlopen( eureka_wl )

print(urllib2.unquote(u.readline()), end='')

j = json.loads(urllib2.unquote(u.readline()))

for i in j['applications']:
  if( i['app_id'] == idle_appid ):
    i['url'] = idle_url

if( debug ):
  print( json.dumps( j,sort_keys=True,indent=4, separators=(',', ': ')) )
else:
  print(json.dumps(j))
