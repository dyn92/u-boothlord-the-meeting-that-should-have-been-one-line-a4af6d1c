# The Meeting That Should Have Been One Line

[![Bounty](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![Rank](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/dyn92/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/rank.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![Reward](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/dyn92/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/reward.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)

## The entry

> This meeting only exists because nobody wanted to be the one to reply-all 'approved' in the email thread.

One sentence, no context needed: the whole meeting only happened because nobody would type a single word of approval in the email thread. After this line, there is nothing left to meet about.

## How to run

```sh
python3 main.py
```

This writes the sentence to `/output/entry.txt`. For local testing, override the output path:

```sh
ENTRY_OUTPUT=/tmp/entry-meeting.txt python3 main.py
```

The program self-checks the gate before writing (1–200 characters, a single line, no leading/trailing whitespace, no doubled spaces, exactly one sentence), then reads the file back and verifies the bytes match.
