
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

sentence = input()
words = create_words(sentence)

def sentence_type(words):
    for i in words:
        if i.upper() == "WHAT" or i.upper() == "HOW" or i.upper() == "WHY" or i.upper() == "WHEN" or i.upper() == "WHERE":
            return "question"
        else:
            return "afirmation"


if sentence_type(words) == "question":
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

    def answer(words):
        brain = open("brain.txt","r+")
        info = ""
        data = brain.readlines()
        for i in data:
            row = list(i)
            if row[0] == "i":
                for j in range(11, len(row)-1):
                    info = info + row[j]
        return info



    def build_answer(verb, subject, question_type, answer):
        preposition = ""
        if question_type == "explain":
            preposition = "because"
        #elif question_type == 
            
        answer = [subject, verb, preposition, answer]
        return answer   

    for i in build_answer(verb(words),subject(words), question_type(words), answer(words)):
        print(i,end=" ")
        
else:

        def subject(words):
            return words[0]

        def verb(words):
            return words[1]

        def preposition(words):
            return words[2]

        def information(words):
            information = []
            
            for i in range(3, len(words)):
                information.append(words[i])
            string = ""
            for j in information:
                string = string + " " + j

            return string
        
        def build_answer(subject, verb, preposition, information, words):
            answer = [subject, verb, preposition, information]

            try:
                string_answer = ""
                for i in answer:
                    string_answer += i
                return string_answer
            except:
                return answer

        def memorize_answer(subject, verb, preposition, information):
            brain = open("brain.txt","a+")
            brain.write("subject: " + subject + "\nverb: " + verb + "\npreposition: "+ preposition +  "\ninformation: " + str(information) + "\n")
            brain.close() 

        for i in build_answer(subject(words), verb(words), preposition(words), information(words), words):
            print(i, end=" ")

        memorize_answer(subject(words), verb(words), preposition(words), information(words))
