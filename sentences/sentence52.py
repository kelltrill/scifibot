from sentences.base_sentence import base_sentence

class sentence52(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'The ' + components['secondary_actors']
        sentence += ' onboard the distant ' + components['transport_desc'] 
        sentence += ' ' + components['transport'] 
        sentence += ' have a taste for human flesh. The ' + components['engine']
        sentence += ' on their ship is powerful. Run.'

        return sentence
