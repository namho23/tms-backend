 # Vehicle Data Request & Request Format
 - [Vehicle history track query](#vehicle-history-track-query)
 - [Vehicle GPS total mileage inquiry](#vehicle-gps-total-mileage-inquiry)
 - [Vehicle GPS daily mileage inquiry](#vehicle-gps-daily-mileage-inquiry)
 - [Vehicle status inquiry](#vehicle-status-inquiry)
 - [Query vehicle status based on equipment](#query-vehicle-status-based-on-equipment)
 - [Bulk vehicle status inquiry](#bulk-vehicle-status-inquiry)
G7 provides python SDK it is based on python2 so I needed to make it python3 compatible

## [Vehicle history track query](http://openapi.huoyunren.com/app/docopenapi/#/productCenter/restApi/detail?uri=%2Fv1%2Fdevice%2Ftruck%2Fhistory_location&method=GET)
 - As the name implies, this api endpoint is used to retrieve the specified vehicle track.
 - In this project, this api is used for playback functionality.
 > This api needs `from` and `to` as start time and finish time, this interval should be less than 31 days. For example if you want to see the vehicle history track from `2019-01-01` to `2010-02-28`, time delta is over 31 days, so this api return error code. So you need to call this api twice to get the full vehicle history track. G7 support pagination and for more information please take a look at [here](http://openapi.huoyunren.com/app/docopenapi/#/productCenter/restApi/detail?uri=%2Fv1%2Fdevice%2Ftruck%2Fhistory_location&method=GET)
### Code
```
from tms.g7.interfaces import G7Interface
queries = {
    'plate_num': '鲁UA3161',
    'from': '2019-06-09 00:00:00',
    'to': '2019-06-10 00:00:00'
}
data = G7Interface.call_g7_http_interface(
    'VEHICLE_HISTORY_TRACK_QUERY',
    queries=queries
)
```
### Request Parameter
```
{
    'plate_num': '鲁UA3161',
    'from': '2019-06-09 00:00:00',
    'to': '2019-06-10 00:00:00'
}
```
### Response
```
{
    'code': 0,
    'msg': 'succ',
    'sub_code': 0,
    'sub_msg': None,
    'req_id': '2573652999440448512',
    'data': [
        {'lng': '120.39689000016968', 'lat': '36.06112266041201', 'speed': 4, 'course': 311, 'time': 1560077821000, 'distance': 1502},
        {'lng': '120.39687900171869', 'lat': '36.061132657660345', 'speed': 6, 'course': 311, 'time': 1560077822000, 'distance': 148},
        {'lng': '120.39679900772626', 'lat': '36.06115662639514', 'speed': 7, 'course': 290, 'time': 1560077826000, 'distance': 767},
        {'lng': '120.39674400786969', 'lat': '36.06113659643059', 'speed': 6, 'course': 252, 'time': 1560077829000, 'distance': 542},
        {'lng': '120.3967240030141', 'lat': '36.06108257485565', 'speed': 5, 'course': 216, 'time': 1560077832000, 'distance': 627}
    ]
}
```

## [Vehicle GPS total mileage inquiry](http://openapi.huoyunren.com/app/docopenapi/#/productCenter/restApi/detail?uri=%2Fv1%2Fdevice%2Ftruck%2Fmileage&method=GET)
- As the name implies, this api endpoint is used to get mileage
 - In this project, this api is used for calculating job mileage and vehicle tire running mileage.
 > This api needs `from` and `to` as start time and finish time, this interval should be less than 31 days. For example if you want to see the vehicle history track from `2019-01-01` to `2010-02-28`, time interval is over 31 days, so this api return error code. So you need to call this api twice to get the total mileage. G7 support pagination and for more information please take a look at [here](http://openapi.huoyunren.com/app/docopenapi/#/productCenter/restApi/detail?uri=%2Fv1%2Fdevice%2Ftruck%2Fmileage&method=GET)
### Code
```
from tms.g7.interfaces import G7Interface
queries = {
    'plate_num': '鲁UA3161',
    'from': '2019-06-09 00:00:00',
    'to': '2019-06-10 00:00:00'
}
data = G7Interface.call_g7_http_interface(
    'VEHICLE_GPS_TOTAL_MILEAGE_INQUIRY',
    queries=queries
)
```
### Request Parameter
```
{
    'plate_num': '鲁UA3161',
    'from': '2019-06-09 00:00:00',
    'to': '2019-06-10 00:00:00'
}
```
### Response
```
{
    'code': 0,
    'msg': 'succ',
    'sub_code': 0,
    'sub_msg': None,
    'req_id': '2573658561033026560',
    'data': {
        'total_mileage': 10642022
    }
}
```

## Vehicle GPS daily mileage inquiry
 - This api is not used in this project
### Code
```
from tms.g7.interfaces import G7Interface
queries = {
    'plate_num': '鲁UA3161',
    'from': '2019-06-09',
    'to': '2019-06-10'
}
data = G7Interface.call_g7_http_interface(
    'VEHICLE_GPS_DAILY_MILEAGE_INQUIRY',
    queries=queries
)
```
### Request Parameter
```
{
    'plate_num': '鲁UA3161',
    'from': '2019-06-09',
    'to': '2019-06-10'
}
```
### Response
```
{
    'code': 0,
    'msg': 'succ',
    'sub_code': 0,
    'sub_msg': None,
    'req_id': '2573659272198241280',
    'data': {
        {'total_mileage': 10642022, 'date': '2019-06-09'},
        {'total_mileage': 52900403, 'date': '2019-06-10'}
    }
}
```

## Vehicle status inquiry
 - As the name implies, this api endpoint is used for getting current vehicle status.
 - In this project, this api is used when the user click the vehicle button on the monitoring view
 
### Code
```
from tms.g7.interfaces import G7Interface
queries = {
    'plate_num': '鲁UA3161',
    'fields': 'loc,status,cold,driver'
}
data = G7Interface.call_g7_http_interface(
    'VEHICLE_STATUS_INQUIRY',
    queries=queries
)
```
### Request Parameter
```
{
    'plate_num': '鲁UA3161',
    'fields': 'loc,status,cold,driver'
}
```
### Response
```
{
    'code': 0,
    'msg': 'succ',
    'sub_code': 0,
    'sub_msg': None,
    'req_id': '2573659272198241280',
    'data': {
        'gpsno': '91302991',
        'time': '2019-06-11 22:49:22',
        'loc': {
            'lng': '116.60331363585708',
            'lat': '37.474271621975795',
            'address': None,
            'speed': 53,
            'course': 238,
            'gps_time': '2019-06-11 22:49:20',
            'location_type': 0
        },
        'status': {
            'battery': -1,
            'acc': 0,
            'gps': 1,
            'gsm': -1,
            'voltage': -1,
            'main_vol': 256,
            'battery_vol': 40,
            'properties': 'acc:0,gps:1,mg:154037.0,doorStatus:0,driftStatus:0,loadStatus:3,satellites:12,signal:31,move:1,engine:1,gpsSpeed:53,batteryVol:40,mainVol:256,deviceRunningTime:2888098,emsengine:1207'
        },
        'cold': None,
        'driver': None,
        'gpsStatus': 4
    }
}
```

## Query vehicle status based on equipment
 - this api is not used in this project
### Code
```
from tms.g7.interfaces import G7Interface
queries = {
    'gpsno': '91302991',
    'fields': 'loc,status,cold,driver',
    'addr_required': True
}
data = G7Interface.call_g7_http_interface(
    'VEHICLE_STATUS_BY_GPS',
    queries=queries
)
```
### Request Parameter
```
{
    'plate_num': '鲁UA3161',
    'fields': 'loc,status,cold,driver',
    'addr_required': True
}
```
### Response
```
{
    'code': 0,
    'msg': 'succ',
    'sub_code': 0,
    'sub_msg': None,
    'req_id': '2573667680196508672',
    'data': {
        'gpsno': '91302991',
        'time': '2019-06-11 23:16:30',
        'loc': {
            'lng': '116.43025177923609',
            'lat': '37.46722295367001',
            'address': '山东省德州市德城区 距德州北外环/崇德五大道(路口)约263米 山东省德州市德城区东南约291米处',
            'speed': 41,
            'course': 299,
            'gps_time': '2019-06-11 23:16:28',
            'location_type': 0
        },
        'status': {
            'battery': -1,
            'acc': 0,
            'gps': 1,
            'gsm': -1,
            'voltage': -1,
            'main_vol': 251,
            'battery_vol': 40,
            'properties': 'acc:0,gps:1,mg:154240.0,doorStatus:0,driftStatus:0,loadStatus:3,satellites:12,signal:26,move:1,engine:1,gpsSpeed:41,batteryVol:40,mainVol:251,deviceRunningTime:2889726,emsengine:1104'
        },
        'cold': None,
        'driver': None,
        'gpsStatus': 4
    }
}
```
## Bulk vehicle status inquiry
### Code
```
from tms.g7.interfaces import G7Interface
from tms.vehicle.models import Vehicle
plate_nums = Vehicle.objects.values_list('plate_num', flat=True)
body = {
    'plate_nums': list(plate_nums),
    'fields': ['loc']
}
data = G7Interface.call_g7_http_interface(
    'BULK_VEHICLE_STATUS_INQUIRY',
    body=body
)
```
### Request Parameter
```
{
    'plate_num': ['鲁UA3161'],
    'fields': ['loc']
}
```
### Response
```
{
    'code': 0,
    'msg': 'succ',
    'sub_code': 0,
    'sub_msg': None,
    'req_id': '2573667680196508672',
    'data': {
        '鲁UG2802': {
            'plate_num': '鲁UG2802',
            'code': 0,
            'msg': 'ok',
            'data': {
                'gpsno': '91302990',
                'time': '2019-06-21 02:37:15',
                'loc': {
                    'lng': '112.88492438805328',
                    'lat': '37.835018526899056',
                    'address': None,
                    'speed': 0,
                    'course': 197,
                    'gps_time': '2019-06-21 02:37:08',
                    'location_type': 0
                },
                'status': None,
                'cold': None,
                'driver': None,
                'gpsStatus': 3
            }
        },
        '鲁UA3161': {
            'plate_num': '鲁UA3161',
            'code': 0,
            'msg': 'ok',
            'data': {
                'gpsno': '91302991',
                'time': '2019-06-21 02:34:32',
                'loc': {
                    'lng': '120.43016001114678',
                    'lat': '36.1991544518921',
                    'address': None,
                    'speed': 0,
                    'course': 13,
                    'gps_time': '2019-06-21 02:34:31',
                    'location_type': 0
                },
                'status': None,
                'cold': None,
                'driver': None,
                'gpsStatus': 3
            }
        },
        '鲁UC6753': {
            'plate_num': '鲁UC6753',
            'code': 0,
            'msg': 'ok',
            'data': {
                'gpsno': '91302992',
                'time': '2019-06-21 02:37:49',
                'loc': {
                    'lng': '118.87882951006411',
                    'lat': '38.06398490721363',
                    'address': None,
                    'speed': 0,
                    'course': 95,
                    'gps_time': '2019-06-21 02:37:43',
                    'location_type': 0
                },
                'status': None,
                'cold': None,
                'driver': None,
                'gpsStatus': 3
            }
        }
    }
}
