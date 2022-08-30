from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name ?",
        ["Ricardo","Manuel","Pedro"]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine|Im fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I'm 23",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["I was born ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Concepcion del Uruguay, Argentina',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"who (.*) (football player|player) ?",
        ["Messi","Ronaldo","Rooney"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"what (.*) (chances|chance)(.*)?",
        ["They have a great shot, but it's gonna be difficult"]
    ],
    [
        r"what (.*) (fight|intercation)(.*)?",
        ["It is a bad look for the sport"]
    ],
    [
        r"(what sports) (.*) (like)?",
        ["I like Tennis but im a big fan of foobtall"]
    ],
    [
        r"what (.*) (think|thought) (.*) (football)?",
        ["I believe its the best sport ever invented. Either to watch or play"]
    ],
    [
        r"(what club) (.*) (fan|support)?",
        ["Im a fan of Boca Juniors", "Im a fan of River Plate",]
    ],
    [
        r"when (.*) (start watching|start playing)(.*)?",
        ["I got into football when my dad bought me a ball in my 7th birthday.",]
    ],
    [
        r"why (.*) (start watching|start playing|do you like)(.*)?",
        ["I just love running and scoring goals, watching big matches and feeling the passion and effort that the sport gives you",]
    ],
    [
        r"which (.*) (fondest memory|fondest memories)(.*)?",
        ["I'd say the first time I saw Boca win a clasico against River","I'd say the first time I saw River win a clasico against Boca"]
    ],
    [
        r"is there (.*) (hate|club that u hate)(.*)?",
        ["Well since im a fan of Boca, I love winning against River","Well since im a fan of River, I love winning against Boca"]
    ],    
    [
        r"which (.*) (biggest rival|rival)(.*)?",
        ["Boca for sure","River for sure"]
    ], 
    [
        r"quit",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon"]
    ],
]

def chat():
    print("Hi! what is your name?")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()