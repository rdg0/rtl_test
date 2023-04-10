import json

from aiogram import types
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from jsonschema import validate
from pymongo.collection import Collection

from settings import GROUP_TYPES
from typing import Dict, List


def validate_msg(message: types.Message) -> bool:
    """Валидируем сообщение от пользователя"""
    schema = {
        "type": "object",
        "properties": {
            "dt_from": {"type": "string"},
            "dt_upto": {"type": "string"},
            "group_type": {"type": "string"}
        },
        "required": ["dt_from", "dt_upto", "group_type"],
    }
    try:
        serializing_msg = json.loads(message.text)
        validate(instance=serializing_msg, schema=schema)
        datetime.fromisoformat(serializing_msg['dt_from'])
        datetime.fromisoformat(serializing_msg['dt_upto'])
        if serializing_msg['group_type'] not in GROUP_TYPES:
            raise ValueError

    except Exception:
        return False
    return True


def create_me_friendly_dict(message: types.Message) -> Dict:
    """ Приводим сообщение к удобному для обработки формату."""
    request = json.loads(message.text)
    request['dt_from'] = datetime.fromisoformat(request['dt_from'])
    request['dt_upto'] = datetime.fromisoformat(request['dt_upto'])
    return request


def get_labels(request: Dict) -> List:
    """Тут мы создаем все лейблы с заданным шагом,
    дабы не потерять в последующем нулевые значения."""
    labels = []
    if request['group_type'] == 'hour':
        step = timedelta(hours=1)
    elif request['group_type'] == 'day':
        step = timedelta(days=1)
    elif request['group_type'] == 'month':
        step = relativedelta(months=1)
    date = request['dt_from']
    while date <= request['dt_upto']:
        labels.append(date.isoformat())
        date += step
    return labels


def preserialazing(
        aggregate_collection: Collection, labels: List, request: Dict
) -> Dict:
    """Подготовливаем формат данных к последующей сериализации в JSON."""
    output = {
        'dataset': [0 for i in range(len(labels))],
        'labels': labels
    }
    for doc in aggregate_collection:
        label = datetime.strptime(
            doc['label'], GROUP_TYPES[request['group_type']]['format']
        )
        try:
            ind = labels.index(label.isoformat())
        except ValueError:
            print('Не мапятся временные ряды, надо разбираться')
        output['dataset'][ind] = doc['value']
    return output
