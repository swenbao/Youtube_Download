import argparse
import pathlib
import yt_dlp

def build_video_opts(outdir: str):
    return {
        # 盡量拿 macOS/QuickTime 友善：H.264(AVC)+AAC，優先 mp4，最後再回退 18（360p 進度式）
        'format': 'bv*[vcodec^=avc1][ext=mp4]+ba[acodec^=mp4a][ext=m4a]/b[ext=mp4]/18/b',
        'merge_output_format': 'mp4',
        'outtmpl': str(pathlib.Path(outdir) / '%(title)s.%(ext)s'),
        'noplaylist': True,

        # 避免 hlsnative 的碎片缺失，交給 ffmpeg
        'hls_prefer_native': False,

        # 穩健下載
        'retries': 10,
        'fragment_retries': 10,

        # 僅 remux，不做有損重編碼；加 faststart
        'postprocessors': [{
            'key': 'FFmpegVideoRemuxer',
            'preferedformat': 'mp4',
        }],
        'postprocessor_args': ['-movflags', '+faststart'],
    }

def build_audio_opts(outdir: str, codec: str):
    return {
        'format': 'bestaudio/best',
        'outtmpl': str(pathlib.Path(outdir) / '%(title)s.%(ext)s'),
        'noplaylist': True,
        'retries': 10,
        'fragment_retries': 10,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': codec,      # wav / mp3 / m4a
            'preferredquality': '0',
        }],
    }

def download(url: str, mode: str, outdir: str, codec: str):
    pathlib.Path(outdir).mkdir(parents=True, exist_ok=True)
    ydl_opts = build_audio_opts(outdir, codec) if mode == 'audio' else build_video_opts(outdir)
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def cli():
    p = argparse.ArgumentParser(prog='ytdl', description='簡易 YouTube 下載器（影片/純音訊）')
    p.add_argument('url', help='YouTube/Shorts 連結')
    p.add_argument('-m', '--mode', choices=['video', 'audio'], default='video',
                   help='下載模式：video（預設）或 audio')
    p.add_argument('-o', '--outdir', default='downloads', help='輸出資料夾（預設 downloads）')
    p.add_argument('--codec', choices=['wav', 'mp3', 'm4a'], default='wav',
                   help='音訊編碼，只在 --mode audio 時有用（預設 wav）')
    args = p.parse_args()
    download(args.url, args.mode, args.outdir, args.codec)

if __name__ == '__main__':
    cli()