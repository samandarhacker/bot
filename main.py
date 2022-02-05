from telebot import *
from telebot.types import *
import os
from random import choice
from time import sleep
def MENU_GO(message,chat_id):
    bot.send_message(chat_id,"🖥 Bosh sahifaga qaytdingiz",reply_markup=menu)

def menu_go(message,chanel_status):

    if chanel_status:
        ism = message.from_user.first_name
        bot.send_message(message.from_user.id, f'''☇ Salom {ism}

    Sizni botda ko‘rib turganimdan xursandman!
      @MyBots_uz_bot  orqali siz o‘zingizning shaxsiy botlaringizni hech qanday qiyinchiliklarsiz yaratishingiz mumkin!

    ⬇️ Ishni boshlash uchun quyidagi tugmalardan foydalaning!''', reply_markup=menu)
    else:
        bot.delete_message(chat_id=message.from_user.id,message_id=message.message.id)
        bot.send_message(message.from_user.id, "😕😒 kanallarga obuna bo'lmadinggiz!",reply_markup=chanel_add)
#buttons
menu = ReplyKeyboardMarkup(True).add("🛠Botlarni boshqarish","💸 Uzcoin to'plash","📱Kabinet","📊 Statistika","💰Pul yechish")
Uzcoin_button = ReplyKeyboardMarkup(True)
Uzcoin_button.add("👥 Takliflar","💰 Xarid qilish")
Uzcoin_button.add("🔙 Menu")
helpbot = ReplyKeyboardMarkup(True).add("📞Murojaat","⚡️Tizim yangiliklari")
helpbot.add("ℹ️Bot haqida","🔙Ortga qaytish")
telefon = ReplyKeyboardMarkup(True).add("📞Telefon Nomer O'zgartirish")
telefon.add("📞Mening Telefon Nomerim")
telefon.add("🔙Ortga qaytish")

bots = ReplyKeyboardMarkup(True)
bots.add("➕ Bot qo'shish","❓ Yordam","🖥 Hosting")
bots.add("🔙Ortga qaytish")

addbot = ReplyKeyboardMarkup(True)
addbot.add("Wikipedia","🔙Ortga qaytish")

tellnomer = ReplyKeyboardRemove()
#inline button
paynet = InlineKeyboardMarkup([[InlineKeyboardButton("💵 Paytnet",callback_data="paynet")],[InlineKeyboardButton("💎 Click",callback_data="click")],[InlineKeyboardButton("🔙 Ortga",callback_data="ortga1")]])
tolov = InlineKeyboardMarkup([[InlineKeyboardButton("📲 Telegram. Yordam",url="https://t.me/Azamov_Samandar")],[InlineKeyboardButton("🔙 Ortga",callback_data="ortga")]])



bot = TeleBot("5254602991:AAG5ZXKfrKLoKz7yzxGIiIAZ91-8nIFaW1Q")



chanel_add = InlineKeyboardMarkup([[InlineKeyboardButton("🔚 Kanal",url="https://t.me/python3600")],[InlineKeyboardButton("🔚 Kanal",url="https://t.me/python36001")],[InlineKeyboardButton("✅ Tekshirish",callback_data="tekshiruv")]])
kabinet_hisob = InlineKeyboardMarkup([[InlineKeyboardButton("💸 Hisobni to'ldirish",callback_data="hisobni_Toldirish")]])
kanall = InlineKeyboardMarkup([[InlineKeyboardButton("🔚 Kanal",url="https://t.me/MyBots_uz")]])
pulyechish = InlineKeyboardMarkup([[InlineKeyboardButton("💸100 uzcoins = 1000 so'm",callback_data="1000")],[InlineKeyboardButton("💸200 uzcoins = 2000 so'm",callback_data="2000")],[InlineKeyboardButton("💸400 uzcoins = 4000 so'm",callback_data="4000")]])

#kanal
def kanal(chat_id):
    try:
        member = bot.get_chat_member("@python3600",chat_id).status
        if member == "member":
            return  True
        elif member == "creator":
            return  True
        elif member == "administrator":
            return  True
        else:
            return False
    except Exception as e:
        return  False
@bot.message_handler(commands=['start'])
def boshlash(message):
    global link_referal
    chat_id = message.chat.id
    status = False
    try:
        os.makedirs(f"{str(message.chat.id)}")
    except:
        pass
    try:
        e_ = open(f"{str(chat_id)}/uzcoin.txt","x")
        e_.write("0")
    except:
        pass
    try:
        a = open(f"members_id.txt","x")
        a.write("1769851684 ")
        a.close()
    except Exception as e:
        pass

    try:
        gg = open("members_id.txt","r+")
        rrr = gg.read()
        if not str(message.chat.id) in str(rrr):
            gg.write(str(message.chat.id)+" ")
            status = True
            bot.send_message(chat_id="1769851684",text='''Name: {name}\nlink: {username}\nid: {id}'''.format(name=message.from_user.first_name,username=message.from_user.username,id=message.chat.id))

        else:
            status = False

    except Exception as bu:
        status = False
    try:
        link_referal = message.text.split(" ")
        link_referal = str(link_referal[1])
    except:
        pass
    try:
        bonustekshiruv = open("bonus.txt","r+")
        try:
            dgg = bonustekshiruv.read()
            err = dgg.split("/")
            botx = err[0]
            bonur = err[1]
            bonur = int(bonur)
        except:
            pass
        botx = str(botx)
        if str(link_referal) == botx:
            print("ishladi")
            bb = open(f"{str(message.chat.id)}/uzcoin.txt","r")
            cc = bb.read()
            cc = int(cc)
            ff = cc + bonur
            print(ff)
            ff = str(ff)
            print(ff)
            ww = open(f"{str(message.chat.id)}/uzcoin.txt","w")
            ww.write(ff)
            open("bonus.txt","w").close()
            bot.send_message(chat_id="-1001743528929",text=f'''⚠️ Diqqat tepadagi promokod ishlatildi.
Endi undan qayta foydalanib bo'lmaydi!
Promokoddan {message.from_user.first_name} foydalandi 
va unga {bonur} Uzcoin taqdim etildi ✅

''')
    except Exception as e:
        pass  

    if status:
        try:
            bot.send_message(chat_id=str(link_referal),text='''📡Tabriklaymiz siz botimizga {} taklif qildingiz! sizga 5 Uzcoin Berildi 😁'''.format(message.from_user.first_name))
        except:
            pass
        try:
            a = open(f"{link_referal}/uzcoin.txt","x")
            a.write("0")
            a.close()
        except Exception as e:
            pass
        try:
            bb = open(f"{link_referal}/uzcoin.txt","r")
            cc = bb.read()
            cc = int(cc)
            ff = cc + 5
            ff = str(ff)
            ww = open(f"{link_referal}/uzcoin.txt","w")
            ww.write(ff)
            print(ff)
        except Exception as e:
            pass
    chanel_status = kanal(chat_id)

    if chanel_status:
        try:
            bot.delete_message(chat_id=message.from_user.id,message_id=message.message.id)
        except:
            pass
        ism = message.from_user.first_name
        bot.send_message(message.chat.id,f'''☇ Salom {ism}

Sizni botda ko‘rib turganimdan xursandman!
  @MyBots_uz_bot  orqali siz o‘zingizning shaxsiy botlaringizni hech qanday qiyinchiliklarsiz yaratishingiz mumkin!

⬇️ Ishni boshlash uchun quyidagi tugmalardan foydalaning!''',reply_markup=menu)
    else:
        bot.send_message(chat_id,"Quyidagi kanallarimizga obuna boʻling. Botni keyin toʻliq ishlatishingiz mumkin!",reply_markup=chanel_add)

@bot.message_handler(commands=['help_host'])
def help_(message):
    bot.send_message(message.chat.id,"Botni ishga tushurish uchun avvalo kerakli kutubxonalarni o'rnatib oling buning uchun\n ✅ /pip/pyTelegramBtAPI ko'rinishida yozing \nbot ko'dini yuboring va sizga id beriladi /run/ kalit so'zidan so'ng idni kiriting\nEslatma:Ko'dlar bitta fayilda bo'lishi zarur va os,sys modullaridan foydalanmang bo'lishinggiz zarur ✅")

@bot.message_handler(content_types=['document'])
def hosting_document(message):
    bot.send_message(message.chat.id,"✅ Id Tayyorlanmoqda kuting...")
    random_id = "qwertyuiopasdfghjklzxcvbnm1234567890"
    document_id = choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)+choice(random_id)
    sleep(2)
    try:
        file_info = bot.get_file(message.document.file_id)
        download_file = bot.download_file(file_info.file_path)
    except:
        bot.send_message(message.chat.id,"Fayilni yuklab olishda hato yuzberdi fayil o'lchami 20 mb dan oshmasligi kerak ‼️")
    try:
        os.makedirs(f'{str(message.chat.id)}/bots/hosting')
    except:
        pass
    try:
        with open(f"{str(message.chat.id)}/bots/hosting/{document_id}.py", "wb") as new_file:
            new_file.write(download_file)

            bot.edit_message_text(chat_id=message.chat.id,text=f"✅ Botni ishga tushurishdan avval kerakli kutubxonalarni o'rnatishni unutmang\n\n/pip/\n\nKutubxonalarni o'rnatib bo'lganinggizdan so'ng \n\n/run {document_id}",message_id=message.message_id + 1)
    except Exception as e:
        print(e)
@bot.message_handler(content_types=['text'])
def bot_text(message):
    kanal_add = kanal(message.chat.id)
    if str(message.chat.id) == "1769851684" and message.text.startswith("/bonus"):
        bon = message.text.split("/")
        try:
            bonu = bon[2]
            ffj = bon[3]
        except:
            bonu = "dfhgdhdfghd"
            ffj = str(10)
        ffj = str(ffj)
        bonu = str(bonu)
        bo = open("bonus.txt","w")
        bo.write(bonu+"/"+ffj)
        bo.close()
        bonusinline = InlineKeyboardMarkup([[InlineKeyboardButton("🎫 Promokodni ishlatish",url=f"https://t.me/MyBots_uz_bot?start={bonu}")]])
        bot.send_message(chat_id="-1001743528929",text=f'''🎫 Yangi Promokod.
🔽 Ishlatish uchun pastdagi tugmani bosing.
🤖 Yutuq {ffj} Uzcoin
''',reply_markup=bonusinline)
    if kanal_add:
        hosting_status = False
        rr = False
        chat_id = message.chat.id
        text = message.text
        uu = text.split(":")
        iop = uu[0]
        if str(message.from_user.id) == "1769851684" and text.startswith("/msg"):
            msg_idy = text.split("/")
            try:
                msg_id = msg_idy[2]
                msg_texty = msg_idy[3]
                bot.send_message(chat_id=str(msg_id),text=str(msg_texty))
                bot.send_message(message.chat.id,"Xabar yetkazildi")
            except:
                bot.send_message(chat_id,"xabar yuborilmadi")
        if text.startswith("/run"):
            run_file = text.split(" ")
            try:
                run_file = run_file[1]
                os.startfile(f"{str(message.chat.id)}\\bots\\hosting\\{run_file}.py")
                bot.send_message(chat_id,"bot muvofaqiyatli ishga tushuruldi 😁 ")
            except:
                bot.send_message(chat_id,'botni ishga tushurisda xato yuzberdi ‼️ ')
        if text.startswith("/pip"):
            try:
                pip_text = text.split(" ")
                pip_text = pip_text[1]
                a = os.system(f"pip install {pip_text}")
                bot.send_message(message.chat.id,"Kutubxona muvofaqiyatli oshiriladi😁✅")
            except:
                bot.send_message(chat_id,"Kutubxona o'rnatishda xato yuzberdi ‼️ ")
        if text == "🖥 Hosting":
            bot.send_message(chat_id,'''Bo'tinggizni ho'stingga joylash uchun qo'llanma😁 :\nBotga dasturinggiz ko'dini yuboring va sizga id beriladi /run/ kalit so'zidan keyin id ni kiriting va bo'tinggiz tayyor\n/pip\nKutubxonalarni o'rnatish\nMisol: /pip/pyTelegramBotAPI\n\n/run\nBotni ishga tushurish uchun\nMisol:  /run/1jhvfiuhh2h2j3hj4b5nbhsdpw\n\n To'liq malumot /help_host''')
            bot.send_message(chat_id,"dastur ko'dini yuboring!!!")
            hosting_status = True
        try:
            jjk = open(f"{str(message.chat.id)}/uzcoin.txt", "r+")
            ttu = jjk.read()
            ttu = int(ttu)
        except:
            ttu = 0
        try:
            bot_types_read = open(f"{str(chat_id)}/bot_types.txt","r+")
            bot_read = bot_types_read.read()
        except:
            bot_read = "None"
        try:
            iop = int(iop)
            iop = str(iop)
            RRR = []
            RRR.extend(iop)
            if str(len(RRR)) == str(10):
                token_status = True
            else:
                token_status = False
        except Exception as e:
            token_status = False
            print("xato",e)

        if token_status and bot_read == "wikipedia" and ttu >= 200:
            rrew = open("tokeni.txt","w")
            rrew.write(str(text))
            os.startfile("{}\\bots\\wikipedia\\main.py".format(str(message.chat.id)))
            bot.send_message(chat_id, "Bot Muvofaqiyatli ishga tushurildi!!!")
            try:
                jjk = open(f"{str(message.chat.id)}/uzcoin.txt", "w")
                ttu = ttu - 200
                jjk.write(str(ttu))
            except:
                pass
        if text == "Wikipedia":
            try:
                os.makedirs(f"{chat_id}/bots/wikipedia")
            except:
                pass
            try:
                bot_types = open(f"{str(chat_id)}/bot_types.txt","w").write("wikipedia")
            except:
                pass
            try:
                jjk = open(f"{str(message.chat.id)}/uzcoin.txt","r+")
                ttu = jjk.read()
                ttu = int(ttu)
            except:
                ttu = 0
            if ttu >= 200:
                bot.send_message(chat_id,'''1️⃣ @BotFather-ga o'ting.  Buning uchun uning ismini bosing.
2️⃣ U bilan yangi bot yarating.  Buning uchun @BotFather ichidagi /newbot buyrug'idan foydalaning.
3️⃣ @BotFather sizga beradigan API tokenidan nusxa oling.
4️⃣ @MyBots_uz_bot -ga qaytib, nusxalangan API tokenini shu botga yuboring.
💥Taxminiy API Token:
 126521644:AAGlXut7dgde4jr94X8PNM1WXHhPwlLA''')
                wikipedia_bot = open("bots/wikipedia/main.py","rb")
                with open(f"{chat_id}/bots/wikipedia/main.py","wb") as file:
                    for eqw in wikipedia_bot:
                        file.write(eqw)

            else:
                bot.send_message(chat_id,"xisobinggizda mablag' yetarli emas")
        if str(message.from_user.id) == "1769851684" and text.startswith("/check"):
            kjl = text.split("/")
            try:
                kjlid = kjl[2]
                kjlj = open(f"{kjlid}/uzcoin.txt","r+")
                rrj = kjlj.read()
                bot.send_message(chat_id="1769851684",text=f"Foydalanuvchi xisobi: {rrj}")
            except:
                bot.send_message(chat_id="1769851684",text="Xato Foydalanvchi mavjud emas!!!")
        if str(message.from_user.id) == "1769851684" and text.startswith("/del"):
            pp = text.split("/")
            try:
                iiii = pp[2]
                rrrr = pp[3]
                ppp = open(f"{iiii}/uzcoin.txt","r+")
                pppp = ppp.read()
                pppp = int(pppp) - int(rrrr)
                ppppp = open(f"{iiii}/uzcoin.txt","w")
                ppppp.write(str(pppp))
            except Exception as e:
                bot.send_message(chat_id="1769851684",text=f"Xato {e}")

        if text == "📞Mening Telefon Nomerim":
            telr = open(f"{message.from_user.id}/tel.txt","r+")
            eew = telr.read()
            bot.send_message(message.from_user.id,f'''📞 Sizning telefon raqaminggiz: +{eew}''')
        if text == "📞Telefon Nomer O'zgartirish":
            telr = open(f"{message.from_user.id}/tel.txt","r+")
            eew = telr.read()
            bot.send_message(message.chat.id,f"📞 Sizning Telefon Nomeringgiz +{eew}\nO'zgartirish uchun Yangi telefon Nomeringgizni yuboring",reply_markup=tellnomer)
        if text == "💰Pul yechish":
            try:
                hhg = open(f"{str(message.from_user.id)}/tel.txt","x")
                hhg.close()
            except:
                pass
            try:
                jjk = open(f"{str(message.chat.id)}/tel.txt","r+")
                ttu = jjk.read()
                ttu = int(ttu)
            except:
                ttu = 0
            if ttu > 998330000000:
                bot.send_message(message.chat.id,"💵Pul yechish",reply_markup=telefon)
                bb = open(f"{str(message.chat.id)}/uzcoin.txt","r")
                cc = bb.read()
                cc = int(cc)
                if cc > 200:
                    bot.send_message(chat_id,f"💵 Xisobinggiz {cc} uzcoins\n\n💰 100 uzcoins = 1000 so'm\n\n💰v 200 uzcoins = 2000 so'm\n\n💰 400 uzcoins = 4000 so'm\n\n💵 Qancha miqdorda pul yechib olmoqchisiz",reply_markup=pulyechish)
                else:
                    bot.send_message(chat_id,'''Pul yechib olish uchun xisobinggizda mablag' yetarli emas‼️\n\n💸 Pul yechib olish uchun minimal summa 💰 200 uzcoin\n\nBo'tga Do'stlaringgizni taklif qiling va 💰 uzcoinlarga ega bo'ling\n\n💰 100 uzcoin = 💵 1000 so\'m\n\n💰 200 uzcoin == 💵 2000 so\'m\n\n💰 400 uzcoin = 💵 4000 so\'m\n\n\nTo\'lov turi: 💎 Paynet''')
            else:
                bot.send_message(message.chat.id,"telefon no'meringgizni kiriting\nMisol: 998943990509\nEslatma telefon no'meringgizni kiritishda foydalanayorgan telefon nomeringgizni kiriting bu pul yechish uchun zarur",reply_markup=tellnomer)
        if text.startswith("998"):
            try:
                text = int(text)
                text = str(text)
                rrh = []
                rrh.extend(text)
                if len(rrh) == 12:
                    tty = open(f"{message.from_user.id}/tel.txt","r+")
                    tty.write(text)
                    bot.send_message(message.chat.id,"Telefon no'meringgiz qabul qilindi!!!",reply_markup=menu)
                else:
                    bot.send_message(message.chat.id,"Telefon no'meringgiz xato!!!",reply_markup=menu)
            except Exception as e:
                bot.send_message(message.chat.id,f"telefon no'meringgiz xato!!! {e}",reply_markup=menu)
        if text == "⚡️Tizim yangiliklari":
            bot.send_message(chat_id,'''📂 Bot yuzasidagi barcha yangiliklar @MyBots_uz kanalida yetkazib boriladi.

🗄 Kanalga obuna boʻlishingizni soʻraymiz! Bu siz uchun muhim!''',reply_markup=kanall)
        if text == "ℹ️Bot haqida":
            bot.send_message(chat_id,'''ℹ️ Ushbu bot orqali siz hech qanday dasturlash tillarini bilmasdan turib va hech qanday hostinglarsiz oson bot yasay olasiz.

✅ Imkoniyatlar
👉 Bepul hostingdan bot yarating
👉 Do'stlarni taklif qiling
👉 Har kunlik bonus oling
👉 Dasturlangan bot yarating.
👉 uzcoinlarni so'mga aylantiring va telefon hisobinggizga o'tkazib oling


♻️ Bot versiyasi: 4.1

🛠 Dasturchi: Samandar
👉 Telegram: @Azamov_Samandar
👉 tel: +998943990509''')
        if str(chat_id) == "1769851684" and not str(message.forward_from) == "None":
            bot.send_message(chat_id,f"/coin/{message.forward_from.id}/")
        if text.startswith("/coin"):
            try:
                qq = text.split("/")
                ddg = qq[2]
                wwe = qq[3]
                ddfs = int(wwe)
                bb = open(f"{str(ddg)}/uzcoin.txt","r")
                cc = bb.read()
                cc = int(cc)
                ff = cc + int(ddfs)
                ff = str(ff)
                ww = open(f"{str(ddg)}/uzcoin.txt","w")
                ww.write(ff)
                tolov = open("tolov.txt", "w")
                bot.send_message(chat_id,"To'lov muvofaqiyatli bajarildi!!!")
                bot.send_message(chat_id=str(ddg),text="xisobinggizga {} uzcoin o'rkazildi".format(wwe))
            except Exception as e:
                bot.send_message(chat_id="1769851684",text=f"Xato {e}")
        if text == "🛠Botlarni boshqarish":
            bot.send_message(chat_id,'''ℹ️ Yangi bot yaratish uchun quyidagi tugmani bosing:
    «➕ Bot qoʻshish»
    
    ℹ️ Tayyor botni oʻchirish yoki sozlash uchun quyidagi tugmani bosing:
    «⚙️Botni sozlash»''',reply_markup=bots)
        if text == "➕ Bot qo'shish":
            bot.send_message(chat_id,'''Qanday turdagi botlarni yaratamiz👇''',reply_markup=addbot)
        if text == "🔙Ortga qaytish":
            MENU_GO(message,chat_id)
        if text == "❓ Yordam":
            bot.send_message(chat_id,'''❓Siz Yordam menusidasiz.
    
    📋 Yordam olish uchun buyruqlardan foydalaning:''',reply_markup=helpbot)

        if text == "📞Murojaat":
            bot.send_message(message.chat.id,'''📞 Sizda biror gʻoya, taklif yoki murojaat boʻlsa bizga murojaat qiling:
@Azamov_Samandar

📂 Texnik qoʻllab-quvvatlash uchun guruhimizga qoʻshiling:
@Azamov_Samandar''')
        try:
            eer = open(f"{message.from_user.id}/uzcoin.txt", "r")
            member_uzcoin = eer.read()
            member_uzcoin = str(member_uzcoin)
        except:
            member_uzcoin = "0"
        if text == "📱Kabinet":
            bot.send_message(chat_id,'''🗄 Kabinetingizga xush kelibsiz!
    
    💵 Sizning balansingiz: {} Uzcoin
    
    ❗️❗️Bot hisobingizni Qiwi orqali to‘ldiryotgangizda izoh qoldirishni unutmang!'''.format(member_uzcoin),reply_markup=kabinet_hisob)
        if text == "🔙 Menu":
            MENU_GO(message,chat_id)
        if text == "💸 Uzcoin to'plash":
            bot.send_message(chat_id,'''💸 Qanday usulda Uzcoin olishni hohlaysiz?
    
    ‼️ Bot orqali yig'gan Uzcoinigizni yechib olomaysiz. Uzcoiningizni botimizdagi har qanday xaridlar uchun sarflashingiz mumkin.''',reply_markup=Uzcoin_button)
        if text == "👥 Takliflar":
            referal_lilk = InlineKeyboardMarkup([[InlineKeyboardButton("Dostlarga yuborish",url=f"https://t.me/share/url?url=https://t.me/MyBots_uz_bot?start={chat_id}")]])
            bot.send_message(chat_id,'''📌Quyidagi havolani do'stlaringizga tarqatib Uzcoin yig'ing:
    
    Eslatib o'tamiz har bir do'stingiz sizga 5 ta Uzcoin beradi!
    Do'stingiz kanalimizga a'zo bo'lmasa sizga Uzcoin berilmaydi!✅''',reply_markup=referal_lilk)
        if text == "💰 Xarid qilish":
            bot.send_message(chat_id,"💵 Hisobni toʻldirish usulini tanlang:",reply_markup=paynet)

        if text == "📊 Statistika":
            ffg = open("members_id.txt","r+")
            ssd = ffg.read()
            ssd = str(ssd)
            ssd = ssd.split(" ")
            bot.send_message(chat_id,"📊 Statistika\nBot a'zolari soni: {ssd} ta".format(ssd=len(ssd)))

    else:
        bot.send_message(message.chat.id,"Quyidagi kanallarimizga obuna boʻling. Botni keyin toʻliq ishlatishingiz mumkin!",reply_markup=chanel_add)






@bot.callback_query_handler(func=lambda call:True)
def calldata_(call):
    bb = open(f"{str(call.from_user.id)}/uzcoin.txt","r")
    cc = bb.read()
    cc = int(cc)
    ii = open(f"{str(call.from_user.id)}/tel.txt","r+")
    oo = ii.read()
    oo = str(oo)
    if call.data == "1000":
        if cc > 100:
            bot.send_message(call.from_user.id,"Sorovinggiz qabul qilindi to'lov 30 daqiqa ichida amalga oshiriladi😁✅")
            bot.send_message(chat_id="1769851684",text=f'''Name: {call.from_user.first_name}\nid: {call.from_user.id}\nusername: @{call.from_user.username}\nto'lov: 1000 so'm\ntel: +{oo}''')
            rry = open(f"{str(call.from_user.id)}/uzcoin.txt","w")
            cc = cc - 100
            rry.write(str(cc))
        else:
            bot.send_message(call.from_user.id,"Pul yechish uchun hisobinggizga mablag' yetarli emas‼️")
   
    if call.data == "2000":
        if cc > 200:
            bot.send_message(call.from_user.id,"Sorovinggiz qabul qilindi to'lov 30 daqiqa ichida amalga oshiriladi😁✅")
            bot.send_message(chat_id="1769851684",text=f'''Name: {call.from_user.first_name}\nid: {call.from_user.id}\nusername: @{call.from_user.username}\nto'lov: 2000 so'm\ntel: +{oo}''')
            rry = open(f"{str(call.from_user.id)}/uzcoin.txt","w")
            cc = cc - 200
            rry.write(str(cc))
        else:
            bot.send_message(call.from_user.id,"Pul yechish uchun hisobinggizga mablag' yetarli emas‼️")
    if call.data == "4000":
        if cc > 400:
            bot.send_message(call.from_user.id,"Sorovinggiz qabul qilindi to'lov 30 daqiqa ichida amalga oshiriladi😁✅")
            bot.send_message(chat_id="1769851684",text=f'''Name: {call.from_user.first_name}\nid: {call.from_user.id}\nusername: @{call.from_user.username}\nto'lov: 4000 so'm\ntel: +{oo}''')
            rry = open(f"{str(call.from_user.id)}/uzcoin.txt","w")
            cc = cc - 400
            rry.write(str(cc))
        else:
            bot.send_message(call.from_user.id,"Pul yechish uchun hisobinggizga mablag' yetarli emas‼️")

    if call.data == "paynet":
        bot.edit_message_text(text='''📋 To'lov tizimi: PAYNET
💡 Avto to'lov holati: OF

💳 Hamyon ( +998943990509 ) -> admin: @Azamov_Samandar
📝 Izoh: 1769851684
📊 Uz. c. Kursi: 
1000 so'm = 200 Uzcoins

Qo'shimcha: To'lovni amalga oshirgach biz bilan bog'laning.''',chat_id=call.from_user.id,message_id=call.message.id,reply_markup=tolov)
    if call.data == "click":
        bot.edit_message_text(text='''📋 To'lov tizimi: Click
    💡 Avto to'lov holati: OF

    💳 Hamyon ( +998943990509 ) -> admin: @Azamov_Samandar
    📝 Izoh: 1769851684
    📊 Uz. c. Kursi: 
    1000 so'm = 200 Uzcoins

    Qo'shimcha: To'lovni amalga oshirgach biz bilan bog'laning.''', chat_id=call.from_user.id,message_id=call.message.id, reply_markup=tolov)

    if call.data == "ortga":
        bot.edit_message_text(text="💵 Hisobni toʻldirish usulini tanlang:",chat_id=call.from_user.id,message_id=call.message.id,reply_markup=paynet)


    if call.data == "ortga1":
        bot.delete_message(chat_id=call.from_user.id,message_id=call.message.id)
        MENU_GO(call.message,call.from_user.id)

    if call.data == "tekshiruv":
        chanel_status = kanal(call.from_user.id)
        menu_go(call,chanel_status)
    if call.data == 'hisobni_Toldirish':
       # bot.delete_message(chat_id=call.from_user.id,message_id=call.message.id)
        try:
            bot.edit_message_text(chat_id=call.from_user.id,text="💵 Hisobni toʻldirish usulini tanlang:",message_id=call.message.id,reply_markup=paynet)
        except:
            bot.send_message(call.from_user.id,"💵 Hisobni toʻldirish usulini tanlang:",reply_markup=paynet)

bot.polling(none_stop=True)