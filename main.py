import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # re-encode if necessary
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_audio_as_wav(url):
    ydl_opts = {
        'format': 'bestaudio/best',  # 抓最高品質的音訊
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # 儲存路徑與命名
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # 最終輸出格式
            'preferredquality': '0',  # 儘管對 wav 無效，但保留以符合語法
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])




# 網址放這裡！
video_url = 'https://youtu.be/sWHIyrS9M70?si=L-DVkIs_QcTwgp3v'


# download_video(video_url)
download_audio_as_wav(video_url)


