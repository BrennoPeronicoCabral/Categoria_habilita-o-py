def categoria_habilitacao(qtd_rodas, peso_bruto, qtd_pessoas):
    if qtd_rodas == 2 or qtd_rodas == 3:
        return "Categoria A: Veículos com duas ou três rodas."
    elif qtd_rodas == 4:
        if qtd_pessoas <= 8 and peso_bruto <= 3500:
            return "Categoria B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg."
        elif peso_bruto > 3500 and peso_bruto <= 6000:
            return "Categoria C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg."
        elif qtd_pessoas > 8:
            return "Categoria D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas."
    elif qtd_rodas >= 4:
        if peso_bruto > 6000:
            return "Categoria E: Veículos com quatro rodas ou mais e com mais de 6000 kg."
    
    return "Categoria inválida ou não especificada."

# Exemplo de uso
qtd_rodas = int(input("Informe a quantidade de rodas do veículo: "))
peso_bruto = float(input("Informe o peso bruto do veículo em kg: "))
qtd_pessoas = int(input("Informe a quantidade de pessoas no veículo: "))

categoria = categoria_habilitacao(qtd_rodas, peso_bruto, qtd_pessoas)
print(categoria)