import requests

url = 'https://www.cdc.gov/flu/avianflu/modules/commercial-backyard-flocks.csv'
response = requests.get(url)

with open('data.csv', 'wb') as f:
    f.write(response.content)