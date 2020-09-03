import requests


def search_address(zipcode):
   response = requests.get(f'https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}')

   results = response.json()['results']

   都道府県名 = (results[0]['address1'])
   市町村名 = (results[0]['address2'])
   町域名 = (results[0]['address3'])

   address = f'{都道府県名}{市町村名}{町域名}'
   return address


def main():
   zipcode = input()
   print(search_address(zipcode))
