# coding: utf-8
import os
import os.path
import codecs
import json
#----------------------------------------------------------
class Database_cl(object):
#----------------------------------------------------------
# da es hier nur darum geht, die Daten dauerhaft zu speichern,
#wird ein sehr einfacher Ansatz verwendet:
#- es können Daten zu genau 15 Teams gespeichert werden
#- je Team werden 2 Teilnehmer mit Namen, Vornamen und Matrikelnummer
#berücksichtigt
#SOWIE ALS Ergänzung: Semesterzahl!
#- die Daten werden als eine JSON-Datei abgelegt
    #-------------------------------------------------------
    def __init__(self):
    #-------------------------------------------------------
        self.data_o = None
    #-------------------------------------------------------
    
    # EOF    