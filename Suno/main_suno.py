import music21
import requests

def load_musicxml(file_path):
    try:
        score = music21.converter.parse(file_path)
        return score
    except Exception as e:
        print(f"Error loading MusicXML file: {e}")
        return None

def get_stylus_prompt():
    prompt = input("Please enter the stylus prompt: ")
    return prompt

def login_to_suno():
    login_url = "https://suno.com/api/google-login"
    try:
        response = requests.post(login_url)
        response.raise_for_status()
        return response.json().get("token")
    except requests.exceptions.RequestException as e:
        print(f"Error logging in to SUNO.COM with Google: {e}")
        return None

def call_suno_api(token, score, prompt):
    api_url = "https://suno.com/api/process"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    files = {
        "file": ("score.musicxml", score.write('musicxml'))
    }
    data = {
        "prompt": prompt
    }
    try:
        response = requests.post(api_url, headers=headers, files=files, data=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling SUNO.COM API: {e}")
        return None

def download_files(file_urls):
    for url in file_urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            file_name = url.split("/")[-1]
            with open(file_name, "wb") as file:
                file.write(response.content)
            print(f"Downloaded {file_name}")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading file {url}: {e}")

def main():
    file_path = input("Enter the path to the MusicXML file (default: halaszok.xml): ") or "halaszok.xml"
    score = load_musicxml(file_path)
    if not score:
        return

    prompt = get_stylus_prompt()
    username = input("Enter your SUNO.COM username: ")
    password = input("Enter your SUNO.COM password: ")
    token = login_to_suno(username, password)
    if not token:
        return

    response = call_suno_api(token, score, prompt)
    if response and "file_urls" in response:
        download_files(response["file_urls"])

if __name__ == "__main__":
    main()
