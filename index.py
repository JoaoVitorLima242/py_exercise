class Professional:
    def __init__(self, name, skill, grade):
        self.name = name
        self.skill = skill
        self.grade = grade

    def showInfo(self):
        return f"{self.name}({self.skill}) - grade: {self.grade}"

class Visitor:
    def __init__(self, name, doc):
        self.name = name
        self.doc = doc

    def showInfo(self):
        return f"{self.name} - DOC: {self.doc}"

class Visit:
    def __init__(self, prof, visitor, date):
        self.prof = prof
        self.visitor = visitor
        self.date = date

    def showInfo(self):
        return f"Profissional: {self.prof.name}\n Visita: {self.visitor.name}\n Data da visita:  {self.date}"
    
def addProf(list):
    while True:
        print('===============================================')
        print('Começou o processo de cadastro do profissional:\n')
        name = input('Digite o nome: ')
        skill = input('Digite a especialidade: ')
        grade = input('Digite o sala: ')

        professional = Professional(name, skill, grade)

        list.append(professional)
        fim = input('Digite fim para acabar o programa: ').lower()
        if fim == 'fim':
            break

def addVisitor(list):
    while True:
        print('===============================================')
        print('Começou o processo de cadastro do visitante:\n')
        name = input('Digite o nome: ')
        doc = input('Digite o documento: ')

        visitor = Visitor(name, doc)

        list.append(visitor)
        fim = input('Digite fim para acabar o programa: ').lower()
        if fim == 'fim':
            break

def addVisit(profList, visitorList, visitList):
    while True:
        print('===============================================')
        print('Começou o processo de cadastro das visitas:\n')
        print('Voce tera que adicionar o professional, o visitante e a data da visita:\n')

        showListInfo(profList)
        profIndex = int(input('Escolha o profissional pelo indice: '))

        showListInfo(visitorList)
        visitorIndex = int(input('Escolha o visitante pelo indice: '))

        prof = profList[profIndex]
        visitor = visitorList[visitorIndex]

        date = input('Digite a data da visita: ')

        visit = Visit(prof, visitor, date)

        visitList.append(visit)

        fim = input('Digite fim para acabar o programa: ').lower()
        if fim == 'fim':
            break

def showListInfo(list):
    for i, item in enumerate(list):
        print(f'{i})', item.showInfo())  

def menu(profList, visitorList, visitList):
    while True:
        print(
        '''
        ======================
        MENU
        ======================
        1- Cadastrar Profissional
        2- Localizar Profissional
        3- Cadastrar Visitante
        4- Registrar Visita
        5- Relatório de Conferência
        '''
    )
        selected = int(input('Escolha: '))
        if selected == 1:
            addProf(profList)
        elif selected == 2:
            showListInfo(profList)
        elif selected == 3:
            addVisitor(visitorList)
        elif selected == 4:
            addVisit(profList, visitorList, visitList)
        elif selected == 5:
            showListInfo(visitList)
            break

profList = []
visitorList = []
visitList = []

menu(profList, visitorList, visitList)
