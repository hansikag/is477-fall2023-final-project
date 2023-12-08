import zipfile
import requests
import hashlib
import os

url = 'https://archive.ics.uci.edu/static/public/109/wine.zip'

response = requests.get(url)

if response.status_code == 200:
    with open('./data/wine.zip', mode='wb') as f:
        f.write(response.content)
    with open('./data/wine.zip', 'rb') as f:
        data = f.read()
        sha256hash = hashlib.sha256(data).hexdigest()
    expected_sha256 = '2bae62c4481220623579d4c4fb36b55652b6b75e06e49fa1981b8198362dfdab'
    if sha256hash == expected_sha256:
        print("Downloaded file verified successfully.")
        with zipfile.ZipFile('./data/wine.zip', 'r') as zip_ref:
            zip_ref.extractall('./data/')
        print("File unzipped successfully.")
    else:
        print(sha256hash)
        print("ERROR: Integrity check failed.")
else:
    print(f"ERROR: Failed to download file. HTTP status code {response.status_code}")



