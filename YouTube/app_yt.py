from flask import Flask, request, render_template_string
from flask_socketio import SocketIO
import yt_dlp as youtube_dl
import os

app = Flask(__name__)
socketio = SocketIO(app)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>YouTube Downloader</title>
    <style>
        body { font-family: Arial; max-width: 800px; margin: 0 auto; padding: 20px; }
        input, button { padding: 10px; margin: 10px 0; }
        input[type="text"] { width: 100%; }
        .progress-bar {
            width: 100%;
            background-color: #f0f0f0;
            padding: 3px;
            border-radius: 3px;
            box-shadow: inset 0 1px 3px rgba(0, 0, 0, .2);
            display: none;
        }
        .progress-bar-fill {
            display: block;
            height: 22px;
            background-color: #659cef;
            border-radius: 3px;
            transition: width 500ms ease-in-out;
            width: 0%;
        }
        .progress-bar-text {
            color: white;
            text-align: center;
            line-height: 22px;
        }
        #status {
            margin-top: 10px;
            color: #666;
        }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            var socket = io();
            const progressBar = document.getElementById('progress-bar');
            const progressBarFill = document.getElementById('progress-bar-fill');
            const progressBarText = document.getElementById('progress-bar-text');
            const statusDiv = document.getElementById('status');
            
            socket.on('progress', function(data) {
                progressBar.style.display = 'block';
                progressBarFill.style.width = data.percent + '%';
                progressBarText.textContent = data.percent + '%';
                statusDiv.textContent = data.status;
            });
            
            socket.on('complete', function(data) {
                statusDiv.textContent = data.message;
                setTimeout(() => {
                    progressBar.style.display = 'none';
                    progressBarFill.style.width = '0%';
                }, 3000);
            });
            
            socket.on('error', function(data) {
                statusDiv.textContent = 'Hiba: ' + data.error;
                progressBar.style.display = 'none';
            });
        });
    </script>
</head>
<body>
    <h1>YouTube Downloader</h1>
    <form method="post">
        <input type="text" name="url" placeholder="YouTube URL" required>
        <button type="submit">Letöltés</button>
    </form>
    
    <div class="progress-bar" id="progress-bar">
        <div class="progress-bar-fill" id="progress-bar-fill">
            <div class="progress-bar-text" id="progress-bar-text">0%</div>
        </div>
    </div>
    
    <div id="status"></div>
</body>
</html>
'''

class MyLogger:
    def debug(self, msg):
        if msg.startswith('[download]'):
            if 'Destination' not in msg and 'Resuming' not in msg:
                progress = msg.split()
                if len(progress) > 1 and '%' in progress[1]:
                    percent = float(progress[1].replace('%', ''))
                    status = ' '.join(progress[2:])
                    socketio.emit('progress', {'percent': percent, 'status': status})

def my_hook(d):
    if d['status'] == 'finished':
        socketio.emit('complete', {'message': 'Letöltés befejezve!'})

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        output_dir = r"C:\Users\Apu\Desktop\YT"  # Módosítsa ezt a saját könyvtárára
        
        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
                'progress_hooks': [my_hook],
                'logger': MyLogger(),
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }]
            }
            
            socketio.start_background_task(download_video, url, ydl_opts)
            return render_template_string(HTML_TEMPLATE)
        except Exception as e:
            socketio.emit('error', {'error': str(e)})
            return render_template_string(HTML_TEMPLATE)
    
    return render_template_string(HTML_TEMPLATE)

def download_video(url, ydl_opts):
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        socketio.emit('error', {'error': str(e)})

if __name__ == '__main__':
    socketio.run(app, debug=True)
