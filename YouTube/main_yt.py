import os
import yt_dlp as youtube_dl
import argparse

def download_video(url, output_dir):
    if not url or not output_dir:
        print("Error: URL and output directory are required")
        return

    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'verbose': True
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download a YouTube video.')
    parser.add_argument('--URL', required=False, help='The URL of the YouTube video to download', default='https://www.youtube.com/watch?v=MxUfw0TjnwA&list=RDMMMxUfw0TjnwA&start_radio=1')
    parser.add_argument('--directory', required=False, help='The directory to save the downloaded video', default=r"C:\Users\Apu\Desktop\YT")

    args = parser.parse_args()
    download_video(args.URL, args.directory)
