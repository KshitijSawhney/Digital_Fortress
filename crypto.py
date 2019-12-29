from tabularecta import *
#import receiver
'''this program works by creating a rotating cleartext function to encode a string and the dercrypt it'''
class encrypter:
        @staticmethod
        def encryptonator(x,key,user):
                spaces=''
                #making keypri
                keyp=''
                keypri=''
                for i in key:
                        keyp+=i+' '
                keyp=keyp.split()
                keyp.reverse()                                
                for i in keyp:
                        keypri+=i
                #spaces more than one
                if x.count(' ')==1:
                        x+=' '
                #space calculator
                for i in range(len(x)):
                        if x[i]==' ':
                                spaces+=((str(i))+' ')
                #key cannot  have spaces
                keya=key.split()
                for i in keya:
                        key+=i
                # string entered cannot have spaces
                l=''
                for i in x:
                        if i is not ' ':
                                l+=i
                #making sure x is a proper length
                while len(l)%5!=0:
                                l+='q'
                #making sure the elements are of proper lengths      
                clear=''
                for i in range(len(l)):
                        if i%5==0:
                                clear+=' '+l[i]
                        else:
                                clear+=l[i]
                clear=clear.split()
                #creating the rotation of cleartext
                blur=''
                for i in range(5):
                        for j in range(len(clear)):
                                blur+=clear[j][i]
                        blur+=' '
                # converting blur into a single string
                blurrer=''
                for i in blur:                  
                    if i!=' ':                                  
                        blurrer+=i                               
                blur=blurrer
                #making keys
                keyf=''
                for i in range(len(blur)):
                        if i<len(key):
                                keyf+=key[i]
                        else:
                                x=i%len(key)
                                keyf+=key[x]
                #finding intersections and final
                crypt=''
                for b in keyf:
                        for a in tabularecta:
                                if a==b:
                                        for k in blur:
                                                count=0
                                                for l in lister:
                                                        if k==l:
                                                                crypt += tabularecta[a][count]
                                                        else:
                                                                count+=1
                        else:
                                crypt+='  '
                crypt=crypt.split()[0]                                                
                tobewritten= crypt+' '+keypri+' '+spaces+'\n'
                written= user+' says '+tobewritten
                return written
#####################################
        @staticmethod
        def decryptonator(inco):

                crypted=inco.split()
                spaces=crypted[2:]
                key=crypted[1]
                crypted=crypted[0]
                #reversing key
                keyf=''
                for i in key:
                        keyf+=i+' '
                keyf=(keyf.split())
                keyf.reverse()
                key=''
                for i in keyf:
                        key+=i
                #making keyf of appropriate length
                keyf=''
                for i in range(len(crypted)):
                        if i<len(key):
                                keyf+=key[i]
                        else:
                                x=i%len(key)
                                keyf+=key[x]
        #finding intersections
                buff=''
                for i in keyf:
                        for j in tabularecta:
                                if i ==j:
                                        for k in crypted:
                                                count = 0
                                                for l in tabularecta[j]:
                                                        if l!=k:
                                                                count+=1
                                                        else:
                                                                buff+=lister[count]
                        else:
                                buff+=' '
                buff=buff.split()[0]
                final=''
                x=len(buff)/5
                for i in range(len(buff)):
                        try:
                                if i%x!=0:
                                        final+=buff[i]
                                else:
                                        final+=' '+buff[i]
                        except:
                                final+=' '+buff[i]
                final=final.split()
                xjl=''
                for i in range(len(final[0])):
                        for j in final:
                                xjl+=j[i]
                final=''
                for i in range(len(xjl)):
                        if i<len(xjl)-4:
                                final+=xjl[i]
                        else:
                                if xjl[i]=='q':
                                        break
                                else:
                                        final+=xjl[i]
                tempo=[]
                for i in final:
                        tempo.append(i)
                final=tempo
        #spaces
                for ji in spaces:
                        ji=int(ji)
                        final.insert(ji,' ')
                f=''
                for i in final:
                        f+=i
                final=f
                return final
obj=encrypter()
def encrypt(x,key,user):
        mess=obj.encryptonator(x,key,user)
        return mess
def decrypt(inco):
        z=obj.decryptonator(inco)
        return z
