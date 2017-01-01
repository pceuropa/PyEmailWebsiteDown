# PyEmailWebsiteDown

App send email notification if your website is down.

## Instalation
This application requires [python3](https://docs.python.org/3/)

## Configure
1. Set the list of URLs to check (configuration is config.py)
2. Set the mail server configurations

Example
```
sites = [
	'https://yii2-menu.pceuropa.net/',
	'https://pceuropa.net',
]

smtp = {
	'server': 'smtp@example.com:587',
	'login': 'info@example.com',
	'password': 'pass',
	'From': 'info@example.com',
	'to': 'info@example.com',
}
```

## Usage
3. Verify the configuration 
```
python3 testurl.py
```

4. Set [cron](https://crontab.guru/) to check your websites on e.g. daily basis

```
crontab -u username -e
```
add the line 
```
@daily python3 /path/to/testUrl/testurl.py
```
