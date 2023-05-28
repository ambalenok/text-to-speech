import pyttsx3
engine = pyttsx3.init()
engine.save_to_file('just test' , 'test.mp3')
engine.runAndWait()