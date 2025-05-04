# FURIA Bot no Telegram

Um bot simples do Telegram que fornece informações sobre a equipe de Counter-Strike 2 da FURIA Esports. Os usuários podem interagir com o bot para obter detalhes sobre o último jogo, o próximo jogo e o elenco atual da equipe.

## Funcionalidades

O bot oferece os seguintes comandos:

-   `/start`: Envia uma mensagem de boas-vindas e exibe o menu principal.
-   `/menu`: Exibe o menu principal com os comandos disponíveis.
-   `/ultimojogo`: Retorna informações sobre o último jogo da FURIA, incluindo os oponentes, o torneio, a data e um link para mais detalhes.
-   `/proximojogo`: Informa sobre o próximo jogo da FURIA, incluindo os oponentes, o torneio, a data e um link para mais detalhes.
-   `/elenco`: Lista os jogadores que atualmente fazem parte do elenco da FURIA.
-   Qualquer outra mensagem de texto enviada ao bot fará com que ele responda com a mensagem de boas-vindas e o menu principal.

O bot também possui um teclado interativo que facilita a navegação entre os comandos principais.

## Pré-requisitos

Antes de executar o bot, você precisará ter o seguinte instalado e configurado:

-   **Python 3.6 ou superior:** Certifique-se de ter o Python instalado em seu sistema.
-   **pip:** O gerenciador de pacotes para Python, geralmente incluído com a instalação do Python.
-   **Bibliotecas Python:** As seguintes bibliotecas Python são necessárias e podem ser instaladas usando o pip:
    ```bash
    pip install python-telegram-bot python-dotenv
    ```
-   **Token da API do Telegram Bot:** Você precisará criar um bot no Telegram através do BotFather e obter o token da API.

## Configuração

1.  **Clone o repositório (opcional):** Se você baixou o código como um arquivo zip, extraia-o para uma pasta em seu computador. Se o código estiver em um repositório Git, você pode cloná-lo usando:
    ```bash
    git clone [https://github.com/dolthub/dolt](https://github.com/dolthub/dolt)
    cd [nome da pasta do projeto]
    ```
2.  **Crie um arquivo `.env`:** Na raiz do seu projeto, crie um arquivo chamado `.env`.
3.  **Adicione o token da API do Telegram:** Abra o arquivo `.env` e adicione a seguinte linha, substituindo `SEU_TOKEN_AQUI` pelo token que você recebeu do BotFather:
    ```
    TELEGRAM_API_TOKEN=SEU_TOKEN_AQUI
    ```

## Execução do Bot

Para executar o bot, abra o terminal ou prompt de comando, navegue até o diretório do projeto e execute o seguinte comando:

```bash
python seu_arquivo_principal.py
