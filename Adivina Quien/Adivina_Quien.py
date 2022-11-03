import pickle

class Node:
    def __init__(self,nam,qst, grp):
        self.name = nam
        self.question = qst
        self.group = grp
        self.next = None
        self.previous = None
        self.left = None
        self.rigth = None

class LinkedList:
    def __init__(self):
        self.first = None

        source = open('Personajes', 'ab+')
        source.seek(0)

        try:
            self.first = pickle.load(source)
        except EOFError:
            pass
        finally:
            source.close()
            del source

    def add (self,name,question,group):
        if self.first is None:
            new_node = Node(name,question,group)
            self.first = new_node
            self.saveCharacters()
            return

        current = self.first

        while True:
            if current.group != group:
                if current.rigth == None:
                    new_node = Node(name,question,group)
                    new_node.left = current
                    current.rigth = new_node
                    self.saveCharacters()
                    return
                else:
                    current = current.rigth
            else:
                while True:
                    if current.next == None:
                        new_node = Node(name,question,group)
                        new_node.previous = current
                        current.next = new_node
                        self.saveCharacters()
                        break
                    else:
                        current = current.next
                break

    def saveCharacters(self):
        files = open('Personajes', 'wb')
        pickle.dump(self.first, files)
        files.close()
        del files

    def printCharacters(self):
        current = self.first
        while True:
            print('Nombre: ',current.name, '\nGrupo: ',current.group, '\n')
            if current.next == None:
                while current.previous != None:
                    current = current.previous
                if current.rigth != None:
                    current = current.rigth
                else:
                    break
            current = current.next

def Preguntas(current):
    while True:
        if input('Tu personaje pertenece al grupo de '+current.group+'?\n') == 'Si':
            while True:
                if input(current.question+'\n') == 'Si':
                    print('Tu personaje es ', current.name)
                    return(0)
                else:
                    if current.next == None:
                        return(1)
                    else:
                        current = current.next
        else:
            if current.rigth == None:
                return(1)
            else:
                current = current.rigth

def Inicio():
    Characters = LinkedList()

    #Characters.add('Goku','Tu personaje vencio a Freezer en Namek?','Sayain Goku')
    #Characters.printCharacters()

    current = Characters.first

    opc = Preguntas(current)

    if opc == 1:
        print('\nAyudame a agregar un nuevo personaje: ')
        name = input('Nombre: ')
        quest = input('Ingrese una pregunta caracteristica para identificar al personaje: ')
        group = input('Ingrese al grupo al que pertenece: ')
        Characters.add(name, quest, group)
    input()
Inicio()