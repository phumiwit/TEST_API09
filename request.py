import requests

if __name__ == "__main__":
    url = "http://127.0.0.1:5000/prediction"
    test_audio = 'MLAPI/doja.wav'
    audio_file = open(test_audio,"rb")
    values = {"file":(test_audio,audio_file,"audio/wav")}
    resp = requests.post(url=url,files=values)
    print(resp.json())