#!/usr/bin/env python3
import sys
import json
import struct
import subprocess
from pathlib import Path

def get_message():
    raw_length = sys.stdin.buffer.read(4)
    if not raw_length:
        return None
    message_length = struct.unpack('=I', raw_length)[0]
    message = sys.stdin.buffer.read(message_length)
    return json.loads(message)

def send_message(message):
    encoded_message = json.dumps(message).encode('utf-8')
    encoded_length = struct.pack('=I', len(encoded_message))
    sys.stdout.buffer.write(encoded_length)
    sys.stdout.buffer.write(encoded_message)
    sys.stdout.buffer.flush()

def main():
    while True:
        message = get_message()
        if message is None:
            break
        
        if message.get('action') == 'download':
            try:
                video_url = message.get('url')
                # Itt hívd meg a main_YT.py vagy app_YT.py szkriptedet
                subprocess.run(['python', 'main_YT.py', video_url])
                send_message({"success": True})
            except Exception as e:
                send_message({"success": False, "error": str(e)})

if __name__ == '__main__':
    main() 