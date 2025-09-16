1. FSM - bu botning foydalanuvchi bn boladigan dialogini xolatlar boyicha boshqarish mexanizimi.

Misol: foydalanuvchi ro‘yxatdan o‘tayotganda:

Ismni kiritadi → State: name
Yoshni kiritadi → State: age
Telefon raqamini kiritadi → State: phone

FSM orqali bot hozir foydalanuvchi qaysi bosqichda turganini aniq bilib turadi.
FSM bolmaganda biz buni if message.text == ... yoki contextni qo‘lda saqlash orqali qilishimiz kerak bo
‘lardi.

FSM dialoglarni soddalashtiradi, kodni modulli qiladi va bir vaqtning o‘zida ko‘p foydalanuvchilar bilan ishlashda chalkashliklarni oldini oladi.

2.Telegram faylni (rasm, video, document) yuborganda sizga file_id beradi.

Database’da saqlashning eng yaxshi usuli:
Faylning file_id sini DB ga saqlash → kerak bo‘lsa, bot Telegram’dan shu faylni qayta yuklab oladi.

Faylni to‘g‘ridan-to‘g‘ri DB ichiga saqlash tavsiya qilinmaydi — bu sekin va og‘ir.

3.Ha, Aiogram 3.x da DI bor. U servislarni (DB, API client va boshqalar) handler’larga injekt qilish imkonini beradi. Bu testlashni yengillashtiradi, kodni modulli qiladi va komponentlarning bog‘liqligini kamaytiradi.

4.
Merchant API:
Asosan bir martalik to‘lovlar uchun ishlatiladi (masalan, mahsulot sotib olish).
Foydalanuvchi to‘lov qiladi → sizga payment_success keladi → xizmat/mahsulotni berasiz.

Subscribe API:
Davomiy (rekurrent) to‘lovlar uchun (masalan, Netflix, Spotify kabi oylik obuna).
Birinchi marta karta bog‘lanadi → keyin avtomatik ravishda vaqtida pul yechiladi.

Merchant API – bir martalik to‘lov.
Subscribe API – takrorlanadigan obuna to‘lovi.

5.CallbackAPI orqali to‘lov provayderi serverga
to‘lov statusini yuboradi. Bu jarayon to‘lovni ishonchli kuzatishni ta’minlaydi, server javob bermagan holatlarda ham biz real statusni olamiz va xizmatni avtomatik faollashtira olamiz.