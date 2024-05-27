import urllib.request
import urllib.error
import urllib.parse
import json
url = 'http://httpbin.org/json'
url = 'http://httpbin.org/post'
url = 'http://example.com/nonexistent'
url = 'http://example.com'
data = {'key1': 'value1', 'key2': 'value2'}
headers = {'User-Agent': 'Mozilla/5.0'}
# open the url and fetch the content
with urllib.request.urlopen(url) as response:
    html = response.read
# print the fetched content
print(html)


# Errors
try:
    with urllib.request.urlopen(url) as reponse:
        html = response.read()
    print(html)
except urllib.error.HTTPError as e:
    print(f'HTTP error occurred: {e.code} {e.reason}')
except urllib.error.URLError as e:
    print(f'URL error occurred: {e.reason}')



# Create a request object
req = urllib.request.Request(url, headers=headers)
# Open the URL and fetch the content
with urllib.request.urlopen(req) as response:
    html = response.read()
print(html)

# Encode the data
data = urllib.parse.urlencode(data).encode()
# create a request object
req = urllib.request.Request(url, data=data)
# Open the URL and fetch the response
with urllib.request.urlopen(req) as response:
    html = response.read()
print(html)



# Open the URL and fetch the content
with urllib.request.urlopen(url) as response:
    data = response.read()
    json_data = json.loads(data)
print(json_data)    