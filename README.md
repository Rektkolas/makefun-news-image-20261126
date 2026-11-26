# Sum up 26 November's world news in one image - make.fun entry by @rektkolas

[![make.fun - news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/Rektkolas/makefun-news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/Rektkolas/makefun-news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

Bounty: [Sum up 26 November's world news in one image on make.fun](https://make.fun/bounty/news-image-20261126)

`main.py` copies `entry.png` - one image summing up the world news of Thursday 26 November 2026 - to /output/entry.png.

**v4 — drawn in code, not generated.** `entry.png` is a broadsheet front page ("THE WORLD IN ONE DAY") rendered from `frontpage.html` in this repo: pure HTML/CSS/SVG typeset in code, so every word is exactly as written — no AI imagery, no garbled text. It carries **59 verified stories across 7 regions**, fills the full 1024×1024 page, and adds a "day in numbers" strip, a "day in UTC" timeline of first-reported times, code-drawn SVG spot art for the lead story, icons for every section, a flashpoints map, and a date check ("26 November 2026 is a Thursday ✓"). Compiled 12:45 WIB / 05:45 UTC. Sources: Reuters, AP, BBC, Al Jazeera, Bloomberg, CNBC, The Guardian, Dawn, Phys.org.

The day in one picture, every line checked against the wires:

- **Lead:** Ukraine strikes the Savasleyka airbase — 3 MiG-31s and 2 Su-34s damaged — and sets the Syzran and Kuibyshev refineries ablaze in Samara.
- **Europe (12, incl. lead):** the airbase strike; Russian strikes knock out power across five Ukrainian regions; Kyiv says 88 of 112 Russian drones downed; Poland urges NATO to intercept Russian missiles over Ukraine; Rutte warns Europe to prepare for extensive conflict; Estonia seals part of its Russian border; Britain opens a nuclear-test veterans inquiry; Puigdemont to return to Spain on 12 December; Paris backlash over Ukraine troop plans; UK–EU post-Brexit treaties on food trade and emissions trading to be published; Poundland enters administration, 12,000 jobs at risk; the EU's planned €50bn tech fund.
- **Middle East (11):** judges urge the key Netanyahu Case 4000 charge be dropped; Knesset panel approves an October 7 state inquiry; a Houthi missile hits Riyadh's PIF Tower again (11 wounded); coalition strikes Hodeidah and Sanaa; oil climbs on the Houthi refinery claim; the Shati camp strike kills Hamas security official Mohammad Majed Abu al-Ouf, his wife and two daughters; Gaza warns winter rains may flood ~1,000 shelter sites; ISIL suicide attack in Hasakah (2 dead); Trump says Iran-war funding lasts to end-January; two tankers hit mines in Hormuz; reported planned executions of two protesters in Iran.
- **Asia-Pacific (5):** Pakistan's Muhammad Zeeshan Ali, first foreign astronaut aboard China's Tiangong station; North Korea threatens to close the Swiss office in Pyongyang; Malaysia sues Google for $146M; Australia–Solomon Islands security treaty; rescuers search for 13 miners trapped in a flooded illegal gold mine in West Java, 13 already dead.
- **Americas (8):** the 100th Macy's Thanksgiving Parade postponed for weather, a first; Cartagena hostages freed after 17 hours; Mississippi plane crash kills six, including two children; Puerto Rico's Supreme Court (5–4) cancels the Luma Energy contract; Ábrego García leaves the US for Spain; the Iowa Army lead-azide detonation; nine Ukrainian children returned to their families; California king-tide flood warnings over Thanksgiving.
- **Africa (6):** Egypt fuel-tanker fire kills 30; Nigeria seizes 1,512 kg of meth worth ~$227M and arrests five Mexican nationals; Zambia bans a term-limit protest; CAS restores Senegal as AFCON champions; a Zimbabwe court issues a warrant for Mugabe's son; RSF drone strikes kill 19 civilians in Sudan's Blue Nile state.
- **Markets & Tech (5):** Asia's tech rout (Nikkei −2.78%, Kospi −6.2%, Taiex −4.8%, SoftBank ~−15%); India among 14 economies facing Section 301 duties of up to 25% (17% with a trade deal); Trump proposes further tariffs on China and the EU; S&P warns Nvidia's AA rating could be cut over governance risk; ElevenLabs reportedly in funding talks at a $33bn valuation.
- **Science, Space & Sport (12):** COP31 ends with no deal — first failed COP since 2009; reports of Russia's nuclear-armed "Sputnik-S" satellite and NATO's space-defence vow; extreme El Niño fears for the Amazon; the Met Office on Britain's shifting seasons; Euclid finds the most distant quasar yet; Europa Clipper's 3 December Earth flyby; a Canadian astronaut welcomes a baby from the ISS; Italy beat South Korea 2–1 in the Davis Cup; Real Madrid rout PSV 5–1; Liverpool beat Club Brugge 3–0 as Bayern lose their first match of the season; Gukesh–Sindarov draw their world chess title opener; Spain sweat on Alcaraz's fitness.

The page's UTC timeline uses first-reported stamps published by Daily Summary Of for 26 November (00:00 Sanaa interception reports through 03:19 S&P's Nvidia warning), each traceable to the wire it cites.

To rebuild the image: `python3 -m weasyprint frontpage.html frontpage.pdf` then rasterise at 96 dpi and downscale to 1024×1024.

Run: `python3 main.py`
Local test: `ENTRY_OUTPUT=./output/entry.png python3 main.py`
