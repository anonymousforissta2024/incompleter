#Source: https://stackoverflow.com/questions/75236264/typeerror-bot-edit-message-media-got-multiple-values-for-argument-media
from aiogram import types
from keyboards.inline.choise_buttons import choice, shop_keyboard
from keyboards.inline.callback_datas import get_callback
from aiogram.types import CallbackQuery, InputMediaPhoto
from loader import dp,bot


@dp.message_handler()
async def bot_reply(message: types.Message):
    photo_url = 'https://pbs.twimg.com/profile_images/1187438234382548994/SesNEhbs_400x400.jpg'
    await bot.send_photo(photo=photo_url,
                         chat_id=message.chat.id,
                         caption='Главное меню',
                         reply_markup=choice,
                               )
    @dp.callback_query_handler(get_callback.filter(category_name='shop'))
    async def open_shop(call: CallbackQuery):
        await call.answer(cache_time=60)
        await bot.edit_message_media(call.message.chat.id,
                                     call.message.message_id,
                                     media = InputMediaPhoto('https://fikiwiki.com/uploads/posts/2022-02/1645044676_1-fikiwiki-com-p-kartinki-lami-1.jpg'))
        await bot.edit_message_caption(call.message.chat.id,
                                       call.message.message_id,
                                       caption='Выберите категорию'
                                       )
        await bot.edit_message_reply_markup(call.message.chat.id,
                                      call.message.message_id,
                                      reply_markup=shop_keyboard
                                      )
    @dp.callback_query_handler(get_callback.filter(category_name='shop'))
    async def open_shop(call: CallbackQuery):
        await call.answer(cache_time=60)
        await bot.edit_message_reply_markup(call.message.chat.id,
                                      call.message.message_id,
                                      reply_markup=shop_keyboard
                                      )

# await call.message.delete()
#     await call.message.answer_photo(photo=photo_url2,
#                               reply_markup=shop_keyboard)
#     @dp.callback_query_handler(get_callback.filter(category_name='royale'))
#     async def open_shop(call: CallbackQuery):
#         photo_url2 = 'https://i.ytimg.com/vi/P2TifLd5OIQ/maxresdefault.jpg'
#         await call.answer(cache_time=60)
#         await call.message.delete()