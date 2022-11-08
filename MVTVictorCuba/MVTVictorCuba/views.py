from django.http import HttpResponse
from django.template import *
from datetime import datetime
from AppCoder.models import *


def ProbandoTemplate(self):

    familiar = Familiar(parentesco ="Papá", nombre= "Andres", apellido ="Cuba", edad=56, fechaNacimiento="1966-09-27")
    familiar.save()

    familiar2 = Familiar(parentesco = "Mamá", nombre = "Sara", apellido = "Larrain", edad = 45, fechaNacimiento ="1977-03-23") 
    familiar2.save()

    familiar3 = Familiar(parentesco = "Hermano", nombre = "Juan Carlos", apellido = "Cuba", edad = 27, fechaNacimiento ="1995-03-05")
    familiar3.save()

    #Abrimos el archivo
    miHtml = open("C:/Users/RUMIMAKI/Desktop/Python-Course/MVTVictorCuba/Plantillas/template.html")

    #Creamos el objeto "Plantilla"
    plantilla = Template(miHtml.read())

    #Cerramos el archivo para liberar recursos
    miHtml.close()

    #Creamos la lista
    familiares = []
    familiares.append(familiar)
    familiares.append(familiar2)
    familiares.append(familiar3)
    #Diccionario con datos para la plantilla
    datos ={"familiares": familiares}

    #Creamos el contexto
    miContexto = Context(datos)

    #Renderizamos la plantilla para crear la respuesta
    documento = plantilla.render(miContexto)

    #Retornamos la respuesta
    return HttpResponse(documento)
