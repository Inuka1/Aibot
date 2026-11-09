
import os
import telebot
import google.generativeai as genai

# ඔබේ ටෝකන් මෙතැනට දාන්න
TELEGRAM_TOKEN = 9223640962:AAHBgetLZlLxQoGyTUHCqlT4KH6jUOWs6zY
GEMINI_API_KEY = AQ.Ab8RN6JTn8eWrSEwVWZ97tP-hBKO2Zxzv5xP3h0XBk9WxkLfuw

# Gemini API සෙටප් කිරීම
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'help'])
function_start(message):
    bot.reply_to(message, "ආයුබෝවන්! මම ඔබේ AI බොට්. මගෙන් ඕනෑම ප්‍රශ්නයක් අහන්න.")

@bot.message_handler(func=lambda message: True)
handle_message(message):
    try:
        user_text = message.text
        # Gemini වෙතින් පිළිතුර ලබා ගැනීම
        response = model.generate_content(user_text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "සමාවෙන්න, දෝෂයක් සිදු විය. කරුණාකර නැවත උත්සාහ කරන්න.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
