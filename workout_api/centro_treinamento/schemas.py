from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    
    nome: Annotated[str, Field(description='nome centro de treinamento', exemple='CT king', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', exemple='Rua Y, Q01', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do centro de treinamento', exemple='Vinicius Costa', max_length=30)]