def encreptionByPolySubstitution(plaintext):
    alpha ="abcdefghijklmnopqrstuvwxyz"
    alpha_l=list(alpha)
    #print(alpha_l)
    plain_l=list(plaintext)
    
    n=4
    key=[3,5,-5,-3]
    cipher=[""]
    
    for i in range (0,(len(plain_l)-1),n) :
        c=0
        while c+i < len(plain_l) :
            cipher.append(alpha_l[((alpha_l.index(plain_l[i+c]))+key[c])%26])
            c=c+1
            if c==4 :
                break 
        
        
    #print(cipher)
    return "".join(cipher) 

#_____________________________________________________________#

plaintext ="helloworld"

ciphertext=encreptionByPolySubstitution(plaintext)

print(ciphertext)
