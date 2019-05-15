# Raw Logs parser

### Input: All ` .log.gz ` files inside `LOGS_INPUT_FOLDER` folder (recursive)
### Output: CSV files (`logs` and `report`)

### Log example:
```js
#Date: 2019-05-15 13:45:07
#Version: 1.0
#Software: Highwinds Software
#Fields: date	time	cs-method	c-ip	cs-version	cs-referrer	cs-user-agent	filesize	cs-bytes	sc-bytes	s-ip	time-taken	sc-status	cs-uri-query	cs-uri-stem	x-byte-range	comment
2019-05-15	13:45:07	GET	255.255.255.0	http	-	AppleCoreMedia/1.0.0.16C50 (iPad; U; CPU OS 12_1_1 like Mac OS X; en_us)	11338143	419	163	255.255.255.255	0.000	206	-	/url/path	bytes=0-1	-
```

### Output example:
#### Logs (parser.py):
##### Fields: date	time	cs-method	c-ip	cs-version	cs-referrer	cs-user-agent	filesize	cs-bytes	sc-bytes	s-ip	time-taken	sc-status	cs-uri-query	cs-uri-stem	x-byte-range	comment
```
2019-05-15,13:45:07,GET,255.255.255.0,http,-,AppleCoreMedia/1.0.0.16C50 (iPad; U; CPU OS 12_1_1 like Mac OS X; en_us),11338143,419,163,255.255.255.255,0.000,206,-,/url/path,bytes=0-1
```

#### Report (report.py):
##### Fields: date	time	cs-method	c-ip	cs-version	cs-referrer	cs-user-agent	filesize	cs-bytes	sc-bytes	s-ip	time-taken	sc-status	cs-uri-query	cs-uri-stem	x-byte-range	comment	hits	visitors
```
2019-05-15,13:45:07,GET,255.255.255.0,http,-,AppleCoreMedia/1.0.0.16C50 (iPad; U; CPU OS 12_1_1 like Mac OS X; en_us),11338143,419,163,255.255.255.255,0.000,206,-,/url/path,bytes=0-1,1,1
```