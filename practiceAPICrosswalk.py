import pandas as pd
import requests

# return a Pandas Dataframe of HUD USPS Crosswalk values

# Note that type is set to 1 which will return values for the ZIP to Tract file and query is set to VA which will return Zip Codes in Virginia
url = "https://www.huduser.gov/hudapi/public/usps?type=1&query=All"

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI2IiwianRpIjoiOGE4OGFmNDc0MDY0NjA0Yjc0ZDljZDJlNjZiYzc4MmY5MDgwYjRhY2U2N2Y0NmE1OGRlYjNmOTY2ZDU2ZTU3NjIwMmExNDYzYmFmMzZmNDciLCJpYXQiOjE3ODM2MjYzNzIuOTA1MjI1LCJuYmYiOjE3ODM2MjYzNzIuOTA1MjI4LCJleHAiOjIwOTkyNDU1NzIuOTAwNDY2LCJzdWIiOiIxMzM4MzgiLCJzY29wZXMiOltdfQ.OIrhwJhJw3AnN7ohGFabWN-f8TjVi0fyOtgqnMfJlhFuvqh1h_FwKG1Oey-5iSmPDVJ41TcD_F2QMIH7w7Akiw"

headers = {"Authorization": "Bearer {0}".format(token)}

response = requests.get(url, headers = headers)

if response.status_code != 200:
	print ("Failure, see status code: {0}".format(response.status_code))
else: 
	df = pd.DataFrame(response.json()["data"]["results"])	
	print(df);
