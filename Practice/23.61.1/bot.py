import telebot
from config import TOKEN
from extensions import CurrencyConverter, APIException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Чтобы узнать цену валюты, отправьте сообщение в формате: "
                                      "<имя валюты> <валюта, в которой нужно узнать цену> <количество валюты>\n"
                                      "Например: rub usd 1\n"
                                      "Для получения списка доступных валют используйте команду /values")


@bot.message_handler(commands=['values'])
def handle_values(message):
    bot.send_message(message.chat.id, "Доступные валюты: usd, eur, rub")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        base, quote, amount = message.text.split()
        price = CurrencyConverter.get_price(base, quote, float(amount))
        bot.send_message(message.chat.id, f'Цена {amount} {base.upper()} в {quote.upper()}: {price}')
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат сообщения. Пожалуйста, введите данные в нужном формате.')
    except APIException as e:
        bot.send_message(message.chat.id, str(e))
    except Exception as e:
        bot.send_message(message.chat.id, f'Произошла ошибка: {str(e)}')


if __name__ == '__main__':
    bot.polling(none_stop=True)
