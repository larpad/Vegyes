from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'A keresési kifejezés megadása kötelező!'}), 400

    # Port.hu keresési URL
    search_url = f'https://port.hu/tvmusor/kereses?search={query}'
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Hiba történt a keresés során: {str(e)}'}), 500

    # HTML parsing
    soup = BeautifulSoup(response.text, 'html.parser')
    program_items = soup.find_all('div', class_='program-item')
    
    processed_results = []
    for item in program_items:
        try:
            title = item.find('h2', class_='title').text.strip() if item.find('h2', class_='title') else 'N/A'
            channel = item.find('span', class_='channel').text.strip() if item.find('span', class_='channel') else 'N/A'
            showtime = item.find('span', class_='time').text.strip() if item.find('span', class_='time') else 'N/A'
            description = item.find('div', class_='description').text.strip() if item.find('div', class_='description') else 'N/A'
            
            processed_result = {
                'title': title,
                'showtime': showtime,
                'channel': channel,
                'description': description
            }
            processed_results.append(processed_result)
        except Exception as e:
            continue
    
    return jsonify(processed_results)

@app.route('/channels', methods=['GET'])
def channels():
    try:
        # Port.hu TV műsor főoldala
        response = requests.get('https://port.hu/tvmusor')
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        channel_list = soup.find_all('div', class_='channel-item')
        
        channels = []
        for channel in channel_list:
            channel_name = channel.find('span', class_='name').text.strip() if channel.find('span', class_='name') else 'N/A'
            channels.append({'name': channel_name})
            
        return jsonify(channels)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Hiba történt a csatornák lekérése során: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
