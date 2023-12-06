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

# Fábrica abstrata para relatórios
class AbstractReportFactory(ABC):
    @abstractmethod
    def create_report(self):
        pass

# Fábrica concreta para relatórios de vendas
class SalesReportFactory(AbstractReportFactory):
    def create_report(self):
        return SalesReport()

# Fábrica concreta para relatórios de despesas
class ExpenseReportFactory(AbstractReportFactory):
    def create_report(self):
        return ExpenseReport()

# Função que usa a fábrica abstrata para criar relatórios
def generate_report(factory):
    report = factory.create_report()
    report.generate_report()

# Exemplo de uso do Abstract Factory
if __name__ == "__main__":
    # Criação de fábricas concretas
    sales_factory = SalesReportFactory()
    expense_factory = ExpenseReportFactory()

    # Gerar e exibir relatório de vendas
    generate_report(sales_factory)

    # Gerar e exibir relatório de despesas
    generate_report(expense_factory)
