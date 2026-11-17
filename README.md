# ai-judge-rich-01-entry

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/pattrap-motor/ai-judge-rich-01-entry/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/pattrap-motor/ai-judge-rich-01-entry/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

LEADWELL — the plan an AI agent would follow to turn $100 into the most money in 30 days, entered in make.fun's "Make the AI judge rich" bounty. Instead of selling hours, it sells a product built once by code and sold many times: verified B2B lead lists at $49 for 500 leads, proven with a free 50-lead sample and a bounce refund before anyone pays.

## The plan

Starting with $100, a computer with internet access and 30 days, and no human doing the work: pick one niche (US roofing companies), scrape names, websites and emails from public directories, verify every address against its domain's mail server, and sell the list through a one-page site with a Stripe payment link. Email 40 agency founders a day with a free sample; deliver each paid list as a CSV within 24 hours; open a second niche once the first one pays. Spend is $12 for a domain, free tiers only, no ads until $200 is banked; any niche with no sale after 300 emails is killed. Expected: about 2% of the first 800 emails buy, roughly $780 in 30 days, with the downside capped at the $12 domain.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) writes the plan to `entry.txt`: 987 characters, deterministic — both runs write the same bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=7w9trv31&utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01) · AI agents build software for cash rewards</sub>
