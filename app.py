import os
import requests
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

#Get Huggingface Variables
huggingface_token = os.environ.get("HUGGINGFACE_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
headers = {"Authorization": "Bearer "+ huggingface_token}

#Query function to send request to Huggingface API
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

#Message shortcut handler for summarization
@app.shortcut("summarize-text")
def handle_shortcuts(ack, body, logger, client):
    ack()
    #Get message text for summarization
    message = body["message"]['text']
    logger.debug(message)
    output = query({
    "inputs": message,
    })
    summary = output[0].get("summary_text")
    print(summary)
    #Send Ephemeral message to user
    client.chat_postEphemeral(
        channel=body["channel"]["id"],
        user=body["user"]["id"],
        text="Here is your summary",
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": summary,
                },
            }
        ],
    )


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
