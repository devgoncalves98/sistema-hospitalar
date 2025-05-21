import heapq
from paciente import Paciente
from xml.etree.ElementTree import Element, SubElement, tostring
import xml.dom.minidom

class SistemaHospitalar:
    def __init__(self):
        self.pacientes_heap = []
        self.pacientes_hash = {}

    def adicionar_paciente(self, nome, cpf, prioridade):
        paciente = Paciente(nome, cpf, prioridade)
        heapq.heappush(self.pacientes_heap, (-prioridade, paciente))
        self.pacientes_hash[cpf] = paciente

    def buscar_paciente(self, cpf):
        return self.pacientes_hash.get(cpf)

    def listar_pacientes_por_prioridade(self):
        print("--- Pacientes por prioridade ---")
        for _, paciente in sorted(self.pacientes_heap, reverse=True):
            print(paciente)

    def exportar_xml(self, filename):
        root = Element("Pacientes")
        for paciente in self.pacientes_hash.values():
            p_elem = SubElement(root, "Paciente")
            SubElement(p_elem, "Nome").text = paciente.nome
            SubElement(p_elem, "CPF").text = paciente.cpf
            SubElement(p_elem, "Prioridade").text = str(paciente.prioridade)

        xml_str = xml.dom.minidom.parseString(tostring(root)).toprettyxml()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(xml_str)