def lyrics_to_frequency(lyrics):
    mydict={}
    for word in lyrics:
        if word in mydict:
            mydict[word]+=1
        else:
            mydict[word]
    return mydict

 #lyrics to sheloves you the beatles
she_loves_you=['r','y']
beatles=lyrics_to_frequency(she_loves_you)





def most_common_words(freqs):
    values=freqs.values()
    best=max(values)
    words=[]
    for k in freqs:
        if freqs[k]==best:
            words.append(k)
    return (words,best)

#/*most common words*/

def words_often(freqs,mintimes):
    result=[]
    done=False
    while not done:
        temp=most_common_words(freqs)
        if temp[1] >=mintimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done=True
        return result
print(words_often(beatles,5))


