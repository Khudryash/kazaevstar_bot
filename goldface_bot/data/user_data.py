from aiogram.dispatcher.filters.state import State, StatesGroup


# residential
class Proofs(StatesGroup):
    screenshot = State()
    card = State()
    bank = State()
    name = State()
