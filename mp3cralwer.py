import requests


# 파일을 다운로드하는 함수
def download_file(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {file_name}")
    else:
        print(f"Failed to download {file_name}, status code: {response.status_code}")


# 기본 URL 패턴
base_url = "https://www.nexusbook.com/qr/eng/miracle100/chn/mp3/1/"

# 1부터 100까지의 파일 다운로드
for i in range(1, 101):
    file_number = str(i)
    file_name = f"{file_number}.mp3"
    url = f"{base_url}{file_name}"

    download_file(url, file_name)
