I built a real time audio chatbot. <br/>It works in several steps:
<br/>
  Takes audio input<br/>
  transcription of audio into text<br/>
  text treatment and generation using LLM (blenderbot)<br/>
  Conversion of generated response text into audio
  <br/>
  <br/>
*Libraries*
  speech Recognition (for audio transcription)<br/>
  gtts (google text to speech for audio generation)<br/>
  use of pipeline to connect to blenderbot llm from hugging face.
