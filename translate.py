#!/usr/bin/python

import requests
import urllib
import sys

def processWubi():
    string = ""
    with open('encoding_zh.txt', mode='r', encoding='utf8') as r:
        for line in r:
            l = line.split('\t')
            word,freq = l[0],l[2]
            # code = getTranslate(word)
            string += word + '\n'
    with open('encoding_en_test.txt', 'w', encoding="utf8") as w:
        w.write(string)


def getTranslate(word):
    url = 'https://translate.googleapis.com/translate_a/single?' # client=gtx&sl=zh&tl=en&dt=t&q='+urllib.parse.quote(word)
    params = dict(
        client='gtx',
        sl='zh',
        tl='en',
        dt='t',
        q=word
    )
    resp = requests.get(url, params)
    data = resp.json()
    print(data)
    return data[0][0][0]


def makeEnEncoding():
    words = []
    with open('corpus_zh.txt', mode='r', encoding='utf8') as r:
        for line in r.readlines():
            words.append(tuple(line.split('\t')))

    with open('corpus_en_w.txt', 'r') as r:
        i=0
        for line in r.readlines():
            words[i] = tuple([words[i][0], line.lower().strip(), words[i][1].strip()])
            i+=1

    with open('corpus_en.txt', 'w', encoding="utf8") as w:
        for word in words:
            w.write('\t'.join(list(word))+'\n')


def sieveSetSubstractionWords():
    existingWords = []
    newCorpusWords = {}

    with open('encoding_zh.txt', mode='r', encoding='utf8') as r:
        for line in r.readlines():
            existingWords.append(line.split('\t')[0])

    with open('ctx.csv', mode='r', encoding='utf8') as r:
        for line in r.readlines():
            word,count = line.split(',')[0], int(line.split(',')[1])
            if len(word) > 1 and count > 1000:
                newCorpusWords[word] = count
    
    newWords = list(newCorpusWords.keys() - set(existingWords))
    print(len(newWords))
    newCorpus = {}
    for word in newWords:
        newCorpus[word] = newCorpusWords[word]

    newWords = sorted(newCorpus.items(), key=lambda x: x[1], reverse=True)

    with open('corpus_zh.txt', 'w', encoding='utf8') as file:
        for word in newWords:
            file.write(word[0]+'\t'+str(word[1]*100)+'\n')


makeEnEncoding()
