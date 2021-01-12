import requests
import json
from threading import Thread

r = requests.get("https://formulae.brew.sh/api/formula.json")

package_json = r.json()
package_str = json.dumps(package_json, indent=4)
package_len = len(package_json)

def api_getter(package):
    try :
        package_name = package['name']
        package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'
        r = requests.get(package_url)
        package_json = r.json()
        #package_str = json.dumps(package_json, indent=4)
        package_api = package_json['analytics']['install']['30d'][package_name]
        print(package_api)
    except Exception as _:
        pass

threads = []
for package in package_json:
    thread = Thread(target=api_getter, args=[package])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()