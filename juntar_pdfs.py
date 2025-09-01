import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger

def juntar_pdfs():
    # Abrir janela para selecionar arquivos
    arquivos = filedialog.askopenfilenames(
        title="Selecione os arquivos PDF",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )

    if not arquivos:
        print("Nenhum arquivo selecionado.")
        return

    # Criar o objeto merger
    merger = PdfMerger()

    for pdf in arquivos:
        merger.append(pdf)

    # Salvar o PDF final
    arquivo_saida = filedialog.asksaveasfilename(
        title="Salvar PDF Final",
        defaultextension=".pdf",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )

    if arquivo_saida:
        merger.write(arquivo_saida)
        merger.close()
        print(f"PDF final salvo em: {arquivo_saida}")
    else:
        print("Operação cancelada.")

# Interface simples
janela = tk.Tk()
janela.withdraw()  # Oculta a janela principal do Tkinter
juntar_pdfs()
