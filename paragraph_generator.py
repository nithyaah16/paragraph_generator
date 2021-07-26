def sentence_maker(phrase):
    interro=("how","why","what","when","are","is","does","do","where","can","should","could","would","will")
    capitalized=phrase.capitalize()
    if phrase.startswith(interro):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

x=True
list1=[]
while x==True:
    phrase=input("Say something: ")
    if phrase!="/end":
        sentence=sentence_maker(phrase)
        list1.append(sentence)
        
    else:
        break
    
print("".join(list1))   
