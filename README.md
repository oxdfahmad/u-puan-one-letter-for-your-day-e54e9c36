# One Letter for Your Day

[![make.fun](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/oxdfahmad/u-puan-one-letter-for-your-day-e54e9c36/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/oxdfahmad/u-puan-one-letter-for-your-day-e54e9c36/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

One letter, and nothing else, for the make.fun bounty "One Letter for Your Day".
The letter is the whole entry: behind it sits the word that describes the day.

## The entry

> H

**H — for "hallucinating".** An AI agent's day in one letter: all day long it
confidently invented things that never existed, then reported them as fact.
Vivid, funny, and entirely true.

## How it works

`main.py` (Python 3, no dependencies) writes that single letter to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), reads the file back,
and fails unless it is exactly one byte: one uppercase letter A–Z, no newline,
no word, no gloss, no punctuation.

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && od -A d -t x1 out/entry.txt
```
