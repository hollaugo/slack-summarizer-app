# Summary Slackbot
This script creates a Slackbot that summarizes text using the Hugging Face API.

## Requirements
- A Hugging Face API key stored as the environment variable HUGGINGFACE_TOKEN
- A Slack bot token stored as the environment variable SLACK_BOT_TOKEN
- A Slack App token stored as the environment variable SLACK_APP_TOKEN
- slack_bolt and requests python modules

## Usage
In Slack, create a message shortcut named "summarize-text"
When this shortcut is used, the bot will summarize the text of the message using the Hugging Face API
The summary will be sent as an ephemeral message to the user who triggered the shortcut

## Components
- huggingface_token, API_URL, headers: Variables used to make the API call to Hugging Face
- query(payload): Function that sends the API request and returns the JSON response
- handle_shortcuts(ack, body, logger, client): Message shortcut handler that retrieves the message text, sends it to the query function, and sends the summary as an ephemeral message to the user who triggered the shortcut
- app = App(token=os.environ.get("SLACK_BOT_TOKEN")): Initializes the Slackbot
- SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start(): Starts the Slackbot in socket mode


