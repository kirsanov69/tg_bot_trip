from aiogram.fsm.storage.base import BaseStorage
import logging
from collections import deque


class StateManager:
    def __init__(self):
        self.storage = {}  # Словарь для хранения deque состояний по user_id

    async def get_state(self, user_id: int) -> str:
        # Получаем текущее состояние пользователя из deque
        user_states = self.storage.get(user_id, deque(["menu"]))
        return user_states[-1]

    async def set_state(self, user_id: int, state: str) -> None:
        # Получаем или создаем deque для состояний пользователя и добавляем новое состояние
        user_states = self.storage.setdefault(user_id, deque(["menu"]))
        user_states.append(state)

        # Логгирование
        logging.info(f'User {user_id} switched to state {state}, list of states: {user_states}, {len(user_states)},{self.storage}')

    async def set_previous_state(self, user_id: int) -> bool:
        # Получаем текущее состояние пользователя из deque
        user_states = self.storage.get(user_id, deque(["menu"]))
        # Если в deque есть предыдущее состояние, возвращаем его
        if len(user_states) > 1:
            previous_state = user_states[-2]
            user_states.pop()
            self.storage[user_id] = user_states
            logging.info(f'User {user_id} successfully returned to the previous state ({previous_state}), list of states: {user_states}, {self.storage}')
            # print(previous_state)
            return True, previous_state

        else:
            logging.info(f'User {user_id} attempted to return to the previous state, but there was no previous state, list of states: {user_states}, {self.storage}')
            return False, previous_state

    async def reset_state(self, user_id: int) -> None:
        # Сбрасываем состояние пользователя (делаем deque пустым)
        if user_id in self.storage:
            self.storage[user_id].clear()
            self.storage[user_id].append("menu")
        # Логгирование
        logging.info(f'User {user_id} reset their state to the default state, {self.storage}')

# state_manager = StateManager()
# import asyncio
# async def main():
#     await state_manager.set_state(1, "moscow")
#     await state_manager.set_state(1, "red_square")
#     print(state_manager.storage)
#     await state_manager.set_previous_state(1)
#     print(state_manager.storage)
# asyncio.run(main())

    # async def set_previous_state(self, user_id: int) -> None:
    #     current_state = await self.get_state(user_id)
    #     if current_state:
    #         await self.storage.set_state(user_id, current_state)
    #         return True
    #     return False


'''
from collections import deque

class StateManager:
    def __init__(self):
        self.storage = {}  # Словарь для хранения deque состояний по user_id

    async def get_state(self, user_id: int) -> str:
        # Получаем текущее состояние пользователя из deque
        user_states = self.storage.get(user_id, deque(["menu"]))
        return user_states[-1]

    async def set_state(self, user_id: int, state: str) -> None:
        # Получаем или создаем deque для состояний пользователя и добавляем новое состояние
        user_states = self.storage.setdefault(user_id, deque(["menu"]))
        user_states.append(state)

        # Логгирование
        logging.info(f'User {user_id} switched to state {state}, list of states: {user_states}, {len(user_states)},{self.storage}')

    async def set_previous_state(self, user_id: int) -> bool:
        # Получаем текущее состояние пользователя из deque
        user_states = self.storage.get(user_id, deque(["menu"]))
        # Если в deque есть предыдущее состояние, возвращаем его
        if len(user_states) > 1:
            previous_state = user_states[-2]
            user_states.pop()
            self.storage[user_id] = user_states
            logging.info(f'User {user_id} successfully returned to the previous state ({previous_state}), list of states: {user_states}, {self.storage}')
            return True
        else:
            logging.info(f'User {user_id} attempted to return to the previous state, but there was no previous state, list of states: {user_states}, {self.storage}')
            return False, previous_state

    async def reset_state(self, user_id: int) -> None:
        # Сбрасываем состояние пользователя (делаем deque пустым)
        if user_id in self.storage:
            self.storage[user_id].clear()
            self.storage[user_id].append("menu")

        # Логгирование
        logging.info(f'User {user_id} reset their state to the default state, {self.storage}')

# state_manager = StateManager()
# import asyncio
# async def main():
#     await state_manager.set_state(1, "moscow")
#     await state_manager.set_state(1, "red_square")
#     print(state_manager.storage)
#     await state_manager.set_previous_state(1)
#     print(state_manager.storage)
# asyncio.run(main())

'''
