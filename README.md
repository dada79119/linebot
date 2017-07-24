### 更新時間:20170724 11:13

# Python Line Bot
It's echo function of Line Bot that use your private ssl certification in Google Cloud Platform.

## Environment
Ubuntu 16.04 LTS </br>
python-3.5.2 </br>
pip freeze > requirements.txt

## HTTP/HTTPS
HTTPS

## Document
In the good cloud platform I open a port 9453 to connect line bot api. </br>
The file of app.py is flask structure.</br>

In line 13 and 14 of app.py you need to type in YOUR_CHANNEL_ACCESS_TOKEN </br>
and YOUR_CHANNEL_SECRET 

In line 44 to 46 of app.py you need to type in file path of certificate.crt ,private.key and ca_bundle.crt. About more details of three files you can google that have something open resource like SSL For Free - Free SSL Certificates in Minutes.

In line 47 of app.py the SERVER PUBLIC IP. Maybe you can set 0.0.0.0, and SERVER PORT means the open port that you set (9453). 
 
## Use
```
git clone https://github.com/dada79119/linebot.git
```


