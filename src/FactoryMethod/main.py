from abc import ABC, abstractmethod

# Classe base para relatórios
class Report(ABC):
    @abstractmethod
    def generate_report(self):
        pass


# Implementação de relatório de vendas
class SalesReport(Report):
    def generate_report(self):
        print("Gerando relatório de vendas")


# Implementação de relatório de despesas
class ExpenseReport(Report):
    def generate_report(self):
        print("Gerando relatório de despesas")


# Factory Method para criar instâncias de relatórios
class ReportFactory:
    def create_report(self, report_type):
        if report_type == "sales":
            return SalesReport()
        elif report_type == "expense":
            return ExpenseReport()
        else:
            raise ValueError("Tipo de relatório desconhecido")


# Exemplo de uso do Factory Method
if __name__ == "__main__":
    # Criação de uma instância de Factory
    factory = ReportFactory()

    # Criar relatório de vendas
    sales_report = factory.create_report("sales")
    sales_report.generate_report()

    # Criar relatório de despesas
    expense_report = factory.create_report("expense")
    expense_report.generate_report()
