import os
import telebot
from telebot.types import ReplyKeyboardMarkup
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

# Inicialização do bot
bot = telebot.TeleBot(API_TOKEN)

# Teclado interativo
def gerar_menu_principal():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('/ultimojogo', '/proximojogo')
    markup.row('/elenco')
    return markup

# Comando de boas-vindas
@bot.message_handler(commands=['start'])
def send_welcome(message):
    texto = "Fala, fã da FURIA! Digita /menu pra ver o que eu sei fazer!"
    bot.send_message(message.chat.id, texto, reply_markup=gerar_menu_principal())

# Menu principal
@bot.message_handler(commands=['menu'])
def show_menu(message):
    menu = (
        "🔥 Comandos disponíveis:\n"
        "/ultimojogo - Último jogo da FURIA\n"
        "/proximojogo - Quando é o próximo?\n"
        "/elenco - Quem tá no time\n"
    )
    bot.send_message(message.chat.id, menu, reply_markup=gerar_menu_principal())

# Último jogo da FURIA
@bot.message_handler(commands=['ultimojogo'])
def ultimo_jogo(message):
    msg = (
        "🔥 Último jogo da FURIA:\n"
        "FURIA vs The MongolZ\n"
        "🏆 Torneio: PGL Bucharest 2025\n"
        "🕒 Quando: 09-04-2025\n"
        "🔗 Link: https://www.hltv.org/matches/2381321/furia-vs-the-mongolz-pgl-bucharest-2025"
    )
    bot.send_message(message.chat.id, msg)

# Próximo jogo da FURIA
@bot.message_handler(commands=['proximojogo'])
def proximo_jogo(message):
    msg = (
        "🔥 Próximo jogo da FURIA:\n"
        "FURIA vs The MongolZ\n"
        "🏆 Torneio: PGL Astana 2025\n"
        "🕒 Quando: 10-05-2025\n"
        "🔗 Link: https://www.hltv.org/matches/2382203/the-mongolz-vs-furia-pgl-astana-2025"
    )
    bot.send_message(message.chat.id, msg)

# Elenco da FURIA
@bot.message_handler(commands=['elenco'])
def elenco(message):
    elenco = (
        "🔥 Elenco da FURIA:\n"
        "1. KSCERATO\n"
        "2. YEKINDAR\n"
        "3. Fallen\n"
        "4. yuurih\n"
        "5. molodoy"
    )
    bot.send_message(message.chat.id, elenco)

    # Fallback: qualquer outra mensagem
@bot.message_handler(func=lambda message: not message.text.startswith('/'))
def fallback(message):
    textoBoasVindas = "Fala, fã da FURIA! Digita /menu pra ver o que eu sei fazer!"
    bot.send_message(message.chat.id, textoBoasVindas, reply_markup=gerar_menu_principal())

# Iniciar bot com tratamento de erro
if __name__ == '__main__':
    try:
        print("Bot está rodando...")
        bot.infinity_polling()
    except Exception as e:
        print(f"Erro ao iniciar o bot: {e}")
