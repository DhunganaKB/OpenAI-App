import os
import re
from pytube import YouTube
import streamlit as st
import openai

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

st.title("YouTube Video Summary:")
#st.subheader("Provide youtube url link to summarize")

url = st.text_input("Provide Your YouTube URL Link Here", "")

def download_audio(url):
    if 'youtube.com' not in url:
        print('Youtube link does not exist, please check!')
        return False
    yt = YouTube(url)

    audio_file = yt.streams.filter(only_audio=True).first()
    
    download_file = audio_file.download()

    if os.path.exists(download_file):
        print('Download complete')
    else:
        print('Downloading Error')
        return False
    filename = os.path.basename(download_file)
    print(filename)
    base = filename.split('.')[0]
    audioname=f'{base}.mp3'
    audioname = re.sub('\s+', '-', audioname)
    os.rename(filename, audioname)
    print(audioname)

    return audioname

def transcribe_video(audioname):
    
    if not os.path.exists(audioname):
        print('audio file not found')
        return False
    
    with open(audioname, 'rb') as fb:
        print('Stranscribing ... ')
        transcript = openai.Audio.transcribe('whisper-1', fb)
    
    base = audioname.split('.')[0]    
    transcript_filename = f'transcript-{base}.txt'        
    return transcript

def summarize_text(transcript):
         
    system_prompt = "I would like for you to assume the role of a Life Coach"
    user_prompt = f"""Generate a concise summary of the text below.
    Text: {transcript}
    
    Add a title to the summary.

    Make sure your summary has useful and true information about the main points of the topic.
    Begin with a short introduction explaining the topic. If you can, use bullet points to list important details,
    and finish your summary with a concluding sentence"""
    
    print('summarizing ... ')
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo-16k',
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt}
        ],
        max_tokens=4096,
        temperature=1
    )
    
    summary = response['choices'][0]['message']['content']
    return summary

if url:
    with st.spinner('Downloading / Model working ...'):
        audio_mp3_file = download_audio(url)
        transcript_file = transcribe_video(audio_mp3_file) 
        summary = summarize_text(transcript_file)
        st.write('<p style="font-size:26px; color:red;">Summary Text: </p>', unsafe_allow_html=True)
        st.write(summary)

