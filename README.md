# IPA-Trainer
This program is a simple tool to help you learn the International Phonetic Alphabet (IPA). It is written in Python using the customtkinter and tkinter modules.

Running the Program
To run the script, you will need to have customtkinter and tkinter installed. Simply run pip install customtkinter tkinter to install these modules.

To start the program, run the following command:

Copy code
python ipa_trainer.py
Alternatively, you can download the pre-compiled executable from the releases tab.

How to Play
When you run the script, a frame will appear with a start button. When you click the start button, the frame will be destroyed and the game frame and stats frame will be created.

The game frame contains a label that displays a random word in IPA, a progress bar that counts down from 10 seconds, a text entry box where you can type in your answer, and a submit button. When you press the submit button or press enter, the program will check your answer. If the answer is correct, the word will flash green and a new word will be displayed. If the answer is incorrect, the word will flash red. If the timer runs out, the word will flash red and a new word will be displayed.

There is also a file called "ipa.txt" that already contains the IPA for the words in "words.txt". "words.txt" should contain a list of words, one word per line. The program will use this file to generate random words.

The stats frame is a thin bar at the top of the window. It will contain the number of correct answers, the number of incorrect answers, and in the center the current streak. The streak is the number of correct answers in a row. If you get an incorrect answer, the streak will reset to 0.