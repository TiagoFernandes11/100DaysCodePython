import http.client


def save_to_mp3_file(text):
    conn = http.client.HTTPSConnection("voicerss-text-to-speech.p.rapidapi.com")

    payload = f"src={text}&hl=en-us&r=0&c=mp3&f=8khz_8bit_mono"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'X-RapidAPI-Key': "2b3f582f4bmshd7f97e6358bd1c6p195267jsn8ab105dfccfa",
        'X-RapidAPI-Host': "voicerss-text-to-speech.p.rapidapi.com"
    }

    conn.request("POST", "/?key=362e0fa3592a44c29bc6dd51a7a47e97", payload, headers)

    res = conn.getresponse()
    data = res.read()

    # Save the binary data to an MP3 file
    with open("output.mp3", "wb") as audio_file:
        audio_file.write(data)

    print("Audio file saved as 'output.mp3'")


save_to_mp3_file("This is a study test")

