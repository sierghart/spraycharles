import pymsteams
from discord_webhook import DiscordWebhook
from notifiers import get_notifier


def slack(webhook, host):
    slack = get_notifier("slack")
    slack.notify(message=f"Credentials guessed for host: {host}", webhook_url=webhook)


def teams(webhook, host):
    notify = pymsteams.connectorcard(webhook)
    notify.text(f"Credentials guessed for host: {host}")
    notify.send()


def discord(webhook, host, customer, username):
    notify = DiscordWebhook(
        url=webhook, content=f"Credentials guessed for host: {host}\nCustomer: {customer}\nUsername: {username}"
    )
    response = notify.execute()
