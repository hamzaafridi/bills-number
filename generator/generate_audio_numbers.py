from gtts import gTTS

#settings
language = "en"

#generate audio files from 1 to 20
# for i in range(1,21):
#     numGTTS = gTTS(text=str(i), lang=language, slow=False) 
#     numGTTS.save("../audio/"+str(i)+".mp3")

for i in range(20,100,10):
    numGTTS = gTTS(text=str(i), lang=language, slow=False) 
    numGTTS.save("../audio/"+str(i)+".mp3")