def calcular_imc(peso, altura_em_metros):
    imc = peso / (altura_em_metros ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return ("\nABAIXO DO PESO", 
                "É recomendado procurar um médico para avaliação criteriosa do resultado. "
                "Pode indicar um estado de consumo do organismo, com poucas reservas e riscos associados.")
    elif 18.5 <= imc < 25:
        return ("\nPESO NORMAL", 
                "Tudo indica que está tudo bem, mas é importante avaliar outros parâmetros da composição corporal, "
                "para compreender se estão dentro do recomendado. Algumas pessoas apresentam IMC dentro da normalidade, "
                "mas têm circunferência abdominal maior que a recomendada e/ou quantidade de massa gorda acima do ideal.")
    elif 25 <= imc < 30:
        return ("\nSOBREPESO", 
                "O sobrepeso está associado ao risco de doenças como diabetes e hipertensão. Então, atenção! "
                "Consulte um médico e reveja hábitos para reverter o quadro. Também é importante avaliar outros parâmetros, "
                "como a circunferência abdominal.")
    elif 30 <= imc < 35:
        return ("\nOBESIDADE GRAU I", 
                "É importante buscar orientação médica e nutricional para entender melhor o seu caso, "
                "mesmo que os exames (colesterol e glicemia, por exemplo) estejam normais.")
    elif 35 <= imc < 40:
        return ("\nOBESIDADE GRAU II", 
                "Indica um quadro de obesidade mais evoluído em relação à classificação anterior e, mesmo com exames "
                "laboratoriais dentro da normalidade, não se deve atrasar a busca por orientação médica e nutricional.")
    else:
        return ("\nOBESIDADE GRAU III", 
                "Nesse ponto, a chance de já estarmos diante de outras doenças associadas é mais elevada. "
                "É fundamental buscar orientação médica.")

def obter_valor_numerico(mensagem):
    while True:
        valor = input(mensagem)
        if valor.isdigit():
            return int(valor)
        else:
            print("Entrada inválida! Por favor, insira um número válido sem pontos ou vírgulas.")

def main():
    print("#### BEM-VINDO(A) À CALCULADORA DE IMC ####")
    print("Aqui você poderá calcular seu Índice de Massa Corporal e obter orientações sobre o resultado.\n")

    while True:
        peso = obter_valor_numerico("Informe seu peso em KG (somente números): ")
        altura_cm = obter_valor_numerico("Informe sua altura em centímetros (ex: 170 para 1,70m): ")

        altura_metros = altura_cm / 100
        imc = calcular_imc(peso, altura_metros)
        classificacao, mensagem = classificar_imc(imc)

        print(f"\nSeu IMC é: {imc:.2f} e indica: {classificacao}")
        print(f"\n{mensagem}")

        continuar = input("\nDeseja calcular outro IMC? Digite 'S' para continuar, ou qualquer outra tecla para encerrar o programa: ").strip().lower()
        if continuar != 's':
            print("Programa encerrado.")
            break

if __name__ == "__main__":
    main()
