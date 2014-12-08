import requests
import json
tfile = open("/home/pi/temperv14/wendu.txt")
text = tfile.read()
tfile.close()
temperature = text
#res ='{"value":%.1f}'% temperature
#output = open('/mnt/tmp/temp.txt','w')
#output.write(res)
#output.close
print "temperature: %s" %temperature
apiurl='http://api.yeelink.net/v1.0/device/16095/sensor/27779/datapoints'
apiheaders = {'U-ApiKey': '1e168412bb6e1a6a3dbb8e1493113caf', 'content-type': 'application/json'}
payload = {'value': temperature}
r = requests.post(apiurl, headers=apiheaders, data=json.dumps(payload))
print "response status: %d" %r.status_code 

