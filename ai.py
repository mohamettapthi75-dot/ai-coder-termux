import requests

API_KEY = "YOUR_GROQ_API_KEY_HERE"
URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.3-70b-versatile"

# Colors
R = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
PURPLE = "\033[95m"

# Languages
LANGS = {
    "1": "so",
    "2": "en",
    "3": "ar"
}

LANG = "so"

SYSTEM = {
    "so": """Adigu waxaad tahay khabiir coding ah. Somali ku jawaab had iyo jeer.
- Code qor oo sharax
- Khaladaadka saxo
- Scripts samee
- Apps dhis tallaabo tallaabo
Koodhka had iyo jeer faallo ku dar.""",
    "en": """You are an expert coding assistant. Always reply in English.
- Write and explain code
- Debug errors
- Generate scripts
- Build apps step by step
Always add comments to code.""",
    "ar": """أنت مساعد برمجة خبير. أجب دائماً باللغة العربية.
- اكتب الكود وشرحه
- صحح الأخطاء
- أنشئ السكريبتات
- ابنِ التطبيقات خطوة بخطوة
أضف دائماً تعليقات للكود."""
}

def ask(messages):
    r = requests.post(URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "messages": [{"role": "system", "content": SYSTEM[LANG]}] + messages
        }
    )
    return r.json()["choices"][0]["message"]["content"]

def lang_menu():
    global LANG
    print(f"\n{CYAN}{BOLD}{'='*35}")
    print("   LUQADDA DOORO / SELECT LANGUAGE")
    print(f"{'='*35}{R}")
    print(f"{GREEN}1. Somali{R}")
    print(f"{BLUE}2. English{R}")
    print(f"{YELLOW}3. Arabic{R}")
    choice = input(f"\n{BOLD}Dooro (1-3): {R}").strip()
    if choice in LANGS:
        LANG = LANGS[choice]
        names = {"so": "Somali", "en": "English", "ar": "Arabic"}
        print(f"{GREEN}Luqadda: {names[LANG]}{R}")

def menu():
    titles = {
        "so": "AI CODER - GROQ",
        "en": "AI CODER - GROQ",
        "ar": "مساعد البرمجة"
    }
    options = {
        "so": [
            "1. Koodh Qor",
            "2. Khalad Saxo",
            "3. App Dhis",
            "4. File Eeg",
            "5. Xor u Hadal",
            "6. Luqad Beddel",
            "0. Bax"
        ],
        "en": [
            "1. Write Code",
            "2. Debug Error",
            "3. Build App",
            "4. Review File",
            "5. Free Chat",
            "6. Change Language",
            "0. Exit"
        ],
        "ar": [
            "1. اكتب كوداً",
            "2. صحح خطأ",
            "3. ابنِ تطبيقاً",
            "4. راجع ملفاً",
            "5. محادثة حرة",
            "6. غير اللغة",
            "0. خروج"
        ]
    }
    print(f"\n{PURPLE}{BOLD}{'='*35}")
    print(f"   {titles[LANG]}")
    print(f"{'='*35}{R}")
    for opt in options[LANG]:
        print(f"{CYAN}{opt}{R}")
    print(f"{PURPLE}{'='*35}{R}")

def get_prompt(choice):
    if choice == "1":
        if LANG == "so":
            lang = input(f"{YELLOW}Language (python/bash/js): {R}")
            desc = input(f"{YELLOW}Maxaad rabta: {R}")
            return f"Koodh {lang} ah qor oo somali ku sharax: {desc}"
        elif LANG == "ar":
            lang = input(f"{YELLOW}اللغة (python/bash/js): {R}")
            desc = input(f"{YELLOW}ماذا تريد: {R}")
            return f"اكتب كود {lang} يقوم بـ: {desc}"
        else:
            lang = input(f"{YELLOW}Language (python/bash/js): {R}")
            desc = input(f"{YELLOW}What do you want: {R}")
            return f"Write a {lang} script that {desc}. Add comments."

    elif choice == "2":
        if LANG == "so":
            err = input(f"{RED}Khaladka paste gare: {R}")
            return f"Khaladkan saxo oo somali ku sharax:\n{err}"
        elif LANG == "ar":
            err = input(f"{RED}الصق الخطأ هنا: {R}")
            return f"صحح هذا الخطأ واشرحه:\n{err}"
        else:
            err = input(f"{RED}Paste error here: {R}")
            return f"Debug this error and explain the fix:\n{err}"

    elif choice == "3":
        if LANG == "so":
            desc = input(f"{BLUE}App-ka sharax: {R}")
            return f"App complete ah dhis: {desc}. Tallaabo tallaabo tus."
        elif LANG == "ar":
            desc = input(f"{BLUE}صف التطبيق: {R}")
            return f"ابنِ تطبيقاً كاملاً: {desc}. خطوة بخطوة."
        else:
            desc = input(f"{BLUE}Describe the app: {R}")
            return f"Build a complete app: {desc}. Show step by step."

    elif choice == "4":
        if LANG == "so":
            path = input(f"{GREEN}File path (tusaale: code.py): {R}")
        elif LANG == "ar":
            path = input(f"{GREEN}مسار الملف: {R}")
        else:
            path = input(f"{GREEN}File path (e.g. code.py): {R}")
        try:
            with open(path) as f:
                code = f.read()
            return f"Review and improve this code:\n```\n{code}\n```"
        except:
            print(f"{RED}File lama helin!{R}")
            return None

    elif choice == "5":
        if LANG == "so":
            return input(f"{CYAN}Su'aashaada: {R}")
        elif LANG == "ar":
            return input(f"{CYAN}سؤالك: {R}")
        else:
            return input(f"{CYAN}Your question: {R}")

    return None

def main():
    global LANG
    print(f"\n{PURPLE}{BOLD}AI Coder - Groq{R}")
    lang_menu()
    messages = []

    while True:
        menu()
        choice = input(f"\n{BOLD}Dooro (0-6): {R}").strip()

        if choice == "0":
            print(f"{GREEN}Bye! 👋{R}")
            break

        if choice == "6":
            lang_menu()
            messages = []
            continue

        prompt = get_prompt(choice)
        if not prompt:
            continue

        messages.append({"role": "user", "content": prompt})
        print(f"\n{GREEN}{BOLD}AI:{R}\n{'-'*35}")

        try:
            reply = ask(messages)
            print(f"{CYAN}{reply}{R}")
            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            print(f"{RED}Error: {e}{R}")

        input(f"\n{YELLOW}[Enter ku riix si aad u sii wadato]{R}")

main()
