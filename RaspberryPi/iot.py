 #!/usr/bin/python23

#required libraries
import sys                                 
import ssl
import json
import boto3
import paho.mqtt.client as mqtt


# for motion sensor
import RPi.GPIO as GPIO
import time
from time import sleep
from datetime import datetime

# for camera
from picamera import PiCamera


#called while client tries to establish connection with the server 
def on_connect(mqttc, obj, flags, rc):
    if rc==0:
        print ("Subscriber Connection status code: "+str(rc)+" | Connection status: successful")
        mqttc.subscribe("$aws/things/raspberrypi/shadow/update/acceptd", qos=0)
        #mqttc.publish("$aws/things/raspberrypi/shadow/update",'{"state":{"reported":{"color":"Fu"}}}')#The names of these topics start with $aws/things/thingName/shadow."
    elif rc==1:
        print ("Subscriber Connection status code: "+str(rc)+" | Connection status: Connection refused")

#called when a topic is successfully subscribed to
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos)+"data"+str(obj))

#called when a message is received by a topic
def on_message(mqttc, obj, msg):
    print("Received message from topic: "+msg.topic+" | QoS: "+str(msg.qos)+" | Data Received: "+str(msg.payload))

#creating a client with client-id=mqtt-test
mqttc = mqtt.Client(client_id="vpanchal")

mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_message = on_message

#Configure network encryption and authentication options. Enables SSL/TLS support.
#adding client-side certificates and enabling tlsv1.2 support as required by aws-iot service
mqttc.tls_set(ca_certs="/home/pi/Downloads/iot/root-ca.pem",
	          certfile="/home/pi/Downloads/iot/4a14304427-certificate.pem.crt",
	          keyfile="/home/pi/Downloads/iot/4a14304427-private.pem.key",
              tls_version=ssl.PROTOCOL_TLSv1_2, 
              ciphers=None)

#connecting to aws-account-specific-iot-endpoint
mqttc.connect("A2Y48V41HE3GSX.iot.us-east-1.amazonaws.com", port=8883) #AWS IoT service hostname and portno

#automatically handles reconnecting
mqttc.loop_start()

sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(sensor,GPIO.IN)




s3 = boto3.resource("s3","us-east-1")
sns = boto3.client("sns","us-east-1")
camera = PiCamera()
camera.rotation = 180

a=0

rc = 0

try:
    while rc == 0:
        i = GPIO.input(sensor)
        if i == 1:
            camera.start_preview()
            print "Intruder Detected"

            for i in range(5):
                camera.capture('/home/pi/Desktop/Iota_Proj/image%s.jpg' %i)
                sleep(1)
            camera.stop_preview()#Camera optn terminates after clicking 5 pics

            
            b=s3.Bucket('intrusion-data')
            b.Acl().put(ACL='public-read')


            
            data = open("/home/pi/Desktop/Iota_Proj/image0.jpg", "rb")
            obj = s3.Bucket("intrusion-data").put_object(Key="101.jpg", Body=data)
            obj.Acl().put(ACL='public-read')
            
            data = open("/home/pi/Desktop/Iota_Proj/image1.jpg", "rb")
            obj = s3.Bucket("intrusion-data").put_object(Key="102.jpg", Body=data)
            obj.Acl().put(ACL='public-read')

            data = open("/home/pi/Desktop/Iota_Proj/image2.jpg", "rb")
            obj = s3.Bucket("intrusion-data").put_object(Key="103.jpg", Body=data)
            obj.Acl().put(ACL='public-read')

            data = open("/home/pi/Desktop/Iota_Proj/image3.jpg", "rb")
            obj = s3.Bucket("intrusion-data").put_object(Key="104.jpg", Body=data)
            obj.Acl().put(ACL='public-read')
        
            data = open("/home/pi/Desktop/Iota_Proj/image4.jpg", "rb")
            obj = s3.Bucket("intrusion-data").put_object(Key="105.jpg", Body=data)
            obj.Acl().put(ACL='public-read')
            
        

            response = sns.publish(
                TopicArn='arn:aws:sns:us-east-1:271308400076:intrusion_detection',
                Message='Intrusion Has Been Detected, Click on the following Link to see who has intruded http://weblab.cs.uml.edu/~sjaiswal/IotaProj/index.php?a='+str(time.time()),
                Subject='Intrusion Detection')
            
            data={}
            data['motion']=i
            data['time']=datetime.now().strftime('%Y/%m/%d %H:%M:%s')
            playload = '{"state":{"reported":'+json.dumps(data)+'}}'
            print(playload)

            #the topic to publish to
            #the names of these topics start with $aws/things/thingName/shadow.
            msg_info = mqttc.publish("$aws/things/raspberry-pi/shadow/update", playload, qos=1)
            
            sleep(180)
            
        elif i == 0:
            print(i)     # i = 1: Motion detected; i = 0: No Motion
            data={}
            data['motion']=i
            data['time']=datetime.now().strftime('%Y/%m/%d %H:%M:%s')
            playload = '{"state":{"reported":'+json.dumps(data)+'}}'
            print(playload)

            #the topic to publish to
            #the names of these topics start with $aws/things/thingName/shadow.
            msg_info = mqttc.publish("$aws/things/raspberry-pi/shadow/update", playload, qos=1)
            print "No Intrusion Detected"
            time.sleep(1)
              

except KeyboardInterrupt:
    pass

GPIO.cleanup()
