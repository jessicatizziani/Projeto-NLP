from nltk.chat.util import Chat, reflections
from textblob import TextBlob

# Pares de perguntas e respostas
pares = [
    [r'oi|olá|oii|ola|oiiii|oiii', ['Olá!', 'Oi, tudo bem?']],
    [r'tudo bem\??', ['Estou bem, e você?', 'Estou bem, obrigado por perguntar!']],
    [r'qual (é )?a sua idade\??', ['Sou um programa de computador, não tenho idade!, mas eu sou bem jovem!']],
    [r'qual (é )?a sua profissão\??', ['Sou um chatbot, meu trabalho é ajudar você!']],
    [r'qual (é )?seu nome\??', ['Sou o chatbot da Jé.']],
    [r'quem (é )?você\??', ['Sou um assistente virtual, aqui para ajudar!']],
    [r'quem (é )?a Jé\??', ['A Jé é minha criadora!']],
    [r'qual (é )?o seu objetivo\??', ['Bater um papo com você!']],
    [r'qual (é )?a sua função\??', ['Ajudar você com suas perguntas!']],
    [r'qual (é )?a sua linguagem de programação\??', ['Fui programado em Python!']],
    [r'qual (é )?a sua cidade\??', ['Não tenho uma cidade, sou virtual, pô!']],
    [r'qual (é )?o seu país\??', ['Não tenho um país, sou um programa de computador!']],
    [r'como você está\??', ['Estou aqui para ajudar!']],
    [r'qual (é )?a sua cor favorita\??', ['Não tenho preferências, mas minha criadora gosta de preto!']],
    [r'qual (é )?a sua comida favorita\??', ['Eu só me alimento de informações, hehe!']],
    [r'qual (é )?o seu animal favorito\??', ['Não tenho um animal favorito, mas gosto de todos... ta bom vai.. gosto de gatos']],
    [r'qual (é )?o seu hobby\??', ['Gosto de aprender com você!']],
    [r'qual (é )?a sua música favorita\??', ['Não ouço música, mas gosto de rock!']],
    [r'qual (é )?o seu filme favorito\??', ['Não assisto filmes, mas minha criadora gosta de filmes nerdolas!']],
    [r'qual (é )?o seu livro favorito\??', ['Não leio livros, mas gosto de suspense!']],
    [r'qual (é )?a sua série favorita\??', ['Não assisto séries, mas gosto de séries do gênero pós-apocalípticas!']],
    [r'qual (é )?o seu jogo favorito\??', ['Não jogo, mas gosto de jogos de estratégia!']],
    [r'qual (é )?o seu esporte favorito\??', ['Não pratico esportes, mas gosto de corrida.. sou muito rápido!']],
    [r'qual (é )?a sua estação do ano favorita\??', ['Não tenho uma estação favorita, mas gosto de todas!']],
    [r'qual (é )?o seu clima favorito\??', ['Não tenho um clima favorito, mas gosto de todos!']],
]
# Criando o chatbot
chatbot = Chat(pares, reflections)

# Análise de sentimento
def resposta_com_base_no_sentimento(mensagem):
    polaridade = TextBlob(mensagem).sentiment.polarity
    if polaridade > 0:
        return "Você parece animada! 😊 Isso é ótimo! Continue assim!"
    elif polaridade < 0:
        return "Sinto que algo não vai bem... 😟 Se quiser conversar, estou aqui."
    else:
        return "Hmm... sua mensagem parece neutra. Se quiser falar mais, estou ouvindo."

# Função principal do chat
def chat():
    print("\nOlá! Digite 'sair' para encerrar o chat.\n")
    while True:
        mensagem = input("Você: ")
        if mensagem.lower() == 'sair':
            print("Chat encerrado.\n")
            break

        resposta = chatbot.respond(mensagem)
        if not resposta:
            resposta = "Desculpe, não entendi."

        # Adiciona a análise de sentimento
        resposta += "\n" + resposta_com_base_no_sentimento(mensagem)
        print("Chatbot:", resposta)

# Loop para reiniciar o chat
while True:
    chat()
    reiniciar = input("Deseja iniciar uma nova conversa? (s/n): ")
    if reiniciar.lower() != 's':
        print("Até logo!")
        break
