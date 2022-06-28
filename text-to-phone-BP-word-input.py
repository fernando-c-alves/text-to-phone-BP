# -*- coding: utf-8 -*-
#from string import maketrans  #[old]Required to call maketrans function. This was for Python 2.7

intab = '\xe3\xf5\xea\xf4\xe1\xe9\xed\xf3\xfa\xe7\xe2\xe0'
outtab = "1234567890;$"
#trantab = maketrans(intab, outtab) [old] revised below for Python 3

trantab = str.maketrans(intab, outtab)

# -*- coding: utf-8 -*-

#word = raw_input('Informe uma palavra: ') [old]in Python 3, raw_input() is replaced by input()
word = input('Informe uma palavra: ')
wordt = word.translate(trantab)

##wordu = word.decode('utf-8').encode('cp1252')

## specify the unicodes for the phones of nasalised vowels, vowels, and other special symbols

atil = u'\u00e3'
etil = 'e' u'\u0303'
itil = 'i' u'\u0303'
otil = 'o' u'\u0303'
util = 'u' u'\u0303'

ebaixo = u'\u025b'
obaixo = u'\u0254'
schwa = u'\u0259'

sh = u'\u0283'  ## som de xícara
jj = u'\u0292'  ##som de jaca
nh = u'\u0272'
lh = u'\u028E'
tepe = u'\u027E'

## turn the string word into a list

ww = list(wordt)
pt = []
itenum = 0
## for every item in the list assign a phone according to their distribution and phonological patterns, and add the phone to a new list

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
        if ww[itenum + 1] == 'm' or ww[itenum + 1] == 'n':
            pt.append(atil)
        else:
            pt.append('a')

    if item == '$':
        pt.append('a')

    ## Second module: vowels

    if item == 'a':  ##it's still wrong
        if itenum < len(ww) - 1:
            if itenum == 0 and len(ww) == 3:  ## a + m or n (word initial)
                if ww[itenum + 1] == 'm' or ww[ww.index(item) + 1] == 'n':
                    pt.append(atil)
                else:
                    pt.append('a')
            elif itenum + 1 == len(ww) - 1:  ## a + m or n (word final)
                if ww[itenum + 1] == 'm' or ww[itenum + 1] == 'n':
                    pt.append(atil)
                    pt.append('u')
                else:
                    pt.append('a')
            elif ww[itenum + 1] == 'm' or ww[itenum + 1] == 'n':  ## a + m or n (nasals as codas or onsets?)
                if ww[itenum + 2] == 'a' or ww[itenum + 2] == 'e' or ww[itenum + 2] == 'i' or ww[itenum + 2] == 'o' or \
                        ww[itenum + 2] == 'u':
                    pt.append('a')
                else:
                    pt.append(atil)
            else:
                pt.append('a')
        else:
            pt.append(schwa)

    if item == 'e':

        if itenum < len(ww) - 1:
            if itenum == 0 and len(ww) == 3:  ## a + m or n (word initial)
                if ww[itenum + 1] == 'm' or ww[ww.index(item) + 1] == 'n':
                    pt.append(etil)
                else:
                    pt.append('e')
            if itenum + 1 == len(ww) - 1:  ## a + m or n (word final)
                if ww[itenum + 1] == 'm' or ww[itenum + 1] == 'n':
                    pt.append(etil + 'j')

                elif ww[itenum + 1] == 's':
                    pt.append('i')
                else:
                    pt.append('e')
            elif ww[itenum + 1] == 'a':  ## gllide for 'e' in 'ea'
                pt.append('j')
            elif ww[itenum + 1] == 'm' or ww[itenum + 1] == 'n':  ## a + m or n (nasals as codas or onsets?)
                if ww[itenum + 2] == 'a' or ww[itenum + 2] == 'e' or ww[itenum + 2] == 'i' or ww[itenum + 2] == 'o' or \
                        ww[itenum + 2] == 'u':
                    pt.append('e')
                else:
                    pt.append(etil)

            else:
                pt.append('e')
        else:
            pt.append('i')

    if item == "i":
        if itenum < len(ww) - 1:
            ww.append(
                '\n')  ##just to evaluate the diphthongs safely i.e. without assessing the last letter of ww instead
            if ww[itenum - 1] == 'e' or ww[itenum - 1] == 'a' or ww[itenum - 1] == 'o':
                pt.append('j')

            else:
                ww.remove('\n')
                if itenum == 0 and len(ww) == 3:  ## i + m or n (word initial)
                    if ww[itenum + 1] == 'm' or ww[ww.index(item) + 1] == 'n':
                        pt.append(itil)
                    else:
                        pt.append('i')
                elif itenum + 1 == len(ww) - 1:  ## i + m or n (word final)
                    if ww[itenum + 1] == 'm' or ww[itenum + 1] == 'n':
                        pt.append(itil)
                    else:
                        pt.append('i')
                else:
                    if ww[itenum + 1] == 'm' or ww[itenum + 1] == 'n':  ## i + m or n (nasals as codas or onsets?)
                        if ww[itenum + 2] == 'a' or ww[itenum + 2] == 'e' or ww[itenum + 2] == 'i' or ww[
                            itenum + 2] == 'o' or ww[itenum + 2] == 'u':
                            pt.append('i')
                        else:
                            pt.append(itil)
                    else:
                        pt.append('i')

        else:  ##word final
            if ww[itenum - 1] == 'e' or ww[itenum - 1] == 'a' or ww[itenum - 1] == 'o':
                pt.append('j')
            else:
                pt.append('i')
    if item == 'o':

        if itenum < len(ww) - 1:
            if itenum == 0 and len(ww) == 3:  ## a + m or n (word initial)
                if ww[itenum + 1] == 'm' or ww[ww.index(item) + 1] == 'n':
                    pt.append(otil)
                else:
                    pt.append('o')
            if itenum + 1 == len(ww) - 1:  ## a + m or n (word final)
                if ww[itenum + 1] == 'm' or ww[itenum + 1] == 'n':
                    pt.append(otil)
                elif ww[itenum + 1] == 's':
                    pt.append('u')
                else:
                    pt.append('o')
            elif ww[itenum + 1] == 'm' or ww[itenum + 1] == 'n':  ## a + m or n (nasals as codas or onsets?)
                if ww[itenum + 2] == 'a' or ww[itenum + 2] == 'e' or ww[itenum + 2] == 'i' or ww[itenum + 2] == 'o' or \
                        ww[itenum + 2] == 'u':
                    pt.append('o')
                else:
                    pt.append(otil)

            else:
                pt.append('o')
        else:
            pt.append('u')

    if item == "u":
        if itenum < len(ww) - 1:
            if ww[itenum - 1] == 'e' or ww[itenum - 1] == 'a' or ww[itenum - 1] == 'o':
                pt.append('w')
            else:
                if itenum == 0 and len(ww) == 3:  ## i + m or n (word initial)
                    if ww[itenum + 1] == 'm' or ww[ww.index(item) + 1] == 'n':
                        pt.append(util)
                    else:
                        pt.append('u')
                elif itenum + 1 == len(ww) - 1:  ## i + m or n (word final)
                    if ww[itenum + 1] == 'm' or ww[itenum + 1] == 'n':
                        pt.append(util)
                    else:
                        pt.append('u')
                elif ww[itenum + 1] == 'm' or ww[itenum + 1] == 'n':  ## i + m or n (nasals as codas or onsets?)
                    if ww[itenum + 2] == 'a' or ww[itenum + 2] == 'e' or ww[itenum + 2] == 'i' or ww[
                        itenum + 2] == 'o' or ww[itenum + 2] == 'u':
                        pt.append('u')
                    else:
                        pt.append(util)

                else:
                    pt.append('u')

                if ww[itenum + 1] == 'e' and ww[itenum - 1] == 'g':  ## if statement to account for 'gu' + e
                    del pt[-1]
                if ww[itenum + 1] == '3' and ww[itenum - 1] == 'g':  ## if statement to account for 'gu' + ê
                    del pt[-1]
                if ww[itenum + 1] == 'i' and ww[itenum - 1] == 'g':
                    del pt[-1]
                if ww[itenum + 1] == 'a' and ww[itenum - 1] == 'g':
                    del pt[-1]
                    pt.append('w')

                if ww[itenum + 1] == 'e' and ww[itenum - 1] == 'q':  ## if statement to account for 'qu' + e
                    del pt[-1]
                if ww[itenum + 1] == 'i' and ww[itenum - 1] == 'q':  ## if statement to account for 'qu' + e
                    del pt[-1]
                if ww[itenum + 1] == 'a' and ww[itenum - 1] == 'q':
                    del pt[-1]
                    pt.append('w')
                if ww[itenum + 1] == ';' and ww[itenum - 1] == 'q':
                    del pt[-1]
                    pt.append('w')
                if ww[itenum + 1] == 'o' and ww[itenum - 1] == 'q':
                    del pt[-1]
                    pt.append('w')




        else:  ##word final
            if ww[itenum - 1] == 'e' or ww[itenum - 1] == 'a' or ww[itenum - 1] == 'o':
                pt.append('w')
            else:
                pt.append('u')

    ## Third module: consonants

    if item == 'b':
        if ww[itenum + 1] == 'p' or ww[itenum + 1] == 't' or \
                ww[itenum + 1] == 'd' or \
                ww[itenum + 1] == 'n' or \
                ww[itenum + 1] == 's' or \
                ww[itenum + 1] == 'z' or \
                ww[itenum + 1] == 'x' or \
                ww[itenum + 1] == 'm' or \
                ww[itenum + 1] == 'k' or \
                ww[itenum + 1] == 'u’\u0292’' or \
                ww[itenum + 1] == 'v' or \
                ww[itenum + 1] == 'l':
            pt.append('bi')

        else:
            pt.append('b')

    if item == 'c':

        if ww[itenum + 1] == 't' or ww[itenum + 1] == 's' or ww[itenum + 1] == 'n':
            pt.append('ki')
        elif ww[itenum + 1] == 'h':
            pt.append(sh)
        elif ww[itenum + 1] == 'e' or ww[itenum + 1] == 'i' or ww[itenum + 1] == '6':
            pt.append('s')
        else:
            pt.append('k')

        if ww[itenum - 1] == 's' and ww[
            itenum + 1] == 'e':  ## it accounts for 'sc' without breaking 'scl' as in 'escleróse'
            pass

    if item == '0':
        pt.append('s')
        if ww[itenum - 1] == 's':  ## it accounts for 'sç'
            del pt[-1]

    if item == 'd':
        if ww[itenum + 1] == 'm' or ww[itenum + 1] == 'v' or ww[itenum + 1] == jj:
            pt.append('di')
        else:
            pt.append('d')

    if item == 'f':
        if ww[itenum + 1] == 't':
            pt.append('fi')
        else:
            pt.append('f')

    if item == 'g':
        if ww[itenum + 1] == 'm' or ww[itenum + 1] == 'n':
            pt.append('gi')
        elif ww[itenum + 1] == 'e' or ww[itenum + 1] == 'i' or ww[itenum + 1] == '3':
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
        if itenum < len(ww) - 1:
            if ww[itenum + 1] == 'a' or ww[itenum + 1] == 'e' or ww[itenum + 1] == 'i' or ww[itenum + 1] == 'o' or ww[
                itenum + 1] == 'u' \
                    or ww[itenum + 1] == '1' or ww[itenum + 1] == '2' or ww[itenum + 1] == '3' or ww[
                itenum + 1] == '4' or ww[itenum + 1] == '5' \
                    or ww[itenum + 1] == '6' or ww[itenum + 1] == '7' or ww[itenum + 1] == '8' or ww[itenum + 1] == '9':
                pt.append('l')
            elif ww[itenum + 1] == 'h':
                pt.append(lh)
            else:
                pt.append('w')
        else:
            pt.append('w')

    if item == 'm':
        if itenum < len(ww) - 1:
            if ww[itenum + 1] == 'a' or ww[itenum + 1] == 'e' or ww[itenum + 1] == 'i' or ww[itenum + 1] == 'o' or ww[
                itenum + 1] == 'u' \
                    or ww[itenum + 1] == '1' or ww[itenum + 1] == '2' or ww[itenum + 1] == '3' or ww[
                itenum + 1] == '4' or ww[itenum + 1] == '5' \
                    or ww[itenum + 1] == '6' or ww[itenum + 1] == '7' or ww[itenum + 1] == '8' or ww[itenum + 1] == '9':
                pt.append('m')
            else:
                pass
        else:
            pass

    if item == 'n':

        if itenum < len(ww) - 1:
            if ww[itenum + 1] == 'h':
                pt.append(nh)
            elif itenum < len(ww) - 1:
                if ww[itenum + 1] == 'a' or ww[itenum + 1] == 'e' or ww[itenum + 1] == 'i' or ww[itenum + 1] == 'o' or \
                        ww[itenum + 1] == 'u' \
                        or ww[itenum + 1] == '1' or ww[itenum + 1] == '2' or ww[itenum + 1] == '3' or ww[
                    itenum + 1] == '4' or ww[itenum + 1] == '5' \
                        or ww[itenum + 1] == '6' or ww[itenum + 1] == '7' or ww[itenum + 1] == '8' or ww[
                    itenum + 1] == '9':
                    pt.append('n')
                else:
                    pass
        else:
            pass
    if item == 'p':
        if ww[itenum + 1] == 't' or ww[itenum + 1] == 's':
            pt.append('pi')

        elif ww[itenum + 1] == 'h':
            pt.append('f')

        else:
            pt.append('p')

    if item == 'q':
        pt.append('k')

    if item == 'r':
        if itenum < len(ww) - 1:
            if itenum == 0:
                pt.append('h')
            elif ww[itenum + 1] == 'r':
                pt.append('h')
            elif ww[itenum - 1] == 'n':
                pt.append('h')
            elif ww[itenum + 1] == 'a' or ww[itenum + 1] == 'e' or ww[itenum + 1] == 'i' or ww[itenum + 1] == 'o' or ww[
                itenum + 1] == 'u' \
                    or ww[itenum + 1] == '1' or ww[itenum + 1] == '2' or ww[itenum + 1] == '3' or ww[
                itenum + 1] == '4' or ww[itenum + 1] == '5' \
                    or ww[itenum + 1] == '6' or ww[itenum + 1] == '7' or ww[itenum + 1] == '8' or ww[itenum + 1] == '9':
                pt.append(tepe)

            else:
                pt.append('h')
        else:
            pt.append('h')

        if ww[itenum - 1] == 'r':
            del pt[-1]

    if item == 's':
        if itenum < len(ww) - 1:
            if itenum == 0:
                pt.append('s')
            elif ww[itenum + 1] == 't':
                pt.append(sh)
            elif ww[itenum + 1] == 'd' or ww[itenum + 1] == 'n':
                pt.append(jj)
            elif ww[itenum + 1] == 'b' or ww[itenum + 1] == 'g' or ww[itenum + 1] == 'm' or ww[itenum + 1] == 'l' or ww[
                itenum + 1] == 'v':  ## assimilation of voicing
                pt.append('z')
            elif ww[itenum + 1] == 'a' or ww[itenum + 1] == 'e' or ww[itenum + 1] == 'i' or ww[itenum + 1] == 'o' or ww[
                itenum + 1] == 'u' \
                    or ww[itenum + 1] == '1' or ww[itenum + 1] == '2' or ww[itenum + 1] == '3' or ww[
                itenum + 1] == '4' or ww[itenum + 1] == '5' \
                    or ww[itenum + 1] == '6' or ww[itenum + 1] == '7' or ww[itenum + 1] == '8' or ww[itenum + 1] == '9':
                if ww[itenum - 1] == 'a' or ww[itenum - 1] == 'e' or ww[itenum - 1] == 'i' or ww[itenum - 1] == 'o' or \
                        ww[itenum - 1] == 'u' \
                        or ww[itenum - 1] == '1' or ww[itenum - 1] == '2' or ww[itenum - 1] == '3' or ww[
                    itenum - 1] == '4' or ww[itenum - 1] == '5' \
                        or ww[itenum - 1] == '6' or ww[itenum - 1] == '7' or ww[itenum - 1] == '8' or ww[
                    itenum - 1] == '9':
                    pt.append('z')
                else:
                    pt.append('s')
            elif ww[itenum + 1] == 'e' and itenum + 1 == len(ww) - 1:
                pt.append('z')
            else:
                pt.append('s')
            if ww[
                itenum - 1] == 's':  ##and ww[itenum-1] != ww[len(ww)-1]: ## this line accounts for 'ss' by following the same method used for 'gu' and 'qu'
                del pt[
                    -1]  ## 20/10/2016 the second sentence in the conjunction is to avoid deleting in words that beging and end with s, but it's unecessary since 'ss' doesn't occur in the begining of words, so I commented it out.
        else:
            pt.append('s')

    if item == 't':
        if ww[itenum + 1] == 'm':
            pt.append('ti')
        else:
            pt.append('t')

    if item == 'v':
        pt.append('v')

    if item == 'w':
        pt.append('w')

    if item == 'x':
        if itenum == 0:
            pt.append(sh)
        else:

            if ww[itenum - 1] == 'n':
                pt.append(sh)
            elif ww[itenum - 1] == 'i':
                pt.append(sh)
            elif ww[itenum + 1] == 't':
                pt.append(sh)
            elif ww[itenum + 1] == '7':
                pt.append('z')
            elif ww[itenum + 1] == 'c':
                pt.append('s')
            elif ww[itenum + 1] == 'i':
                if ww[itenum - 1] == 'o' or ww[itenum - 1] == '8':
                    pt.append('s')
            else:
                pt.append('z')

    if item == 'y':
        pt.append('i')

    if item == 'z':
        if itenum == len(ww) - 1:
            pt.append('s')
        else:
            pt.append('z')

    ##module 4: hyphen

    if item == '-':
        pass

    itenum += 1

if len(pt) > 1:  ## ad hoc solution for repeated vowels in the beginning of words
    if pt[0] == pt[1]:
        del pt[0]

if pt[0] == 'j':  ## ad hoc solution for diphthong evaluation of vowels in the beginning of words ww[itenum-1]...
    pt[0] = 'i'

if pt[0] == 'w':
    pt[0] = 'u'

print(''.join(pt))