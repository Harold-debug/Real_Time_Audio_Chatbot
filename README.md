I built a real time audio chatbot. <br/>It works in several steps:
<br/><br/>
  Takes audio input<br/><br/>
  &nbsp;&nbsp; transcription of audio into text<br/>
  &nbsp;&nbsp; text treatment and generation using LLM (blenderbot)<br/>
  &nbsp;&nbsp; Conversion of generated response text into audio
  <br/>
  <br/>
*Libraries*<br/><br/>
  &nbsp;&nbsp; speech Recognition (for audio transcription)<br/>
  &nbsp;&nbsp; gtts (google text to speech for audio generation)<br/>
  &nbsp;&nbsp; use of pipeline to connect to blenderbot llm from hugging face.
