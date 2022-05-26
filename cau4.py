import requests
import json
import meraki_info
def get_inventory_devices():
    url_inven = meraki_info.base_url + f"/organizations/{meraki_info.org_id}/inventory/devices"
    headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Cisco-Meraki-API-Key":meraki_info.api_key,
        }

    respon = requests.get(url_inven, headers=headers)
    data_device = respon.json()
    # print (data_device)
    # print(json.dumps(data_device, indent=4))
    return data_device

def get_netID():
    data_device = get_inventory_devices()
    num_device = len(data_device)
    # print (num_device)
    list_device = []
    for i in range(num_device):
        if data_device[i]["networkId"] == None:
            list_device.append(data_device[i])
            # print(json.dumps(list_device, indent=4))
            # print(list_device)
    list_device_null = len(list_device)
    print(list_device_null)
    for j in range(list_device_null):
        print(list_device[j]["networkId"])
     
if __name__=="__main__":
    # get_inventory_devices()
    get_netID()
