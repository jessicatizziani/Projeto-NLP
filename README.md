# Relatório Final da Atividade Prática - Projeto NLP

Meu primeiro projeto de NLP com chatboot

✅ 1. Introdução

Este relatório apresenta o desenvolvimento de um chatbot simples utilizando a linguagem Python, com a aplicação de conceitos de Processamento de Linguagem Natural (NLP) através das bibliotecas nltk e textblob. O projeto foi realizado como parte das atividades práticas da disciplina de NLP, com o objetivo de compreender o funcionamento de diálogos homem-máquina e de aplicar análise de sentimento em mensagens de entrada.

✅ 2. Objetivos

- Compreender os fundamentos do NLP com Python.

- Construir um chatbot funcional utilizando padrões de linguagem (regex).

- Integrar análise de sentimento às interações do chatbot.

- Criar uma interface de terminal interativa.

- Permitir reinício automático do chat.

✅ 3. Desenvolvimento

3.1 Preparação do ambiente
As bibliotecas utilizadas foram:

nltk – para construção do chatbot baseado em regras

textblob – para análise de sentimento

re (via expressões regulares) – para interpretar entradas do usuário


3.2 Definição dos pares de diálogo
O chatbot foi alimentado com padrões de perguntas e múltiplas respostas possíveis para torná-lo mais natural. As entradas foram definidas com expressões regulares.


3.3 Implementação da análise de sentimento
A biblioteca TextBlob foi utilizada para identificar o tom emocional das mensagens do usuário, retornando classificações como positiva, negativa ou neutra.


3.4 Lógica do chatbot no terminal
Foi implementado um loop interativo onde o usuário pode conversar com o chatbot, que responde tanto com base nos padrões quanto com base no humor detectado.


3.5 Recurso de reinício de conversa
Após digitar sair, o chatbot oferece a opção de iniciar uma nova conversa sem reiniciar o programa.


✅ 4. Resultados

O chatbot desenvolvido foi capaz de:

- Interpretar frases básicas e responder com mensagens predefinidas.

- Reagir emocionalmente com base na análise de sentimento do texto do usuário.

- Alternar entre respostas personalizadas e padrão conforme o reconhecimento da entrada.

- Reiniciar automaticamente o diálogo com o usuário após encerramento.


✅ 5. Conclusão

A atividade prática proporcionou a aplicação real de conceitos fundamentais de NLP em Python. O projeto demonstrou como é possível integrar componentes como regex e análise de sentimento para tornar uma interação homem-máquina mais personalizada e responsiva.

Além disso, a implementação incremental (com reconhecimento de entradas, análise emocional e reinício automático) permitiu experimentar o ciclo de desenvolvimento de um chatbot do zero, reforçando o aprendizado em programação, lógica e processamento textual.


✅ 6. Referências

https://www.nltk.org

https://textblob.readthedocs.io

Documentação oficial do Python