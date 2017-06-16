'''
Assignment 35 :

The International Civil Aviation Organization (ICAO) alphabet assigns code words to the letters of the English alphabet
acrophonically (Alfa for A, Bravo for B, etc.) so that critical combinations of letters (and numbers) can be pronounced
and understood by those who transmit and receive voice messages by radio or telephone regardless of their native
language, especially when the safety of navigation or persons is essential. Here is a Python dictionary covering one
version of the ICAO alphabet:

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}

Your task in this exercise is to write a procedure speak_ICAO() able to translate any text (i.e. any string) into spoken
ICAO words. You need to import at least two libraries: os and time. On a mac, you have access to the system TTS
(Text-To-Speech) as follows: os.system('say ' + msg), where msg is the string to be spoken. (Under UNIX/Linux and
Windows, something similar might exist.) Apart from the text to be spoken, your procedure also needs to accept two
additional parameters: a float indicating the length of the pause between each spoken ICAO word, and a float indicating
the length of the pause between each word spoken.

'''
import pyttsx
import time
d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}


def speak_ICAO(Input_text):
    Check_space = False
    for Char in Input_text:
        if Char == " ":
            Check_space = True
            break
    '''if Check_space:
        words_from_input_text = Input_text.split(" ")
        print words_from_input_text
    else:
        words_from_input_text = list()
        words_from_input_text.append(Input_text)'''

    engine = pyttsx.init()
    Rate = engine.getProperty("rate")
    print Rate
    engine.setProperty("rate", Rate - Rate)
    pause_between_words = 2.5   # 2 sec
    pause_between_ICAOwords = 4.5  # 1 sec
    #for word in words_from_input_text:
    word = Input_text
    print engine.getProperty("rate")
    engine.say("Given word is" + word, "word")
    print "Given word is: %s" % word
    for i in range(len(word)):
        if word[i] != " ":
            ICAO_word = d[word[i]]
            engine.say(word[i] + "for" +ICAO_word,  "ICAO_word") # say() Queues a Command to speak an utterance.
            print "%c for %s"% (word[i], ICAO_word)
    engine.runAndWait()   # Blocks engine's executions while processing all currently queued Commands. It returns
                          # when all Commands queued before this call are emptied from the queue.

    time.sleep(pause_between_words)
    engine.stop()

'''Text = raw_input(" Enter your text to convert it into ICAO Text and Spech :")
speak_ICAO(Text)'''

fp = open("ICAO.txt", "r")
for Line in fp:
    Line = Line.strip('\n')
    print "Current line from file : ", Line
    speak_ICAO(Line)

