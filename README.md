# Instagram-Rare-Username-Checker
A simple asynchronous tool that checks if an Instagram username is taken or not

## About
It is a proxyless tool that checks the availablity of Instagram usernames in blazing fast
speed. It checks if the http request status code is ```404```. If it is, it will automatically assume that the Instagram username is not taken. 

This tool can be inaccurate at times because it does not use the actual Instagram api. It only checks if the username's Instagram url is invalid.

This tool is used for educational purposes only. 

## Picture
![Picture](https://i.ibb.co/DYkq3rK/Screenshot-159.png)

## How to use
- Python must be installed

1. If you dont have python installed, download python 3.7.6
and make sure you click on the 'ADD TO PATH' option during
the installation.

2. Type ```pip install aiohttp``` in cmd

3.  Add the usernames you want to check in ```usernames.txt```. Do not put a lot of usernames because you can get rate limited and it can become more inaccurate. It is recommended to check around 500 usernames then wait 24 hours before you can check again.  

4.  Make sure you are in the same directory as the folder you downloaded it in.  Type
```python main.py``` in cmd to run

5. Once it is done running, available usernames will be saved in ```hits.txt```. 
