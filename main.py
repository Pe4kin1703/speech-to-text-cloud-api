from google.cloud import speech

def run_quickstart() -> speech.RecognizeResponse:
    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    audio_file_path = "ef3e_int_pe1_1-33.mp3"

    # gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
    with open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        # sample_rate_hertz=16000,
        language_code="en-US",
        sample_rate_hertz=44100,
        audio_channel_count=2,
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)
    print(f"{response=}")

    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")

if __name__ == "__main__":
    run_quickstart()