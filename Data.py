#๐ช๐๐ฎ๐ซโป๏ธ๐๐๐บ๐ฅ๏ธโ๏ธ๐๏ธ๐ง๐ป๐น๐จโ๐ป๐งโ๐ป๐จโโ๏ธ๐ต๏ธ๐ค๐๐๏ธ๐ช๐โจ๐๏ธ๐๐โฅ๏ธโฆ๏ธ๐๐ง๐ ๏ธ๐โ๏ธโ๏ธ๐๐ฒ๐ธ๐ก๐ฅ๐ท๐น๐ผ๐๐๐๐๐๐๐๐ต๐ถ๐ช๐ธ๐ท๐ด

from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
๐Hello {}

Welcome to {}

I m Force Subscribe Bot !
Send /help Visit My Help Menu

๐ For All Users ๐๐

๐ฅ Powered By Emo Network โ
โ๏ธ Simple & Friendly BOT โ
๐ชค Keep Original Appearance โ
๐ฏ Group Supported โ
โก๏ธ Fast Response โ
โ 24 Hour Active โ
๐คฉ New OS โ

๐Powerd By @EmoBotDevolopers

    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="๐๏ธ Return Home ๐๏ธ", callback_data="home")],
        [InlineKeyboardButton("โฃ Emo Bot Devolopers โฃ", url="https://t.me/EmoBotDevolopers")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("๐ชDemo Bot", url="https://t.me/ImRishmika_Bot")],
        [
            InlineKeyboardButton("โ How to Use โ", callback_data="help"),
            InlineKeyboardButton("โพ๏ธ About โพ๏ธ", callback_data="about")
        ],
        [InlineKeyboardButton("๐จโ๐ป Devoloper ๐จโ๐ป", url="https://t.me/ImRishmika")],
        [InlineKeyboardButton("๐ฌ Support ๐ฌ", url="https://t.me/EmoBotSupport")],
    ]

    # Help Message
    HELP = """
1) Add me as **Admin** to a group.

2) Add me to the particular chat as **Admin** where you want to force your users to join. It can be any group or channel, public or private.

3) Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub -1001742371821` or `/forcesubscribe -1001742371821`

4) [Optional] Use /settings to change settings!

5) You are good to go. Leave the rest to me.

๐ **Available Commands** ๐

/fsub - See current force subscribe chat
/fsub chat_id/username - Force users to join the particular chat
/settings - Change Group Settings
/id - Get the chat id of any group or channel
/about - About The Bot
/help - This Message
/start - Start the Bot

**Note** - You can also use `/forcesubscribe` instead of `/fsub`

๐ฅ Powerd By [Emo Network](t.me/EmoBotDevolopers)
    """

    # About Message
    ABOUT = """
**About This Bot** 

A Telegram Force Subscribing Bot by @ImRishmika

๐ชPowerd By : @EmoBotDevolopers

๐Framework : [Pyrogram](docs.pyrogram.org)

๐Language : [Python](www.python.org)

๐Developer : @ImRishmika

๐ฅ๏ธ Host Sever : Heroku 


    """
