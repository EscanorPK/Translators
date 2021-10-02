from googletrans import Translator

def translate( sc,dt,text ):
    translator = Translator()
    translated_text = translator.translate(text, src=sc, dest = dt)
    print(f"The Actual Text was {text}")
    print(f"The Translated Text is: {translated_text.text}")
    print(f"The Translated Text pronunciation is {translated_text.pronunciation}")


mode=input("Enter the translator mode you want to choose: \t 1:Eng to Jap \t 2:Jap to Eng \t 3:Exit \n")
while(mode!="3"):
    if (mode=="1"):
        src="en"
        dst="ja"
    elif(mode=="2"):
        src="ja"
        dst="en"
    txt=input("Enter text to be translated:")
    translate(src,dst,txt)
    mode=input("Enter for next operation:")



