I built a real time audio chatbot. It works in several steps:
  Takes audio input
  transcription of audio into text
  text treatment and generation using LLM (blenderbot)
  Conversion of generated response text into audio
Libraries
  speech Recognition (for audio transcription)
  gtts (google text to speech for audio generation)
  use of pipeline to connect to blenderbot llm from hugging face.
