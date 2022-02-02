import time
import helper
from slack_bolt import App
from messages import DailySlackReport
from slack_bolt.adapter.socket_mode import SocketModeHandler
from configs.SlackCredentials import BOT_TOKEN, APP_LEVEL_TOKEN

app = App(token=BOT_TOKEN)


if __name__ == '__main__':
    SocketModeHandler(app, APP_LEVEL_TOKEN).start()

    # infinitely send message to Slack channel every day
    while True:
        message = DailySlackReport.getMessage()
        helper.sendTextMessage(app, '<channel_id>', message)
        time.sleep(86400)

