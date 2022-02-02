from slack_sdk.errors import SlackApiError


def sendTextMessage(app, channelId, message):
    try:
        app.client.chat_postMessage(
            channel=channelId,
            text=message
        )
    except SlackApiError as e:
        print(f"Error: {e}")
