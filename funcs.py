from telethon import Button

messages = {
    'welcome': 'سلام {}، به ربات اتاق فرار فردوسی خوش اومدی،\n❗️ پیشنهاد میشه قبل از ایجاد تیم راهنمایی مسابقه رو بخونی'
               'تا در مورد شیوه ثبت نام و برگزاری مسابقه آشنا بشی',
    'sos': 'راهنمایی مسابقه',
    'payment': '💰صورت حساب\nهزینه ثبت نام: {}\nکسر هزینه از کد تخفیف: {}\n----------------------------------------\n'
               'قابل پرداخت: {}\nدرگاه: {}',
    'create_team': 'به اتاق فرار فردوسی خوش اومدی👻، تیم \"{}\" با موفقیت ایجاد شد🤠\n هر یک از اعضا باید با لینک زیر'
                   'در بات استارت بزنن تا عضو گروه بشن\n{}\n'
                   '**بعد از اینکه هریک از هم تیمی هات استارت زدن، پیامی برای تایید یا عدم تایید هم تیمی برات میاد\n',
    # https://t.me/FUMGame_bot?start=teamecode
    'login_team': 'درخواست شما برای عضویت در تیم \"{}\" به سرگروه ارسال شد،'
                  'بعد از تایید پیام عضویت برای شما ارسال میشود',
    'request_leader': 'کاربری با نام {} درخواست عضویت در تیم را داد، در صورت تایید، عضو تیم خواهد شد',
    'accepted_player': 'عضویت شما در تیم توسط {} تایید شد',
    'ignored_player': 'متاسفانه عضویت شما در تیم تایید نشد',
}


async def player_register(conv, sender):
    await conv.send_message('👤 نام و نام خانوادگی خود را وارد کنید:')
    name = await conv.get_response()
    await conv.send_message('🆔 شماره دانشجویی خود را وارد کنید :')
    studentid = await conv.get_response()
    studentid = studentid.message
    while not studentid.isnumeric():
        await conv.send_message("شماره دانشجویی معتبر نیست، دوباره وارد کنید")
        studentid = await conv.get_response()
        studentid = studentid.message
    but = [[Button.request_phone('Send phone')]]
    await conv.send_message('☎️برای ارتباط و دسترسی بهتر، شماره تلفن خود را از دکمه پایین برای ارسال'
                            'انتخاب کنید.', buttons=but)
    phonenumber = await conv.get_response()
    return [sender.id, studentid, phonenumber.media.phone_number, sender.username, name.message]

