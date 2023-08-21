import spacy
nlp = spacy.load('en_core_web_md')

#Words to compare
word1 = nlp("Cat")
word2 = nlp("monkey")
word3 = nlp("banana")

#Compare all words against each other
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"


#Note to code checker: The original sentences had backslashes. I've omitted them as it seemed more likely these were typos rather than intended as escape characters
sentences = ["Where did my dog go",
"Hello, there is my car",
"I've lost my key in my car",
"I'd like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


# Comparison between .md and .sm SpaCy Modules:
#  A lot of word associations scored higher with the .sm module than I think are appropriate. For example, 'cat' and 'apple' scored .69 with .sm, but only .20 with .md
#  And some associations were rated lower similarity, such as "Why is my cat on the car" and "where did my dog go" (.md: 0.60, .sm:0.41) I suspect .md, being a more detailed module,
# picked up onm both statements being a question pertaining to the nature of one's pet. 