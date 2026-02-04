class AgenteIA:
    def __init__(self, nome):
        self.nome = nome

    def analisar_mensagem(self, mensagem):
        mensagem = mensagem.lower()

        if "problema" in mensagem or "erro" in mensagem:
            return "Entendi que você está com um problema técnico. Vou tentar te ajudar."
        
        elif "preço" in mensagem or "valor" in mensagem:
            return "Você gostaria de saber informações sobre valores ou planos disponíveis."
        
        elif "ajuda" in mensagem or "suporte" in mensagem:
            return "Claro! Estou aqui para te ajudar. Pode me explicar melhor?"
        
        else:
            return "Pode me dar mais detalhes para que eu possa tomar a melhor decisão?"

    def responder(self, mensagem):
        resposta = self.analisar_mensagem(mensagem)
        return resposta


# Simulação de uso do agente
if __name__ == "__main__":
    agente = AgenteIA("Agente Virtual")

    print("Digite uma mensagem para o agente (ou 'sair' para encerrar):")

    while True:
        mensagem_usuario = input("> ")

        if mensagem_usuario.lower() == "sair":
            print("Encerrando atendimento. Até mais!")
            break

        resposta = agente.responder(mensagem_usuario)
        print(f"{agente.nome}: {resposta}")
