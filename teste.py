class AnaliseFinanceiraSoftware:
    def __init__(self, investimento_inicial, receita_mensal, custo_mensal):
        self.investimento_inicial = investimento_inicial
        self.receita_mensal = receita_mensal
        self.custo_mensal = custo_mensal

    # ROI = (Ganho - Custo) / Custo
    def calcular_roi(self):
        ganho_total = self.receita_mensal - self.custo_mensal
        roi = (ganho_total / self.investimento_inicial) * 100
        return roi

    # PAYBACK = investimento / lucro mensal
    def calcular_payback(self):
        lucro_mensal = self.receita_mensal - self.custo_mensal
        if lucro_mensal <= 0:
            return None
        return self.investimento_inicial / lucro_mensal

    # BREAKEVEN = investimento / margem de contribuição
    def calcular_breakeven(self):
        margem = self.receita_mensal - self.custo_mensal
        if margem <= 0:
            return None
        return self.investimento_inicial / margem

    def resumo(self):
        roi = self.calcular_roi()
        payback = self.calcular_payback()
        breakeven = self.calcular_breakeven()

        print("\n===== ANÁLISE FINANCEIRA DO MÓDULO DE SOFTWARE =====")
        print(f"Investimento Inicial: R$ {self.investimento_inicial:.2f}")
        print(f"Receita Mensal Estimada: R$ {self.receita_mensal:.2f}")
        print(f"Custo Mensal (manutenção): R$ {self.custo_mensal:.2f}")

        print("\n>> RESULTADOS:")

        print(f"ROI: {roi:.2f}%")

        if payback is None:
            print("Payback: Não ocorre (lucro mensal é zero ou negativo).")
        else:
            print(f"Payback: {payback:.2f} meses")

        if breakeven is None:
            print("Breakeven: Nunca ocorre (margem negativa).")
        else:
            print(f"Ponto de Equilíbrio: {breakeven:.2f} meses")

        print("=====================================================\n")


# ------------------------- EXEMPLO DE USO -------------------------
if __name__ == "__main__":
    print("Cálculo de ROI, Payback e Breakeven de um Módulo de Software")

    investimento = float(input("Digite o investimento inicial (R$): "))
    receita = float(input("Digite a receita mensal estimada (R$): "))
    custo = float(input("Digite o custo mensal (R$): "))

    analise = AnaliseFinanceiraSoftware(investimento, receita, custo)
    analise.resumo()
