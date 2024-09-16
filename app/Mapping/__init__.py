from app.models.CustomModels import (PersonToCustomEntity, UserToCustomEntity, CompanyToCustomEntity,
                                     ProductToCustomEntity, CategoryToCustomEntity, EmployeeToCustomEntity,
                                     SubCategoryToCustomEntity, CustomEntityToCustomEntity)
from app.models.DefaultModels import (User, UserProfile, Permissions, SubCategory, InputOutputStock, Company, Category,
                                      Employees, Product, Person, ProductCategory)
from app.database import Base

models_mapping: dict[str, Base] = {
    "PersonToCustomEntity": PersonToCustomEntity,
    "UserToCustomEntity": UserToCustomEntity,
    "CompanyToCustomEntity": CompanyToCustomEntity,
    "ProductToCustomEntity": ProductToCustomEntity,
    "CategoryToCustomEntity": CategoryToCustomEntity,
    "EmployeeToCustomEntity": EmployeeToCustomEntity,
    "SubCategoryToCustomEntity": SubCategoryToCustomEntity,
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
    "CustomEntityToCustomEntity": CustomEntityToCustomEntity
}

models_fields_mapping: dict[str, Base] = {
    "PersonToCustomEntity": ("person_id", "entity_id"),
    "UserToCustomEntity": ("user_id", "entity_id"),
    "CompanyToCustomEntity": ("company_id", "entity_id"),
    "ProductToCustomEntity": ("product_id", "entity_id"),
    "CategoryToCustomEntity": ("category_id", "entity_id"),
    "EmployeeToCustomEntity": ("employee_id", "entity_id"),
    "SubCategoryToCustomEntity": ("subcategory_id", "entity_id"),
    "CustomEntityToCustomEntity": ("entity_id_1", "entity_id_2"),
    "ProductCategory": ("id_prod", "id_cat")
}
