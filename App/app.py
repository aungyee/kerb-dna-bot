import time
import helper
from slack_bolt import App
from messages import DailySlackReport
from slack_bolt.adapter.socket_mode import SocketModeHandler
from configs.SlackCredentials import BOT_TOKEN, APP_LEVEL_TOKEN

app = App(token=BOT_TOKEN)

socket = SocketModeHandler(app, APP_LEVEL_TOKEN)

if __name__ == '__main__':
    socket.start()

# infinitely send message to Slack channel every day

message = DailySlackReport.getMessage()
helper.sendTextMessage(app, 'C02EM7MMFCJ', message)

socket.close()



