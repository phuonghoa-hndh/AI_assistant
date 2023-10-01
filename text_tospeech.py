from gtts import gTTS
import playsound
import os

print("Xin mời nhập nội dung: ")
text = str(input())
output = gTTS(text, lang="vi", slow=False)
output.save("output.mp3")
#playsound.playsound('output.mp3', True)
os.system("output.mp3")



