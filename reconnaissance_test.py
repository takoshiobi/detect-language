# SHCHERBAKOVA
# ELELWA-NASULI

import unittest

from test import (short_name, check_spanish, check_french, _nameOf, final_detection, UNKNOWN)

class reco_test(unittest.TestCase):
    def test_final_detection(self):
        tests = [
            ("Hoffenheim gegen Mainz. Julian Nagelsmann ist nun der jüngste Bundesligatrainer, der ein Spiel gewonnen hat. Zwei Versuche hat er nur gebraucht. Gegen die siegesgewohnten Mainzer setzte er auf Offensive. Wir müssen Spiele gewinnen, dazu müssen wir Tore schießen, lautet sein Credo. Klingt irgendwie selbstverständlich, aber Nagelsmann muss diesen Satz so oft, so laut, so schön gesagt haben, dass er wirkte. Gilt auch für seine Taktik. Er brachte alles, was Tore schießen kann. Er stellte den Stürmer Philipp Ochs als linken Verteidiger auf, mit ihm kam Schwung über Außen. Den Stürmer Mark Uth, der in dieser Saison bislang keine Rolle spielte, ließ er vorne in der Mitte ran. Zwei Tore schoss er. Während des Spiels sah man von Nagelsmann Jubelfäuste, danach kokette Blicke in TV-Kameras.", "de", "Allemand"),
            ("Les Innocents ont raflé la première Victoire de la soirée. Déjà récompensé à trois reprises entre 1993 et 1997, le groupe a décroché la Victoire de l'album rock, pour son retour après quinze ans de silence. Désormais réduits à un duo (JP Nataf et Jean-Christophe Urbain)", "fr", "Français"),
            ("En cuanto al público, Alfaya ha apuntado que el festival cuenta con unas 1.300 personas 'Amigos de la Quincena', que realizan una pequeña aportación anual y pueden comprar entradas antes de la venta general, y otros nueve mil a los aficionados guipuzcoanos a la música clásica fieles al festival, entre los que se encuentran también los abonados.", "es", "Espagnol"),
            ("Aiemmat tutkimukset ovat osoittaneet, että lapsen saaminen vanhemmalla iällä kasvattaa lapsen riskiä saada esimerkiksi Downin oireyhtymä tai sairastua myöhemmin Alzheimerin tautiin tai diabetekseen. Maanantaina Population and Development Review -tiedelehdessä julkaistun tutkimuksen perusteella", "fi", "Finnois"),
            ("Chi cerca da una vacanza il giusto compromesso tra storia e natura, sicuramente a rispondere al meglio a tali esigenze è il Perù, un Paese millenario che ha fascino da vendere. Tutti possono catapultarsi in una terra che invita a tornare indietro nel tempo per scoprire da vicino l'eredità culturale degli Incas, abbracciata e nascosta da un territorio selvaggio. Non è un caso che qui si trovano ben 12", "it", "Italien"),
            ("De rechtbank noemde Van U. ernstig ziek en gevaarlijk en vindt dat hij zeer, zeer langdurige tbs nodig heeft.", "nl", "Néerlandais"),
            ("Och faktiskt mer än så. Verket de framför är uppbyggt så att i stort sett alla gör varsitt solo, och hos till exempel Shroof skönjer man rentav 50-talets Miles Davis. von Schlippenbach å sin sida har en förmåga att återkalla ännu äldre jazz, kanske delvis via inspiratören Monks förankring i stridestilen från Harlem men också av egen kraft. Till sin helhet är stycket samtidigt i sådan obeveklig framåtrörelse och liksom uppslukat av sin egen energi att formen för musiken mer eller mindre säger sig själv.", "sv", "Suédois"),
            ("That was then, and this is both then and now: her second volume of collaborative remixes/re-recordings with diverse guests draws its source material from all stages of Ono’s career", "en", "Anglais")
            ]

        for text, name, long in tests:
            self.assertEqual(name, short_name(long))

    def setUp(self):
        pass


if __name__ == '__main__':
    unittest.main()    
            
