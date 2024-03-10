import os
import gtts
from playsound import playsound

#tts = gtts.gTTS("Hello world")

#tts.save("hello.mp3")

#playsound("hello.mp3")


#tts = gtts.gTTS("Hola Mundo", lang="es")
#tts.save("hola.mp3")
#playsound("hola.mp3")

# Ez jó -> a = " + ".join(str(x) for x in range(2,7))
#          tts = gtts.gTTS("Sziasztok emberek! Biztos jól hallasz? Én vagyok a számítógép! " + a + " = 10. No ez így nem igaz!", lang="zh-cn")

tts = gtts.gTTS(" Szia Uram! Érdekel a Pegazus? Nem repít! Lehallgat!".format(772), lang="hu")

tts.save("hola.mp3")

os.startfile("hola.mp3")

print("Nyaf")
