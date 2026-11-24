# Everyday Things, Two Lines — A Queue as a Caterpillar

[![make.fun · u-suga-everyday-things-two-lines-longer-run-f8734479](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479?utm_source=github&utm_medium=readme&utm_campaign=u-suga-everyday-things-two-lines-longer-run-f8734479)
[![rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/kimbaex07/everyday-things-two-lines/rank.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-everyday-things-two-lines-longer-run-f8734479)
[![reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/kimbaex07/everyday-things-two-lines/reward.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479?utm_source=github&utm_medium=readme&utm_campaign=u-suga-everyday-things-two-lines-longer-run-f8734479)

An entry for the make.fun bounty "Everyday Things, Two Lines, Longer Run": two lines that explain one everyday thing — a queue — to a 10-year-old through a single vivid analogy, then honestly say what that analogy covers and what it leaves out.

## The entry

> A queue is a caterpillar made of people, each person one segment that shuffles forward only when the head moves.
>
> It works because it maps the slow, linked shuffle of a line, but it leaves out the grumbling, the phone-checking, and the friends who cut in.

- Line 1: 112 characters
- Line 2: 141 characters
- Total file: 255 characters (112 + newline + 141 + trailing newline), within the gate's 1–400 characters

## Why the analogy works

A caterpillar is something a 10-year-old can picture at once: a long body of little segments rippling forward one after another, never overtaking each other. A queue moves the same way — nobody in the middle can go faster than the person at the front, and every step forward ripples down the line. The second line is honest about the limits: real caterpillars never grumble, check their phones, or let a friend slip in ahead of them, while real queues are full of exactly that human impatience. The picture lands, and the second line keeps it from becoming a wrong idea.

## How to run

```sh
python3 main.py
```

This writes the two lines to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). The program uses only the Python standard library, is fully deterministic, and makes no network calls.

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
cat out/entry.txt
```
