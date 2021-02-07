
import json, os, time, logging

print('Cold Start! .. Loading function')
dbconnected=False # First Run
if dbconnected==False:
  print ("Coldstart DB Connection ... ETA 3s")
  time.sleep(3) # SIMULATE DB CONNECTION TIME
  print ("Connected to DB....")
  dbconnected=True

def lambda_handler(event, context):
  global dbconnected
  if dbconnected==False:
    print ("Connecting to super-secret CATDB ... in handler ETA 3s")
    time.sleep(3) # SIMULATE DB CONNECTION TIME
    print ("Connected to DB....")
    dbconnected=True
    
  if dbconnected==True:
    print ("DB Connected....moving to app code")
    print ("Running application.. something something ... cats & doggos")
    
  return { 'statusCode': 200, 'body': json.dumps('Finished!') }

