import random
import json 
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()

intents = json.loads(open("firstaid.json").read())

words = pickle.load(open("words.pkl","rb"))
classes = pickle.load(open("classes.pkl","rb"))

model = load_model("chatbotmodel.h5")

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_word = clean_up_sentence(sentence)
    bag = [0]  * len(words)

    for w in sentence_word:
        for i,word in enumerate(words):
            if word == w:
                bag[i] = 1

    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    result = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(result) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x : x[1],reverse=True)

    result_list = []
    for r in results:
        result_list.append({"intent":classes[r[0]],"probablity":str(r[1])})
        return result_list


def get_response(intents_list,intents_json):
    #intents_list = list(intents_list)
    tag = intents_list[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result

print("ChatBot is running!!!")


while True:
    message = input("You:")
    ints = predict_class(message)
    res = get_response(ints,intents)
    print("ChatBot:",res)



        
    

