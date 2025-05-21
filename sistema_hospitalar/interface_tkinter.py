import tkinter as tk
from tkinter import messagebox, ttk
from sistema import SistemaHospitalar

class AppHospitalar:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Hospitalar")
        self.sistema = SistemaHospitalar()

        self.ordem_cpf = False
        self.ordem_prioridade = False

        self.frame_cadastro = tk.LabelFrame(root, text="Cadastrar Paciente", padx=10, pady=10)
        self.frame_cadastro.pack(padx=10, pady=10, fill="x")

        tk.Label(self.frame_cadastro, text="Nome:").grid(row=0, column=0)
        tk.Label(self.frame_cadastro, text="CPF:").grid(row=1, column=0)
        tk.Label(self.frame_cadastro, text="Prioridade (1-10):").grid(row=2, column=0)

        self.nome_entry = tk.Entry(self.frame_cadastro)
        self.cpf_entry = tk.Entry(self.frame_cadastro)
        self.prioridade_entry = tk.Entry(self.frame_cadastro)

        self.nome_entry.grid(row=0, column=1)
        self.cpf_entry.grid(row=1, column=1)
        self.prioridade_entry.grid(row=2, column=1)

        tk.Button(self.frame_cadastro, text="Cadastrar", command=self.cadastrar).grid(row=3, column=0, columnspan=2, pady=5)

        self.frame_lista = tk.LabelFrame(root, text="Pacientes por Prioridade", padx=10, pady=10)
        self.frame_lista.pack(padx=10, pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(self.frame_lista, columns=("CPF", "Prioridade"), show="headings")
        self.tree.heading("CPF", text="CPF", command=self.ordenar_por_cpf)
        self.tree.heading("Prioridade", text="Prioridade", command=self.ordenar_por_prioridade)

        self.tree.column("CPF", width=150, anchor="center")
        self.tree.column("Prioridade", width=100, anchor="center")

        self.tree.pack(fill="both", expand=True)

        self.btn_exportar = tk.Button(root, text="Exportar XML", command=self.exportar)
        self.btn_exportar.pack(pady=10)

    def cadastrar(self):
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        try:
            prioridade = int(self.prioridade_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Prioridade deve ser um número.")
            return

        self.sistema.adicionar_paciente(nome, cpf, prioridade)
        self.atualizar_lista()
        self.nome_entry.delete(0, tk.END)
        self.cpf_entry.delete(0, tk.END)
        self.prioridade_entry.delete(0, tk.END)

    def atualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for _, paciente in sorted(self.sistema.pacientes_heap, reverse=True):
            self.tree.insert("", "end", values=(paciente.cpf, paciente.prioridade))

    def ordenar_por_cpf(self):
        pacientes = [(paciente.cpf, paciente.prioridade) for _, paciente in self.sistema.pacientes_heap]
        pacientes.sort(key=lambda x: x[0], reverse=self.ordem_cpf)
        self.ordem_cpf = not self.ordem_cpf

        for item in self.tree.get_children():
            self.tree.delete(item)
        for cpf, prioridade in pacientes:
            self.tree.insert("", "end", values=(cpf, prioridade))

    def ordenar_por_prioridade(self):
        pacientes = [(paciente.cpf, paciente.prioridade) for _, paciente in self.sistema.pacientes_heap]
        pacientes.sort(key=lambda x: x[1], reverse=self.ordem_prioridade)
        self.ordem_prioridade = not self.ordem_prioridade

        for item in self.tree.get_children():
            self.tree.delete(item)
        for cpf, prioridade in pacientes:
            self.tree.insert("", "end", values=(cpf, prioridade))

    def exportar(self):
        self.sistema.exportar_xml("pacientes.xml")
        messagebox.showinfo("Exportação", "Dados exportados para pacientes.xml com sucesso!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppHospitalar(root)
    root.mainloop()
