import time
import helper
from slack_bolt import App
from messages import DailySlackReport
from slack_bolt.adapter.socket_mode import SocketModeHandler
from configs.SlackCredentials import BOT_TOKEN, APP_LEVEL_TOKEN

app = App(token=BOT_TOKEN)

# infinitely send message to Slack channel every day
while True:
    message = DailySlackReport.getMessage()
    helper.sendTextMessage(app, 'C02EM7MMFCJ', message)
    time.sleep(86399.8)


if __name__ == '__main__':
    SocketModeHandler(app, APP_LEVEL_TOKEN).start()




