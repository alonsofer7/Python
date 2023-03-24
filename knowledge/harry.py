from logic import *

rain = Symbol("rain")                   #It is raining
hagrid = Symbol("hagrid")               #Harry visited Hagrid
dumbledore = Symbol("dumbledore")       #Harry visited Dumbledore

sentence = And(rain, hagrid)            #An example sentence

knowledge = And(                        #This is the knowledge base
    Implication(Not(rain), hagrid),     #If it 
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print(sentence.formula())

print(model_check(knowledge, rain)) #base in knowledge, is it raining?