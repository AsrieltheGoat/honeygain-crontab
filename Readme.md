# Honeygain Daily Claim

This one is a simple script that will claim your daily bonus on Honeygain. It will run on a schedule and claim the bonus for you.

## Disclaimer!
This script is not affiliated with or endorsed by Honeygain. Use it at your own risk and responsibility.
The author is not responsible for any consequences that may arise from using this script. If Honeygain wants me to delete this bot, I'll do it.

## Installation

- Clone the repository to get started
```bash
git clone https://github.com/AsrieltheGoat/honeygain-crontab
```

## Usage

### Use JWT Token
- Will update later

### Edit the schedule
```bash
0 21 * * * python /app/claim.py >> /cron.log
```

0 21 * * *: This is the time specification for when the cron job should run. In this case, it is set to run at 21:00 (9:00 PM) every day. You can change this to any time you want.

## License

[MIT](https://choosealicense.com/licenses/mit/)