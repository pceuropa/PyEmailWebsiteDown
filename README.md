# PyEmailServerDown

Python3 send email notification if your website is down.

## Instalation
This application requires [python3](https://docs.python.org/3/) and module [requests](http://docs.python-requests.org/en/master/)
```
pip install requests
```

## Configure
1. Set the list of URLs to check (configuration is file testurl.py)
2. Set the mail server configurations

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
59 23 * * * python3 /path/to/testUrl/testurl.py
```
