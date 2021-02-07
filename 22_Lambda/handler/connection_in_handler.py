import json, os, time

def lambda_handler(event, context):
  dbconnected=False # First Run
    
  if dbconnected==False:
    print ("Connecting to some super-secret CATDB ... in handler ETA 3 seconds")
    time.sleep(3) # SOME DB CONNECTION CODE - it's not really, but you get the idea
    print ("Connected to DB....")
    dbconnected=True
    
  if dbconnected==True:
    print ("Connected to DB....moving to app code")
    print ("Running application.. something something ... cats & doggos")
    print ("Finished running app.....")

        
  # TODO implement
  return {
    'statusCode': 200,
    'body': json.dumps('Finished!')
  }
