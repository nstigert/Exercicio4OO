class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome

class Professor(Pessoa):
    def __init__(self, nome, departamento):
        super().__init__(nome)
        self._departamento = departamento

class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self._matricula = matricula

class Disciplina:
    def __init__(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome

class Turma:
    def __init__(self, codTurma, professor, disciplina):
        self._codTurma = codTurma
        self._professor = professor
        self._disciplina = disciplina
        self._alunos = []

    def adicionarAluno(self, aluno):
        self._alunos.append(aluno)

    def getNomeTodosAlunos(self):
        for aluno in self._alunos:
            print(aluno.getNome())

    def getNomeProfessor(self):
        return self._professor.getNome()

    def getnomeDisciplina(self):
        return self._disciplina.getNome()

    def verificarAluno(self,aluno):
        if aluno in self._alunos:
            print("O aluno esta na turma")
        else:
            print("O aluno nao esta na turma")

    def removerAluno(self,aluno):
        self._alunos.remove(aluno)
        print("O aluno foi removido")

class Curso:
    def __init__(self, nome):
        self._nome = nome
        self._alunos = []
        self._turmas = []

    def adicionarTurma(self,turma):
        self._turmas.append(turma)

    def getNomeProfessorTurmas(self):
        for turma in self._turmas:
            print(turma.getNomeProfessor())

    def getNomeAlunosTurmas(self):
        for turma in self._turmas:
            turma.getNomeTodosAlunos()

    def matricularAluno(self,aluno):
        self._alunos.append(aluno)

    def getNomeAlunosCurso(self):
        for aluno in self._alunos:
            print(aluno.getNome())

    def getnomeDisciplinaTurmas(self):
        for turma in self._turmas:
            print(turma.getnomeDisciplina())

    def verificarAluno(self, aluno):
        if aluno in self._alunos:
            print("O aluno esta no curso")
        else:
            print("O aluno nao esta no curso")

    def verificarTurma(self, turma):
        if turma in self._turmas:
            print("Esta turma e do curso")
        else:
            print("Esta turma nao e do curso")

    def removerTurma(self,turma):
        self._turmas.remove(turma)
        print("A turma foi removida")

    def desmatricularAluno(self,aluno):
        self._alunos.remove(aluno)
        print("O aluno foi desmatriculado")

professor1 = Professor("Professor1","Computacao")
professor2 = Professor("Professor2","Computacao")
aluno1 = Aluno("Aluno1","Matricula1")
aluno2 = Aluno("Aluno2","Matricula2")
aluno3 = Aluno("Aluno3","Matricula3")
aluno4 = Aluno("Aluno4","Matricula4")

disciplina1 = Disciplina("Orientacao a Objetos")
disciplina2 = Disciplina("Algoritmos")

turma1 = Turma("cod1",professor1,disciplina1)
turma2 = Turma("cod2",professor2,disciplina2)
turma3 = Turma("cod3",professor2,disciplina2)

curso = Curso("Sistemas de Informacao")

turma1.adicionarAluno(aluno1)
turma1.adicionarAluno(aluno2)
turma2.adicionarAluno(aluno3)
turma2.adicionarAluno(aluno2)

curso.adicionarTurma(turma1)
curso.adicionarTurma(turma2)
curso.matricularAluno(aluno1)
curso.matricularAluno(aluno2)
curso.matricularAluno(aluno3)

print("01)Qual o nome do professor de uma turma?")
print(turma1.getNomeProfessor())
print(turma2.getNomeProfessor())
print("\n02)Qual o nome de todos os alunos da turma?")
turma1.getNomeTodosAlunos()
print("\n03)Quais os nomes dos professores que lecionam em uma turma de um curso?")
curso.getNomeProfessorTurmas()
print("\n04)Quais os nomes dos alunos que estao registrados em alguma turma do curso?")
curso.getNomeAlunosTurmas()
print("\n05)Quais os nomes dos alunos que estao registrados em algum curso?")
curso.getNomeAlunosCurso()
print("\n06)Quais as disciplinas que estao em alguma turma de um curso?")
curso.getnomeDisciplinaTurmas()
print("\n07)Verificar se um aluno esta em uma turma.")
turma1.verificarAluno(aluno1)
turma1.verificarAluno(aluno3)
print("\n08)Verificar se o aluno esta em um curso.")
curso.verificarAluno(aluno1)
curso.verificarAluno(aluno4)
print("\n09)Verificar se uma turma esta em um curso.")
curso.verificarTurma(turma1)
curso.verificarTurma(turma3)
print("\n10)Excluir um aluno de uma turma")
turma1.getNomeTodosAlunos()
turma1.removerAluno(aluno1)
turma1.getNomeTodosAlunos()
print("\n11)Excluir uma turma de um curso")
curso.getnomeDisciplinaTurmas()
curso.removerTurma(turma1)
curso.getnomeDisciplinaTurmas()
print("\n12)Excluir um aluno de um curso")
curso.getNomeAlunosCurso()
curso.desmatricularAluno(aluno2)
curso.getNomeAlunosCurso()
