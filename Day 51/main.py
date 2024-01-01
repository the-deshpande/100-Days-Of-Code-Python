from internet_speed_bot import InternetSpeedTwitterBot

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
print('Got the data')
bot.tweet_internet_speed()
