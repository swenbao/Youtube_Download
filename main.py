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

# Example usage
video_url = 'https://www.youtube.com/watch?v=1qlQUQ_pRVI'
download_video(video_url)

# ffmpeg -i "input.mp4" -c:v libx264 -c:a aac "output_fixed.mp4"
