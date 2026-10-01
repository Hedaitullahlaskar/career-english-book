# Phase: Human proofread
# For the human proofreader's corrections, from HUMAN-PROOFREAD-REGISTER.csv.
#
# Every fix(...) or rule(...) in this file is logged with source "Human proofread"
# (apply_corrections.py adds the label; an optional source= adds detail, such as the reviewer and page, e.g. source="reviewer initials, PDF p. 52").
# Rows are appended after the 941 historical entries, which must not change (correction-log-frozen.json).
# More files for this phase can be added as 96-human-proofread-<topic>.py.
#
# Example (commented out):
# fix("CE-L01-M01-L01", "exact text to find", "replacement text",
#     "reason for the change", "language", source="...")
