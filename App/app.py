from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from configs.SlackCredentials import BOT_TOKEN, APP_LEVEL_TOKEN

app = App(token=BOT_TOKEN)

# implement schedule message here

if __name__ == '__main__':
    SocketModeHandler(app, APP_LEVEL_TOKEN).start()
