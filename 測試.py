from discord_webhook import DiscordWebhook


webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/1019081282002632744/aOhQ3FBys64iqsO85c1n4yw8cwSgA5Kl7LWb4qR6jSG6Gk82O-h2djkVnNPDrXHOAi7z', rate_limit_retry=True,
                            content="9/15日更新，移除公告內文，並將於每日下午五點公告最新消息連結，多則連結將會一同發布 <Bug Resolved!>")
response = webhook.execute()

print("Done.")