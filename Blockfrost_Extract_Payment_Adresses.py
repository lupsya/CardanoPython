########### This script is extracting payment addresses from each staking address, using BLockfrost API, so BLockfrost API key is needed
import csv
import json
import requests

### credentials, and API request
headers = {'project_id': '<BLOCKFROST API KEY>'}
url = "https://cardano-mainnet.blockfrost.io/api/v0/accounts/stake1uyhv8wae6z03455tmudvaw7sxvt7e536tlm6rnglkdqzqqsz9vrqa/addresses"

## Loading JSON file with stake addresses
f = open('sample.json')
data = json.load(f)
f.close()
payment_addresses_list = []

#### loop extracting data from BLockfrost API using stake addresses
for i in data['data']:
    url = "https://cardano-mainnet.blockfrost.io/api/v0/accounts/"+(i["stake_address"])+"/addresses?count=1"
    response = requests.get(url, headers=headers)
    response = response.json()
    print(response)
    payment_addresses_list.append(response)

print(payment_addresses_list)

"""
# Save as txt
with open('payment addys.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(f'{tup[0]} {tup[1]}' for tup in payment_addresses_list.append))
"""
""" 
###### JSON FILE saving  #######
# Serializing json
json_object = json.dumps(payment_addresses_list.append, indent=4)

Writing to sample.json
with open("final_extracted_addresses.json", "w") as outfile:
    outfile.write(json_object)
"""

