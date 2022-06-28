# -*- coding: utf-8 -*-
## Important: when reading the lines, the program is taking an empty string to be the last element in 'ww'...
## so for every reference to word final distributions, I have to apply the following change: itenum+1 == len(ww)-1 --> itenum+1 == len(ww)-2
## it happens in two contexts: with vowels, and with consonants that can occupy coda position.
## how to solve it? http://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines

## open the file you wish

# -*- coding: utf-8 -*-
FILE_NAME = '' ##Paste the directory of the file containing the list of words between the ''
f = open(FILE_NAME, 'r')
content = f.readlines()

## turn every line into an element of a list

for line in content:
    # -*- coding: utf-8 -*-
   
    ##from string import maketrans   # Required to call maketrans function. [old] Python 2.7

    intab = '\xe3\xf5\xea\xf4\xe1\xe9\xed\xf3\xfa\xe7\xe2\xe0'
    outtab = "1234567890;$"
    trantab = str.maketrans(intab, outtab) ##added str. for Python 3

    line = line.translate(trantab)  ## this line fixed the super bug of not reading accented characters (what a slip! But living and learning)
    
    ##wordu = word.decode('utf-8').encode('cp1252')
    
    ## specify the unicodes for the phones of nasalised vowels

    atil = u'\u00e3'
    etil = 'e' u'\u0303'
    itil = 'i' u'\u0303'
    otil = 'o' u'\u0303'
    util = 'u' u'\u0303'

    ebaixo = u'\u025b'
    obaixo = u'\u0254'
    schwa = u'\u0259' 

    sh = u'\u0283'
    jj = u'\u0292' ##som de jaca
    nh = u'\u0272'
    lh = u'\u028E' 
    tepe = u'\u027E' 

    dipu = u'\u028A'

    ## turn the string word into a list

    ww = list(line)
    pt = []
    spt = []
    itenum = 0
    
    if ('\n') in ww: ## this line is to avoid the error with the last word
        ww.remove('\n') ## this fixes the second bug by deleting this string from the list, thus allowing word final processes to occur
    
    ## transcribe every element of the list with written words (ww)
    
    for item in ww:
        ##First module: accented vowels
     
        if item == '1':
            pt.append(atil)
    
        if item == '2':
            pt.append(otil)
     
        if item == '3':
            pt.append('e')
            
        if item == '4':
            pt.append(otil)
        if item == '6':
            if itenum < len(ww)-1:
                if ww[itenum+1] == 'm': 
                    pt.append(etil)
                    pt.append('j')
                else:
                    pt.append(ebaixo)
            else:
                pt.append(ebaixo)
        if item == '8':
            pt.append(obaixo)
         
        if item == '5':
            pt.append('a')
     
        if item == '7':
            pt.append('i')
     
        if item == '9':
            pt.append('u')
    
        if item == ';':
            if ww[itenum+1] == 'm' or ww[itenum+1] == 'n':
                pt.append(atil)
            else:
                pt.append('a')
        
        if item == '$': ##20/10/2016 I've added the translation for 'à', which I had previously forgotten.
            pt.append('a')
     
        ## Second module: vowels
     
     
        if item == 'a':  ##it's still wrong
            if itenum < len(ww)-1:
                if itenum+1 == len(ww)-1: ## a + m or n (word final)
                    if  ww[itenum+1] == 'm' or ww[itenum+1] == 'n':
                        pt.append(atil)
                        pt.append('u')
                    else:
                        pt.append('a')
                
                elif itenum+1 <= len(ww)-2: ##20/10/2016 ##this is just one possibility of guaranteeing that there will be at least two more graphemes after <a>.    
                    if ww[itenum+1] == 'm' or ww[itenum+1] == 'n': ## a + m or n (nasals as codas or onsets?)
                        if ww[itenum+2] != 'a' and ww[itenum+2] != 'e' and ww[itenum+2] != 'i' and ww[itenum+2] != 'o' and ww[itenum+2] != 'u'\
                        and ww[itenum+2] != 1 and ww[itenum+2] != 2 and ww[itenum+2] != 3 and ww[itenum+2] != 4 and ww[itenum+2] != 5\
                        and ww[itenum+2] != 6 and ww[itenum+2] != 7 and ww[itenum+2] != 8 and ww[itenum+2] != 9:
                            pt.append(atil)
                        else:
            
                            if len(ww)<=6: ##this avoids the suffix -mente, which doesn't nasalise the preceding vowels               
                                pt.append(atil)
                            else:
                                pt.append('a')
                    else:
                        pt.append('a')
                    
                else: ##this will never be executed
                    pt.append('a')
                        
            else:
                pt.append(schwa)
                
                ##if itenum == 0 and len(ww) == 3: ## a + m or n (word initial)  19/10/2016: I will substitute == for >=
                    ##if ww[itenum+1] == 'm' or ww[ww.index(item)+1] == 'n':
                       ##pt.append(atil)
                    ##else:
                        ##pt.append('a')
                ##elif itenum+1 == len(ww)-1: ## a + m or n (word final)
                    ##if  ww[itenum+1] == 'm' or ww[itenum+1] == 'n':
                        ##pt.append(atil)
                        ##pt.append('u')
                    ##else:
                        ##pt.append('a')
                ##elif ww[itenum+1] == 'm' or ww[itenum+1] == 'n': ## a + m or n (nasals as codas or onsets?)
                    ##if ww[itenum+2] == 'a' or ww[itenum+2] == 'e' or ww[itenum+2] == 'i' or ww[itenum+2] == 'o' or ww[itenum+2] == 'u':
                        ##pt.append('a')
                    ##else:
                        ##pt.append(atil)
                ##else:
                    ##pt.append('a')
            ##else:
                ##pt.append(schwa)       
        
     
    
        if item == 'e':
        
            if itenum < len(ww)-1:
                if itenum == 0 and len(ww) == 3: ## a + m or n (word initial)
                    if ww[itenum+1] == 'm' or ww[ww.index(item)+1] == 'n':
                        pt.append(etil)
                    else:
                        pt.append('e')
                if itenum+1 == len(ww)-1: ## a + m or n (word final)
                    if  ww[itenum+1] == 'm' or ww[itenum+1] == 'n':
                        pt.append(etil)
                        pt.append('j')
                    elif ww[itenum+1] == 's':
                        pt.append('i')
                    else:
                        pt.append('e')
                elif ww[itenum+1] == 'a':  ## gllide for 'e' in 'ea'
                    pt.append('j')
                elif ww[itenum+1] == 'm' or ww[itenum+1] == 'n': ## a + m or n (nasals as codas or onsets?)
                    if ww[itenum+2] == 'a' or ww[itenum+2] == 'e' or ww[itenum+2] == 'i' or ww[itenum+2] == 'o' or ww[itenum+2] == 'u':
                        pt.append('e')
                    else:
                        pt.append(etil)
        
                else:
                    pt.append('e')
            else:
                pt.append('i')
        
     
        if item == "i":
            if itenum < len(ww)-1:
                ww.append('\n') ##just to evaluate the diphthongs safely i.e. without assessing the last letter of ww instead
                if ww[itenum-1] == 'e' or ww[itenum-1] == 'a' or ww[itenum-1] == 'o': 
                        pt.append('j')
                
                else:
                    ww.remove('\n')
                    if itenum == 0 and len(ww) == 3: ## i + m or n (word initial)
                        if ww[itenum+1] == 'm' or ww[ww.index(item)+1] == 'n':
                            pt.append(itil)
                        else:
                            pt.append('i')
                    elif itenum+1 == len(ww)-1: ## i + m or n (word final)
                        if  ww[itenum+1] == 'm' or ww[itenum+1] == 'n':
                            pt.append(itil)
                        else:
                            pt.append('i')
                    else: 
                        if ww[itenum+1] == 'm' or ww[itenum+1] == 'n': ## i + m or n (nasals as codas or onsets?)
                            if ww[itenum+2] == 'a' or ww[itenum+2] == 'e' or ww[itenum+2] == 'i' or ww[itenum+2] == 'o' or ww[itenum+2] == 'u':
                                pt.append('i')
                            else:
                                pt.append(itil)
                        else:
                            pt.append('i')
        
            else: ##word final
                if ww[itenum-1] == 'e' or ww[itenum-1] == 'a' or ww[itenum-1] == 'o':
                    pt.append('j')
                else:
                    pt.append('i')
        if item == 'o':
        
            if itenum < len(ww)-1:
                if itenum == 0 and len(ww) == 3: ## a + m or n (word initial)
                    if ww[itenum+1] == 'm' or ww[ww.index(item)+1] == 'n':
                        pt.append(otil)
                    else:
                        pt.append('o')
                if itenum+1 == len(ww)-1: ## a + m or n (word final)
                    if  ww[itenum+1] == 'm' or ww[itenum+1] == 'n':
                        pt.append(otil)
                    elif ww[itenum+1] == 's':
                        pt.append('u')
                    else:
                        pt.append('o')
                elif ww[itenum+1] == 'm' or ww[itenum+1] == 'n': ## a + m or n (nasals as codas or onsets?)
                    if ww[itenum+2] == 'a' or ww[itenum+2] == 'e' or ww[itenum+2] == 'i' or ww[itenum+2] == 'o' or ww[itenum+2] == 'u':
                        pt.append('o')
                    else:
                        pt.append(otil)
        
                else:
                    pt.append('o')
            else:
                pt.append('u')
     
        if item == "u":
            if itenum < len(ww)-1:
                if ww[itenum-1] == 'e' or ww[itenum-1] == 'a' or ww[itenum-1] == 'o':
                    pt.append('w')
                else:
                    if itenum == 0 and len(ww) == 3: ## i + m or n (word initial)
                        if ww[itenum+1] == 'm' or ww[ww.index(item)+1] == 'n':
                            pt.append(util)
                        else:
                            pt.append('u')
                    elif itenum+1 == len(ww)-1: ## i + m or n (word final)
                        if  ww[itenum+1] == 'm' or ww[itenum+1] == 'n':
                            pt.append(util)
                        else:
                            pt.append('u')
                    elif ww[itenum+1] == 'm' or ww[itenum+1] == 'n': ## i + m or n (nasals as codas or onsets?)
                        if ww[itenum+2] == 'a' or ww[itenum+2] == 'e' or ww[itenum+2] == 'i' or ww[itenum+2] == 'o' or ww[itenum+2] == 'u':
                            pt.append('u')
                        else:
                            pt.append(util)
            
                    else:
                        pt.append('u')
           
                    if ww[itenum+1] == 'e' and ww[itenum-1] == 'g': ## if statement to account for 'gu' + e
                        del pt[-1]
                    if ww[itenum+1] == '3' and ww[itenum-1] == 'g': ## if statement to account for 'gu' + ê
                        del pt[-1]
                    if ww[itenum+1] == 'i' and ww[itenum-1] == 'g':
                        del pt[-1]
                    if ww[itenum+1] == 'a' and ww[itenum-1] == 'g':
                        del pt[-1]
                        pt.append('w')
            
                    if ww[itenum+1] == 'e' and ww[itenum-1] == 'q' : ## if statement to account for 'qu' + e
                        del pt[-1]
                    if ww[itenum+1] == 'i' and ww[itenum-1] == 'q' : ## if statement to account for 'qu' + e
                        del pt[-1]
                    if ww[itenum+1] == 'a' and ww[itenum-1] == 'q':
                        del pt[-1]
                        pt.append('w')
                    if ww[itenum+1] == ';' and ww[itenum-1] == 'q':
                        del pt[-1]
                        pt.append('w')
                    if ww[itenum+1] == 'o' and ww[itenum-1] == 'q':
                        del pt[-1]
                        pt.append('w')
            
            
            else: ##word final
                if ww[itenum-1] == 'e' or ww[itenum-1] == 'a' or ww[itenum-1] == 'o':
                    pt.append(dipu)
                else:
                    pt.append('u')
     
        ## Third module: consonants
     
        if item == 'b':
            if ww[itenum+1] == 'p'or  ww[itenum+1] == 't' or \
            ww[itenum+1] == 'd' or \
            ww[itenum+1] == 'n' or \
            ww[itenum+1] == 's' or \
            ww[itenum+1] == 'z' or \
            ww[itenum+1] == 'x' or \
            ww[itenum+1] == 'm' or \
            ww[itenum+1] == 'k' or \
            ww[itenum+1] == 'u’\u0292’' or \
            ww[itenum+1] == 'v' or \
            ww[itenum+1] == 'l':
                pt.append('bi')
            
            else:
                pt.append('b')
    
    
        if item == 'c':
        
            if ww[itenum+1] == 't' or ww[itenum+1] == 's' or ww[itenum+1] == 'n':
                pt.append('ki')
            elif ww[itenum+1] == 'h':
                pt.append(sh)
            elif ww[itenum+1] == 'e' or ww[itenum+1] == 'i' or ww[itenum+1] == '6':
                pt.append('s')
            else:
                pt.append('k') 
     
            if ww[itenum-1] == 's' and ww[itenum+1] == 'e': ## it accounts for 'sc' without breaking 'scl' as in 'escleróse' (but it deleted 's' in the beginning of centros, for example)
                pass 
     
        if item == '0':
            pt.append('s')
            if ww[itenum-1] == 's':  ## it accounts for 'sç'
              del pt[-1]
    
        if item == 'd':
            if ww[itenum+1] == 'm'or  ww[itenum+1] == 'v' or ww[itenum+1] == jj:
                pt.append('di')
            else:
                pt.append('d')
     
        if item == 'f':
            
            if itenum < len(ww)-1: ##
                if ww[itenum+1] == 't': 
                    pt.append('fi')
                else:
                    pt.append('f')
            
            else: 
                pt.append('fi')
    
        if item == 'g':
            if ww[itenum+1] == 'm' or ww[itenum+1] == 'n':
                pt.append('gi')
            elif ww[itenum+1] == 'e' or ww[itenum+1] == 'i' or ww[itenum+1] == '3':
                pt.append(jj)
            else:
                pt.append('g')
     
        if item == 'h':
            pass
     
        if item == 'j':
            pt.append(jj)
     
        if item == 'k':
            pt.append('k')
     
        if item == 'l':
            if itenum < len(ww)-1:  
                if ww[itenum+1] == 'a' or ww[itenum+1] == 'e' or ww[itenum+1] == 'i' or ww[itenum+1] == 'o' or ww[itenum+1] == 'u'\
                or ww[itenum+1] == '1' or ww[itenum+1] == '2' or ww[itenum+1] == '3' or ww[itenum+1] == '4' or ww[itenum+1] == '5'\
                or ww[itenum+1] == '6' or ww[itenum+1] == '7' or ww[itenum+1] == '8' or ww[itenum+1] == '9':
                    pt.append('l')
                elif ww[itenum+1] == 'h':
                    pt.append(lh)
                else: 
                    pt.append('w')
            else:
                pt.append('w')
         
        if item == 'm':
            if itenum < len(ww)-1:
                if ww[itenum+1] == 'a' or ww[itenum+1] == 'e' or ww[itenum+1] == 'i' or ww[itenum+1] == 'o' or ww[itenum+1] == 'u'\
                or ww[itenum+1] == '1' or ww[itenum+1] == '2' or ww[itenum+1] == '3' or ww[itenum+1] == '4' or ww[itenum+1] == '5'\
                or ww[itenum+1] == '6' or ww[itenum+1] == '7' or ww[itenum+1] == '8' or ww[itenum+1] == '9':
                    pt.append('m')
                else:
                    pass
            else:
                pass
             
        if item == 'n':
            if itenum < len(ww)-1:
                if ww[itenum+1] == 'h':
                    pt.append(nh)
                elif itenum < len(ww)-1:
                    if ww[itenum+1] == 'a' or ww[itenum+1] == 'e' or ww[itenum+1] == 'i' or ww[itenum+1] == 'o' or ww[itenum+1] == 'u'\
                    or ww[itenum+1] == '1' or ww[itenum+1] == '2' or ww[itenum+1] == '3' or ww[itenum+1] == '4' or ww[itenum+1] == '5'\
                    or ww[itenum+1] == '6' or ww[itenum+1] == '7' or ww[itenum+1] == '8' or ww[itenum+1] == '9':
                        pt.append('n')
                    else:
                        pass
            else:
                pass
     
        if item == 'p':
            if ww[itenum+1] == 't'or  ww[itenum+1] == 's':
                pt.append('pi')
         
            elif ww[itenum+1] == 'h':
                pt.append('f')
         
            else:
                pt.append('p')
             
        if item == 'q':
            pt.append('k')  
                          
        if item == 'r':
            if itenum < len(ww)-1:
                if itenum == 0:
                    pt.append('h')
                elif ww[itenum+1] == 'r':
                    pt.append('h')
                elif ww[itenum-1] == 'n':
                    pt.append('h')
                elif ww[itenum+1] == 'a' or ww[itenum+1] == 'e' or ww[itenum+1] == 'i' or ww[itenum+1] == 'o' or ww[itenum+1] == 'u'\
                or ww[itenum+1] == '1' or ww[itenum+1] == '2' or ww[itenum+1] == '3' or ww[itenum+1] == '4' or ww[itenum+1] == '5'\
                or ww[itenum+1] == '6' or ww[itenum+1] == '7' or ww[itenum+1] == '8' or ww[itenum+1] == '9':
                    pt.append(tepe)
                
                else:
                    pt.append('h')
            else:
                pt.append('h')
         
            if ww[itenum-1] == 'r':
                del pt[-1] 
                              
        if item == 's':
            if itenum < len(ww)-1:
                
                if itenum == 0:
                    pt.append('s')
                elif ww[itenum+1] == 't':
                    pt.append(sh)
                elif ww[itenum+1] == 'd' or ww[itenum+1] == 'n':
                    pt.append(jj)
                elif ww[itenum+1] == 'b' or ww[itenum+1] == 'g' or ww[itenum+1] == 'm' or ww[itenum+1] == 'l' or ww[itenum+1] == 'v': ## assimilation of voicing
                        pt.append('z')
                elif ww[itenum+1] == 'a' or ww[itenum+1] == 'e' or ww[itenum+1] == 'i' or ww[itenum+1] == 'o' or ww[itenum+1] == 'u'\
                or ww[itenum+1] == '1' or ww[itenum+1] == '2' or ww[itenum+1] == '3' or ww[itenum+1] == '4' or ww[itenum+1] == '5'\
                or ww[itenum+1] == '6' or ww[itenum+1] == '7' or ww[itenum+1] == '8' or ww[itenum+1] == '9':
                    if ww[itenum-1] == 'a' or ww[itenum-1] == 'e' or ww[itenum-1] == 'i' or ww[itenum-1] == 'o' or ww[itenum-1] == 'u'\
                    or ww[itenum-1] == '1' or ww[itenum-1] == '2' or ww[itenum-1] == '3' or ww[itenum-1] == '4' or ww[itenum-1] == '5'\
                    or ww[itenum-1] == '6' or ww[itenum-1] == '7' or ww[itenum-1] == '8' or ww[itenum-1] == '9':
                        pt.append('z')
                    else:
                        pt.append('s')
                      
                
                elif ww[itenum+1] == 'e' and itenum+1 == len(ww)-1:
                    pt.append('z')
                else:
                    pt.append('s')
                
                if ww[itenum-1] == 's': ##and ww[itenum-1] != ww[len(ww)-1]: ## this line accounts for 'ss' by following the same method used for 'gu' and 'qu'
                    del pt[-1]  ## 20/10/2016 the second sentence in the conjunction is to avoid deleting in words that beging and end with s, but it's unecessary since 'ss' doesn't occur in the begining of words, so I commented it out.
                
            else:
                pt.append('s')
     
        if item == 't':
            
            if itenum < len(ww)-1: ##to avoid getting index out of range for foreign words
                if ww[itenum+1] == 'm':
                    pt.append('ti')                                                                                              
                else:
                    pt.append('t')                                                                                                                                                                           
     
            else:
                pt.append('ti')
     
        if item == 'v':
            pt.append('v')
    
        if item == 'w':
            pt.append('w')
     
        if item == 'x':
            if itenum == 0:
                pt.append(sh)
            else:          
                if ww[itenum-1] == 'n':
                    pt.append(sh)
                elif ww[itenum-1] == 'i':
                    pt.append(sh)
                elif ww[itenum+1] == 't':
                    pt.append(sh)            
                elif ww[itenum+1] == '7':
                    pt.append('z')
                elif ww[itenum+1] == 'c':
                    pt.append('s')
                elif ww[itenum+1] == 'i':
                    if ww[itenum-1] == 'o' or ww[itenum-1] == '8':
                        pt.append('s')
                else:
                    pt.append('z')
             
        if item == 'y':
            pt.append('i')
     
        if item == 'z':
            if itenum == len(ww)-1:
                pt.append('s')
            else:
                pt.append('z')
        ##module 4: hyphen
     
        if item == '-':
            pass
     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        itenum+=1

    if len(pt)>1:  ## ad hoc solution for repeated vowels in the beginning of words
        if pt[0] == pt[1]:
            del pt[0]

    if pt != []:    
        if pt[0] == 'j': ## ad hoc solution for diphthong evaluation of vowels in the beginning of words ww[itenum-1]...
            pt[0] = 'i'

        if pt[0] == 'w':
            pt[0]='u'
    
        
    
    ##print ''.join(pt)
        
    
    
    if ('\n') in pt: ## this line is to avoid the error with the last word
        pt.remove('\n')
    
    ##30/11/2016 I had, for some reason, added an empty space to the spt list after adding each special symbol (which can be seen commented out below)...
    ##...and as a result, the join function being used with an empty string added a second empty space between each symbol...
    ##it turns out that this double space was the cause of the big bug of not generating the output grammar file in the Maxent PL
    ##Now it's solved!!!!!!!!!!! 
    
    
    for i in pt:
        
        if i == 'p':
            spt.append('p')
            ##spt.append('')
        
        if i == 'b':
            spt.append('b')
            ##spt.append('')
        
        if i == 't':
            spt.append('t')
            ##spt.append('')
        
        if i == 'd':
            spt.append('d')
            ##spt.append('')
        
        if i == 'k':
            spt.append('k')
            ##spt.append('')
        
        if i == 'g':
            spt.append('g')
            ##spt.append('')
        
        if i == 'f':
            spt.append('f')
            ##spt.append('')
        
        if i == 'v':
            spt.append('v')
            ##spt.append('')
        
        if i == 's':
            spt.append('s')
            ##spt.append('')
        
        if i == 'z':
            spt.append('z')
            ##spt.append('')
        
        if i == u'\u0283':
            spt.append('x')
            ##spt.append('')
        
        if i == u'\u0292': ## the jaca sound (voiced palatal fricative)
            spt.append('jj')
            ##spt.append('')
        
        if i == 'h':
            spt.append('h')
            ##spt.append('')
        
        if i == 'm':
            spt.append('m')
            ##spt.append('')
        
        if i == 'n':
            spt.append('n')
            ##spt.append('')
        
        if i == u'\u0272': ##nh
            spt.append('nh')
            ##spt.append('')
        
        if i == 'l':
            spt.append('l')
            ##spt.append('')
        
        if i == u'\u028E': ##lh
            spt.append('lh')
            ##spt.append('')
        
        if i == u'\u027E' :
            spt.append('r')
            ##spt.append('')
        
        if i == 'i':
            spt.append('i')
            ##spt.append('')
        
        if i == 'e':
            spt.append('e')
            ##spt.append('')
        
        if i == u'\u025b':  ##open 'e'
            spt.append('ee')
            ##spt.append('')
        
        if i == 'a': 
            spt.append('a')
            ##spt.append('')
        
        if i == u'\u0254': ##open 'o'
            spt.append('oo')
            ##spt.append('')
        
        if i == 'o':
            spt.append('o')
            ##spt.append('')
        
        if i == 'u':
            spt.append('u')
            ##spt.append('')
        
        if i == u'\u028A':
            spt.append('u')
            ##spt.append('')
        
        if i == u'\u00e3':
            spt.append('an')
            ##spt.append('')
        
        if i == 'e' u'\u0303':
            spt.append('en')
            ##spt.append('')
        
        if i == 'i' u'\u0303':
            spt.append('in')
            ##spt.append('')
        
        if i == 'o' u'\u0303':
            spt.append('on')
            ##spt.append('')
        
        if i == 'u' u'\u0303':
            spt.append('un')
            ##spt.append('')
        
        if i == u'\u0259':
            spt.append('q')
            ##spt.append('')
        
        if i == 'w':
            spt.append('w')
            ##spt.append('')
        
        if i == 'j':
            spt.append('j')
            ##spt.append('')
    
    
    ##30/11/2016 following lines were commented out because they were used to delete the last empty space of spt when I wrongly added these
    ##...spaces above instead of just doing it using only join.' '. Now that I commented out those empty spaces it was deleting the last symbol in spt.
    
    ##if len(spt)>0:
        ##del spt[-1]
        
   
    ##adding tab + '2' after each word in spt 20/10
    
    sptf = ' '.join(spt)
    
    print(sptf) #added parentheses for Python 3 syntax of print
    
    
    
    

    
        
    ##print ' '.join(spt)
        