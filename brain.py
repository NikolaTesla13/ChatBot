def create_words(sentence):
    words =[]
    temp = ""
    for i in sentence:
        if i != " " :
            temp+=i
        elif i == " ":
            words.append(temp)
            temp=""
        if i == "." or i == "?" or i=="!" or i=="":
            words.append(temp)
            temp=""
    return words

def sentence_type(words):
    for i in words:
        if i.upper() == "WHAT" or i.upper() == "HOW" or i.upper() == "WHY" or i.upper() == "WHEN" or i.upper() == "WHERE":
            return "question"
        else:
            return "command"

def question_type(words):
    for i in words:
        if i.upper() == "WHAT":
            return "thing"
        if i.upper() == "HOW":
            return "action"
        if i.upper() == "WHY":
            return "explain"
        if  i.upper() == "WHEN":
            return "time"
        if i.upper() == "WHERE":
            return "place"

def verb_type_error(words):
    for i in words:
        if i.upper() == "IS" or i.upper() == "ARE" or i.upper() == "WAS" or i.upper() == "WERE":
            return "being"
def verb_type(words):
    v = words[-1]
    l = list(v)
    l[-1] = ""
    verb = "".join(l)
    
    if verb_type_error(words) == None:
        return "action"
    else:
        return "being"

def verb(words):
    v = words[2]
    l = list(v)
    if l[-1] == "." or l[-1] == "?" or l[-1] == "!":
        l[-1] = ""
    verb = "".join(l)
    return verb

def subject(words):
    return words[1]

def build_answer(verb, subject, question_type):
    preposition = ""
    if question_type == "explain":
        preposition = "because"
    #elif question_type == ... 
        
    answer = [subject, verb, preposition, "BETA"]
    return answer
            

sentence = input()
words = create_words(sentence)
for i in build_answer(verb(words),subject(words), question_type(words)):
    print(i,end=" ")
    
    
