import pandas as pd
import requests
from xml.etree import ElementTree as ET
import xmltodict

APIKEY = "x+wB0jStYlKe8vROEBp+XGXpIXAMHSzYaDWZ6DEciNEfl3ypAAvQwkFXN/cnZ67xg+mr13V9TZjeRT7Xkog4rg=="
URL = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade"
CODE = "11110"
START = "2011-01"
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
data.to_csv('apt.csv', encoding ='utf-8-sig')

df = pd.read_csv('apt.csv')
print(df.head(3))
print(df.columns)
new_df = pd.DataFrame(df, columns=['ymd','법정동','아파트','전용면적','거래금액'])
print(new_df.head(3))
new_df.to_csv('apt2.csv',encoding ='utf-8-sig')