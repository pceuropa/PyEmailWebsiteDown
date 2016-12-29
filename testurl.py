#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
from smtp import EmailBySmtp
import config

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0'}

r = requests
for i in config.sites:
	try:
		code = r.get(i, timeout=2)
		print(code.status_code)
		if code.status_code != 200:
			EmailBySmtp({
				'subject': i,
				'message': i,
			}).send()
	except (r.exceptions.MissingSchema, r.exceptions.ReadTimeout, r.exceptions.ConnectionError):
		EmailBySmtp({
				'subject': i,
				'message': i,
			}).send()
