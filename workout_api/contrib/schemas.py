from pydantic import BaseModel
    
class BaseSchema(BaseModel):
    class config:
        extra = 'forbid'
        from_atributes = True   