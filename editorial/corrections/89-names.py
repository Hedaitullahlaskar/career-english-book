# Character-name continuity, applied after every per-lesson correction so
# that the per-lesson `find` strings can use the original text.

VENDOR = ["CE-L04-M01-L02", "CE-L04-M01-L03", "CE-L04-M01-L04", "CE-L04-M01-L05", "CE-L04-M08-L02", "CE-L04-CAPSTONE"]
WHY_VENDOR = ("The linen supplier's account manager was called 'Mr. Kabir Hossain' — the same surname as Mr. Hossain, Arif's supervisor in Level 1, "
              "and the same name as Mr. Kabir, the hotel's director (Level 1) and Head of Finance (Level 4). He is renamed Mr. Tariq Mostafa.")
rule("names-vendor-full", r"Mr\. Kabir Hossain", "Mr. Tariq Mostafa", WHY_VENDOR, "continuity",
     fields=("body_html", "practice_html", "objectives_html"), targets=VENDOR)
rule("names-vendor-short", r"\bHossain\b", "Mostafa", WHY_VENDOR, "continuity",
     fields=("body_html", "practice_html", "objectives_html"), targets=VENDOR)

rule("names-guest-delwar", r"\bHossain\b", "Talukder",
     "A loyalty guest was also called 'Mr. Delwar Hossain', a third Hossain in the book (after Arif's supervisor and the vendor). He is renamed Mr. Delwar Talukder.",
     "continuity", fields=("body_html", "practice_html", "objectives_html"), targets=["CE-L04-M02-L01"])
