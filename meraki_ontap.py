import requests
import meraki_info
import json
def get_org():
    url_org = meraki_info.base_url + "/organizations"

    header = {
        "X-Cisco-Meraki-api-key":meraki_info.api_key,
    }

    respon = requests.get(url_org, headers=header)
    # data = respon.text
    # print(type(data))
    data = respon.json()
    # print(json.dumps(data, indent=4))

    num = len(data)
    # print(num)
    list_id = []
    org_id = int(input("Mời nhập org muốn lấy: "))
    # for org_id in range(num):
    org  = data[org_id]
    print(org)
    # print(list_id)
    # org_id = input("Mời nhập Id muốn lấy: ")
    # for j in list_id:
    #     # print(j)
    #     if j == org_id:
    #         return j
    
if __name__ == "__main__":
    get_org()PP
