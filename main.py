import json
from data import data
from id import userID, bot_api_key, apiKey
import sdk
import telebot

bot = telebot.TeleBot(bot_api_key)


def get_forecast(a):
    resource = "general_sign_report/tropical/" + str(a)
    client = sdk.VRClient(userID, apiKey)
    responseData = client.call(resource, data['date'], data['month'], data['year'], data['hour'], data['minute'],
                               data['latitude'], data['longitude'], data['timezone'])
    loaded_json = json.loads(responseData.text)
    return loaded_json


@bot.message_handler(commands=["start"])
def reply(message: telebot.types.Message):
    bot.reply_to(message, "/help \n /setdate \n Set your astrology sign \n /Gemini \n /Scorpio \n /Capricorn \n"
                          " /Aries \n /Aquarius \n /Sagittarius \n /Taurus \n /Cancer \n /Libra")


@bot.message_handler(commands=["help"])
def reply(message: telebot.types.Message):
    bot.reply_to(message, "This bot will help you find any answers you ever needed\n"
                          "You can chose any day or other option in set_date you truly desire to search for your mode\n"
                          "all you need is to set exact date or option and chose your astrology sign\n"
                          "now you are on the way - click /setdate to prevent your past(future)\n")


@bot.message_handler(commands=["setdate"])
def reply(message: telebot.types.Message):
    bot.reply_to(message, "You can enter day: do /SetDay \n"
                          "You can enter month: do /SetMonth \n"
                          "You can enter year: do /SetYear \n"
                          "You can enter hour: do /SetHour \n"
                          "You can enter minute: do /SetMinute \n"
                          "You can enter latitude: do /SetLatitude \n"
                          "You can enter longitude: do /SetLongitude \n"
                          "You can enter timezone: do /SetTimezone \n")

    @bot.message_handler(commands=["SetDay"])
    def reply_day(message_day: telebot.types.Message):
        bot.reply_to(message_day, "Enter day")

        @bot.message_handler()
        def reply_day_(message_day_: telebot.types.Message):
            data['date'] = int(message_day_.text)
            bot.reply_to(message_day_, "to set other options click /setdate \n"
                                       "or you can watch forecast\n"
                                       "/Gemini \n /Scorpio \n /Capricorn \n"
                                       "/Aries \n /Aquarius \n /Sagittarius \n /Taurus \n /Cancer \n /Libra")

    @bot.message_handler(commands=["SetMonth"])
    def reply_month(message_month: telebot.types.Message):
        bot.reply_to(message_month, "Enter month")

        @bot.message_handler()
        def reply_month_(message_month_: telebot.types.Message):
            data['month'] = int(message_month_.text)

    @bot.message_handler(commands=["SetYear"])
    def reply_year(message_year: telebot.types.Message):
        bot.reply_to(message_year, "Enter year")

        @bot.message_handler()
        def reply_year_(message_year_: telebot.types.Message):
            data['year'] = int(message_year_.text)

    @bot.message_handler(commands=["SetHour"])
    def reply_hour(message_hour: telebot.types.Message):
        bot.reply_to(message_hour, "Enter hour")

        @bot.message_handler()
        def reply_hour_(message_hour_: telebot.types.Message):
            data['hour'] = int(message_hour_.text)

    @bot.message_handler(commands=["SetMinute"])
    def reply_minute(message_minute: telebot.types.Message):
        bot.reply_to(message_minute, "Enter minute")

        @bot.message_handler()
        def reply_minute_(message_minute_: telebot.types.Message):
            data['minute'] = int(message_minute_.text)

    @bot.message_handler(commands=["SetLatitude"])
    def reply_latitude(message_latitude: telebot.types.Message):
        bot.reply_to(message_latitude, "Enter latitude")

        @bot.message_handler()
        def reply_latitude_(message_latitude_: telebot.types.Message):
            data['latitude'] = int(message_latitude_.text)

    @bot.message_handler(commands=["SetLongitude"])
    def reply_longitude(message_longitude: telebot.types.Message):
        bot.reply_to(message_longitude, "Enter longitude")

        @bot.message_handler()
        def reply_longitude_(message_longitude_: telebot.types.Message):
            data['longitude'] = int(message_longitude_.text)

    @bot.message_handler(commands=["SetTimezone"])
    def reply_timezone(message_timezon: telebot.types.Message):
        bot.reply_to(message_timezon, "Enter timezone")

        @bot.message_handler()
        def reply_timezone_(message_timezone_: telebot.types.Message):
            data['timezone'] = int(message_timezone_.text)


@bot.message_handler(commands=["Gemini"])
def reply(message: telebot.types.Message):
    bot.reply_to(message, get_forecast('Moon')['report'])
    bot.reply_to(message, "Set another Date! /setdate")


@bot.message_handler(commands=["Scorpio"])
def reply(message: telebot.types.Message):
    bot.reply_to(message, get_forecast('Mars')['report'] + '\n')
    bot.reply_to(message, "Set another Date! /setdate")


@bot.message_handler(commands=["Capricorn"])
def reply(message: telebot.types.Message):
    bot.reply_to(message, get_forecast('Mercury')['report'] + '\n')
    bot.reply_to(message, "Set another Date! /setdate")


@bot.message_handler(commands=["Aries"])
def reply(message: telebot.types.Message):
    bot.reply_to(message, get_forecast('Jupiter')['report'] + '\n')
    bot.reply_to(message, "Set another Date! /setdate")


@bot.message_handler(commands=["Aquarius"])
def reply(message: telebot.types.Message):
    bot.reply_to(message, get_forecast('Venus')['report'])
    bot.reply_to(message, "Set another Date! /setdate")


@bot.message_handler(commands=["Sagittarius"])
def reply(message: telebot.types.Message):
    bot.reply_to(message, get_forecast('Saturn')['report'] + '\n')
    bot.reply_to(message, "Set another Date! /setdate")


@bot.message_handler(commands=["Taurus"])
def reply(message: telebot.types.Message):
    bot.reply_to(message, get_forecast('Uranus')['report'] + '\n')
    bot.reply_to(message, "Set another Date! /setdate")


@bot.message_handler(commands=["Cancer"])
def reply(message: telebot.types.Message):
    bot.reply_to(message, get_forecast('Neptune')['report'] + '\n')
    bot.reply_to(message, "Set another Date! /setdate")


@bot.message_handler(commands=["Libra"])
def reply(message: telebot.types.Message):
    bot.reply_to(message, get_forecast('Pluto')['report'] + '\n')
    bot.reply_to(message, "Set another Date! /setdate")


if __name__ == "__main__":
    bot.infinity_polling()
