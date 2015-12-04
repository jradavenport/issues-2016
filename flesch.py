# flesch.py

# test sentence
#sentence = "Miles runs the voodoo down."

def to_cv(word):
    """ Convert word to a cv-list.
    Each vowel of word is replaced by a "v" in the cv-list, and each
    non-vowel is replaced by a 'c'.
    """
    cv_list = []
    for ch in word:
        if ch in 'aeiou':
            cv_list.append('v')
        else:
            cv_list.append('c')
    return cv_list

def count_cv(cv):
    """ Count the # of times "c", "v" occur consecutively in cv.
    """
    count = 0
    i = 0
    while i < len(cv) - 1:  # the -1 is important!
        if cv[i] == 'c' and cv[i+1] == 'v':
            count += 1
        i += 1
    return count

def count_vowel_groups(word):
    """ Return the # of vowel-groups in word.
    """
    cv = to_cv(word)
    count = count_cv(cv)
    if cv[0] == 'v':
        count += 1
    return count

def count_syllables_in_word(word):
    vgc = count_vowel_groups(word)
    if vgc == 0:
        return 1
    else:
        return vgc

def count_syllables(text):
    """ Returns total # of syllables in all words of text.
    """
    words = text.split()
    total_syllables = 0
    for w in words:
        total_syllables += count_syllables_in_word(w)
    return total_syllables

def count_sentences(s):
    return s.count('.') + s.count('!') + s.count('?')

def count_words(s):
    return len(s.split())


def summarize(s):
    try:
        text = open(s, 'r').read().lower()
        #print 'Successfully opened ' + s
    except IOError:
        text = s

    # get text stats
    sy_count = count_syllables(text)
    w_count = count_words(text)
    sent_count = count_sentences(text)

    # FRES: Flesch Readability Ease score
    if sent_count == 0:
        sent_count = -99

    fres = 206.876 - 1.015 * (float(w_count)/sent_count) - 84.6 * (float(sy_count)/w_count)

    # Flesch-Kincaid Grade Level
    fkgl = 0.39 * (float(w_count)/sent_count) + 11.8 * (float(sy_count)/w_count) - 11.59

    # print readability report
#    print
## #   print 'Readability report for ' + s

#    print 'Total # syllables: ' + str(sy_count)
#    print 'Total # words: ' + str(w_count)
#    print 'Total # sentences: ' + str(sent_count)
#    print 'Flesch reading ease score (FRES): ' + str(fres)
#    print 'Flesch-Kincaid grade level: ' + str(fkgl)

    #return str(sy_count)+' '+str(w_count)+' '+str(sent_count)+' '+str(fres)+' '+ str(fkgl)
    return (sy_count, w_count, sent_count, fres, fkgl)
