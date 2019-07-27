from django.http import HttpResponse
from django.shortcuts import render
from cryptography.fernet import Fernet
import operator
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def homepage(request):
    return render(request,'home.html',{'name':'Hi There The Stencil'})

def Count(request):
    data= request.GET['Fulltextarea']
    encrpt=data.encode()
    salt=b'\xca\xeaK)\xa2-\xb1\x13(n1\x9f\xa1\xf7+\x92'
    kdf=PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
    )
    key=base64.urlsafe_b64encode(kdf.derive(encrpt))
    wordlist=data.split(' ')
    lenlis=len(wordlist)
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] = 1
            sortedlist =sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'Count.html',{'fulltext':data,'Length':lenlis,'worddictionary':sortedlist,'encrpt':key})

def About(request):
    file=open('key.key','rb')
    key=file.read()
    file.close()
    return render(request,'About.html',{'Keys':key})
