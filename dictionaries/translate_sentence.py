#create an empty dictionary
acronyms1 = {}
acronyms1['LOL'] = 'laugh out loud'
acronyms1['IDK'] = "I don't know"
acronyms1['TBH'] = "to be honest"

print ("acronyms1: " + str(acronyms1))


#var2
acronyms = { 
    'LOL': 'laugh out loud',
    'IDK': "I don't know",
    'TBH': 'To be honest'
}
print ("acronyms: " + str(acronyms))

acronyms['TBH'] = "honesly"

print(acronyms['TBH'])  

del acronyms['LOL']

print(acronyms)

# using get() won't crach your program with an error
# instead, get() will return None if the key doesn't exist

definition = acronyms.get('BTW')

print(acronyms)

if definition:
    print(definition)
else:
    print("Key doesn't exist")

#Translate the sentence

sentence = 'IDK' + 'what happend ' + 'TBH'
translation = acronyms.get('IDK') + ' what happend ' + acronyms.get('TBH')

print ('sentence: ', sentence)
print('translation: ', translation)

