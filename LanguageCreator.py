import random, string

def createSyllable():
    syllableLength = random.randint(2,3)
    weighted_alphabet = "aaabbccdddeeeeffgghhiijkklllmmmnnnnooppqrrssstttuuvwwxyzz"
    syllable = weighted_alphabet[random.randint(0,len(weighted_alphabet)-1)]
    #syllable = string.ascii_lowercase[random.randint(0,len(string.ascii_lowercase)-1)]
    for i in range(syllableLength):
        if syllable[i] in "aeiou":
            syllable += "bbccdddffgghhjkklllmmmnnnnppqrrssstttvwwxyzz"[random.randint(0,len("bbccdddffgghhjkklllmmmnnnnppqrrssstttvwwxyzz")-1)]
        else:
            syllable += "aaeeeiou"[random.randint(0,len("aaeeeiou")-1)]
    return syllable

def createWord():
    wordLength = int(abs(random.gauss(0,1))*2+1)
    word = ""
    for i in range(wordLength):
        word += createSyllable()
        if random.randint(1,5) == 5:
            word = word.capitalize()
    return word

def createSentence():
    sentenceLength = int(abs(random.gauss(0,1))*6+3)
    sentence = ""
    for i in range(sentenceLength):
        sentence += createWord() + " "
    sentence = sentence[:-1] + "."
    sentence = sentence.capitalize()
    #print(sentence)
    return sentence

def createText(num_sentences, num_paragraphs = None):
    text = []
    for i in range(num_sentences):
        if i > 0:
            text.append(" " + createSentence())
        else:
            text.append(createSentence())
    if num_paragraphs:
        for i in range(1, num_paragraphs):
            pos = int(i*num_sentences/num_paragraphs + random.gauss(0,1)*1.5)
            text.insert(pos, "\n\n\n")    
    text_string = ""
    for s in text:
        text_string += s
    return text_string

try:
    file = open("D:/Beispieltext 1.odt", "w")
    file.write(createText(90, 3))
    file.close()
except:
    pass
#print(createText(60,3))
