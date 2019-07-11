import  requests

def gettest():
    r=requests.get('https://microzuul3.hyjf.com/hyjf-wbs/web/user/userinfo/100')
    print(r.status_code)
    print(r.json())

def posttest():
    paramete={
        "loginPassword": "1adbb3178591fd5bb0c248518f39bf6d",
        "readAgreement": 'true',
        "utmId": "8001",
        "customerId": "",
        "loginUserName": "13210002383"
    }
    r=requests.post('https://microzuul3.hyjf.com/hyjf-wbs/web/user/bind',json=paramete)
    print(r.status_code)
    print(r.json())


if __name__ == '__main__':
    posttest()