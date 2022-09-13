from discord_webhook import DiscordWebhook


webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/1019081282002632744/aOhQ3FBys64iqsO85c1n4yw8cwSgA5Kl7LWb4qR6jSG6Gk82O-h2djkVnNPDrXHOAi7z', rate_limit_retry=True,
                            content="自動推播功能已設定完成，以後若有校網公告會自動發佈在此\n此程式由Bernie開發，Github連結:https://github.com/Unforgettableeternalproject/School-Infomation-To-Webhook")
response = webhook.execute()

print("Done.")