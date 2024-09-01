from pydub import AudioSegment
from pydub.utils import which

import os
# ffmpeg 및 ffprobe의 경로 확인
ffmpeg_path = which("ffmpeg")
ffprobe_path = which("ffprobe")

print(f"ffmpeg path: {ffmpeg_path}")
print(f"ffprobe path: {ffprobe_path}")

AudioSegment.converter = ffmpeg_path
AudioSegment.ffprobe = ffprobe_path


# 앞부분 자르기 함수 (8초 = 8000ms)
def trim_audio(file_path, output_path, start_trim=8000):
    audio = AudioSegment.from_mp3(file_path)
    trimmed_audio = audio[start_trim:]
    trimmed_audio.export(output_path, format="mp3")
    print(f"Trimmed {output_path}")


# 입력 파일과 출력 파일의 디렉터리 설정
input_directory = "D:/pyprojects/utilities/audios/originial"  # 입력 파일들이 있는 디렉터리 경로
output_directory = "D:/pyprojects/utilities/audios/trimmed"  # 자른 파일들을 저장할 디렉터리 경로

# 디렉터리 확인 및 생성 (출력 디렉터리가 존재하지 않으면 생성)
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 1부터 100까지의 MP3 파일 앞부분 자르기
for i in range(1, 101):
    input_file_name = f"{i}.mp3"
    output_file_name = f"trimmed_{i}.mp3"

    input_path = input_directory+"/"+input_file_name
    output_path = output_directory+"/"+output_file_name

    trim_audio(input_path, output_path)
