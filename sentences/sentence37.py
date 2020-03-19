from sentences.base_sentence import base_sentence

class sentence37(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['place_article_on_desc'].title()
        sentence += ' ' + components['place_desc'] 
        sentence += ' ' + components['place']
        sentence += ' orbits ' + components['place2_article_on_desc']
        sentence += ' ' + components['place2_desc']
        sentence += ' ' + components['place2']
        sentence += '. Raging storms of ' + components['liquid_desc']
        sentence += ' ' + components['liquid']
        sentence += ' fill its skies.'

        return sentence