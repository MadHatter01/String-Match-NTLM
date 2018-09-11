# Python module to match string from URL Contents for NTLM Associated sites

The module consists of method to match particular word from the url contents.

## Getting Started

The script requires a python environment to run successfully.

### Environment

Python version : 3.x

Modules used:
* requests
* requests_ntlm
* re

requests_ntlm module needs to be installed.
Official Documentation for requests_ntlm can be found here: https://pypi.python.org/pypi/requests_ntlm/0.2.0

### Steps on installing requests_ntlm:
Following prerequisites must be met to set up code execution environment.

### prerequisites:
* python needs to be installed 
* pip needs to be installed

Now to install ntlm_requests , follow the below commands.

```
pip install requests_ntlm
```


Now try to execute 
```
import requests_ntlm
```

If there are no errors, that means the module is successfully installed.

## Running the Scripts

The module can be called by

```
import ntlm_authentication
```

The method used to match the file content is "match_content". It uses four arguments

* url : Pass in any NTLM supported URL 
* username : user name
* password : password credentials
* match word : Pass in the word you would like to match in the contents

It can be called by:

```
ntlm_authentication.match_content(url,username,password,match_word)
```

The parameters can be passed accordingly.
