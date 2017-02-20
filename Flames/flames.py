import datetime
from pymongo import MongoClient

##
##client = MongoClient(host="localhost",port = 	27017)
a = raw_input('your Name ')
b = raw_input('Welcome %s!!! What is your Lover name ? ' %a)
a = a.lower()
b = b.lower()
a = a.replace(" ","")
b = b.replace(" ","")

##db = client["hi"]
#assert db.connection == client

def remove_let(word,let):
    ind = word.index(let)

    le = len(word)
    list1 = list(word)
    for i in range(0,le):
        if (i == ind):

            for j in range(i,le-1):

                list1[j] = list1[j+1]
    word1 = ''.join(list1)
    word1 = word1[:(le-1)]
    return word1

a1 = a
b1 = b
i= 0
for let in list(a1):
    if let in list(b1):

        a1 = ''.join(list(a1))
        b1 = ''.join(list(b1))
        a1 = remove_let(a1,let)
        b1 = remove_let(b1,let)

        i = i+1
th = (len(a)-i) + (len(b)-i)


fl = list("FLAMES")
g = fl
def rev(word,p):
    for i in range(p , len(word)-1):
        x = word[p+1:len(word)]
        y = word[0: p]
        g = x + y
        return g
def cancel(li,k):
    l = len(li)
    f = li
    o = k % l
    if  o == 0:
        f = f[:l-1]



    elif (k > l):
        pos = (k%l)-1
        f = rev(f,pos)
    elif (k == 0):
        f = f[1:l]

    else:
        f = rev(f,k-1)



    return f

for i in  range(6):

    if(len(g)>1):
        g = cancel(g,th)
     
t = str(datetime.datetime.now())
print t
#gs = str(g)
#info='\n' + a + '---' + b +'---' + t + '---' + gs
#file = open("C:/nltk/names1.dat",'a')
#file.write(info)
#file.close()   

        
        
'''user_doc = {
"user name" : a,
"Lover name" : b,
"result" : g,
"Time" : t,

}
db.flames.insert(user_doc)
print "success"'''
g = str(g)
if(g[2]=='L'):
    print "This Proves that you guys are really loving each other"
    
elif(g[2]=='M'):
    print("Happy Marriage Life guys")
elif(g[2]=='E'):
    print("You guys were tough enemies to each other")
elif(g[2]=='S'):
	print "You are brothers and sisters"
elif(g[2]=='A'):
	print "The thing between you two guys is just affection"
elif(g[2]=='F'):
	print "You are really good friends"
