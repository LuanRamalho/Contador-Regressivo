import tkinter as tk
from tkinter import messagebox

# Função para iniciar o contador
def iniciar_contador():
    try:
        tempo = int(entry_tempo.get())
        if tempo < 0:
            messagebox.showerror("Erro", "Insira um número positivo!")
        else:
            contador_regressivo(tempo)
    except ValueError:
        messagebox.showerror("Erro", "Insira um número válido!")

# Função de contagem regressiva
def contador_regressivo(tempo):
    if tempo > 0:
        label_contador['text'] = f"Tempo restante: {tempo} segundos"
        janela.after(1000, contador_regressivo, tempo - 1)
    else:
        label_contador['text'] = "Tempo esgotado!"
        messagebox.showinfo("Fim do contador", "O contador terminou!")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Contador Regressivo")
janela.geometry("300x200")
janela.configure(bg="#ADD8E6")  # Fundo azul claro

# Título
titulo = tk.Label(janela, text="Contador Regressivo", font=("Arial", 16, "bold"), bg="#ADD8E6", fg="#00008B")
titulo.pack(pady=10)

# Entrada de tempo em segundos
frame_tempo = tk.Frame(janela, bg="#ADD8E6")
frame_tempo.pack(pady=10)

label_tempo = tk.Label(frame_tempo, text="Tempo (s):", font=("Arial", 12), bg="#ADD8E6", fg="#00008B")
label_tempo.pack(side=tk.LEFT)

entry_tempo = tk.Entry(frame_tempo, font=("Arial", 12), width=10)
entry_tempo.pack(side=tk.LEFT)

# Botão para iniciar o contador
botao_iniciar = tk.Button(janela, text="Iniciar", font=("Arial", 12), bg="#32CD32", fg="#FFFFFF", command=iniciar_contador)
botao_iniciar.pack(pady=10)

# Label do contador
label_contador = tk.Label(janela, text="", font=("Arial", 14), bg="#ADD8E6", fg="#8B0000")
label_contador.pack(pady=10)

janela.mainloop()
