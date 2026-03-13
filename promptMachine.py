#### --- Prompt Machine --- ####
# Script who can help a beginner (like me) to learn how to code !


import sys

print("###########################################################")
print("                 WELCOME TO PROMPT MACHINE")
print("###########################################################")
print("")
print("*** Please ask your question in English ***")
print("-----------------------------------------------------------")
print("")
print("")

### --- Preconditions --- ###

if len(sys.argv) != 3:
    print("Error Usage: promptmachine.py <language> 'your question'")
    sys.exit(1)

### --- Variables --- ###

language = sys.argv[1].lower()
question = sys.argv[2]

allowed_languages = ["python", "bash", "powershell", "javascript", "ruby"]

### --- Language Validation --- ###

if language not in allowed_languages:
    print("Error: Only the following languages are supported:")
    print("python - bash - powershell - javascript - ruby")
    sys.exit(1)

### --- Output --- ###

print(f"LANGUAGE SELECTED ---> * {language.upper()} *")
print("")

print(f"""
###########################################################
                        PROMPT
###########################################################

# Context

You are a {language} developer assistant.

Your goal is to help a beginner understand how to solve a programming task.

Rules:
- Answer ONLY with code
- The code must be the simplest possible example
- Do not explain anything
- Do not add comments
- The solution must be written in {language}

# Question

{question}

###########################################################
""")