# ami_bios_codes
Provides the data that POST codes from the AMI BIOS mean.

Written with Python 3 run the file like so:
`python3 ami.py <bios code>`

This will provide output in this form:
```
Message
Phase
Checkpoint
Type
```

Full example:
```
$ python3 ami.py 55
Memory not installed
PEI Phase
PEI Errors
Error
```

This data is gathered from:
https://ami.com/ami_downloads/Aptio_V_Status_Codes.pdf
