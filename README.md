I built a real time audio chatbot. <br/>It works in several steps:
<br/><br/>
  Takes audio input<br/><br/>
  &#9 transcription of audio into text<br/>
  <tab/>text treatment and generation using LLM (blenderbot)<br/>
  <tab/>Conversion of generated response text into audio
  <br/>
  <br/>
*Libraries*<br/><br/>
  <tab/>speech Recognition (for audio transcription)<br/>
  <tab/>gtts (google text to speech for audio generation)<br/>
  <tab/>use of pipeline to connect to blenderbot llm from hugging face.
