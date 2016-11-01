# jcapi
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import jcapi 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import jcapi
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import jcapi
from jcapi.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = jcapi.DefaultApi()
x_api_key = 'x_api_key_example' # str |  (optional)
limit = 56 # int |  (optional)

try:
    # Get JumpCloud systemusers.
    api_response = api_instance.systemusers_get(x_api_key=x_api_key, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->systemusers_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:3004/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**systemusers_get**](docs/DefaultApi.md#systemusers_get) | **GET** /systemusers | Get JumpCloud systemusers.


## Documentation For Models

 - [InlineResponse200](docs/InlineResponse200.md)
 - [SystemUser](docs/SystemUser.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author


