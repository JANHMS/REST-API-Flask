from ma import ma
from models.item import ItemModel
from models.store import StoreModel
from schema.item import ItemSchema


class ItemSchema(ma.ModelSchema):
    items = ma.Nested(ItemSchema, many=True)
    
    class Meta:
        model = ItemModel
        dump_only = ("id",)
        include_fk = True
