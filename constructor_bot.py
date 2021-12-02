from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random
from config import TOKEN
import keyboards as kb

EMPTY_CELL_SYMBOL = '\U000023F9'  # squad symbol
TAK_SYMBOL = '\U0000274C'  # "X" - symbol
TOE_SYMBOL = '\U00002B55'  # "O" - symbol


def draw_field(field):
    field_message = ''
    for it in field:
        for jt in it:
            if jt == 0:
                field_message += '\U000023F9'
            elif jt == 1:
                field_message += '\U00002B55'
            else:
                field_message += '\U0000274C'
        field_message += '\n'
    return field_message


def check_win(game_field):
    """Checking the winning combination. If the function wins,
    it returns a tuple of the True value and the winning symbol.
    If there is no winner, returns False.
    """
    lenght = len(game_field[0])

    # Check row
    for it in game_field:
        if it.count(it[0]) == lenght and it[0] != 0:
            return True, it[0]

    # Check column
    for it in range(0, lenght):
        row_from_column = []
        for jt in range(0, lenght):
            row_from_column.append(game_field[jt][it])
        if row_from_column.count(row_from_column[0]) == lenght and row_from_column[0] != 0:
            return [True, row_from_column[0]]

    # Check main diagonal
    row_from_diagonal = []
    for it in range(0, lenght):
        row_from_diagonal.append(game_field[it][it])
    if row_from_diagonal.count(row_from_diagonal[0]) == lenght and row_from_diagonal[0] != 0:
        return True, row_from_diagonal[0]

    # Check reverse diagonal
    row_from_diagonal = []
    for it, jt in zip(range(lenght - 1, -1, -1), range(0, lenght)):
        row_from_diagonal.append(game_field[jt][it])
    if row_from_diagonal.count(row_from_diagonal[0]) == lenght and row_from_diagonal[0] != 0:
        return [True, row_from_diagonal[0]]

    return False


def bot_mark(game_field):
    free_cell = []
    cell_count = 0
    for it in game_field:
        for jt in it:
            cell_count += 1
            if jt == 0:
                free_cell.append(str(cell_count))
    print(free_cell)
    if free_cell:
        put = str(random.choice(free_cell))
        print(put)
        game_board[num_in_array[put][0]][num_in_array[put][1]] = 2


def mark_field(num_in_message):
    game_board[num_in_array[num_in_message][0]][num_in_array[num_in_message][1]] = 1


num_in_array = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                '4': (1, 0), '5': (1, 1), '6': (1, 2),
                '7': (2, 0), '8': (2, 1), '9': (2, 2), }

# bot = telebot.TeleBot('2145551349:AAEvTby4sRkkw7YCtoSp_f7hOdX7E4prfHI')

answer_dict = {
    'Привет': 'Здорова',
    '/help': 'Напиши привет',
    'Да': 'Нет',
    'Че': 'Каво',
}

game_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

msg_db = '\U000023F9\U000023F9\U000023F9\n' \
         '\U000023F9\U000023F9\U000023F9\n' \
         '\U000023F9\U000023F9\U000023F9'
msg_db2 = EMPTY_CELL_SYMBOL, EMPTY_CELL_SYMBOL, EMPTY_CELL_SYMBOL, '\n', \
          EMPTY_CELL_SYMBOL, EMPTY_CELL_SYMBOL, EMPTY_CELL_SYMBOL, '\n', \
          EMPTY_CELL_SYMBOL, EMPTY_CELL_SYMBOL, EMPTY_CELL_SYMBOL


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f"Привет! Давай поиграем в крестики нолики\n{msg_db}", reply_markup=kb.greet_kb)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg.text in num_in_array:
        mark_field(msg.text)
        print(check_win(game_board))
        bot_mark(game_board)
        print(game_board)
        await bot.send_message(msg.from_user.id, draw_field(game_board))
    else:
        await bot.send_message(msg.from_user.id, f'Ну привет, {msg.from_user.first_name}, ТЫ ПИДР{msg_db}')
    print(msg.from_user.first_name)


if __name__ == '__main__':
    executor.start_polling(dp)
