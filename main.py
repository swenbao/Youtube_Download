import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio',
        'merge_output_format': 'mp4',  # Ensures video + audio are merged
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'progress_hooks': [lambda d: print(f"Status: {d['status']} - {d.get('filename', '')}")],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
video_url = 'https://www.youtube.com/watch?v=1qlQUQ_pRVI'
download_video(video_url)
