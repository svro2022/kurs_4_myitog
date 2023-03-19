from contextlib import suppress
from typing import Any, Dict, List, Type

from sqlalchemy.exc import IntegrityError

from project.config import config

from project.models import Genre
from project.models import Director
from project.models import Movie

from project.server import create_app
from project.setup.db import db, models
from project.utils import read_json


def load_data(data: List[Dict[str, Any]], model: Type[models.Base]) -> None:
    for item in data:
        item['id'] = item.pop('pk')
        db.session.add(model(**item))


if __name__ == '__main__':
    fixtures: Dict[str, List[Dict[str, Any]]] = read_json("fixtures.json")

    app = create_app(config)

    with app.app_context():
        db.drop_all()
        db.create_all()

        load_data(fixtures['directors'], Director)
        load_data(fixtures['movies'], Movie)
        load_data(fixtures['genres'], Genre)

        with suppress(IntegrityError):
            db.session.commit()
