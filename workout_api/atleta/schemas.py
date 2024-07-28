from typing import Annotated
from pydantic import  Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='nome do atleta', exemple='joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', exemple='1223451221', max_length=11)]
    idade: Annotated[int, Field(description='idade do atleta', exemple='30')]
    peso: Annotated[PositiveFloat, Field(description='altura do atleta', exemple='1.70')]
    sexo: Annotated[str, Field(description='sexo do atleta', exemple='M',max_length=1)]
