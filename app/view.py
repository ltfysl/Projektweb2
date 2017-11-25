# coding: utf-8
import os.path
from mako.template import Template
from mako.lookup import TemplateLookup
#----------------------------------------------------------
class View_cl(object):
#----------------------------------------------------------
#-------------------------------------------------------
    def __init__(self, path_spl):
        #-------------------------------------------------------
        # Pfad hier zur Vereinfachung fest vorgeben
        self.path_s = os.path.join(path_spl, "template")
        self.lookup_o = TemplateLookup(directories=self.path_s)
        # ... weitere Methoden
        #-------------------------------------------------------
# EOF       