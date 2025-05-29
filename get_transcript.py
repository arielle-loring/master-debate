from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
import json

# Replace with the ID of the video you want
video_id = 'Fk9NyPZghRE'

try:
    # Fetch transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
except TranscriptsDisabled:
    print(f"Transcripts are disabled for video {video_id}.")
    transcript = None
except NoTranscriptFound:
    print(f"No transcript found for video {video_id}.")
    transcript = None
except VideoUnavailable:
    print(f"Video {video_id} is unavailable.")
    transcript = None
except Exception as e:
    print(f"An error occurred: {e}")
    transcript = None

if transcript:
    # Save to a JSON file
    with open(f'{video_id}_transcript.json', 'w', encoding='utf-8') as f:
        json.dump(transcript, f, indent=2, ensure_ascii=False)

    print(f"Transcript saved as {video_id}_transcript.json")

    with open(f'{video_id}_transcript.txt', 'w', encoding='utf-8') as txt:
        for entry in transcript:
            txt.write(entry["text"] + "\n")
else:
    print("Transcript could not be retrieved.")


