import zipfile
import requests
import hashlib

def download_and_validate(url, output_path, expected_hash):
    response = requests.get(url)

    if response.status_code == 200:
        with open(output_path, mode='wb') as f:
            f.write(response.content)
        with open(output_path, 'rb') as f:
            data = f.read()
            sha256hash = hashlib.sha256(data).hexdigest()
        if sha256hash == expected_hash:
            print("Downloaded file verified successfully.")
            with zipfile.ZipFile(output_path, 'r') as zip_ref:
                zip_ref.extractall('./data/')
            print("File unzipped successfully.")
        else:
            print(sha256hash)
            print("ERROR: Integrity check failed.")
    else:
        print(f"ERROR: Failed to download file. HTTP status code {response.status_code}")

if __name__ == "__main__":
    wine_url = 'https://archive.ics.uci.edu/static/public/109/wine.zip'
    wine_path = './wine.zip'
    wine_hash = '2bae62c4481220623579d4c4fb36b55652b6b75e06e49fa1981b8198362dfdab'

    download_and_validate(wine_url, wine_path, wine_hash)
