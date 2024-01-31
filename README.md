I built a real time audio chatbot. <br/>It works in several steps:
<br/><br/>
  Takes audio input<br/><br/>
  <t/>transcription of audio into text<br/>
  <t/>text treatment and generation using LLM (blenderbot)<br/>
  <t/>Conversion of generated response text into audio
  <br/>
  <br/>
*Libraries*<br/><br/>
  <t/>speech Recognition (for audio transcription)<br/>
  <t/>gtts (google text to speech for audio generation)<br/>
  <t/>use of pipeline to connect to blenderbot llm from hugging face.
