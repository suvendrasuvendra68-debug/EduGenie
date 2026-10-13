def generate_response(prompt: str, mode: str = 'question') -> str:
    p = prompt.lower().strip()
    if mode == 'quiz':
        if 'pythagoras' in p:
            return '''Quiz: Pythagoras Theorem\n\n1. Formula? A) a+b=c B) a²+b²=c² C) a²-b²=c² D) ab=c²\n2. Hypotenuse is? A) Shortest B) Side opposite the right angle C) Base D) Any side\n3. If a=3,b=4, c=? A) 5 B) 6 C) 7 D) 12\n4. Used with? A) Equilateral B) Isosceles C) Right-angled D) Obtuse\n5. 5² = ? A) 10 B) 15 C) 20 D) 25\n\nAnswer Key: 1-B, 2-B, 3-A, 4-C, 5-D'''
        if 'sql' in p:
            return '''Quiz: SQL\n\n1. SQL stands for? A) Simple Query Language B) Structured Query Language C) System Query List D) Standard Question Language\n2. Retrieve data? A) SELECT B) DELETE C) UPDATE D) DROP\n3. Add records? A) INSERT B) SELECT C) ALTER D) WHERE\n4. Filter records? A) ORDER BY B) WHERE C) GROUP BY D) CREATE\n5. Change existing data? A) INSERT B) UPDATE C) SELECT D) CREATE\n\nAnswer Key: 1-B, 2-A, 3-A, 4-B, 5-B'''
        if 'python' in p:
            return '''Quiz: Python\n\n1. Python comment symbol? A) // B) # C) <!-- D) **\n2. Display output? A) print() B) display() C) show() D) output()\n3. True/False type? A) int B) str C) bool D) list\n4. Function keyword? A) function B) def C) fun D) define\n5. Python extension? A) .java B) .cpp C) .py D) .html\n\nAnswer Key: 1-B, 2-A, 3-C, 4-B, 5-C'''
        return f'Quiz: {prompt}\n\n1. What is the basic definition?\n2. What is the main purpose?\n3. Where is it commonly used?\n4. Give one example.\n5. State one advantage.\n\nDemo Mode sample quiz. Gemini can be added later for dynamic quizzes.'
    if mode == 'path':
        if 'sql' in p:
            return '''SQL Learning Path — 4 Weeks\n\nWeek 1: Database basics, tables, SELECT, WHERE, ORDER BY\nWeek 2: INSERT, UPDATE, DELETE, aggregate functions, GROUP BY, JOINs\nWeek 3: Views, indexes, transactions, constraints\nWeek 4: Student database project and query practice\n\nDaily: 45–60 minutes + at least 5 SQL queries.'''
        if 'python' in p:
            return '''Python Learning Path — 4 Weeks\n\nWeek 1: Variables, data types, input/output, operators, conditions, loops\nWeek 2: Lists, tuples, sets, dictionaries, functions, modules, files, exceptions\nWeek 3: OOP, classes, objects, constructors, inheritance, polymorphism\nWeek 4: Build a small Python project\n\nDaily: one concept + 3 small programs.'''
        return f'''Learning Path: {prompt}\n\nStage 1 — Beginner: definitions, terminology, simple examples\nStage 2 — Intermediate: techniques and practical exercises\nStage 3 — Advanced: advanced concepts and real-world examples\nStage 4 — Project: design, implement, test and improve\n\nSuggested timeline: 4 weeks, 45–60 minutes per day.'''
    if mode == 'summary':
        parts = [s.strip() for s in prompt.replace('\n',' ').split('.') if s.strip()]
        if not parts: return 'Please enter some text to summarize.'
        return 'Summary:\n• ' + '\n• '.join(parts[:3])
    if 'largest ocean' in p or 'biggest ocean' in p:
        return 'Answer: The Pacific Ocean is the largest ocean on Earth.'
    if 'pythagoras' in p:
        return 'Pythagoras Theorem: In a right-angled triangle, a² + b² = c². Example: 3² + 4² = 5².'
    if p == 'sql' or 'what is sql' in p:
        return 'SQL stands for Structured Query Language. It is used to create, read, update and delete data in relational databases.'
    if 'python' in p and ('what is' in p or 'define' in p):
        return 'Python is a high-level, general-purpose programming language used for web development, automation, data science and AI.'
    return "Demo Mode: Try 'Which is the largest ocean?', 'What is Pythagoras Theorem?', or 'What is SQL?'. No Gemini API key is required."
