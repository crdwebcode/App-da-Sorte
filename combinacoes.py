import tkinter as tk  # Importa o módulo tkinter para criar a interface gráfica
from tkinter import messagebox  # Importa a classe messagebox do módulo tkinter para exibir caixas de diálogo
from itertools import combinations  # Importa a função combinations do módulo itertools para gerar combinações

class CombinationsApp:
    def __init__(self, master):
        self.master = master  # Atribui o objeto Tkinter pai à variável self.master
        master.title("Combinações")  # Define o título da janela principal como "Combinações"

        # Cria um rótulo para instruir o usuário a inserir as dezenas para descarte
        self.label_descarte = tk.Label(master, text="Digite 5 dezenas para descarte (separadas por vírgula):")
        self.label_descarte.grid(row=0, column=0, padx=10, pady=5, sticky="w")  # Define a posição do rótulo na grade

        # Cria uma entrada de texto para o usuário inserir as dezenas para descarte
        self.entry_descarte = tk.Entry(master, width=50)
        self.entry_descarte.grid(row=1, column=0, padx=10, pady=5)  # Define a posição da entrada de texto na grade

        # Cria um botão "Gerar Combinações" que chama a função generate_combinations
        self.generate_button = tk.Button(master, text="Gerar Combinações", command=self.generate_combinations)
        self.generate_button.grid(row=2, column=0, padx=10, pady=5)  # Define a posição do botão na grade

        # Cria um botão "Limpar" que chama a função clear_all
        self.clear_button = tk.Button(master, text="Limpar", command=self.clear_all)
        self.clear_button.grid(row=2, column=1, padx=10, pady=5)  # Define a posição do botão na grade

        # Cria um frame para exibir as combinações geradas
        self.combination_frame = tk.Frame(master)
        self.combination_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5)  # Define a posição do frame na grade

    def generate_combinations(self):
        try:
            # Obtém as dezenas para descarte inseridas pelo usuário
            descarte_input = self.entry_descarte.get().strip()
            discarded_numbers = [int(num.strip()) for num in descarte_input.split(',')]

            # Verifica se o usuário inseriu exatamente 5 dezenas
            if len(discarded_numbers) != 5:
                raise ValueError("Por favor, insira exatamente 5 números.")

            # Verifica se as dezenas para descarte estão no intervalo de 1 a 25
            if any(num < 1 or num > 25 for num in discarded_numbers):
                raise ValueError("Os números devem estar no intervalo de 1 a 25.")

            # Gera os números disponíveis excluindo os números descartados
            available_numbers = [num for num in range(1, 26) if num not in discarded_numbers]

            # Define as configurações desejadas de pares e ímpares
            configurations = [(7, 8), (8, 7), (6, 9), (9, 6), (5, 10), (10, 5)]

            # Limpa o frame de combinações
            self.clear_combinations()

            # Gera e exibe as combinações para cada configuração desejada
            for idx, (pairs, odds) in enumerate(configurations, start=1):
                combinations = self.generate_combinations_list(available_numbers, pairs, odds)
                label = tk.Label(self.combination_frame, text=f"Combinações de {pairs} pares e {odds} ímpares:")
                label.grid(row=idx, column=0, padx=5, pady=2, sticky="w")
                for combination in combinations[:4]:
                    label = tk.Label(self.combination_frame, text=str(combination))
                    label.grid(row=idx, column=1, padx=5, pady=2, sticky="w")

        except ValueError as ve:
            messagebox.showerror("Erro", str(ve))  # Exibe uma caixa de mensagem de erro se ocorrer uma exceção

    def generate_combinations_list(self, numbers, pairs, odds):
        # Encontra todas as combinações com a quantidade especificada de pares e ímpares
        valid_combinations = []
        for combination in combinations(numbers, pairs + odds):
            if sum(1 for num in combination if num % 2 == 0) == pairs and sum(1 for num in combination if num % 2 != 0) == odds:
                valid_combinations.append(combination)
        return valid_combinations

    def clear_combinations(self):
        # Limpa todos os widgets do frame de combinações
        for widget in self.combination_frame.winfo_children():
            widget.destroy()

    def clear_all(self):
        # Limpa a entrada de dados e o frame de combinações
        self.entry_descarte.delete(0, tk.END)
        self.clear_combinations()

def main():
    root = tk.Tk()  # Cria uma instância da classe Tk, que é a janela principal do aplicativo
    app = CombinationsApp(root)  # Cria uma instância da classe CombinationsApp, passando a janela principal como argumento
    root.mainloop()  # Inicia o loop principal do tkinter para manter a janela aberta

if __name__ == "__main__":
    main()  # Chama a função main quando o script é executado diretamente
