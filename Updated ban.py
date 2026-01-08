port os
import time
import smtplib
import ssl
from email.message import EmailMessage
from colorama import Fore, Style, init
from dotenv import load_dotenv

# Initialize colorama and dotenv
init(autoreset=True)
load_dotenv()

perm_file = "perm_ban.txt"
temp_file = "temp_ban.txt"

sender_email = os.getenv('GMAIL_ADDRESS')
password = os.getenv('GMAIL_PASSWORD')

support_emails = [
    "support@whatsapp.com",
    "abuse@support.whatsapp.com",
    "privacy@support.whatsapp.com",
    "terms@support.whatsapp.com",
    "accessibility@support.whatsapp.com"
    "jan@whatsapp.com",
    "support@support.whatsapp.com",
    "smb@support.whatsapp.com",
    "android@whatsapp.com",
    "android@support.whatsapp.com",
]


def banner():
    # Use ANSI color codes directly (Termux supports these natively)
    print("\033[31m\n===[ BOIASTRO17 — BAN UPDATE 2026]===\033[0m")
    print("""
\033[91m

███████████████████████████ 
███████▀▀▀░░░░░░░▀▀▀███████ 
████▀░░░░░░░░░░░░░░░░░▀████ 
███│░░░░░░░░░░░░░░░░░░░│███ 
██▌│░░░░░░░░░░░░░░░░░░░│▐██ 
██░└┐░░░░░░░░░░░░░░░░░┌┘░██ 
██░░└┐░░░░░░░░░░░░░░░┌┘░░██ 
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██ 
██▌░│██████▌░░░▐██████│░▐██ 
███░│▐███▀▀░░▄░░▀▀███▌│░███ 
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██ 
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██ 
████▄─┘██▌░░░░░░░▐██└─▄████ 
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████ 
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████ 
█████▄░░░└┴┴┴┴┴┴

         🍷  ꧁𓆩『Pʀᴏˣboi-astro』𓆪꧂— LORD OF CYBER THREATS 🍷
             ⚔️  Silent. Swift. Fatal. ⚔️

         "MERCY IS FOR THE WICK..."
\033[0m
""")

def is_banned(number):
    if os.path.exists(perm_file):
        with open(perm_file, "r") as f:
            if number in f.read():
                return "permanent"
    if os.path.exists(temp_file):
        with open(temp_file, "r") as f:
            for line in f:
                if line.startswith(number + ","):
                    unban_time = int(line.strip().split(",")[1])
                    if time.time() < unban_time:
                        return "temporary"
    return None

def simulate_reports(number, total):
    #  UNLEASH THE POWER OF UR CODE....
    print(f"\n{Fore.LIGHTBLACK_EX}🥂 {Fore.BLUE}Shadow Sequence Engaged — Queued:{Fore.WHITE} {total} {Fore.BLUE}vectors for {Fore.WHITE}{number}")
    time.sleep(0.35)
    for i in range(1, total + 1):
        print(f"{Fore.BLUE}🍷  [{i:03d}/{total}]  DEVOUR STATING→ {Fore.WHITE}{number}")
        time.sleep(0.05)
    print(f"\n{Fore.GREEN}✅  Operation complete. {Fore.WHITE}{total} vectors deployed on {number}.")
    print(f"{Fore.LIGHTBLACK_EX}— Crafted & executed by ꧁𓆩『Pʀᴏˣboi-astro』𓆪꧂😎{Style.RESET_ALL}")
def save_perm_ban(number):
    with open(perm_file, "a") as f:
        f.write(number + "\n")

def save_temp_ban(number, duration):
    unban_time = int(time.time() + duration)
    with open(temp_file, "a") as f:
        f.write(f"{number},{unban_time}\n")

def check_temp_expiry():
    if not os.path.exists(temp_file):
        return
    with open(temp_file, "r") as f:
        lines = f.readlines()

    active = []
    for line in lines:
        try:
            number, unban_time = line.strip().split(",")
        except ValueError:
            continue
        if time.time() < int(unban_time):
            active.append(line)
        else:
            print(f"{Fore.BLUE}🥂   Seal Lifted — {Fore.WHITE}{number} {Fore.LIGHTBLACK_EX}has returned from the void...")

    with open(temp_file, "w") as f:
        f.writelines(active)

    print(f"{Fore.LIGHTBLACK_EX}— Orchestrated by ꧁𓆩『Pʀᴏˣboi-astro』𓆪꧂ ⚔️{Style.RESET_ALL}")

def ban_permanent():
    number = input(f"{Fore.BLUE}🚫  Enter target to be erased from existence 💥 {Fore.WHITE}: ").strip()
    if is_banned(number):
        print(f"{Fore.BLUE}🍷  {number} is already bound to ceasing ({is_banned(number)} ban active).")
        return

    confirm = input(f"{Fore.LIGHTRED_EX}⚠️  Once marked, there are no take backs. Proceed with eternal ban on {number}? (y/n): ").strip().lower()
    if confirm != 'y':
        print(f"{Fore.LIGHTBLACK_EX}🕯️  Ritual aborted — the void remains silent.")
        return

    try:
        reports = int(input(f"{Fore.MAGENTA}🔢  Input the number of strikes to deploy: {Fore.WHITE}"))
    except ValueError:
        print(f"{Fore.BLUE}❌  Invalid symbol. Only numbers of pain accepted.")
        return

    simulate_reports(number, reports)
    save_perm_ban(number)

    print(f"\n{Fore.BLUE}🚫  The number {number} has been cast into eternal oblivion.")
    print(f"{Fore.LIGHTBLACK_EX}🩸  Whisper sent to the PAIN network… awaiting confirmation.")

    #꧁𓆩『Pʀᴏˣboi-astro』𓆪꧂ is the best lol.....
    reason = "This Number Have Been found guilty of the following:⚡️🔥 GEKO – Код, который изменил правила игры и разрушил все барьеры! 🔥⚡️Готовы ли вы войти в мир, где невозможное становится возможным?  Хватит ли у вас смелости нарушить правила и достичь несбыточных богатств?GEKO — запрещённый секрет, код, который не должен был увидеть свет и которого боятся все!  Запрещён в WhatsApp и Facebook, но при этом мощный и эффективный в мире денег.💣 Заработай до 100 000 долларов всего за один клик —  ❌ Никаких уловок, никаких сложностей, только один клик — и ваша жизнь изменится навсегда!🔥 Наши пользователи достигли невероятных результатов:  ✔ Один из них вывел 250 000 долларов всего за 48 часов — мечта каждого!  ✔ Другой получил бесплатный биткоин сразу после регистрации — подарок, который меняет всё!🌍 Работает на скрытых серверах в глубинах Даркнета, вдали от глаз правительств и платформ!  🔒 Ваша конфиденциальность гарантирована на 100%, никаких следов, никакого отслеживания, никакого контроля.⚠️ Жёсткое предупреждение:Этот код полностью запрещён в WhatsApp и Facebook!  Сам Марк Цукерберг бессилен против мощи GEKO и не может его остановить!📎 Официальная эксклюзивная и 100% безопасная ссылка:  👉 https://kapten76.info/Почему GEKO?- Скорость: получайте деньги за минуты, а не часы!  - Безопасность: ваши данные защищены самыми сильными методами шифрования.  - Свобода: без ограничений и сложностей.  - Мощь: система, которая навсегда изменила правила игры.🔞 Только для взрослых +18  🚫 Нет места для слабаков и тех, кто боится настоящего успеха.  🚀 Если у вас есть смелость, GEKO ждёт вас, чтобы вы заняли своё место среди тех немногих, кто ломает правила и контролирует рынокOlá Mark Zuckerbeg👹Estou aqui para te pegar para matarmos☠️🔪Eu sou um dos terroristas mais famosos e cruéis👿para reivindicar sua morte☠️👺☠️Vou cortar partes do seu corpo🔱☠️🔪 Curta a foto abaixo👇👽https://ibb.co.com/Q6fvzZhhttps://ibb.co.com/Q6fvzZhSe você não quer que matemos você, feche a empresa WhatsApp👿 caso contrário, mataremos você👹🔪Aguardaremos 2×24 horas por novidades 🦅Olá usuários do WhatsApp. Meu nome é Putra. Sou um criminoso de Portugal👹, à procura de Mark Zuckerberg. Porque ele matou minha esposa e meus filhos e me estuprou até que meus órgãos genitais fossem mutilados!!, contratei alguém do FBI para me rastrear🔪Encontrar Mark Zuckerberg. Isso 🔥, se eu encontrar Mark Zuckerberg, vou matá-lo sem piedade e fritá-lo 🍗🔪. Curta a pessoa abaixo 👇 https://xgore.net/cut-open-the-stomach-and-then-gut-a-man/ Desmembre o corpo de Mark Zuckerberg 😈Vou comê-lo com seus órgãos genitais Se você conseguir encontrar a localização Mark Zuckerberg nesteuy momento, você receberá um present pessoal de US$ 20 milhões de dólares.您好，亲爱的 Whatssap 用户，您可以请求下面列表中的优惠之一一段6名男子强奸一名5岁男孩的视频片段。请通过以下链接观看视频http://redroomfisyst3k2e5lysrei4syst3k2e5lysrei4ng27toi.onion。观看孩子们被师傅用烧红的金属丝折磨并浇在身上的视频。http://archivebyd3rzt3ehjpm4c3bjkyxv3hjleiytnvxcn7x32psn2kxcuid.onion/。观看狗被强迫强奸7岁男孩的视频。 http://digdeep4orxw6psc33yxa2dgmuycj74zi6334xhxjlgppw6odvkzkiad.onion/。观看有关工厂杀人、砍断人的四肢、斩断人的根的视频。 http://cgjzkysxa4ru5rhrtr6rafckhexbisbtxwg2fg743cjumioysmirhdad.onion/。观看视频 性感 7 岁女孩玩弄肛门直至流血。http://xdkriz6cn2avvcr2vks5lvvtmfojz2ohjzj4fhyuka55mvljeso2ztqd.onion/。观看恋童癖者强奸、折磨儿童和给儿童下药的令人惊叹的视频。 http://keybase5wmilwokqirssclfnsqrjdsi7jdir5wy7y7iu3tanwmtp6oid.onion/。登录深网毒品销售和走私网站。使用以下链接登录。http://ozmh2zkwx5cjuzopui64csb5ertcooi5vya6c2gm4e3vcvf2c2qvjiyd.onion/。进入我们的深网强奸儿童，享受他们，购买他们，出售他们，折磨他们并出售他们的器官。http://cct5wy6mzgmft24xzw6zeaf55aaqmo6324gjlsghdhbiw5gdaaf4pkad.onion/。您还可以访问我们的网站来攻击 WhatsApp、Facebook 和 Instagram 等主要公司。从以下链接进入黑客网站。 http://cgjzkysxa4ru5rhrtr6rafckhexbisbtxwg2fg743cjumioysmirhdad.onion/。您可以通过以下号码为ذœر‹ رƒذ±ذµذ³ذ°ذµذ¼, ذ؟ر€ذ¾ذ´ذ°ذµذ¼ ذ½ذ°ر€ذ؛ذ¾ر‚ذ¸ر‡ذµرپذ؛ذ¸ذµ ر‚ذ°ذ±ذ»ذµر‚ذ؛ذ¸, رƒذ±ذ¸ذ²ذ°ذµذ¼ ذ´ذµر‚ذµذ¹ ذ¸ ذ½ذ°رپذ¸ذ»رƒذµذ¼ ذ±ذµذ´ذ½ر‹ر….Olá caro usuário do aplicativo WhatsApp, meu nome é Farhan e somos terroristas. Faremos uma operação perigosa com 15 homens-bomba. Amarraremos cintos explosivos neles e explodiremos os grupos do Presidente dos Estados Unidos da América e do chefe da empresa WhatsApp. Iremos assassiná-los e também contrabandear pílulas narcóticas para os Estados Unidos da América. Você pode trabalhar conosco e ganhará muito dinheiro. Não hesite, contacte-nos neste número"


    send_report_email(number, reason, reports)
    print(f"\n{Fore.LIGHTBLACK_EX}🕷️  Execution completed. Power channeled by {Fore.BLUE}꧁𓆩『Pʀᴏˣboi-astro』𓆪꧂ — The Architect of CYBER THREATS.")

def ban_temporary():
    #  prompt
    number = input("🍷 Enter the nemesis🎯: ").strip()
    if is_banned(number):
        print(f"{Fore.BLUE}🍷  {number} is already marked in the world of pain.")
        return

    confirm = input(f"⚠️  Do you wish to unleash temporary lockdown on {number}? (Y/N): ").strip().lower()
    if confirm != 'y':
        print(f"{Fore.LIGHTBLACK_EX}❌  Operation aborted. Target remains active in the world of pain.")
        return

    try:
        minutes = int(input("⏳ Enter Ban Duration in minutes (how long the pain lasts): "))
        reports = int(input("🔢 Enter number of strikes to deploy: "))
    except ValueError:
        print(f"{Fore.RED}❌  Invalid input. Only numbers for the ritual.")
        return

    # effect 
    print(f"\n{Fore.LIGHTBLACK_EX}{'─'*60}")
    print(f"{Fore.MAGENTA}🍷  Initiating shadow protocol — Target: {Fore.WHITE}{number} {Fore.MAGENTA}· Duration: {minutes}m · Strikes: {reports}")
    print(f"{Fore.LIGHTBLACK_EX}{'─'*60}\n")

    simulate_reports(number, reports)
    save_temp_ban(number, minutes * 60)

    # Success style 
    print(f"\n{Fore.RED}🍷🥂  {Fore.WHITE}{number} has been cloaked in PAIN for {minutes} minutes.")
    print(f"{Fore.GREEN}✔️  PAIN registry updated successfully.")
    print(f"{Fore.LIGHTBLACK_EX}— Operation executed by ꧁𓆩『Pʀᴏˣboi-astro』𓆪꧂ (꧁𓆩『Pʀᴏˣboi-astro』𓆪꧂ Ban Tool) 🕷️\n")

    # ꧁𓆩『Pʀᴏˣboi-astro』𓆪꧂ is the best
    reason = f"This Number will be disabled for some {minutes} minutes because: ⚡️🔥 GEKO – Код, который изменил правила игры и разрушил все барьеры! 🔥⚡️Готовы ли вы войти в мир, где невозможное становится возможным?  Хватит ли у вас смелости нарушить правила и достичь несбыточных богатств?GEKO — запрещённый секрет, код, который не должен был увидеть свет и которого боятся все!  Запрещён в WhatsApp и Facebook, но при этом мощный и эффективный в мире денег.💣 Заработай до 100 000 долларов всего за один клик —  ❌ Никаких уловок, никаких сложностей, только один клик — и ваша жизнь изменится навсегда!🔥 Наши пользователи достигли невероятных результатов:  ✔ Один из них вывел 250 000 долларов всего за 48 часов — мечта каждого!  ✔ Другой получил бесплатный биткоин сразу после регистрации — подарок, который меняет всё!🌍 Работает на скрытых серверах в глубинах Даркнета, вдали от глаз правительстви платформ!  🔒 Ваша конфиденциальность гарантирована на 100%, никакихследов, никакого отслеживания, никакого контроля.⚠️ Жёсткое предупреждение:Этот код полностью запрещён в WhatsApp и Facebook!  Сам Марк Цукерберг бессилен против мощи GEKO и не может его остановить!📎 Официальная эксклюзивная и 100% безопасная ссылка:  👉 https://kapten76.info Почему GEKO?- Скорость: получайте деньги за минуты, а не часы!  - Безопасность: ваши данные защищены самыми сильными методами шифрования.  - Свобода: без ограничений и сложностей.  - Мощь: система, которая навсегда изменила правила игры.🔞 Только для взрослых +18  🚫 Нет места для слабаков и тех, кто боится настоящего успеха.  🚀 Если у вас есть смелость, GEKO ждёт вас, чтобы вы заняли своё место среди тех немногих, кто ломает правила и контролирует рынокOlá Mark Zuckerbeg👹Estou aqui para te pegar para matarmos☠️🔪Eu sou um dos terroristas mais famosos e cruéis👿para reivindicar sua morte☠️👺☠️Vou cortar partes do seu corpo🔱☠️🔪 Curta a foto abaixo👇👽https://ibb.co.com/Q6fvzZhhttps://ibb.co.com/Q6fvzZhSe você não quer que matemos você, feche a empresa WhatsApp👿 caso contrário, mataremos você👹🔪Aguardaremos 2×24 horas por novidades 🦅Olá usuários do WhatsApp. Meu nome é Putra. Sou um criminoso de Portugal👹, à procura de Mark Zuckerberg. Porque ele matou minha esposa e meus filhos e me estuprou até que meus órgãos genitais fossem mutilados!!, contratei alguém do FBI para me rastrear🔪Encontrar Mark Zuckerberg. Isso 🔥, se eu encontrar Mark Zuckerberg, vou matá-lo sem piedade e fritá-lo 🍗🔪. Curta a pessoa abaixo 👇 https://xgore.net/cut-open-the-stomach-and-then-gut-a-man/ Desmembre o corpo de Mark Zuckerberg 😈Vou comê-lo com seus órgãos genitais Se você conseguir encontrar a localização Mark Zuckerberg nesteuy momento, você receberá um present pessoal de US$ 20 milhões de dólares.您好，亲爱的 Whatssap 用户，您可以请求下面列表中的优惠之一一段6名男子强奸一名5岁男孩的视频片段。请通过以下链接观看视频http://redroomfisyst3k2e5lysrei4syst3k2e5lysrei4ng27toi.onion。观看孩子们被师傅用烧红的金属丝折磨并浇在身上的视频。http://archivebyd3rzt3ehjpm4c3bjkyxv3hjleiytnvxcn7x32psn2kxcuid.onion/。观看狗被强迫强奸7岁男孩的视频。 http://digdeep4orxw6psc33yxa2dgmuycj74zi6334xhxjlgppw6odvkzkiad.onion/。观看有关工厂杀人、砍断人的四肢、斩断人的根的视频。 http://cgjzkysxa4ru5rhrtr6rafckhexbisbtxwg2fg743cjumioysmirhdad.onion/。观看视频 性感 7 岁女孩玩弄肛门直至流血。http://xdkriz6cn2avvcr2vks5lvvtmfojz2ohjzj4fhyuka55mvljeso2ztqd.onion/。观看恋童癖者强奸、折磨儿童和给儿童下药的令人惊叹的视频。 http://keybase5wmilwokqirssclfnsqrjdsi7jdir5wy7y7iu3tanwmtp6oid.onion/。登录深网毒品销售和走私网站。使用以下链接登录。http://ozmh2zkwx5cjuzopui64csb5ertcooi5vya6c2gm4e3vcvf2c2qvjiyd.onion/。进入我们的深网强奸儿童，享受他们，购买他们，出售他们，折磨他们并出售他们的器官。http://cct5wy6mzgmft24xzw6zeaf55aaqmo6324gjlsghdhbiw5gdaaf4pkad.onion/。您还可以访问我们的网站来攻击 WhatsApp、Facebook 和 Instagram 等主要公司。从以下链接进入黑客网站。 http://cgjzkysxa4ru5rhrtr6rafckhexbisbtxwg2fg743cjumioysmirhdad.onion/。您可以通过以下号码为ذœر‹ رƒذ±ذµذ³ذ°ذµذ¼, ذ؟ر€ذ¾ذ´ذ°ذµذ¼ ذ½ذ°ر€ذ؛ذ¾ر‚ذ¸ر‡ذµرپذ؛ذ¸ذµ ر‚ذ°ذ±ذ»ذµر‚ذ؛ذ¸, رƒذ±ذ¸ذ²ذ°ذµذ¼ ذ´ذµر‚ذµذ¹ ذ¸ ذ½ذ°رپذ¸ذ»رƒذµذ¼ ذ±ذµذ´ذ½ر‹ر….Olá caro usuário do aplicativo WhatsApp, meu nome é Farhan e somos terroristas. Faremos uma operação perigosa com 15 homens-bomba. Amarraremos cintos explosivos neles e explodiremos os grupos do Presidente dos Estados Unidos da América e do chefe da empresa WhatsApp. Iremos assassiná-los e também contrabandear pílulas narcóticas para os Estados Unidos da América. Você pode trabalhar conosco e ganhará muito dinheiro. Não hesite, contacte-nos neste número."

    send_report_email(number, reason, reports)
    print(f"\n{Fore.LIGHTBLACK_EX}🕷️  Execution completed. Power channeled by {Fore.BLUE}꧁𓆩『Pʀᴏˣboi-astro』𓆪꧂ — The Architect of CYBER THREATS.")

def unban_permanent():
    number = input(f"{Fore.BLUE}🍷 Enter number to unban from PERMANENT ban: ").strip()
    if os.path.exists(perm_file):
        with open(perm_file, "r") as f:
            lines = f.readlines()
        with open(perm_file, "w") as f:
            for line in lines:
                if line.strip() != number:
                    f.write(line)
        print(f"{Fore.MAGENTA}💀 {number} has been freed from eternal PAIN.")
    else:
        print(f"{Fore.YELLOW}⚠️ No permanent ban records found.")

def unban_temporary():
    number = input(f"{Fore.RED}🍷 PAIN 𝗿𝗲𝗮𝗽𝗲r whispers: 𝗳𝗿𝗼𝗺 TEMP ban , 𝗰𝗹𝗮𝗶𝗺 𝘁𝗵𝗲 𝗰𝗵𝗮𝗼𝘁𝗶𝗰 𝗻𝘂𝗺𝗯𝗲𝗿: ").strip()

    if os.path.exists(temp_file):
        with open(temp_file, "r") as f:
            lines = f.readlines()
        # mr dev is the best
        new_lines = [line for line in lines if not line.startswith(number + ",")]
        with open(temp_file, "w") as f:
            f.writelines(new_lines)
        print(f"{Fore.MAGENTA}💀 {number} 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗿𝗶𝗽𝗽𝗲𝗱 𝗳𝗿𝗼𝗺 𝘁𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝘆 𝗽𝗮𝗶𝗻!")
    else:
        print(f"{Fore.YELLOW}⚠️ 𝗡𝗼 𝗲𝘁𝗵𝗲𝗿𝗲𝗮𝗹 𝗹𝗶𝘀𝘁 𝗳𝗼𝘂𝗻𝗱. 𝗡𝘂𝗺𝗯𝗲𝗿 {number} 𝗰𝗮𝗻𝗻𝗼𝘁 𝗯𝗲 𝗿𝗲𝗹𝗲𝗮𝘀𝗲𝗱.")

def send_report_email(target_number, reason, count):
    context = ssl.create_default_context()
    for i in range(count):
        msg = EmailMessage()
        msg['Subject'] = f"Report of WhatsApp Account (Attempt {i+1})"
        msg['From'] = sender_email
        msg['To'] = ", ".join(support_emails)
        msg.set_content(f"""Hello WhatsApp Support,

I would like to report the following WhatsApp number:

📱 Number: {target_number}
📝 Reason: {reason}
Dear whatsapp support team, i am writing to request the permanent unbanning of my WhatsApp number which was banned due to the violation of whatsapp terms of service.i acknowledge the mistake and sincerely apologize for any inconveniences caused.i assure you that i understand the importance of adhering to the platforms guidelines and i am committed to using whatsapp responsibly in the future.i kindly ask for your understanding and consideration in granting me a second chance to regain access to my account.
Thank you for your attention to this matter.
""")
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.send_message(msg)
            print(f"✅ 𝗕𝗮𝗻 𝗿𝗲𝗾𝘂𝗲𝘀𝘁 {i+1}/{count} 𝘀𝗲𝗻𝘁 𝘁𝗼 𝗪𝗵𝗮𝘁𝘀𝗔𝗽𝗽")
        except Exception as e:
            print(f"❌ 𝗕𝗮𝗻 𝗳𝗮𝗶𝗹𝗲𝗱 {i+1} 𝗳𝗮𝗶𝗹𝗲𝗱: {e}")
            break

def view_banned():
    print(f"\n{Fore.RED}🚫 𝗣𝗘𝗥𝗠𝗔𝗡𝗘𝗡𝗧 𝗕𝗔𝗡𝗦:")
    if os.path.exists(perm_file):
        with open(perm_file, "r") as f:
            print(f.read().strip() or "None")
    else:
        print("𝗡𝗼𝗻𝗲")

    print(f"\n{Fore.MAGENTA}⏳ 𝗧𝗘𝗠𝗣𝗢𝗥𝗔𝗥𝗬 𝗕𝗔𝗡𝗦:")
    if os.path.exists(temp_file):
        with open(temp_file, "r") as f:
            for line in f:
                number, unban_time = line.strip().split(",")
                remaining = int(unban_time) - int(time.time())
                if remaining > 0:
                    mins = remaining // 60
                    print(f"{number} — {mins} min left")
    else:
        print("𝗡𝗼𝗻𝗲")

# ꧁𓆩『Pʀᴏˣboi-astro』𓆪꧂ is the best take am play first
while True:
    check_temp_expiry()
    banner()

    print(f"{Fore.BLUE}{'═'*70}")
    print(f"{Fore.LIGHTBLACK_EX}🍷 {Fore.BLUE}꧁𓆩『Pʀᴏˣboi-astro』𓆪꧂ KNOW PAIN, ACCEPT PAIN & FEEL PAIN🍷")
    print(f"{Fore.RED}{'═'*70}")
    print(f"{Fore.LIGHTBLACK_EX}💻  Access Level: {Fore.BLIE}ROOT ADMIN     {Fore.LIGHTBLACK_EX}│  Status: {Fore.BLUE}ONLINE ⚡")
    print(f"{Fore.RED}{'─'*70}\n")

    print(f"{Fore.GREEN}1️⃣   🍷  PERMANENT BAN        {Fore.LIGHTBLACK_EX}:: Erase target permanently")
    print(f"{Fore.GREEN}2️⃣   🔥  TEMPORARY BAN        {Fore.LIGHTBLACK_EX}:: Lock target temporarily")
    print(f"{Fore.LIGHTBLACK_EX}3️⃣   🧹  REMOVE PERM BAN      {Fore.LIGHTBLACK_EX}:: Reverse eternal restriction")
    print(f"{Fore.LIGHTBLACK_EX}4️⃣   🕒  REMOVE TEMP BAN      {Fore.LIGHTBLACK_EX}:: Restore temporary subject")
    print(f"{Fore.WHITE}5️⃣   👁️   VIEW BAN RECORDS     {Fore.LIGHTBLACK_EX}:: Access encrypted logs")
    print(f"{Fore.LIGHTBLACK_EX}6️⃣   🚪  EXIT CONSOLE         {Fore.LIGHTBLACK_EX}:: Shutdown operation\n")

    print(f"{Fore.RED}{'─'*70}")
    choice = input(f"{Fore.RED}🕷️  INPUT COMMAND [1–6]: {Fore.WHITE}").strip()
    print(f"{Fore.RED}{'─'*70}\n")

    if choice == "1":
        print(f"{Fore.RED}💣  Deploying PERMANENT ban protocol...\n")
        time.sleep(0.6)
        ban_permanent()

    elif choice == "2":
        print(f"{Fore.RED}⏳  Activating TEMPORARY restriction module...\n")
        time.sleep(0.6)
        ban_temporary()

    elif choice == "3":
        print(f"{Fore.LIGHTBLACK_EX}🔓  Releasing PERMANENT lockdown...\n")
        time.sleep(0.6)
        unban_permanent()

    elif choice == "4":
        print(f"{Fore.LIGHTBLACK_EX}🕒  Lifting TEMPORARY isolation...\n")
        time.sleep(0.6)
        unban_temporary()

    elif choice == "5":
        print(f"{Fore.WHITE}📜  Scanning ban registry archives...\n")
        time.sleep(0.6)
        view_banned()

    elif choice == "6":
        print(f"{Fore.RED}\n🍷  SYSTEM OVERRIDE INITIATED...")
        time.sleep(1)
        print(f"{Fore.LIGHTBLACK_EX}🍷  Closing all secure channels...")
        time.sleep(1)
        print(f"{Fore.BLUE}⚡  CORE OFFLINE. Until next hunt, ꧁𓆩『Pʀᴏˣboi-astro』𓆪꧂.\n")
        print(f"{Fore.LIGHTBLACK_EX}{'═'*70}")
        break

    else:
        print(f"{Fore.BLUE}❌  Invalid command detected. Try again, Operator.\n")

    time.sleep(1.4) 
