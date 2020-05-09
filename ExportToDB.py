from influxdb import InfluxDBClient
import Secret

#influxdb for local tests
host = 'localhost'
port = 8086
username = 'root'
password = 'root'
dbName = 'test'

dbClient = InfluxDBClient(Secret.host,Secret.port,Secret.username,Secret.password,Secret.dbName, ssl=False, verify_ssl=False)
dbClient.switch_database(Secret.dbName)

def ssid_rogue_detected(rogue_mode,rogue_ssid,rogue_apname_last,rogue_detected_ch,rogue_mac_address,rogue_rssi):
    json_body = [{
                "measurement": 'ssid_rogue_detected',
                "tags": {
                    "mode": rogue_mode
                },
                "fields": {
                    "detected_ch": rogue_detected_ch,
                    "ssid": rogue_ssid,
                    "rogue_mac_address":rogue_mac_address,
                    "rssi":rogue_rssi,
                    "ap_name":rogue_apname_last
                        }
                    }
                ]
    print(json_body)
    dbClient.write_points(json_body)

#it works 
def uptime_instance(date_string):
    json_body = [{
                "measurement": 'uptime_instance',
                "tags": {
                    "name": 'uptime_instance',
                },
                "fields": {
                    "value": str(date_string)}
                    }
                ]
    print(json_body)
    dbClient.write_points(json_body)

def send_to_db(mac_address,ip_address,ap_name,ssid,username):
    tosend_body = [{
        "measurement": 'no_of_clients',
        "tags": {
            "type": 'active_users',
            "wlan_ssid": ssid,
            "ap_name": ap_name #this is how we identify floor
        },
        "fields": {
            "mac_address":mac_address,
            "ip_address":ip_address,
            "username":username,
            "wlan_ssid": ssid
            }
    }]                
    dbClient.write_points(tosend_body)
