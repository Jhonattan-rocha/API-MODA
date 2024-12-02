from app.models.CustomModels import (CustomEntityToEntity, DynamicEntity, DynamicFields, DynamicFieldToEntityValue)
from app.models.DefaultModels import (User, UserProfile, Permissions, SubCategory, InputOutputStock, Company, Category,
                                      Employees, Product, Person, ProductCategory, File)
from typing import Any

models_mapping: dict[str, Any] = {
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
    "DynamicFieldToEntityValue": DynamicFieldToEntityValue,
    "File": File,
    "*": DynamicFieldToEntityValue
}

models_fields_mapping: dict[str, tuple] = {
    "CustomEntityToEntity": ("entity_id_1", "entity_id_2"),
    "ProductCategory": ("id_prod", "id_cat"),
    "User": ("name", "email", "lang", "profile_id"),
    "UserProfile": ("name",),
    "SubCategory": ("name", "id_cat"),
    "InputOutputStock": ("type", "qtd", "date", "product_id", "user_id"),
    "Company": ("name", "social_reason", "cnpj", "tel", "email", "address"),
    "Employees": ("id_emp", "name", "cpf", "tel", "email", "address"),
    "Product": ("name", "description", "price"),
    "Person": ("name", "cpf", "tel", "email", "address"),
    "*": ("entity_id", "entity_id_instance", "field_id", "value")
}
