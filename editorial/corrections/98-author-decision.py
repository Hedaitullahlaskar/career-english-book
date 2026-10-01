# Phase: Author decision
# For changes that carry out a decision recorded in editorial/AUTHOR-DECISIONS.md.
#
# Every fix(...) or rule(...) in this file is logged with source "Author decision"
# (apply_corrections.py adds the label; an optional source= adds detail, such as the the decision, e.g. source="Decision A (linen contract)").
# Rows are appended after the 941 historical entries, which must not change (correction-log-frozen.json).
# More files for this phase can be added as 98-author-decision-<topic>.py.
#
# Example (commented out):
# fix("CE-L01-M01-L01", "exact text to find", "replacement text",
#     "reason for the change", "language", source="...")
