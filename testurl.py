#!/usr/bin/env python
#-*- coding:utf-8 -*-
from smtp import EmailBySmtp
import config
import urllib.request

    
for i in config.sites:
	try:
		urllib.request.urlopen(i)
		print (i, "working connection")

	except urllib.error.URLError:
		print (i, "ERROR: working connection")
		EmailBySmtp({
			'subject': i,
			'message': i,
		}).send()
