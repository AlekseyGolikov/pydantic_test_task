
import json
from pydantic import BaseModel
from typing import Dict


def format_numbers(phone_number: str) -> str:
    """
        Форматированный вывод телефонного номера
    """
    return '{0}{1}{2}-{3}{4}-{5}{6}'.format(*[i for i in phone_number])


class InputData(BaseModel):
    description: str
    employment: str
    address: Dict
    name: str
    contacts: Dict
    salary: Dict


class OutputData(BaseModel):
    address: str
    allow_messages: bool
    billing_type: str
    business_area: int
    contacts: Dict
    coordinates: Dict
    description: str
    experience: Dict
    html_tags: bool
    image_url: str
    name: str
    salary: int
    salary_range: Dict
    schedule: Dict


def parse(in_json):
    parse_data = InputData(**in_json)
    out_data = OutputData(
        address=parse_data.address['value'],
        allow_messages=True,
        billing_type='packageOrSingle',
        business_area=1,
        coordinates={
            'latitude': parse_data.address['lat'],
            'longitude': parse_data.address['lng']
        },
        contacts={
            'email': parse_data.contacts['email'],
            'name': parse_data.contacts['fullName'],
            'phone': {
                'city': parse_data.contacts['phone'][1:4],
                'country': parse_data.contacts['phone'][0],
                'number': format_numbers(parse_data.contacts['phone'][4:])
            }
        },
        description=parse_data.description,
        experience={
            'id': 'noMatter'
        },
        html_tags=True,
        image_url='https://img.hhcdn.ru/employer-logo/3410666.jpeg',
        name=parse_data.name,
        salary=70000,
        salary_range={
            'from': parse_data.salary['from'],
            'to': parse_data.salary['to']
        },
        schedule={
            'id': parse_data.employment
        }
    )
    return out_data


if __name__ == '__main__':
    with open('in.json', encoding='utf-8') as f:
        in_data = json.load(f)
    out_data = parse(in_data)

    with open('out.json', encoding='utf-8') as f:
        od = json.load(f)
    assert out_data == od, 'Successfully!'

