# https://py.checkio.org/en/mission/text-editor/
# Difficulty : Simple

class Text: 
    text=font=''
    
    def write(self,text):
        self.text+=text
    
    def restore(self,old):
        self.text, self.font=old
          
    def set_font(self,font):
        self.font="["+font+"]"

    def show(self):
        return self.font+self.text+self.font

class SavedText(list): 
    get_version=list.__getitem__    
    
    def save_text(self,text): 
        self.append((text.text,text.font))
        
# Example
# text = Text()
# saver = SavedText()
#    
# text.write("At the very beginning ")
# saver.save_text(text)
# text.set_font("Arial")
# saver.save_text(text)
# text.write("there was nothing.")
# text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
#    
# text.restore(saver.get_version(0))
# text.show() == "At the very beginning "
