"""
IPA Trainer

This program is a simple tool to help you learn the International Phonetic Alphabet (IPA).
A random word in IPA is displayed in a label. Under the label is a progress bar that
counts down from 10 seconds. Below the progress bar is a text entry box where you can
type in your answer. When you press the "Submit" button or press enter, the program will check your
answer. If the answer is correct, color of the word will flash green and a new word will be displayed.
If the answer is incorrect, the word will flash red. If the timer runs out, the word will flash red and
a new word will be displayed. The program will keep track of how many words you get correct and how 
many you get incorrect. It will display your stats at the bottom of the window.

A file called "words.txt" must be in the same directory as this program. The file should contain
a list of words, one word per line. The program will use this file to generate random words.

There is also a file called "ipa.txt" that already contains the IPA for the words in "words.txt".

The program will start by creating a frame called Start with a button in the center. When the button is clicked,
the frame will be destroyed and the game frame and the stats frame will be created. The game frame will contain
the word label, progress bar, entry box, and submit button. The stats frame will contain the stats.

The stats frame will be a thin bar at the top of the window. It will contain the number of correct answers,
the number of incorrect answers, and in the center the current streak. The streak is the number of correct
answers in a row. If you get an incorrect answer, the streak will reset to 0.
"""

import customtkinter as ctk
import tkinter as tk
import random

IPA_WORDS = [('the', 'ðˈə'), ('of', 'ˈʌv'), ('to', 'tˈuː'), ('and', 'ˈænd'), 
             ('a', 'ˈe͡ɪ'), ('in', 'ˈɪn'), ('is', 'ˈɪz'), ('it', 'ˈɪt'), 
             ('you', 'jˈuː'), ('that', 'ðˈæt'), ('he', 'hˈiː'), ('was', 'wˈʌz'), 
             ('for', 'fˈɔː͡ɹ'), ('on', 'ˈɔn'), ('are', 'ˈɑː͡ɹ'), ('with', 'wˈɪð'), 
             ('as', 'ˈæz'), ('I', 'ˈa͡ɪ'), ('his', 'hˈɪz'), ('they', 'ðˈe͡ɪ'), 
             ('be', 'bˈiː'), ('at', 'ˈæt'), ('one', 'wˈʌn'), ('have', 'hˈæv'), 
             ('this', 'ðˈɪs'), ('from', 'fɹˈʌm'), ('or', 'ˈɔː͡ɹ'), 
             ('had', 'hˈæd'), ('by', 'bˈa͡ɪ'), ('word', 'wˈɜːd'), ('but', 'bˈʌt'), 
             ('what', 'wˈʌt'), ('some', 'sˈʌm'), ('we', 'wˈiː'), ('can', 'kˈæn'), 
             ('out', 'ˈa͡ʊt'), ('other', 'ˈʌðɚ'), ('were', 'wˈɜː'), ('all', 'ˈɔːl'), 
             ('there', 'ðˈɛ͡ɹ'), ('when', 'wˈɛn'), ('up', 'ˈʌp'), ('use', 'jˈuːs'), 
             ('your', 'jˈʊ͡ɹ'), ('how', 'hˈa͡ʊ'), ('said', 'sˈɛd'), ('an', 'ˈæn'), 
             ('each', 'ˈiːt͡ʃ'), ('she', 'ʃˈiː'), ('which', 'wˈɪt͡ʃ'), ('do', 'dˈuː'), 
             ('their', 'ðˈɛ͡ɹ'), ('time', 'tˈa͡ɪm'), ('if', 'ˈɪf'), ('will', 'wˈɪl'), 
             ('way', 'wˈe͡ɪ'), ('about', 'ɐbˈa͡ʊt'), ('many', 'mˈɛni'), ('then', 'ðˈɛn'), 
             ('them', 'ðˈɛm'), ('write', 'ɹˈa͡ɪt'), ('would', 'wˈʊd'), ('like', 'lˈa͡ɪk'), 
             ('so', 'sˈo͡ʊ'), ('these', 'ðˈiːz'), ('her', 'hˈɜː'), ('long', 'lˈɔŋ'), 
             ('make', 'mˈe͡ɪk'), ('thing', 'θˈɪŋ'), ('see', 'sˈiː'), ('him', 'hˈɪm'), 
             ('two', 'tˈuː'), ('has', 'hˈæz'), ('look', 'lˈʊk'), ('more', 'mˈoː͡ɹ'), 
             ('day', 'dˈe͡ɪ'), ('could', 'kˈʊd'), ('go', 'ɡˈo͡ʊ'), ('come', 'kˈʌm'), 
             ('did', 'dˈɪd'), ('number', 'nˈʌmbɚ'), ('sound', 'sˈa͡ʊnd'), ('no', 'nˈo͡ʊ'), 
             ('most', 'mˈo͡ʊst'), ('people', 'pˈiːpə͡l'), ('my', 'mˈa͡ɪ'), ('over', 'ˈo͡ʊvɚ'), 
             ('know', 'nˈo͡ʊ'), ('water', 'wˈɔːɾɚ'), ('than', 'ðˈɐn'), ('call', 'kˈɔːl'), 
             ('first', 'fˈɜːst'), ('who', 'hˈuː'), ('may', 'mˈe͡ɪ'), ('down', 'dˈa͡ʊn'), 
             ('side', 'sˈa͡ɪd'), ('been', 'bˈɪn'), ('now', 'nˈa͡ʊ'), ('find', 'fˈa͡ɪnd'), 
             ('any', 'ˈɛni'), ('new', 'nˈuː'), ('work', 'wˈɜːk'), ('part', 'pˈɑː͡ɹt'), 
             ('take', 'tˈe͡ɪk'), ('get', 'ɡˈɛt'), ('place', 'plˈe͡ɪs'), ('made', 'mˈe͡ɪd'), 
             ('live', 'lˈa͡ɪv'), ('where', 'wˈɛ͡ɹ'), ('after', 'ˈæftɚ'), ('back', 'bˈæk'), 
             ('little', 'lˈɪɾə͡l'), ('only', 'ˈo͡ʊnli'), ('round', 'ɹˈa͡ʊnd'), ('man', 'mˈæn'), 
             ('year', 'jˈɪ͡ɹ'), ('came', 'kˈe͡ɪm'), ('show', 'ʃˈo͡ʊ'), ('every', 'ˈɛvɹi'), 
             ('good', 'ɡˈʊd'), ('me', 'mˈiː'), ('give', 'ɡˈɪv'), ('our', 'ˈa͡ʊɚ'), ('under', 'ˈʌndɚ'), 
             ('name', 'nˈe͡ɪm'), ('very', 'vˈɛɹi'), ('through', 'θɹˈuː'), ('just', 'd͡ʒˈʌst'), 
             ('form', 'fˈɔː͡ɹm'), ('sentence', 'sˈɛntəns'), ('great', 'ɡɹˈe͡ɪt'), ('think', 'θˈɪŋk'), 
             ('say', 'sˈe͡ɪ'), ('help', 'hˈɛlp'), ('low', 'lˈo͡ʊ'), ('line', 'lˈa͡ɪn'), 
             ('differ', 'dˈɪfɚ'), ('turn', 'tˈɜːn'), ('cause', 'kˈɔːz'), ('much', 'mˈʌt͡ʃ'), 
             ('mean', 'mˈiːn'), ('before', 'bᵻfˈoː͡ɹ'), ('move', 'mˈuːv'), ('right', 'ɹˈa͡ɪt'), 
             ('boy', 'bˈɔ͡ɪ'), ('old', 'ˈo͡ʊld'), ('too', 'tˈuː'), ('same', 'sˈe͡ɪm'), ('tell', 'tˈɛl'), 
             ('does', 'dˈʌz'), ('set', 'sˈɛt'), ('three', 'θɹˈiː'), ('want', 'wˈɔnt'), ('air', 'ˈɛ͡ɹ'), 
             ('well', 'wˈɛl'), ('also', 'ˈɔːlso͡ʊ'), ('play', 'plˈe͡ɪ'), ('small', 'smˈɔːl'), 
             ('end', 'ˈɛnd'), ('put', 'pˈʊt'), ('home', 'hˈo͡ʊm'), ('read', 'ɹˈiːd'), ('hand', 'hˈænd'),
             ('port', 'pˈoː͡ɹt'), ('large', 'lˈɑː͡ɹd͡ʒ'), ('spell', 'spˈɛl'), ('add', 'ˈæd'), 
             ('even', 'ˈiːvən'), ('land', 'lˈænd'), ('here', 'hˈɪ͡ɹ'), ('must', 'mˈʌst'), 
             ('big', 'bˈɪɡ'), ('high', 'hˈa͡ɪ'), ('such', 'sˈʌt͡ʃ'), ('follow', 'fˈɑːlo͡ʊ'), 
             ('act', 'ˈækt'), ('why', 'wˈa͡ɪ'), ('ask', 'ˈæsk'), ('men', 'mˈɛn'), ('change', 't͡ʃˈe͡ɪnd͡ʒ'), 
             ('went', 'wˈɛnt'), ('light', 'lˈa͡ɪt'), ('kind', 'kˈa͡ɪnd'), ('off', 'ˈɔf'), ('need', 'nˈiːd'), 
             ('house', 'hˈa͡ʊs'), ('picture', 'pˈɪkt͡ʃɚ'), ('try', 'tɹˈa͡ɪ'), ('us', 'ˈʌs'), ('again', 'ɐɡˈɛn'), 
             ('animal', 'ˈænɪmə͡l'), ('point', 'pˈɔ͡ɪnt'), ('mother', 'mˈʌðɚ'), ('world', 'wˈɜːld'), 
             ('near', 'nˈɪ͡ɹ'), ('build', 'bˈɪld'), ('self', 'sˈɛlf'), ('earth', 'ˈɜːθ'), ('father', 'fˈɑːðɚ'), 
             ('head', 'hˈɛd'), ('stand', 'stˈænd'), ('own', 'ˈo͡ʊn'), ('page', 'pˈe͡ɪd͡ʒ'), ('should', 'ʃˈʊd'), 
             ('country', 'kˈʌntɹi'), ('found', 'fˈa͡ʊnd'), ('answer', 'ˈænsɚ'), ('school', 'skˈuːl'), 
             ('grow', 'ɡɹˈo͡ʊ'), ('study', 'stˈʌdi'), ('still', 'stˈɪl'), ('learn', 'lˈɜːn'), 
             ('plant', 'plˈænt'), ('cover', 'kˈʌvɚ'), ('food', 'fˈuːd'), ('sun', 'sˈʌn'), ('four', 'fˈoː͡ɹ'), 
             ('between', 'bᵻtwˈiːn'), ('state', 'stˈe͡ɪt'), ('keep', 'kˈiːp'), ('eye', 'ˈa͡ɪ'), 
             ('never', 'nˈɛvɚ'), ('last', 'lˈæst'), ('let', 'lˈɛt'), ('thought', 'θˈɔːt'), 
             ('city', 'sˈɪɾi'), ('tree', 'tɹˈiː'), ('cross', 'kɹˈɔs'), ('farm', 'fˈɑː͡ɹm'), 
             ('hard', 'hˈɑː͡ɹd'), ('start', 'stˈɑː͡ɹt'), ('might', 'mˈa͡ɪt'), ('story', 'stˈoːɹi'), 
             ('saw', 'sˈɔː'), ('far', 'fˈɑː͡ɹ'), ('sea', 'sˈiː'), ('draw', 'dɹˈɔː'), ('left', 'lˈɛft'), 
             ('late', 'lˈe͡ɪt'), ('run', 'ɹˈʌn'), ("don't", 'dˈo͡ʊnt'), ('while', 'wˈa͡ɪl'), ('press', 'pɹˈɛs'), ('close', 'klˈo͡ʊs'), ('night', 'nˈa͡ɪt'), ('real', 'ɹˈiːəl'), ('life', 'lˈa͡ɪf'), ('few', 'fjˈuː'), ('north', 'nˈɔː͡ɹθ'), ('open', 'ˈo͡ʊpən'), ('seem', 'sˈiːm'), ('together', 'təɡˈɛðɚ'), ('next', 'nˈɛkst'), ('white', 'wˈa͡ɪt'), ('children', 't͡ʃˈɪldɹən'), ('begin', 'bɪɡˈɪn'), ('got', 'ɡˈɑːt'), ('walk', 'wˈɔːk'), ('example', 'ɛɡzˈæmpə͡l'), ('ease', 'ˈiːz'), ('paper', 'pˈe͡ɪpɚ'), ('group', 'ɡɹˈuːp'), ('always', 'ˈɔːlwe͡ɪz'), ('music', 'mjˈuːzɪk'), ('those', 'ðˈo͡ʊz'), ('both', 'bˈo͡ʊθ'), ('mark', 'mˈɑː͡ɹk'), ('often', 'ˈɔfən'), ('letter', 'lˈɛɾɚ'), ('until', 'ʌntˈɪl'), ('mile', 'mˈa͡ɪl'), ('river', 'ɹˈɪvɚ'), ('car', 'kˈɑː͡ɹ'), ('feet', 'fˈiːt'), ('care', 'kˈɛ͡ɹ'), ('second', 'sˈɛkənd'), ('book', 'bˈʊk'), ('carry', 'kˈæɹi'), ('took', 'tˈʊk'), ('science', 'sˈa͡ɪ͡əns'), ('eat', 'ˈiːt'), ('room', 'ɹˈuːm'), ('friend', 'fɹˈɛnd'), ('began', 'bɪɡˈæn'), ('idea', 'a͡ɪdˈi͡ə'), ('fish', 'fˈɪʃ'), ('mountain', 'mˈa͡ʊntɪn'), ('stop', 'stˈɑːp'), ('once', 'wˈʌns'), ('base', 'bˈe͡ɪs'), ('hear', 'hˈɪ͡ɹ'), ('horse', 'hˈɔː͡ɹs'), ('cut', 'kˈʌt'), ('sure', 'ʃˈʊ͡ɹ'), ('watch', 'wˈɑːt͡ʃ'), ('color', 'kˈʌlɚ'), ('face', 'fˈe͡ɪs'), ('wood', 'wˈʊd'), ('main', 'mˈe͡ɪn'), ('enough', 'ɪnˈʌf'), ('plain', 'plˈe͡ɪn'), ('girl', 'ɡˈɜːl'), ('usual', 'jˈuːʒuːə͡l'), ('young', 'jˈʌŋ'), ('ready', 'ɹˈɛdi'), ('above', 'əbˈʌv'), ('ever', 'ˈɛvɚ'), ('red', 'ɹˈɛd'), ('list', 'lˈɪst'), ('though', 'ðˈo͡ʊ'), ('feel', 'fˈiːl'), ('talk', 'tˈɔːk'), ('bird', 'bˈɜːd'), ('soon', 'sˈuːn'), ('body', 'bˈɑːdi'), ('dog', 'dˈɑːɡ'), ('family', 'fˈæmɪli'), ('direct', 'dᵻɹˈɛkt'), ('pose', 'pˈo͡ʊz'), ('leave', 'lˈiːv'), ('song', 'sˈɔŋ'), ('measure', 'mˈɛʒɚ'), ('door', 'dˈoː͡ɹ'), ('product', 'pɹˈɑːdʌkt'), ('black', 'blˈæk'), ('short', 'ʃˈɔː͡ɹt'), ('numeral', 'nˈuːmɚɹə͡l'), ('class', 'klˈæs'), ('wind', 'wˈɪnd'), ('question', 'kwˈɛst͡ʃən'), ('happen', 'hˈæpən'), ('complete', 'kəmplˈiːt'), ('ship', 'ʃˈɪp'), ('area', 'ˈɛɹi͡ə'), ('half', 'hˈæf'), ('rock', 'ɹˈɑːk'), ('order', 'ˈɔː͡ɹdɚ'), ('fire', 'fˈa͡ɪ͡ɚ'), ('south', 'sˈa͡ʊθ'), ('problem', 'pɹˈɑːbləm'), ('piece', 'pˈiːs'), ('told', 'tˈo͡ʊld'), ('knew', 'nˈuː'), ('pass', 'pˈæs'), ('since', 'sˈɪns'), ('top', 'tˈɑːp'), ('whole', 'hˈo͡ʊl'), ('king', 'kˈɪŋ'), ('space', 'spˈe͡ɪs'), ('heard', 'hˈɜːd'), ('best', 'bˈɛst'), ('hour', 'ˈa͡ʊɚ'), ('better', 'bˈɛɾɚ'), ('true .', 'tɹˈuː .'), ('during', 'dˈʊ͡ɹɹɪŋ'), ('hundred', 'hˈʌndɹɪd'), ('five', 'fˈa͡ɪv'), ('remember', 'ɹᵻmˈɛmbɚ'), ('step', 'stˈɛp'), ('early', 'ˈɜːli'), ('hold', 'hˈo͡ʊld'), ('west', 'wˈɛst'), ('ground', 'ɡɹˈa͡ʊnd'), ('interest', 'ˈɪntɹɛst'), ('reach', 'ɹˈiːt͡ʃ'), ('fast', 'fˈæst'), ('verb', 'vˈɜːb'), ('sing', 'sˈɪŋ'), ('listen', 'lˈɪsən'), ('six', 'sˈɪks'), ('table', 'tˈe͡ɪbə͡l'), ('travel', 'tɹˈævə͡l'), ('less', 'lˈɛs'), ('morning', 'mˈɔː͡ɹnɪŋ'), ('ten', 'tˈɛn'), ('simple', 'sˈɪmpə͡l'), ('several', 'sˈɛvɹə͡l'), ('vowel', 'vˈa͡ʊə͡l'), ('toward', 'təwˈɔː͡ɹd'), ('war', 'wˈɔː͡ɹ'), ('lay', 'lˈe͡ɪ'), ('against', 'ɐɡˈɛnst'), ('pattern', 'pˈætɚn'), ('slow', 'slˈo͡ʊ'), ('center', 'sˈɛntɚ'), ('love', 'lˈʌv'), ('person', 'pˈɜːsən'), ('money', 'mˈʌni'), ('serve', 'sˈɜːv'), ('appear', 'ɐpˈɪ͡ɹ'), ('road', 'ɹˈo͡ʊd'), ('map', 'mˈæp'), ('rain', 'ɹˈe͡ɪn'), ('rule', 'ɹˈuːl'), ('govern', 'ɡˈʌvɚn'), ('pull', 'pˈʊl'), ('cold', 'kˈo͡ʊld'), ('notice', 'nˈo͡ʊɾɪs'), ('voice', 'vˈɔ͡ɪs'), ('unit', 'jˈuːnɪt'), ('power', 'pˈa͡ʊɚ'), ('town', 'tˈa͡ʊn'), ('fine', 'fˈa͡ɪn'), ('certain', 'sˈɜːʔn̩'), ('fly', 'flˈa͡ɪ'), ('fall', 'fˈɔːl'), ('lead', 'lˈiːd'), ('cry', 'kɹˈa͡ɪ'), ('dark', 'dˈɑː͡ɹk'), ('machine', 'məʃˈiːn'), ('note', 'nˈo͡ʊt'), ('wait', 'wˈe͡ɪt'), ('plan', 'plˈæn'), ('figure', 'fˈɪɡjɚ'), ('star', 'stˈɑː͡ɹ'), ('box', 'bˈɑːks'), ('noun', 'nˈa͡ʊn'), ('field', 'fˈiːld'), ('rest', 'ɹˈɛst'), ('correct', 'kɚɹˈɛkt'), ('able', 'ˈe͡ɪbə͡l'), ('pound', 'pˈa͡ʊnd'), ('done', 'dˈʌn'), ('beauty', 'bjˈuːɾi'), ('drive', 'dɹˈa͡ɪv'), ('stood', 'stˈʊd'), ('contain', 'kəntˈe͡ɪn'), ('front', 'fɹˈʌnt'), ('teach', 'tˈiːt͡ʃ'), ('week', 'wˈiːk'), ('final', 'fˈa͡ɪnə͡l'), ('gave', 'ɡˈe͡ɪv'), ('green', 'ɡɹˈiːn'), ('oh', 'ˈo͡ʊ'), ('quick', 'kwˈɪk'), ('develop', 'dɪvˈɛləp'), ('ocean', 'ˈo͡ʊʃən'), ('warm', 'wˈɔː͡ɹm'), ('free', 'fɹˈiː'), ('minute', 'mˈɪnɪt'), ('strong', 'stɹˈɔŋ'), ('special', 'spˈɛʃə͡l'), ('mind', 'mˈa͡ɪnd'), ('behind', 'bᵻhˈa͡ɪnd'), ('clear', 'klˈɪ͡ɹ'), ('tail', 'tˈe͡ɪl'), ('produce', 'pɹədˈuːs'), ('fact', 'fˈækt'), ('street', 'stɹˈiːt'), ('inch', 'ˈɪnt͡ʃ'), ('multiply', 'mˌʌltɪplˈa͡ɪ'), ('nothing', 'nˈʌθɪŋ'), ('course', 'kˈoː͡ɹs'), ('stay', 'stˈe͡ɪ'), ('wheel', 'wˈiːl'), ('full', 'fˈʊl'), ('force', 'fˈoː͡ɹs'), ('blue', 'blˈuː'), ('object', 'ˈɑːbd͡ʒɛkt'), ('decide', 'dᵻsˈa͡ɪd'), ('surface', 'sˈɜːfɪs'), ('deep', 'dˈiːp'), ('moon', 'mˈuːn'), ('island', 'ˈa͡ɪlənd'), ('foot', 'fˈʊt'), ('system', 'sˈɪstəm'), ('busy', 'bˈɪzi'), ('test', 'tˈɛst'), ('record', 'ɹˈɛkɚd'), ('boat', 'bˈo͡ʊt'), ('common', 'kˈɑːmən'), ('gold', 'ɡˈo͡ʊld'), ('possible', 'pˈɑːsᵻbə͡l'), ('plane', 'plˈe͡ɪn'), ('stead', 'stˈɛd'), ('dry', 'dɹˈa͡ɪ'), ('wonder', 'wˈʌndɚ'), ('laugh', 'lˈæf'), ('thousand', 'θˈa͡ʊzənd'), ('ago', 'ɐɡˈo͡ʊ'), ('ran', 'ɹˈæn'), ('check', 't͡ʃˈɛk'), ('game', 'ɡˈe͡ɪm'), ('shape', 'ʃˈe͡ɪp'), ('equate', 'ɪkwˈe͡ɪt'), ('hot', 'hˈɑːt'), ('miss', 'mˈɪs'), ('brought', 'bɹˈɔːt'), ('heat', 'hˈiːt'), ('snow', 'snˈo͡ʊ'), ('tire', 'tˈa͡ɪ͡ɚ'), ('bring', 'bɹˈɪŋ'), ('yes', 'jˈɛs'), ('distant', 'dˈɪstənt'), ('fill', 'fˈɪl'), ('east', 'ˈiːst'), ('paint', 'pˈe͡ɪnt'), ('language', 'lˈæŋɡwɪd͡ʒ'), ('among', 'ɐmˈʌŋ'), ('grand', 'ɡɹˈænd'), ('ball', 'bˈɔːl'), ('yet', 'jˈɛt'), ('wave', 'wˈe͡ɪv'), ('drop', 'dɹˈɑːp'), ('heart', 'hˈɑː͡ɹt'), ('am', 'ˈæm'), ('present', 'pɹˈɛzənt'), ('heavy', 'hˈɛvi'), ('dance', 'dˈæns'), ('engine', 'ˈɛnd͡ʒɪn'), ('position', 'pəzˈɪʃən'), ('arm', 'ˈɑː͡ɹm'), ('wide', 'wˈa͡ɪd'), ('sail', 'sˈe͡ɪl'), ('material', 'mətˈɪɹiə͡l'), ('size', 'sˈa͡ɪz'), ('vary', 'vˈɛɹi'), ('settle', 'sˈɛɾə͡l'), ('speak', 'spˈiːk'), ('weight', 'wˈe͡ɪt'), ('general', 'd͡ʒˈɛnɚɹə͡l'), ('ice', 'ˈa͡ɪs'), ('matter', 'mˈæ��ɚ'), ('circle', 'sˈɜːkə͡l'), ('pair', 'pˈɛ͡ɹ'), ('include', 'ɪŋklˈuːd'), ('divide', 'dᵻvˈa͡ɪd'), ('syllable', 'sˈɪləbə͡l'), ('felt', 'fˈɛlt'), ('perhaps', 'pɚhˈæps'), ('pick', 'pˈɪk'), ('sudden', 'sˈʌdən'), ('count', 'kˈa͡ʊnt'), ('square', 'skwˈɛ͡ɹ'), ('reason', 'ɹˈiːzən'), ('length', 'lˈɛŋθ'), ('represent', 'ɹˌɛpɹᵻzˈɛnt'), ('art', 'ˈɑː͡ɹt'), ('subject', 'sˈʌbd͡ʒɛkt'), ('region', 'ɹˈiːd͡ʒən'), ('energy', 'ˈɛnɚd͡ʒi'), ('hunt', 'hˈʌnt'), ('probable', 'pɹˈɑːbəbə͡l'), ('bed', 'bˈɛd'), ('brother', 'bɹˈʌðɚ'), ('egg', 'ˈɛɡ'), ('ride', 'ɹˈa͡ɪd'), ('cell', 'sˈɛl'), ('believe', 'bᵻlˈiːv'), ('fraction', 'fɹˈækʃən'), ('forest', 'fˈɔːɹɪst'), ('sit', 'sˈɪt'), ('race', 'ɹˈe͡ɪs'), ('window', 'wˈɪndo͡ʊ'), ('store', 'stˈoː͡ɹ'), ('summer', 'sˈʌmɚ'), ('train', 'tɹˈe͡ɪn'), ('sleep', 'slˈiːp'), ('prove', 'pɹˈuːv'), ('lone', 'lˈo͡ʊn'), ('leg', 'lˈɛɡ'), ('exercise', 'ˈɛksɚsˌa͡ɪz'), ('wall', 'wˈɔːl'), ('catch', 'kˈæt͡ʃ'), ('mount', 'mˈa͡ʊnt'), ('wish', 'wˈɪʃ'), ('sky', 'skˈa͡ɪ'), ('board', 'bˈoː͡ɹd'), ('joy', 'd͡ʒˈɔ͡ɪ'), ('winter', 'wˈɪntɚ'), ('sat', 'sˈæt'), ('written', 'ɹˈɪʔn̩'), ('wild', 'wˈa͡ɪld'), ('instrument', 'ˈɪnstɹəmənt'), ('kept', 'kˈɛpt'), ('glass', 'ɡlˈæs'), ('grass', 'ɡɹˈæs'), ('cow', 'kˈa͡ʊ'), ('job', 'd͡ʒˈɑːb'), ('edge', 'ˈɛd͡ʒ'), ('sign', 'sˈa͡ɪn'), ('visit', 'vˈɪzɪt'), ('past', 'pˈæst'), ('soft', 'sˈɔft'), ('fun', 'fˈʌn'), ('bright', 'bɹˈa͡ɪt'), ('gas', 'ɡˈæs'), ('weather', 'wˈɛðɚ'), ('month', 'mˈʌnθ'), ('million', 'mˈɪli͡ən'), ('bear', 'bˈɛ͡ɹ'), ('finish', 'fˈɪnɪʃ'), ('happy', 'hˈæpi'), ('hope', 'hˈo͡ʊp'), ('flower', 'flˈa͡ʊɚ'), ('clothe', 'klˈo͡ʊð'), ('strange', 'stɹˈe͡ɪnd͡ʒ'), ('gone', 'ɡˈɔn'), ('jump', 'd͡ʒˈʌmp'), ('baby', 'bˈe͡ɪbi'), ('eight', 'ˈe͡ɪt'), ('village', 'vˈɪlɪd͡ʒ'), ('meet', 'mˈiːt'), ('root', 'ɹˈuːt'), ('buy', 'bˈa͡ɪ'), ('raise', 'ɹˈe͡ɪz'), ('solve', 'sˈɑːlv'), ('metal', 'mˈɛɾə͡l'), ('whether', 'wˈɛðɚ'), ('push', 'pˈʊʃ'), ('seven', 'sˈɛvən'), ('paragraph', 'pˈæɹəɡɹˌæf'), ('third', 'θˈɜːd'), ('shall', 'ʃˈæl'), ('held', 'hˈɛld'), ('hair', 'hˈɛ͡ɹ'), ('describe', 'dᵻskɹˈa͡ɪb'), ('cook', 'kˈʊk'), ('floor', 'flˈoː͡ɹ'), ('either', 'ˈiːðɚ'), ('result', 'ɹɪzˈʌlt'), ('burn', 'bˈɜːn'), ('hill', 'hˈɪl'), ('safe', 'sˈe͡ɪf'), ('cat', 'kˈæt'), ('century', 'sˈɛnt͡ʃɚɹi'), ('consider', 'kənsˈɪdɚ'), ('type', 'tˈa͡ɪp'), ('law', 'lˈɔː'), ('bit', 'bˈɪt'), ('coast', 'kˈo͡ʊst'), ('copy', 'kˈɑːpi'), ('phrase', 'fɹˈe͡ɪz'), ('silent', 'sˈa͡ɪlənt'), ('tall', 'tˈɔːl'), ('sand', 'sˈænd'), ('soil', 'sˈɔ͡ɪl'), ('roll', 'ɹˈo͡ʊl'), ('temperature', 'tˈɛmpɹɪt͡ʃɚ'), ('finger', 'fˈɪŋɡɚ'), ('industry', 'ˈɪndʌstɹi'), ('value', 'vˈæljuː'), ('fight', 'fˈa͡ɪt'), ('lie', 'lˈa͡ɪ'), ('beat', 'bˈiːt'), ('excite', 'ɛksˈa͡ɪt'), ('natural', 'nˈæt͡ʃɚɹə͡l'), ('view', 'vjˈuː'), ('sense', 'sˈɛns'), ('ear', 'ˈɪ͡ɹ'), ('else', 'ˈɛls'), ('quite', 'kwˈa͡ɪt'), ('broke', 'bɹˈo͡ʊk'), ('case', 'kˈe͡ɪs'), ('middle', 'mˈɪdə͡l'), ('kill', 'kˈɪl'), ('son', 'sˈʌn'), ('lake', 'lˈe͡ɪk'), ('moment', 'mˈo͡ʊmənt'), ('scale', 'skˈe͡ɪl'), ('loud', 'lˈa͡ʊd'), ('spring', 'spɹˈɪŋ'), ('observe', 'əbzˈɜːv'), ('child', 't͡ʃˈa͡ɪld'), ('straight', 'stɹˈe͡ɪt'), ('consonant', 'kˈɑːnsənənt'), ('nation', 'nˈe͡ɪʃən'), ('dictionary', 'dˈɪkʃənˌɛɹi'), ('milk', 'mˈɪlk'), ('speed', 'spˈiːd'), ('method', 'mˈɛθəd'), ('organ', 'ˈɔː͡ɹɡən'), ('pay', 'pˈe͡ɪ'), ('age', 'ˈe͡ɪd͡ʒ'), ('section', 'sˈɛkʃən'), ('dress', 'dɹˈɛs'), ('cloud', 'klˈa͡ʊd'), ('surprise', 'sɚpɹˈa͡ɪz'), ('quiet', 'kwˈa͡ɪ͡ət'), ('stone', 'stˈo͡ʊn'), ('tiny', 'tˈa͡ɪni'), ('climb', 'klˈa͡ɪm'), ('cool', 'kˈuːl'), ('design', 'dɪzˈa͡ɪn'), ('poor', 'pˈʊ͡ɹ'), ('lot', 'lˈɑːt'), ('experiment', 'ɛkspˈɛɹɪmənt'), ('bottom', 'bˈɑːɾəm'), ('key', 'kˈiː'), ('iron', 'ˈa͡ɪ͡ɚn'), ('single', 'sˈɪŋɡə͡l'), ('stick', 'stˈɪk'), ('flat', 'flˈæt'), ('twenty', 'twˈɛnti'), ('skin', 'skˈɪn'), ('smile', 'smˈa͡ɪl'), ('crease', 'kɹˈiːs'), ('hole', 'hˈo͡ʊl'), ('trade', 'tɹˈe͡ɪd'), ('melody', 'mˈɛlədi'), ('trip', 'tɹˈɪp'), ('office', 'ˈɑːfɪs'), ('receive', 'ɹᵻsˈiːv'), ('row', 'ɹˈo͡ʊ'), ('mouth', 'mˈa͡ʊθ'), ('exact', 'ɛɡzˈækt'), ('symbol', 'sˈɪmbə͡l'), ('die', 'dˈa͡ɪ'), ('least', 'lˈiːst'), ('trouble', 'tɹˈʌbə͡l'), ('shout', 'ʃˈa͡ʊt'), ('except', 'ɛksˈɛpt'), ('wrote', 'ɹˈo͡ʊt'), ('seed', 'sˈiːd'), ('tone', 'tˈo͡ʊn'), ('join', 'd͡ʒˈɔ͡ɪn'), ('suggest', 'səd͡ʒˈɛst'), ('clean', 'klˈiːn'), ('break', 'bɹˈe͡ɪk'), ('lady', 'lˈe͡ɪdi'), ('yard', 'jˈɑː͡ɹd'), ('rise', 'ɹˈa͡ɪz'), ('bad', 'bˈæd'), ('blow', 'blˈo͡ʊ'), ('oil', 'ˈɔ͡ɪl'), ('blood', 'blˈʌd'), ('touch', 'tˈʌt͡ʃ'), ('grew', 'ɡɹˈuː'), ('cent', 'sˈɛnt'), ('mix', 'mˈɪks'), ('team', 'tˈiːm'), ('wire', 'wˈa͡ɪ͡ɚ'), ('cost', 'kˈɔst'), ('lost', 'lˈɔst'), ('brown', 'bɹˈa͡ʊn'), ('wear', 'wˈɛ͡ɹ'), ('garden', 'ɡˈɑː͡ɹdən'), ('equal', 'ˈiːkwə͡l'), ('sent', 'sˈɛnt'), ('choose', 't͡ʃˈuːz'), ('fell', 'fˈɛl'), ('fit', 'fˈɪt'), ('flow', 'flˈo͡ʊ'), ('fair', 'fˈɛ͡ɹ'), ('bank', 'bˈæŋk'), ('collect', 'kəlˈɛkt'), ('save', 'sˈe͡ɪv'), ('control', 'kəntɹˈo͡ʊl'), ('decimal', 'dˈɛsɪmə͡l'), ('gentle', 'd͡ʒˈɛntə͡l'), ('woman', 'wˈʊmən'), ('captain', 'kˈæptɪn'), ('practice', 'pɹˈæktɪs'), ('separate', 'sˈɛpɹət'), ('difficult', 'dˈɪfɪkə͡lt'), ('doctor', 'dˈɑːktɚ'), ('please', 'plˈiːz'), ('protect', 'pɹətˈɛkt'), ('noon', 'nˈuːn'), ('whose', 'hˈuːz'), ('locate', 'lo͡ʊkˈe͡ɪt'), ('ring', 'ɹˈɪŋ'), ('character', 'kˈæɹɪktɚ'), ('insect', 'ˈɪnsɛkt'), ('caught', 'kˈɔːt'), ('period', 'pˈi͡əɹɪəd'), ('indicate', 'ˈɪndᵻkˌe͡ɪt'), ('radio', 'ɹˈe͡ɪdɪˌo͡ʊ'), ('spoke', 'spˈo͡ʊk'), ('atom', 'ˈæɾəm'), ('human', 'hjˈuːmən'), ('history', 'hˈɪstɚɹi'), ('effect', 'ɪfˈɛkt'), ('electric', 'ᵻlˈɛktɹɪk'), ('expect', 'ɛkspˈɛkt'), ('crop', 'kɹˈɑːp'), ('modern', 'mˈɑːdɚn'), ('element', 'ˈɛlɪmənt'), ('hit', 'hˈɪt'), ('student', 'stˈuːdənt'), ('corner', 'kˈɔː͡ɹnɚ'), ('party', 'pˈɑː͡ɹɾi'), ('supply', 'səplˈa͡ɪ'), ('bone', 'bˈo͡ʊn'), ('rail', 'ɹˈe͡ɪl'), ('imagine', 'ɪmˈæd͡ʒɪn'), ('provide', 'pɹəvˈa͡ɪd'), ('agree', 'ɐɡɹˈiː'), ('thus', 'ðˈʌs'), ('capital', 'kˈæpɪɾə͡l'), ("won't", 'wˈo͡ʊnt'), ('chair', 't͡ʃˈɛ͡ɹ'), ('danger', 'dˈe͡ɪnd͡ʒɚ'), ('fruit', 'fɹˈuːt'), ('rich', 'ɹˈɪt͡ʃ'), ('thick', 'θˈɪk'), ('soldier', 'sˈo͡ʊld͡ʒɚ'), ('process', 'pɹˈɑːsɛs'), ('operate', 'ˈɑːpɚɹˌe͡ɪt'), ('guess', 'ɡˈɛs'), ('necessary', 'nˈɛsᵻsɚɹi'), ('sharp', 'ʃˈɑː͡ɹp'), ('wing', 'wˈɪŋ'), ('create', 'kɹiːˈe͡ɪt'), ('neighbor', 'nˈe͡ɪbɚ'), ('wash', 'wˈɑːʃ'), ('bat', 'bˈæt'), ('rather', 'ɹˈæðɚ'), ('crowd', 'kɹˈa͡ʊd'), ('corn', 'kˈɔː͡ɹn'), ('compare', 'kəmpˈɛ͡ɹ'), ('poem', 'pˈo͡ʊᵻm'), ('string', 'stɹˈɪŋ'), ('bell', 'bˈɛl'), ('depend', 'dᵻpˈɛnd'), ('meat', 'mˈiːt'), ('rub', 'ɹˈʌb'), ('tube', 'tˈuːb'), ('famous', 'fˈe͡ɪməs'), ('dollar', 'dˈɑːlɚ'), ('stream', 'stɹˈiːm'), ('fear', 'fˈɪ͡ɹ'), ('sight', 'sˈa͡ɪt'), ('thin', 'θˈɪn'), ('triangle', 'tɹˈa͡ɪæŋɡə͡l'), ('planet', 'plˈænɪt'), ('hurry', 'hˈɜːɹi'), ('chief', 't͡ʃˈiːf'), ('colony', 'kˈɑːləni'), ('clock', 'klˈɑːk'), ('mine', 'mˈa͡ɪn'), ('tie', 'tˈa͡ɪ'), ('enter', 'ˈɛntɚ'), ('major', 'mˈe͡ɪd͡ʒɚ'), ('fresh', 'fɹˈɛʃ'), ('search', 'sˈɜːt͡ʃ'), ('send', 'sˈɛnd'), ('yellow', 'jˈɛlo͡ʊ'), ('gun', 'ɡˈʌn'), ('allow', 'ɐlˈa͡ʊ'), ('print', 'pɹˈɪnt'), ('dead', 'dˈɛd'), ('spot', 'spˈɑːt'), ('desert', 'dˈɛzɚt'), ('suit', 'sˈuːt'), ('current', 'kˈɜːɹənt'), ('lift', 'lˈɪft'), ('rose', 'ɹˈo͡ʊz'), ('continue', 'kəntˈɪnjuː'), ('block', 'blˈɑːk'), ('chart', 't͡ʃˈɑː͡ɹt'), ('hat', 'hˈæt'), ('sell', 'sˈɛl'), ('success', 'səksˈɛs'), ('company', 'kˈʌmpəni'), ('subtract', 'sʌbtɹˈækt'), ('event', 'ᵻvˈɛnt'), ('particular', 'pɚtˈɪkjʊlɚ'), ('deal', 'dˈiːl'), ('swim', 'swˈɪm'), ('term', 'tˈɜːm'), ('opposite', 'ˈɑːpəzˌɪt'), ('wife', 'wˈa͡ɪf'), ('shoe', 'ʃˈuː'), ('shoulder', 'ʃˈo͡ʊldɚ'), ('spread', 'spɹˈɛd'), ('arrange', 'ɚɹˈe͡ɪnd͡ʒ'), ('camp', 'kˈæmp'), ('invent', 'ɪnvˈɛnt'), ('cotton', 'kˈɑːʔn̩'), ('born', 'bˈɔː͡ɹn'), ('determine', 'dɪtˈɜːmɪn'), ('quart', 'kwˈɔː͡ɹt'), ('nine', 'nˈa͡ɪn'), ('truck', 'tɹˈʌk'), ('noise', 'nˈɔ͡ɪz'), ('level', 'lˈɛvə͡l'), ('chance', 't͡ʃˈæns'), ('gather', 'ɡˈæðɚ'), ('shop', 'ʃˈɑːp'), ('stretch', 'stɹˈɛt͡ʃ'), ('throw', 'θɹˈo͡ʊ'), ('shine', 'ʃˈa͡ɪn'), ('property', 'pɹˈɑːpɚɾi'), ('column', 'kˈɑːlʌm'), ('molecule', 'mˈɑːlɪkjˌuːl'), ('select', 'sᵻlˈɛkt'), ('wrong', 'ɹˈɔŋ'), ('gray', 'ɡɹˈe͡ɪ'), ('repeat', 'ɹᵻpˈiːt'), ('require', 'ɹᵻkwˈa͡ɪ͡ɚ'), ('broad', 'bɹˈɔːd'), ('prepare', 'pɹɪpˈɛ͡ɹ'), ('salt', 'sˈɔlt'), ('nose', 'nˈo͡ʊz'), ('plural', 'plˈʊ͡ɹɹə͡l'), ('anger', 'ˈæŋɡɚ'), ('claim', 'klˈe͡ɪm'), ('continent', 'kˈɑːntɪnənt'), ('oxygen', 'ˈɑːksɪd͡ʒən'), ('sugar', 'ʃˈʊɡɚ'), ('death', 'dˈɛθ'), ('pretty', 'pɹˈɪɾi'), ('skill', 'skˈɪl'), ('women', 'wˈɪmɪn'), ('season', 'sˈiːzən'), ('solution', 'səlˈuːʃən'), ('magnet', 'mˈæɡnɪt'), ('silver', 'sˈɪlvɚ'), ('thank', 'θˈæŋk'), ('branch', 'bɹˈænt͡ʃ'), ('match', 'mˈæt͡ʃ'), ('suffix', 'sˈʌfɪks'), ('especially', 'ɪspˈɛʃə͡li'), ('fig', 'fˈɪɡ'), ('afraid', 'ɐfɹˈe͡ɪd'), ('huge', 'hjˈuːd͡ʒ'), ('sister', 'sˈɪstɚ'), ('steel', 'stˈiːl'), ('discuss', 'dɪskˈʌs'), ('forward', 'fˈɔː͡ɹwɚd'), ('similar', 'sˈɪmɪlɚ'), ('guide', 'ɡˈa͡ɪd'), ('experience', 'ɛkspˈi͡əɹɪəns'), ('score', 'skˈoː͡ɹ'), ('apple', 'ˈæpə͡l'), ('bought', 'bˈɔːt'), ('led', 'lˈɛd'), ('pitch', 'pˈɪt͡ʃ'), ('coat', 'kˈo͡ʊt'), ('mass', 'mˈæs'), ('card', 'kˈɑː͡ɹd'), ('band', 'bˈænd'), ('rope', 'ɹˈo͡ʊp'), ('slip', 'slˈɪp'), ('win', 'wˈɪn'), ('dream', 'dɹˈiːm'), ('evening', 'ˈiːvnɪŋ'), ('condition', 'kəndˈɪʃən'), ('feed', 'fˈiːd'), ('tool', 'tˈuːl'), ('total', 'tˈo͡ʊɾə͡l'), ('basic', 'bˈe͡ɪsɪk'), ('smell', 'smˈɛl'), ('valley', 'vˈæli'), ('nor', 'nˈɔː͡ɹ'), ('double', 'dˈʌbə͡l'), ('seat', 'sˈiːt'), ('arrive', 'ɚɹˈa͡ɪv'), ('master', 'mˈæstɚ'), ('track', 'tɹˈæk'), ('parent', 'pˈɛɹənt'), ('shore', 'ʃˈoː͡ɹ'), ('division', 'dᵻvˈɪʒən'), ('sheet', 'ʃˈiːt'), ('substance', 'sˈʌbstəns'), ('favor', 'fˈe͡ɪvɚ'), ('connect', 'kənˈɛkt'), ('post', 'pˈo͡ʊst'), ('spend', 'spˈɛnd'), ('chord', 'kˈɔː͡ɹd'), ('fat', 'fˈæt'), ('glad', 'ɡlˈæd'), ('original', 'ɚɹˈɪd͡ʒɪnə͡l'), ('share', 'ʃˈɛ͡ɹ'), ('station', 'stˈe͡ɪʃən'), ('dad', 'dˈæd'), ('bread', 'bɹˈɛd'), ('charge', 't͡ʃˈɑː͡ɹd͡ʒ'), ('proper', 'pɹˈɑːpɚ'), ('bar', 'bˈɑː͡ɹ'), ('offer', 'ˈɔfɚ'), ('segment', 'sˈɛɡmənt'), ('slave', 'slˈe͡ɪv'), ('duck', 'dˈʌk'), ('instant', 'ˈɪnstənt'), ('market', 'mˈɑː͡ɹkɪt'), ('degree', 'dᵻɡɹˈiː'), ('populate', 'pˈɑːpjʊlˌe͡ɪt'), ('chick', 't͡ʃˈɪk'), ('dear', 'dˈɪ͡ɹ'), ('enemy', 'ˈɛnəmi'), ('reply', 'ɹᵻplˈa͡ɪ'), ('drink', 'dɹˈɪŋk'), ('occur', 'əkˈɜː'), ('support', 'səpˈoː͡ɹt'), ('speech', 'spˈiːt͡ʃ'), ('nature', 'nˈe͡ɪt͡ʃɚ'), ('range', 'ɹˈe͡ɪnd͡ʒ'), ('steam', 'stˈiːm'), ('motion', 'mˈo͡ʊʃən'), ('path', 'pˈæθ'), ('liquid', 'lˈɪkwɪd'), ('log', 'lˈɔɡ'), ('meant', 'mˈɛnt'), ('quotient', 'kwˈo͡ʊʃənt'), ('teeth', 'tˈiːθ'), ('shell', 'ʃˈɛl'), ('neck', 'nˈɛk')]

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("IPA Trainer")
        self.geometry("500x300")
        
        self.words = []
        self.ipa = []
        self.guess = tk.StringVar(value="")
        self.current_ipa = tk.StringVar(value="")
        self.current_word = tk.StringVar(value="Word")
        self.correct = tk.IntVar(value=0)
        self.incorrect = tk.IntVar(value=0)
        self.streak = tk.IntVar(value=0)
        self.progress = 0
        self.isGameRunning = False
        
        # Load the words and IPA
        self.load_words()
        self.load_ipa()
        
        # Create the start frame
        self.create_start_frame()
        
        # Set trace on the guess variable
        self.guess.trace("w", self.guess_changed)
        
        self.after(100, self.is_progress_done)
                
    def load_words(self):
        # Load from IPA_WORDS list
        for word in IPA_WORDS:
            self.words.append(word[0])
                
    def load_ipa(self):
        # Load from IPA_WORDS list
        for word in IPA_WORDS:
            self.ipa.append(word[1])
                
    def create_start_frame(self):
        self.start_frame = ctk.CTkFrame(self)
        self.start_frame.pack(fill="both", expand=True)
        
        self.start_button = ctk.CTkButton(self.start_frame, 
                                          text="Start", command=self.start)
        self.start_button.pack(fill="x", expand=True, padx=20)
        
    def start(self):
        self.start_frame.destroy()
        self.create_stats_frame()
        self.create_game_frame()
        
        self.isGameRunning = True
        self.next_word()

        
    def create_game_frame(self):
        self.game_frame = ctk.CTkFrame(self)
        self.game_frame.pack(fill="both", expand=True, pady=[0,10], padx=10)
        
        self.ipa_and_progress_frame = ctk.CTkFrame(self.game_frame)
        self.ipa_and_progress_frame.pack(fill="both", expand=True)
        
        self.ipa_label = ctk.CTkLabel(self.ipa_and_progress_frame, textvariable=self.current_ipa, font=("Arial", 32))
        self.ipa_label.pack(fill="both", expand=True, pady=10)
        
        # Create the progress bar and color it green
        self.progress_bar = ctk.CTkProgressBar(self.ipa_and_progress_frame)
        self.progress_bar.configure(mode="determinate", determinate_speed=0.1, progress_color="green")
        
        self.progress_bar.pack(fill="x", expand=True, pady=[10, 0], padx=20, side="bottom")
        
        self.entry = ctk.CTkEntry(self.game_frame, textvariable=self.guess)
        self.entry.pack(fill="both", expand=True, pady=5)
        
        self.submit_button = ctk.CTkButton(self.game_frame, text="Submit", command=self.submit)
        self.submit_button.pack(fill="both", expand=True)
        
        self.entry.bind("<Return>", self.submit)
        
    def create_stats_frame(self):
        self.stats_frame = ctk.CTkFrame(self)
        
        # Stats frame will be a thin bar at the top of the window
        # 3 frames will be placed inside the stats frame in a grid 
        # The first frame will contain the number of correct answers
        
        # Configure rows and columns
        self.stats_frame.grid_columnconfigure(0, weight=1)
        self.stats_frame.grid_columnconfigure(1, weight=1)
        self.stats_frame.grid_columnconfigure(2, weight=1)
        
        self.correct_frame = ctk.CTkFrame(self.stats_frame)
        
        self.correct_label = ctk.CTkLabel(self.correct_frame, text="Correct:", font=("Arial", 12))
        self.correct_label.pack(fill="x", padx=(0, 5))
        
        self.correct_count = ctk.CTkLabel(self.correct_frame, 
                                          textvariable=self.correct , 
                                          font=("Arial", 25), text_color="#4AB19D")
        self.correct_count.pack(fill="x", padx=(0, 5))
        
        self.correct_frame.grid(row=0, column=0, sticky="new")
        
        # The frame will contain the current streak
        self.streak_frame = ctk.CTkFrame(self.stats_frame)
        
        self.streak_label = ctk.CTkLabel(self.streak_frame, text="Streak:", font=("Arial", 12))
        self.streak_label.pack(fill="x", padx=(0, 5))
        
        self.streak_count = ctk.CTkLabel(self.streak_frame, 
                                         textvariable=self.streak, 
                                         font=("Arial", 25))
        self.streak_count.pack(fill="x", padx=(0, 5))
        
        self.streak_frame.grid(row=0, column=1, sticky="new")
        
        # The frame will contain the number of incorrect answers
        self.incorrect_frame = ctk.CTkFrame(self.stats_frame)

        self.incorrect_label = ctk.CTkLabel(self.incorrect_frame, text="Incorrect:", font=("Arial", 12))
        self.incorrect_label.pack(fill="x", padx=(0, 5))
        
        self.incorrect_count = ctk.CTkLabel(self.incorrect_frame, 
                                            textvariable=self.incorrect, 
                                            font=("Arial", 25), text_color="#EF3D59")
        self.incorrect_count.pack(fill="x", padx=(0, 5))
        
        self.incorrect_frame.grid(row=0, column=2, sticky="new")
        
        self.stats_frame.pack(fill="x", side="top", padx=10, pady=[10, 0])
        
    def guess_changed(self, *args):
        if self.isGameRunning:
            if self.guess.get().lower() == self.current_word.get().lower():
                self.handle_correct()

    def next_word(self): 
        # Reset the entry
        self.guess.set("")
        
        # Get a random number between 0 and the length of the words list
        index = random.randint(0, len(self.words) - 1)
        
        # Get the word and IPA at that index
        self.current_word.set(self.words[index])
        self.current_ipa.set(self.ipa[index])
        
        # Start the progress bar
        self.progress_bar.set(0)
        self.progress_bar.start()
        
        self.isGameRunning = True
        
        self.update_idletasks()
        
    def submit(self, event=None):
        if self.isGameRunning:
            if self.guess.get().lower() == self.current_word.get().lower():
                self.handle_correct()
            else:
                self.handle_incorrect()

    def handle_incorrect(self):
        self.progress_bar.stop()
        self.isGameRunning = False
        
        self.flash_red()
        self.streak.set(0)
        self.incorrect.set(self.incorrect.get() + 1)
        
        # Set the ipa label to the correct answer
        self.current_ipa.set(self.current_word.get())
        
        self.update_idletasks()
        
        # Wait 1 second then generate a new word
        self.after(1000, self.next_word)
        
    def handle_correct(self):
        self.progress_bar.stop()
        self.isGameRunning = False
        
        self.correct.set(self.correct.get() + 1)
        self.streak.set(self.streak.get() + 1)
        
        self.flash_green()
        self.next_word()
        
    def flash_green(self):
        self.ipa_label.configure(text_color="green")
        self.after(100, self.reset_color)
        
    def flash_red(self):
        self.ipa_label.configure(text_color="red")
        self.after(1000, self.reset_color)
        
    def reset_color(self):
        self.ipa_label.configure(text_color="black")

    def color_map(self, start_color, end_color, num):
        # Convert the hex colors to RGB
        start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
        end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))

        # Calculate a color for each step between the start and end colors
        color_range = [(int(start_rgb[i] + (float(num)/100) * (end_rgb[i] - start_rgb[i]))) for i in range(3)]

        # Convert the calculated color back to hex
        intermediate_color = '#%02x%02x%02x' % tuple(color_range)

        return intermediate_color
        
    def is_progress_done(self):
        if self.isGameRunning:
            self.progress = self.progress_bar.get()
            
            color = self.color_map('#4AB19D', '#EF3D59', round(self.progress * 100))

            self.progress_bar.configure(progress_color=color)
            
            if self.progress > 0.99:
                self.handle_incorrect()
                
        self.after(100, self.is_progress_done)
            
if __name__ == "__main__":
    app = App()
    app.mainloop()
    
    
