from youtube_transcript_api import YouTubeTranscriptApi
from utils.translate import translate_text

batch_size=20

def transcribe_video(video_id):
    transcript = YouTubeTranscriptApi()
    fetched_transcript = transcript.fetch(video_id, languages=["hi", "en"])

    for snippet in fetched_transcript:
        print(snippet.text)

    print("snippet count", len(fetched_transcript))

    for i in range(0, len(fetched_transcript), batch_size):
        batch = fetched_transcript[i: i+batch_size]
        texts = []

        for snippet in batch:
            texts.append(snippet.text)
        
        translate_text(texts)
