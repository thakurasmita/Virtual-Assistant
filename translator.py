from translate import Translator
translator= Translator(to_lang="Hindi")
translation = translator.translate("kaise ho")
translator2= Translator(to_lang="English")
translation2 = translator2.translate(translation)
print(translation2)