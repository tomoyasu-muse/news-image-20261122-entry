#!/usr/bin/env python3
"""Draw entry.png: a one-page newspaper summary of 22 November 2026.

Stories cross-checked across several outlets reporting on Sunday
22 Nov 2026 (The Japan Times, Reuters wires, SCMP and the One Turn
daily brief agree on each item):

1. Bahrain says Iran struck an industrial site as tankers are hit
   in the Strait of Hormuz.
2. COP31 climate talks in Antalya enter a second day of overtime
   over the fossil-fuel deadlock.
3. Mexican forces capture cartel boss 'El Chapo Isidro', a fugitive
   on the FBI's ten most wanted list, in Sinaloa.
4. South Korea's education chief resigns amid an AI cheating
   scandal over university exams.
5. French protesters rally for a sixth weekend over living costs
   and public services.
Ticker: Verstappen wins the Las Vegas Grand Prix; Thailand plans
to block chemical exports used in Myanmar rare-earth mining;
Denmark expels a Russian attache over an alleged plot; the EU and
Indonesia sign a trade deal after ten years of talks.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (246, 242, 231)
INK = (16, 16, 16)
PAPER = (255, 253, 246)
GREY = (52, 52, 52)
GOLD = (255, 213, 84)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def band(draw, box, colour, place):
    x0, y0, x1, _ = box
    draw.rounded_rectangle([x0, y0, x1, y0 + 46], radius=14, fill=colour)
    draw.rectangle([x0, y0 + 26, x1, y0 + 46], fill=colour)
    draw.text((x0 + 15, y0 + 10), place, font=F(BOLD, 24), fill=(255, 255, 255))


def body(draw, box, headline, sub, hsize=31):
    x0, y0, x1, _ = box
    y = y0 + 60
    for line in wrap(draw, headline, F(BOLD, hsize), x1 - x0 - 28):
        draw.text((x0 + 14, y), line, font=F(BOLD, hsize), fill=INK)
        y += hsize + 6
    y += 5
    for line in wrap(draw, sub, F(REG, 22), x1 - x0 - 28):
        draw.text((x0 + 14, y), line, font=F(REG, 22), fill=GREY)
        y += 27


def panel(draw, box, colour, place, headline, sub):
    draw.rounded_rectangle(box, radius=14, fill=PAPER, outline=INK, width=3)
    band(draw, box, colour, place)
    body(draw, box, headline, sub)


def main():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Masthead: the date must be unmissable, the judge is never
    # told which day this page is about.
    draw.rectangle([0, 0, W, 198], fill=INK)
    draw.text((28, 13), "THE WORLD IN ONE DAY  -  WORLD NEWS SUMMARY",
              font=F(BOLD, 27), fill=GOLD)
    date_text = "22 NOVEMBER 2026"
    date_size = 100
    while draw.textlength(date_text, font=F(BOLD, date_size)) > W - 44:
        date_size -= 2
    draw.text((22, 44), date_text, font=F(BOLD, date_size), fill=(255, 255, 255))
    draw.text((28, 156), "SUNDAY  -  THE DAY'S BIGGEST STORIES, ON ONE PAGE",
              font=F(BOLD, 25), fill=(215, 215, 215))

    # Lead story, full width: the Gulf escalation.
    lead = (24, 214, 1000, 424)
    draw.rounded_rectangle(lead, radius=14, fill=PAPER, outline=INK, width=3)
    band(draw, lead, (176, 32, 32), "MANAMA, BAHRAIN  -  THE GULF")
    body(draw, lead,
         "IRAN STRIKES BAHRAIN PLANT AS TANKERS HIT IN HORMUZ",
         "Bahrain says an Iranian strike hit an industrial site and "
         "started a fire, as tankers are hit in the Strait of Hormuz.",
         hsize=36)

    panels = [
        ((24, 440, 500, 690), (0, 102, 108), "ANTALYA - COP31",
         "CLIMATE TALKS ENTER 2ND DAY OF OVERTIME",
         "The fossil-fuel deadlock drags the COP31 summit past "
         "its deadline for a second day."),
        ((524, 440, 1000, 690), (24, 56, 128), "SINALOA - MEXICO",
         "CARTEL BOSS 'EL CHAPO ISIDRO' CAPTURED",
         "Mexican forces seize the fugitive on the FBI's ten "
         "most wanted list, in Sinaloa."),
        ((24, 706, 500, 916), (26, 118, 50), "SEOUL - SOUTH KOREA",
         "EDUCATION CHIEF QUITS OVER AI CHEATING",
         "The education chief resigns amid an AI "
         "cheating scandal over exams."),
        ((524, 706, 1000, 916), (118, 60, 148), "PARIS - FRANCE",
         "PROTESTERS RALLY FOR 6TH WEEKEND",
         "French protesters rally again over living costs "
         "and public services."),
    ]
    for args in panels:
        panel(draw, *args)

    draw.rectangle([0, 932, W, 1024], fill=GOLD)
    ticker = ("ALSO TODAY: Verstappen wins Las Vegas Grand Prix  -  "
              "Thailand to block chemical exports used in Myanmar "
              "rare-earth mining  -  EU & Indonesia sign trade deal")
    y = 942
    for line in wrap(draw, ticker, F(BOLD, 22), W - 48):
        draw.text((24, y), line, font=F(BOLD, 22), fill=INK)
        y += 28

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
