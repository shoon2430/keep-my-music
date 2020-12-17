import youtube_dl  # 라이브러리
import os

# 다운로드 경로
output_dir = os.path.join('./download', '%(title)s.%(ext)s')

def run():
    video_url = input("Please enter tho YouTube Video URL : ")

    video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
    filename = f"{video_info['id']}" + ".%(ext)s"
    options = {
        "format": "bestaudio/best", # 가장 좋은 화질로 선택(화질을 선택하여 다운로드 가능)
        'outtmpl': output_dir,       # 다운로드 경로 설정
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
        "postprocessor_args": ["-ar", "16000"],
        "prefer_ffmpeg": True,
        "keepvideo": True,
    }
    
    with youtube_dl.YoutubeDL(options) as ydl:
        info_dict = ydl.extract_info(video_info["webpage_url"], download=True)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get("title", None)
        video_length = info_dict.get("duration")


if __name__ == "__main__":
    run()