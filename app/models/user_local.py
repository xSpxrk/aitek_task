

class User:
    """
    Класс для пользователей, если пользователь настроен для хранения локально данных.
    """
    _id: int = 1

    def __init__(self, fio: str):
        self.fio = fio
        self.id = User._id
        User._change_id()

    @classmethod
    def _change_id(cls):
        User._id += 1

    @classmethod
    def get_id(cls) -> int:
        return User._id
