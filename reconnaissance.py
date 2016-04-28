# SHCHERBAKOVA
# ELELWA-NASULI

import difflib
from tkinter import *


MIN_LENGTH = 30

UNKNOWN = 'UNKNOWN'

FRENCH_SPECIAL_CARACTER = ['ç', 'œ', 'î']

SPANISH_SPECIAL_CARACTER = ['ñ','¿','¡']


NAME_MAP = {
    "de" : "Allemand",
    "en" : "Anglais",
    "es" : "Espagnol",
    "fi" : "Finnois",
    "fr" : "Français",
    "it" : "Italien",
    "nl" : "Néerlandais",
    "sv" : "Suédois"
}


def common_words(file, n):
    """On utilise cette fonction pour former le list 'global_list'"""
    with open(file) as f:
        word_list = [word for line in f for word in line.split()]
    word_counter = {}
    for word in word_list:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
    top_words = popular_words[:n]
    return top_words



global_list = [['der', 'mit', 'in', 'den', 'ist', 'und', 'die', 'von', 'im', 'das'],
               ['de', 'el', 'no', 'que', 'en', 'es', 'y', 'a', 'por', 'lo'],
               ['de', 'le', 'des', 'la', 'à', 'les', 'et', 'dans', 'pour', 'une'],
               ['di', 'e', 'non', 'che', 'una', 'per', 'è','mi', 'si', 'ma'],
               ['att', 'i', 'och', 'är', 'på', 'en', 'som', 'vara',  'för', 'det'],
               ['the', 'to', 'and', 'he', 'of', 'in', 'a', 'what', 'or', 'have'],
               ['de','een','en','het', 'dat', 'ik', 'je', 'hij', 'niet', 'wat'],
               ['se', 'ja', 'että', 'mutta', 'joka', 'olla', 'ei', 'on', 'hän', 'ole']]




def check_french(chaine):
    """On verif. si il y a des caracteres 'ç', 'œ', 'î' dans la chaine."""
    b = list(chaine)
    if len([i for i in FRENCH_SPECIAL_CARACTER if i in b]) > 0:
        return True
    else:
        return False

def check_spanish(chaine):
    """On verif. si il y a des caracteres 'ñ','¿','¡' dans la chaine."""
    b = list(chaine)
    if len([i for i in SPANISH_SPECIAL_CARACTER if i in b]) > 0:
        return True
    else:
        return False
    
def _nameOf(iana):
    """input: 'fr' output: 'Français'"""
    return NAME_MAP.get(iana, UNKNOWN)

def short_name(name):
    return (list(NAME_MAP.keys())[list(NAME_MAP.values()).index(name)])


def final_detection(chaine):
    """La fonction finale. Elle prend la chaine comme parametre et renvoie la langue la plus probable d'un texte."""
    assert type(chaine) == str
    chaine = chaine.strip().lower()
    listed = chaine.split()
    word_counter = {}
    for word in listed:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
    top_words = popular_words[:len(global_list[0])]

    _de = difflib.SequenceMatcher(None,global_list[0],top_words)
    de = _de.ratio() * 100
    de_ =  { de : 'Allemand'}
    print (de, '%', _nameOf('de'))

    _es = difflib.SequenceMatcher(None,global_list[1],top_words)
    es = _es.ratio() * 100
    es_ = { es : 'Espagnol'}
    print (es,'%', _nameOf('es'))

    _fr = difflib.SequenceMatcher(None,global_list[2],top_words)
    fr = _fr.ratio() * 100
    fr_ = { fr : 'Français'}
    print (fr,'%', _nameOf('fr'))

    _it = difflib.SequenceMatcher(None,global_list[3],top_words)
    it = _it.ratio() * 100
    it_ = { it : 'Italien'}
    print (it,'%', _nameOf('it'))

    _sv = difflib.SequenceMatcher(None,global_list[4],top_words)
    sv = _sv.ratio() * 100
    sv_ = { sv : 'Suédois'}
    print (sv,'%', _nameOf('sv'))

    _en = difflib.SequenceMatcher(None,global_list[5],top_words)
    en = _en.ratio() * 100
    en_ = { en : 'Anglais'}
    print (en,'%', _nameOf('en'))

    _nl = difflib.SequenceMatcher(None,global_list[6],top_words)
    nl = _nl.ratio() * 100
    nl_ = { nl : 'Néerlandais'}
    print (nl,'%', _nameOf('nl'))

    _fi = difflib.SequenceMatcher(None,global_list[7],top_words)
    fi = _fi.ratio() * 100
    fi_ = { fi : 'Finnois'}
    print (fi,'%', _nameOf('fi'))       

    if len(chaine.split()) < MIN_LENGTH:
        return 'Try with longer text (min 30 words)'
    elif de > it and de > fr and de > es and de > sv and de > en and de > nl and de > fi:
        return _nameOf('de'), de_, fr_, it_, es_, sv_, en_, nl_, fi_
    elif es > de and es > fr and es > it and es > sv and es > en and es > nl and es > fi or check_spanish(chaine) == True:
        return _nameOf('es'), de_, fr_, it_, es_, sv_, en_, nl_, fi_
    elif fr > it and fr > de and fr > es and fr > sv and fr > en and fr > nl and fr > fi or check_french(chaine) == True:
        return _nameOf('fr'), de_, fr_, it_, es_, sv_, en_, nl_, fi_
    elif it > es and it > fr and it > de and it > sv and it > en and it > nl and it > fi:
        return _nameOf('it'), de_, fr_, it_, es_, sv_, en_, nl_, fi_
    elif sv > it and sv > fr and sv > es and sv > de and sv > en and sv > nl and sv > fi:
        return _nameOf('sv'), de_, fr_, it_, es_, sv_, en_, nl_, fi_
    elif en > it and en > fr and en > es and en > sv and en > de and en > nl and en > fi:
        return _nameOf('en'), de_, fr_, it_, es_, sv_, en_, nl_, fi_
    elif nl > it and nl > fr and nl > es and nl > sv and nl > de and nl > en and nl > fi:
        return _nameOf('nl'), de_, fr_, it_, es_, sv_, en_, nl_, fi_
    elif fi > it and fi > fr and fi > es and fi > sv and fi > de and fi > nl and fi > en:
        return _nameOf('fi'), de_, fr_, it_, es_, sv_, en_, nl_, fi_
    elif chaine in {'quit', 'exit'}:
        return    
    else:
        return 'Langue inconnue.'


def main():
    """ Point principal d'entrée du programme: créer les fenetres et coup l'envoi de la boucle d'événements."""
    tk = Tk()
    tk.title("Reconnaissance de langues")
    canvas = Canvas(tk, width=700, height=10, bg='#00cfcf')
    canvas.pack()
    import tkinter.scrolledtext
    text = Text(tk, height=15, width=50, bg='#474747', fg='white')
    text = tkinter.scrolledtext.ScrolledText(tk)
    text.pack()
    

    def process_callback(*args):
    #Callback pour le bouton 'Enter'

        # figure out what the response to the input should be
        response = final_detection(entry.get())

        if response is None:
            tk.quit()
            tk.destroy()
            return

        # write the response
        text.insert(END, '\n{}\n'.format(response))

        # clear the input field
        entry.delete(0, END)
    v = StringVar(tk, value='La longueur minimale du texte est 30 mots')
    entry = Entry(tk, width=65, bd=5, bg = '#f6ffff', textvariable = v, fg="grey")
    
    
    entry.pack()
    entry.pack(ipady = 50)
    entry.focus()
    entry.bind('<Return>', process_callback)
    
    btn = Button(tk, width=50, bd=3, bg='#00cfcf', text='Submit',
                    command=process_callback)
    btn.pack()

    text.insert(END, "              ---*--- La langue la plus probable d’un texte ---*---\n")
    
    tk.mainloop()

if __name__ == '__main__':
    main()

