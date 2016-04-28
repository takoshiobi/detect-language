# SHCHERBAKOVA
# ELELWA-NASULI

### Reconnaissance de langues


@ Reference : https://github.com/tonythedealer/Projet


########## Comment fonctionne FINAL_DETECTION ##########




Programme utilise l'algorithme "trigrams". Elle forme une liste de mots plus frequents de la chaine d'entrée, et compare cette liste 
avec chaque liste dans variable 'global liste'. 

<!> La longueur minimale du texte est 30 mots. <!>




########## Description plus précise ##########




1. On utilise la fonction common_words(chaine) pour former 'global_list'. On a aussi utilisé Frequency Lists pour l'analyse du texte plus precis.
   Frequency Lists : https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists

2. On a formé global list avec 8 lists (de, fr, nl, sv, ...). La longueur de chaque list est identique. len(global_list[i]) = 10;

3. J'ai fait des fonctions 'check_spanish' et 'check_french' pour verifier si il y a des caracteres uniques dans le texte.

4. La fonction _nameOf renvoie le nom de langue et j'ai fait aussi la fonction short_name pout le UNITTEST.

5. La fonction final_detection renvoie le pourcentage de chaque langue dans le text et elle renvoie aussi la langue la plus probable du texte.



########## Exemple d'utilisation sans Tkinter ##########



final_detection("Yael Naim été sacrée artiste féminine de l'année aux Victoires de la musique au cours d'une cérémonie marquée par l'irrésistible ascension de Louane et l'émotion de William Sheller à qui a été rendu un hommage. Après Christine and The Queens l'an dernier, la Franco-Israélienne a raflé l'un des trophées les plus prestigieux distribués sur la scène du Zénith de Paris, qu'elle avait déjà obtenu en 2011. Une récompense qu'elle doit à son très bel album Older sorti l'an dernier et enregistré, comme d'habitude, avec son compagnon David Donatien.")
0.0 % Allemand
20.0 % Espagnol
40.0 % Français
0.0 % Italien
0.0 % Suédois
10.0 % Anglais
10.0 % Néerlandais
0.0 % Finnois
('Français', {0.0: 'Allemand'}, {40.0: 'Français'}, {0.0: 'Italien'}, {20.0: 'Espagnol'}, {0.0: 'Suédois'}, {10.0: 'Anglais'}, {10.0: 'Néerlandais'}, {0.0: 'Finnois'})



final_detection("He was born in Calgary, Canada, in 1970 but grew up in Texas with his mother, computer programmer Eleanor Cruz, and father Ted Cruz, a Cuban refugee who fled to the US after being imprisoned and tortured in his home country. He attended the University of Texas and later started a seismic-data processing firm for oil drilling. The elder Mr Cruz is now a Christian pastor in Dallas. His son attended two private high schools before studying Public Policy at Princeton University, where he won awards for debating before going to study law at Harvard. Mr Cruz then embarked on a legal career including representing the National Rifle Association in its efforts to impeach President Bill Clinton in the 1990s. He is married with two daughters. Ted Cruz greets his wife Heidi and daughters Caroline (R) and Catherine (C) before taking the stage announce his candidacy for the Republican nomination to run for US President March 23, 2015 What it his career history? He briefly entered politics in 1999 as a domestic policy advisor in George W Bush’s Presidential campaign and aided his legal cases during vote recounts in FloridaHe appears to refer to “religious liberty” only within Christianity, talking about “our faith”.")
10.0 % Allemand
10.0 % Espagnol
0.0 % Français
0.0 % Italien
0.0 % Suédois
50.0 % Anglais
0.0 % Néerlandais
0.0 % Finnois
('Anglais', {10.0: 'Allemand'}, {0.0: 'Français'}, {0.0: 'Italien'}, {10.0: 'Espagnol'}, {0.0: 'Suédois'}, {50.0: 'Anglais'}, {0.0: 'Néerlandais'}, {0.0: 'Finnois'})


########## TESTING : UNITTEST ##########

>>> reconnaissance_test.py


########## INTERFACE ##########

Tkinter. 

from Tkinter import * 








