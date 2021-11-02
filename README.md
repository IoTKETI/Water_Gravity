# Water_Gravity

Water_Gravity는 Nodejs를 기반으로 개발되었으며, 해당 어플리케이션은 센서로부터 물의 탁도(NTU)를 측정하여 serial(i2c)로 부터 전송받아 데이터를 oneM2M 플랫폼에 축적한다.

## version 
1.0.0

## Installation
<div align="center">
<img src="https://user-images.githubusercontent.com/29790334/28315422-497d1300-6bf9-11e7-92c7-a0f82d8b4a29.png" width="400"/>
</div><br/>

- [Node.js](https://nodejs.org/en/)<br/>
Node.js는 오픈 소스 JavaScript 엔진인 크롬 V8에 비동기 이벤트 처리 라이브러리인 libuv를 결합한 플랫폼이다. <br/>
JavaScript로 브라우저 밖에서 서버를 구축하는 등의 코드를 실행할 수 있게 해주는 런타임 환경이다.<br/>
Water_Gravity은 Nodejs LTS14.x을 사용한다.
  https://nodejs.org/en/download/
  
## Configuration
- Water_Gravity 동작시키기 위해 설정해야 하는 것은 conf.js에 있다.
- 또한, Water_Gravity는 Gravity sensor를 동작시키기위한 python 모듈 혹은 코드 동작이 필요하다.
- Water_Gravity 폴더에 접근후에 아래 명령어를 입력한다.
- 아래 명령어를 입력하게 되면 Water_Gravity 동작에 필요한 모듈이 설치가 된다.
```
 
 npm install
 
```

- oneM2M 플랫폼 연결을 위한 설정은 conf.js에서 한다.
```
var conf = {};
var cse = {};
var ae = {};
var cnt = {};
var noti = {};
//cse config
cse.host = "203.253.128.139";  //CSE HOST IP
cse.port = "7599";             //CSE HTTP PORT
cse.name = "wdc_base";
cse.id = "/wdc_base";
cse.mqttport = "1883";         //CSE MQTT BOROKER PORT

//ae config
ae.name = "kwater-poc";        //AE NAME
ae.id = "SM";                  //AE ID
ae.parent = "/" + cse.name;
ae.appid = "kwater-poc"

cnt.name = 'sensor4';          //CNT NAME
cnt.flexcnt = 'WtqltGnrlMesureIem';  // FLEX CNT NAME
cnt.flexsub = 'WtqltMesureSetup';    // FLEX SUBSCRIPTION NAME

noti.id = 'nodered';                //NOTIFICATION ID

conf.cse = cse;
conf.ae = ae;
conf.cnt = cnt;
conf.noti = noti;
module.exports = conf;
 
```

```
var delay = 5000;                // Upload time to oneM2M platform 

```

## Gravity sensor python code
```
- Gravity sensor는 아두이노에서 동작되는 탁도센서로, 물의 탁도를 측정해주는 센서이다.
```
<img src="https://user-images.githubusercontent.com/29790334/139806139-5213a7b9-edcd-49aa-8c1f-970b90f384d3.png" width="400"/>
```
- 라즈베리파이는 Analog 신호를 받지 못하기 때문에 ADC Converter를 통해 Digital 신호로 변화하는 장치가 필요하다.
- ADC Converter는 sparkfun의 ADS1015를 사용했다.
```
![image](https://user-images.githubusercontent.com/29790334/139806416-8eba805a-749e-4bb8-b230-b59d6a116ab6.png)
```
- 동작시키기 위한 모듈은 "adafruit_ads1x15" 이며, 해당 모듈을 설치하면 동작시킬 수 있다.
https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15
import board
import busio
import time
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
chan = AnalogIn(ads,ADS.P0)

volt = chan.voltage+0.6
if(volt < 2.5):
  y = 3000.0
else:
  y = -1120.4*pow(volt,2) + 5742.3 *volt - 4353.8

print(round(y,3))

```

## Running
Nodejs는 아래와 같은 명령어를 통해 실행을 합니다.
```
node app.js
```
