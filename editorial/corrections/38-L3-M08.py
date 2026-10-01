# Level 3 · Module 8 · Pronunciation & Confident Speaking
QA = "QA review of the reference PDF"
CD = "Cambridge Dictionary pronunciation"
D = 16

# ---------- 8.1 Word Stress and Sentence Stress ----------
L = "CE-L03-M08-L01"
STRESS = ("The five versions of 'I didn't say she took it' are meant to differ only in which word is stressed, but the dialogue versions "
          "showed no marking at all and the bold elsewhere was easy to miss; the stressed word is now in bold capitals (CSS class 'stress').")
MARK = {"1": "<strong class=\"stress\">I</strong> didn't say she took it.",
        "2": "I <strong class=\"stress\">DIDN'T</strong> say she took it.",
        "3": "I didn't <strong class=\"stress\">SAY</strong> she took it.",
        "4": "I didn't say <strong class=\"stress\">SHE</strong> took it.",
        "5": "I didn't say she <strong class=\"stress\">TOOK</strong> it."}
rule("L3-8.1-dialogue-stress",
     r"(Version (\d) -- stress on [^<]*</div>.*?<span class=\"dialogue-text\">)I didn't say she took it\.",
     lambda m: m.group(1) + MARK[m.group(2)],
     STRESS, "pronunciation", fields=("body_html",), flags=D, targets=[L], expect=5)
rule("L3-8.1-bold-to-stress", r"<strong>(I|didn't|say|she|took)</strong>(?= ?(?:didn't|say|she|took|it))",
     lambda m: '<strong class="stress">' + m.group(1).upper() + "</strong>",
     STRESS, "pronunciation", fields=("body_html", "practice_html"), targets=[L], expect=15)
rule("L3-8.1-meaning-label", r'<span class="dialogue-speaker">note:</span> <span class="dialogue-text">Meaning -- ',
     '<span class="dialogue-speaker">Meaning:</span> <span class="dialogue-text">',
     "A pseudo-speaker 'note:' was used for the meaning lines.", "structure", fields=("body_html",), targets=[L], expect=5)
fix(L, 'landing hard on the <strong>bold</strong>', 'landing hard on the word in <strong>bold capitals</strong>', STRESS, "pronunciation")
fix(L, '<p>The same seven words, with the stress', '<p>The same six words, with the stress',
    "'I didn't say she took it' has six words, not seven.", "factual")
fix(L, 'All five versions use the exact same seven words', 'All five versions use the exact same six words',
    "'I didn't say she took it' has six words, not seven.", "factual")
fix(L, '"comfortable" has four syllables\n (com-fort-a-ble).',
    '"comfortable" has four syllables when said carefully (com-fort-a-ble), and in everyday speech often three (COMF-ta-ble) — the stress stays on the first.',
    "Both pronunciations are standard; learners will hear the three-syllable form far more often.", "pronunciation", source=CD + ", 'comfortable'")
fix(L, 'the new information is <em>report</em> and <em>three</em> -- so those get the stress, and <em>I</em>, <em>need</em>,\n<em>the</em>, and <em>by</em> stay light.',
    'the content words are <em>need</em>, <em>report</em> and <em>three</em> — so those are stressed, with the strongest stress on the new information, <em>report</em> and <em>three</em>; <em>I</em>, <em>the</em> and <em>by</em> stay light.',
    "The tip said 'need' stays light, contradicting the lesson's own pattern ('I NEED the REPORT by THREE') and Exercise 3.", "pronunciation")
fix(L, '<p>Match each version of "I didn\'t say she took it" (stress shown in bold) to what it actually means.</p>',
    '<p>Match each version of "I didn\'t say she took it" (the stressed word is in bold capitals) to what it means. Meanings: (a) I never said that at all. (b) I said she did something else with it, not "took". (c) Someone else said it, not me. (d) I said someone else took it, not her. (e) I didn\'t say it outright — I only implied it.</p>',
    "The matching exercise gave no meanings to match against, so it could not be answered without copying the lesson table.",
    "answer-key", source=QA + " pp.499–501")
rule("L3-8.1-matching-key", r'(<span class="answer-number">2\.</span> <p>).*?(All five versions)',
     r"""\1(1) <strong class="stress">I</strong> → (c). (2) <strong class="stress">DIDN'T</strong> → (a). (3) <strong class="stress">SAY</strong> → (e). (4) <strong class="stress">SHE</strong> → (d). (5) <strong class="stress">TOOK</strong> → (b). \2""",
     "Answer key rewritten to match the lettered meanings.", "answer-key", fields=("practice_html",), flags=D, targets=[L], expect=1)

# ---------- 8.3 Connected Speech and Commonly Confused Sounds ----------
L = "CE-L03-M08-L03"
LINK = "The linking notation 'loo‿k‿into‿it' was garbled; 'into it' joins vowel to vowel with a light /w/ glide."
fix(L, "<td>We'll loo‿k‿into‿it.</td>", "<td>We'll loo‿kin‿to‿(w)it.</td>", LINK, "pronunciation")
fix(L, '<strong>We\'ll loo‿k‿into‿it</strong> (the final consonant of "look" slides onto the\nvowel that follows, and "into" then glides smoothly into the vowel that starts "it")',
    '<strong>We\'ll loo‿kin‿to‿(w)it</strong> (the final /k/ of "look" slides onto "into", and a light /w/ sound joins "into" to "it", because one word ends and the next begins with a vowel)',
    LINK, "pronunciation")
fix(L, '(sounds like "wery," not a real word, or drifts toward\n"very"/"wary" ambiguity)',
    '("wery" is not a word, so the listener has to guess; with pairs such as vest/west or vine/wine, the mix-up produces a different real word)',
    "The explanation was muddled ('drifts toward very/wary ambiguity').", "pronunciation")
rule("L3-8.3-l1-note", r"(<blockquote>\s*<p>)Bengali/Hindi note: Bengali does not treat.*?(</p>\s*</blockquote>)",
     r"""\1Bengali/Hindi note: Bengali has no separate /v/ and /w/ sounds, and Hindi व is used for both, so "very" and "wary", "vest" and "west" can sound the same. With /s/ and /sh/, the pattern differs: many Bengali speakers pronounce স, শ and ষ all as /ʃ/, so "see" can come out as "she", while some Hindi speakers do the reverse ("she" → "see"). These are not errors in Bengali or Hindi — they are different sound systems. In English these pairs distinguish real words, so a few minutes of targeted practice on exactly these pairs goes further than general pronunciation drilling.\2""",
     "The note was vague ('narrow the gap … in certain positions'); it now names the specific patterns: Bengali s→sh, Hindi sh→s for some speakers, and the v/w merger.",
     "l1-support", fields=("body_html",), flags=D, targets=[L], expect=1)

# ---------- 8.4 Speaking with Confidence ----------
L = "CE-L03-M08-L04"
fix(L, '<div class="dialogue-note">Good <strong>AFTERnoon</strong>, everyone. ↘ [pause] I\'ll be walking you <strong>THROUGH</strong> las‿t‿month\'s <strong>FRONT</strong>-desk guest-satisfaction <strong>SCORES</strong>, ↘ [pause] and what we\'re <strong>DOING</strong> to raise them further this <strong>QUARter</strong>. ↘</div>',
    '<div class="dialogue-note">Good after<strong>NOON</strong>, everyone. ↘ [pause] I\'ll be <strong>WALK</strong>ing you through <strong>LAST</strong> month\'s front-desk <strong>GUEST</strong>-satisfaction <strong>SCORES</strong>, ↘ [pause] and what we\'re <strong>DO</strong>ing to <strong>RAISE</strong> them this <strong>QUAR</strong>ter. ↘</div>',
    "'Afternoon' is stressed on its last syllable (af-ter-NOON), not 'AFTERnoon'; the preposition 'through' should not carry the main stress; "
    "'las‿t‿month's' misrepresents the common dropping of /t/ before /m/ (\"las' month\"); stress is now marked on syllables, as everywhere else in the book.",
    "pronunciation", source=CD + ", 'afternoon'")
fix(L, "-- scored holistically for clarity, stress, and confidence markers, per the curriculum map's Module 8 assessment strategy.</p>",
    "— score 0–4, one point each for content-word stress, falling intonation on statements, natural linking, and no more than one or two fillers. Pass at 3.</p>",
    "Production language ('per the curriculum map') and no scoring scale.", "assessment")
