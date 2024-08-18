def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "peso normal"
    elif 25 <= imc < 29.9:
        return "sobrepeso"
    elif 30 <= imc < 34.9:
        return "obesidade grau I"
    elif 35 <= imc < 39.9:
        return "obesidade grau II"
    else:
        return "obesidade grau III"

def obter_valor_numerico(mensagem):
    while True:
        valor = input(mensagem)
        valor = valor.replace(',', '.')

        try:
            return float(valor)
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido.")

def main():
    while True:
        peso = obter_valor_numerico("Informe o peso em KG: ")
        altura = obter_valor_numerico("Informe a altura em metros (use ponto ou vírgula): ")

        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)

        print(f"Seu IMC é: {imc:.2f} e indica {classificacao}")

        continuar = input("Deseja calcular outro IMC? (s/n): ").strip().lower()
        if continuar != 's':
            print("Programa encerrado.")
            break

if __name__ == "__main__":
    main()
