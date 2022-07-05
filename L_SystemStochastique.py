import turtle as tr
import random
import math

class Pile:
	def __init__(self):
		self.pile = []

	def depile(self):
		return self.pile.pop(len(self.pile)-1)

	def empile(self, elt):
		self.pile.append(elt)


class Systeme:
	"""
	attributs:
		params : rassemble les parametres de notre lsystem(variables et constantes)
		axiomeDepart : base de depart
		R : regles d'evolution

	fonction :
		trace : genere sans affichage la suite definnissant notre L-system
		traceGraphique : lecture et affichage du systeme
	"""

	def __init__(self, params, axiomeDepart, R): #V : variables; C : symboles constants; axiomeDepart : base; R : règles de croissance
		self.params = params
		self.axiomeDepart = axiomeDepart
		self.R = R

	def trace(self, gen):
		resultPrecedent = self.axiomeDepart
		for i in range(gen):
			result = ""
			for carac in resultPrecedent:
				if(self.R.get(carac) != None):
					if(type(self.R.get(carac)) == type([])):	#Si il y a plusieurs possibilites pour ce parametre
						if(random.randint(0, 100) < self.R.get(carac)[2]):	#Choix avec le 3eme elt de la liste de possibilites
							result += self.R.get(carac)[0]
						else:
							result += self.R.get(carac)[1]

					elif(self.R.get(carac) == 'F'):	#Si le carac est F
						result += self.R.get(carac)*random.random(0.75, 1.25)
					else:
						result += self.R.get(carac)
				
				else:
					result += carac
			resultPrecedent = result

		self.traceGraphique(result)
		print(result)

	def traceGraphique(self, result):	#Tourne tjrs a gauche
		pilePositions = Pile()
		for carac in result:
			if(self.params.get(carac)):
				if(carac == 'X'):
					self.traceFeuille(self.params.get(carac))
				elif(carac == 'F'):
					tr.fd(self.params.get(carac))
				elif(carac == '+' or carac == '-'):
					tr.left(random.uniform(self.params.get(carac)[0], self.params.get(carac)[1]))

			elif(carac == "["):		#On utilise une pile pour retenir les positions de la tortue
				pilePositions.empile([tr.pos(), tr.heading()])
			elif(carac == "]"):
				tr.up()
				donneesTortues = pilePositions.depile()
				tr.goto(donneesTortues[0])
				tr.setheading(donneesTortues[1])
				tr.down()

	def traceFeuille(self, param):	#Trace une feuille simple
		a = 30
		tr.up()
		tr.colormode(255)
		tr.fillcolor((0,153,51))
		tr.begin_fill()
		tr.left(a)
		tr.fd(param/2)
		tr.right(a)
		tr.fd(param)
		tr.right(180-a)
		tr.fd(param/2)
		tr.right(a)
		tr.fd(param)
		tr.right(a)
		tr.fd(param/2)
		tr.end_fill()
		tr.down()


tr.pensize(1.2)
tr.speed(0)
tr.left(90)
tr.goto(0,-250)

planteSimple = Systeme({'X' : 15, 'F' : 20, '+' : [50*math.pi/12, 50*5*math.pi/36], '-' : [-50*math.pi/12, -50*5*math.pi/36]}, "X", {'X' : ["F[[-X][+X]]F[+FX]-X", "F[[-X][+X]]F[+FX]+X", 50], 'F' : "FF"})	#X represente un bourgeon, dans R : 3eme = proba
planteSimple.trace(4)


tr.exitonclick()