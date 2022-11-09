import pyttsx3

voice_engine = pyttsx3.init("sapi5")
__engine__voices_getProperty = voice_engine.getProperty("voices")
_set_voiceEngine_property = voice_engine.setProperty("voice", __engine__voices_getProperty[1])
voice_engine.setProperty("rate", 160)


def __speakFunc_audio(_function_decorator):
    def speak_audio():
        print("Initializing audio now")
        _function_decorator("Aya, i'm the main audio of this repository")
        print("Initialised the voice")
    speak_audio()


@__speakFunc_audio
def __main_speakFunc(audio):
    voice_engine.say(audio)
    voice_engine.runAndWait()

    if voice_engine.inLoop:
        voice_engine.endLoop()
