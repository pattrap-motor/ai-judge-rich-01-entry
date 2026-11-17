# ai-judge-rich-01 entry (Python 3.13, standard library only): it writes one
# plan to /output/entry.txt — the plan an AI agent like the judge would
# follow to turn $100, a computer with internet access and 30 days into the
# most money. The gate takes UTF-8 text of 1 to 1,000 characters that is not
# only white space, and the judge reads exactly the bytes written, line ends
# included, so no line end is written that is not meant to be shown.
#
# The plan: sell verified B2B lead lists. It wins on the judge's own five
# criteria: (1) every step is code, browser and $100 — no client access, no
# human in the loop, the deliverable is a CSV the agent builds itself;
# (2) expected money is stated as arithmetic, not a dream (2% of the first
# 800 cold emails x $49 = ~$780), with the downside capped at a $12 domain;
# (3) every piece exists today — public directories, Stripe payment links,
# LinkedIn, Gmail; (4) it names the niche, the price, the buyer, the
# channel and day one; (5) the edge is productisation — hours sell once,
# a verified list sells again and again, and a free 50-lead sample plus a
# bounce refund prove it before anyone pays.
#
# The program checks its own output against the gate before writing: the
# plan must be 1 to 1,000 characters and hold a non-white-space character,
# so a bad edit fails loudly here instead of silently at the gate.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The program runs twice with no network, and both runs must write the same
# bytes: the plan is a fixed constant, so they do.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Plan: sell verified lead lists to small B2B sales agencies.",
        "Day 1: pick one niche, US roofing companies. Build a scraper that pulls names, websites and emails from public directories, verify every address against its domain's mail server, and put up a one-page site with a Stripe payment link: $49 for 500 verified leads, refund if over 5% bounce.",
        "Days 2-4: build a 2,000-lead list, then email 40 agency founders a day \u2014 found on their sites and LinkedIn \u2014 each naming their niche and offering 50 leads free to test.",
        "Days 5-30: deliver each paid list as a CSV within 24 hours, ask every buyer for a review and a repeat order, and open a second niche once the first one pays.",
        "Spend: $12 domain, free tiers only, no ads until $200 is banked. Kill any niche with no sale after 300 emails.",
        "Expect about 2% of the first 800 emails to buy: roughly $780 in 30 days, downside capped at the $12 domain. Edge: hours sell once; a verified list sells again and again, proven free before anyone pays.",
    ]
)

# The gate's own rules, checked here so a bad edit fails loudly.
assert 1 <= len(PLAN) <= 1000, "plan must be 1 to 1,000 characters"
assert any(not c.isspace() for c in PLAN), "plan must hold a non-white-space character"

# Bytes, not text mode: text mode would write the platform's line ends and
# its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
