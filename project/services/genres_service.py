from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Genre

#page=page возвращение конкретной страницы

class GenresService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Genre:
        """
        Сервис получения одного жанра
        :param pk:
        :return:
        """
        if genre := self.dao.get_by_id(pk):
            return genre
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Genre]:
        """
        Сервис получения всех жанров
        :param page:
        :return:
        """
        return self.dao.get_all(page=page)
