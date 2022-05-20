import pandas as pd
import requests
from xml.etree import ElementTree as ET
import xmltodict

APIKEY = "zOVsayBFwURddA1RPDX0L2MzMSH9k7Ivls+AztXTeudlmP4d7Z/zL50JEdI4Eu82mhRBur/IYHJgb5GJR8jpzQ=="
URL = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade"
CODE = "11110"
START = "2012-01"
END = "2021-12"

data = []
for ymd in pd.date_range(START, END, freq="1M").strftime("%Y%m").to_list():
    response = requests.get(
        URL,
        params={
            'serviceKey' : APIKEY,
            'LAWD_CD' : CODE,
            'DEAL_YMD' : ymd
        }
    )
    df = pd.DataFrame.from_dict(xmltodict.parse(ET.tostring(ET.fromstring(response.text)[1][0], encoding='unicode')).get('items').get('item'))
    df['ymd'] = ymd
    data.append(df)
data = pd.concat(data)
print(data.info())