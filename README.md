# 22 November 2026 — The World in One Day

[![make.fun bounty](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/tomoyasu-muse/news-image-20261122-entry/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/tomoyasu-muse/news-image-20261122-entry/reward.svg)](https://make.fun/bounty/news-image-20261122)

A program that writes one image summing up the world news of
**Sunday 22 November 2026** to `/output/entry.png`, entered in the
[make.fun bounty "Sum up 22 November's world news in one image"](https://make.fun/bounty/news-image-20261122).

## What the image shows

A newspaper front page with the date **22 NOVEMBER 2026** in extra
large type and five stories, each cross-checked across several news
sources reporting that day:

- Iran striking an industrial site in Bahrain as tankers are hit in the Strait of Hormuz
- COP31 climate talks in Antalya entering a second day of overtime over fossil fuels
- Mexican forces capturing cartel boss 'El Chapo Isidro', an FBI ten-most-wanted fugitive
- South Korea's education chief resigning amid an AI cheating scandal
- French protesters rallying for a sixth weekend over living costs and public services

A ticker adds Verstappen's Las Vegas Grand Prix win, Thailand's
plan to block chemical exports used in Myanmar rare-earth mining,
and the EU–Indonesia trade deal.

## How it works

`entry.png` is drawn by `draw_entry.py` (Python + Pillow) before
submission. `main.py` (Python 3.13, standard library only) copies
that finished image to `/output/entry.png`, so two runs in the
offline grading sandbox always write exactly the same bytes.

Run it locally:

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
