from cloudify_rest_client import CloudifyClient
import json

#in this section I assumed that have the json file that is gcp service account key
with  open('myhelloworldproject-270109-6f259abe5490.json', 'r') as gcp_json_file:
    gcp_json_string = gcp_json_file.read()

client = CloudifyClient(username='admin', password='admin', tenant='default_tenant', host='172.17.0.2')
# on this operation we should validate schema of the gcp json_string
client.secrets.create(key='gcp_json_secret', value=gcp_json_string, update_if_exists=True)
response_dict = json.loads(client.secrets.get('gcp_json_secret').value)

#now i can use each field
print response_dict.get('project_id')
