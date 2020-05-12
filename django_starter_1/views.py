from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    text=request.GET['text']
    text_split=text.split()
    worddict={}
    for word in text_split:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1
    sortedword=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
    print(text)
    return render(request,'count.html',{'originaltext':text,'total':len(text_split),'wordlist':sortedword})