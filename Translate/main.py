from translate import Translator

translator = Translator(from_lang='english', to_lang='german')
translation = translator.translate('This is a useful library')
print(translation)