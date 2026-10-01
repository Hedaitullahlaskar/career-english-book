# Level 1 · Module 3 · Greetings & Small Talk

# ---------- 3.1 Formal and Informal Greetings ----------
L = "CE-L01-M03-L01"
fix(L, 'Same morning, three doors down. Arif is a few weeks into the job now, and greetings have stopped feeling like a performance',
    'It\'s a Monday morning, a few weeks into the job, and greetings have stopped feeling like a performance for Arif',
    "'Same morning, three doors down' referred to nothing (this is the first scene of the module).", "continuity")
fix(L, 'Priyanka, a peer from Accounts who joined around the same time as Arif',
    'Priyanka, a front-office colleague who joined a couple of weeks before Arif',
    "Priyanka is Arif's front-office peer throughout the book (she sits next to him from his first day, Lesson 2.2).", "continuity")
fix(L, '<li><strong>hospitality:</strong>', '<li><strong>Hospitality:</strong>', "Industry labels are capitalised elsewhere.", "typography")

# ---------- 3.2 Starting a Conversation ----------
L = "CE-L01-M03-L02"
fix(L, '<li><strong>hospitality/retail:</strong> the same', '<li><strong>Hospitality/retail:</strong> The same',
    "Industry labels are capitalised elsewhere.", "typography")
fix(L, '<li><strong>office:</strong> small talk', '<li><strong>Office:</strong> Small talk', "Industry labels are capitalised elsewhere.", "typography")
fix(L, '<p>Priyanka opens with a workload question before moving on to the weekend and the commute.</p>',
    '<p>"Busy morning so far?" — a question about workload. She then moves on to the weekend and the commute.</p>',
    "The key described the opener but did not quote it.", "answer-key")
fix(L, '<p>"How about you?" is the simplest, most natural way to return a question.</p>',
    '<p><strong>How about</strong> (or <strong>What about</strong>) — "Pretty quiet, actually. How about you?" This is the simplest, most natural way to return a question.</p>',
    "The key did not give the words that fill the blank.", "answer-key")

# ---------- 3.3 Safe and Unsafe Small-Talk Topics ----------
L = "CE-L01-M03-L03"
fix(L, '<p>The right-hand-column topics from the lesson\'s working list all carry a real risk of discomfort; the left-hand ones are broadly safe defaults.</p>',
    '<p><strong>Safe:</strong> weather, weekend plans, local restaurants. <strong>Unsafe / needs care:</strong> salary, religion, relationship status, someone\'s age. '
    '<strong>Depends:</strong> company news — safe when it is public and non-sensitive (a new restaurant opening in the hotel), not when it is about '
    'people\'s jobs, pay or rumours. The key question is whether the topic could make someone uncomfortable or reveal something private.</p>',
    "The answer key did not sort the eight topics and ignored the 'Depends' category the exercise asks for.", "answer-key")

# ---------- 3.4 Ending a Conversation Politely ----------
L = "CE-L01-M03-L04"
fix(L, '<h2>Module 3 assessment</h2>\n<p>This lesson\'s final activity (A04) doubles as the Module 3 capstone: a short, unscripted\nsmall-talk role-play that draws on all four lessons -- choosing the right register (L01),\nopening and following up (L02), staying on safe topics or redirecting when needed (L03), and\nclosing cleanly (L04).</p>',
    '<h2>Module 3 final task</h2>\n<p>Exercise 4 is the final task for Module 3: a short, unscripted small-talk role-play that uses all four lessons — choosing the right register (Lesson 3.1), opening and following up (Lesson 3.2), staying on safe topics or redirecting when needed (Lesson 3.3), and closing cleanly (Lesson 3.4).</p>',
    "Internal activity and lesson codes (A04, L01–L04) replaced; 'capstone' is reserved for the level capstones.", "reference")
fix(L, 'Module 3 capstone. Play a short', 'Module 3 final task. Play a short',
    "'Capstone' is reserved for the end-of-level capstones.", "assessment")
fix(L, '<p>"Get back to it" is the standard phrase for returning to work after small talk.</p>',
    '<p><strong>get back</strong> — "Well, I\'d better get back to it." This is the standard phrase for returning to work after small talk.</p>',
    "The key did not give the words that fill the blanks.", "answer-key")
fix(L, '<p>What to listen/look for: Demonstrates all four Module 3 skills',
    '<p>Scoring: give one point for each of the four Module 3 skills shown',
    "The assessment item had no scoring; it now states what earns credit.", "assessment")
fix(L, 'and a two-part closing line (warm comment + transition back to work).</p>',
    'and a two-part closing line (warm comment + transition back to work). 4 points = task complete; 3 = complete with one weak area to practise; 2 or fewer = repeat the lesson whose skill was missing.</p>',
    "The assessment item had no scoring scale.", "assessment")
