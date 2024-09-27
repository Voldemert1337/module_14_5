from aiogram.dispatcher.filters.state import State, StatesGroup
API_KEY = ''

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

