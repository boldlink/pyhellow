# pyHelloW
[![Build Status](https://drone.tools.boldlink.io/api/badges/boldlink/pyHelloW/status.svg)](https://drone.tools.boldlink.io/boldlink/pyHelloW)

Python RestAPI for demo testing and creating platforms while development is still underway

The output you should get is:
```json
{
  "hostname": "pyhellow-api-xxxxxxxx-xxxxxx",
  "greeting": "Hello World",
  "now": "Fri, 24 Jul 2020 09:55:54 GMT"
}
```
If the OS Env variable isn't set your request will be:
```json
{
  "greeting": "Hello World",
  "now": "Fri, 24 Jul 2020 09:55:54 GMT"
}
```