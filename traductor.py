from translate import Translator
def translateWords(word):
        trad = Translator(from_lang="spanish",to_lang="english")
        res = trad.translate(word)
        return print(res)