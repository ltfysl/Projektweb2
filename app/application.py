# coding: utf-8
import cherrypy
import sys, json
import string
from mako.template import Template
#--------------------------------------
class Application_cl(object):
#--------------------------------------
    #----------------------------------
    def __init__(self):
        #--------------------------------------
        # constructor
        pass
    @cherrypy.expose

    #--------------------------------------
    def loginEmail(self, email):
    #--------------------------------------
        # try catch einbauen
        lehrendePersonen = open('./data/Lehrender.json', 'r')
        lehrendeJSON = json.load(lehrendePersonen)
        lehrendePersonen.close()

        studiengange = open('./data/Studiengang.json', 'r')
        studiengangeJSON = json.load(studiengange)
        studiengange.close()

        # Stringfunktion email zerlegen und vergleichen und auf Studiengangliste verweisen
        str1 = email
        if str1.find("stud.hn.de") > 0:
            return Template(filename = "./content/student.tpl").render(studiengange = studiengangeJSON)

        for lehrender in lehrendeJSON:
            if (lehrender["email"] == email):
                exists = 0
                break
            else:
                exists = 1

        if (exists == 0):
            return self.loginPassword(email)
        else:
            raise cherrypy.HTTPRedirect('/')

    @cherrypy.expose

    #--------------------------------------
    def loginPassword(self, email):
    #--------------------------------------
        return Template(filename = './content/loginPassword.tpl').render(email = email)
    @cherrypy.expose

    #--------------------------------------
    def loginSubmitPassword(self, email, password):
    #--------------------------------------
        lehrendePersonen = open('./data/Lehrender.json', 'r')
        lehrendeJSON = json.load(lehrendePersonen)
        lehrendePersonen.close()

        module = open('./data/Modul.json', 'r')
        moduleJSON = json.load(module)
        module.close()

        studiengange = open('./data/Studiengang.json', 'r')
        studiengangeJSON = json.load(studiengange)
        studiengange.close()

        modulRolle = 0
        studiengangRolle = 0

        for lehrender in lehrendeJSON:
            if (lehrender["email"] == email and lehrender["password"] == password):
                
                for modul in moduleJSON:
                    for modulZuweisung in modul["Lehrende"]:
                        if (modulZuweisung == lehrender["email"]):
                            modulRolle = 1
                            break
                        else: 
                            modulRolle = 0

                for studiengang in studiengangeJSON:
                    for studiengangZuweisung in studiengang["Lehrende"]:
                        if (studiengangZuweisung == lehrender["email"]):
                            studiengangRolle = 1
                            break
                        else: 
                            studiengangRolle = 0

                if modulRolle == 1:
                    return self.StudiengangLV()
                elif studiengangRolle == 1:
                    return self.StudiengangModule()

                break

            else:
                # Zur Startseite bei Fehleingabe des Passworts
                redirect = 1

        if (redirect == 1):
            raise cherrypy.HTTPRedirect('/')
    @cherrypy.expose

    #--------------------------------------
    def StudiengangLV(self):
    #--------------------------------------
        studiengange = open('./data/Studiengang.json', 'r')
        studiengangeJSON = json.load(studiengange)
        studiengange.close()

        return Template(filename = "./content/studiengangModule.tpl").render(studiengange = studiengangeJSON)
        return 'studiengangmitLV'
    @cherrypy.expose


    #--------------------------------------
    def StudiengangModule(self):
    #--------------------------------------
        studiengange = open('./data/Studiengang.json', 'r')
        studiengangeJSON = json.load(studiengange)
        studiengange.close()

        return Template(filename = "./content/studiengangLv.tpl").render(studiengange = studiengangeJSON)
        return 'StudiengangModule'
    @cherrypy.expose
    

    #--------------------------------------
    def default(self, *arglist, **kwargs):
        #--------------------------------------
        msg_s = "unbekannte Anforderung: " + \
            str(arglist) + \
            ''+\
            str(kwargs) 
        raise cherrypy.HTTPError(404, msg_s)
# EOF