from aiogram.utils import executor
from create_bot import dp
import handlers

handlers.register_handler(dp)




if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)