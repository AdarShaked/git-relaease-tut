from cloudify_rest_client import CloudifyClient
import json

# in this section i created the "gcp_json_secret" with -f flag using cli command
#note that the backend should add schema validation  of the gcp json that cloudify recieves
client = CloudifyClient(username='admin', password='admin', tenant='default_tenant', host='172.17.0.2')
json_string = client.secrets.get('gcp_json_secret').value
json_dict = json.loads(json_string)

# get value
print json_dict.get('project_id')
