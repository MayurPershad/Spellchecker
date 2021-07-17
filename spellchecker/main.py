from textblob import TextBlob

a="Corrct"
print("original text:"+str(a))

b=TextBlob(a)

print("corrected text:"+str(b.correct()))
