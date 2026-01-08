from aiogram.fsm.state import State, StatesGroup

class RegistrationStates(StatesGroup):
    waiting_for_fullname = State()
    waiting_for_phone = State()
    waiting_for_language = State()  

class PurchaseStates(StatesGroup):
    selecting_product = State()
    confirming_payment = State()
    processing_payment = State()