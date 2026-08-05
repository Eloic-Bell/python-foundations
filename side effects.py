emoticon = ":("
def main():
    global emoticon
    say("is anyone there?")
    emoticon = ":D"
    say("oh, there you are!")

def say(phrase):
    print(phrase, " ", emoticon)

main()
