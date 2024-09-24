from app.models.CustomModels import (CustomEntityToEntity, DynamicEntity, DynamicFields, DynamicFieldToEntityValue)
from app.models.DefaultModels import (User, UserProfile, Permissions, SubCategory, InputOutputStock, Company, Category,
                                      Employees, Product, Person, ProductCategory)
from app.database import Base

models_mapping: dict[str, Base] = {
    "User": User,
    "UserProfile": UserProfile,
    "Permissions": Permissions,
    "SubCategory": SubCategory,
    "InputOutputStock": InputOutputStock,
    "Company": Company,
    "Category": Category,
    "Employees": Employees,
    "Product": Product,
    "Person": Person,
    "ProductCategory": ProductCategory,
    "CustomEntityToEntity": CustomEntityToEntity,
    "DynamicEntity": DynamicEntity,
    "DynamicFields": DynamicFields,
    "DynamicFieldToEntityValue": DynamicFieldToEntityValue
}

models_fields_mapping: dict[str, tuple] = {
    "CustomEntityToEntity": ("entity_id_1", "entity_id_2"),
    "ProductCategory": ("id_prod", "id_cat")
}
