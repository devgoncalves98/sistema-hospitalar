class Paciente:
    def __init__(self, nome, cpf, prioridade):
        self.nome = nome
        self.cpf = cpf
        self.prioridade = prioridade

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf}, Prioridade: {self.prioridade})"