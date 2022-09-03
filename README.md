# Pali suttas Telegarm bot

## Installation
```bash
python3 -m venv env
. env/bin/activate
pip3 install -e .
```

## Usage
- Create a bot with [BotFather](https://t.me/BotFather)
- Get the bot token
- Set the token in the [config.py](./config.py)

Run with:
```bash
. env/bin/activate
pali_bot
```

## TODO
- Serialize data to JSON or YAML
- ~~Implement setup.py~~
- Buttons menu
- Testing: run commands, check no exceptions
- Suggestion: rename commands like `/any`, `/theragatha`...
- Suggestion: automatic tags to easily search messages
- Suggestion: bold title of a sutta
