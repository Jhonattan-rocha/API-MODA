from app.controllers.DefaultControllers import (get_category, get_categories, create_category,
                                                delete_category,
                                                update_category)
from app.controllers.DefaultControllers import get_product, get_products, create_product, \
    delete_product, update_product
from app.controllers.DefaultControllers import (get_product_category, create_product_category,
                                                update_product_category,
                                                get_product_categories,
                                                delete_product_category)
from app.controllers.DefaultControllers import (delete_subcategory, get_subcategory,
                                                get_subcategories, create_subcategory,
                                                update_category)
from app.controllers.DefaultControllers import get_people, get_person, create_person, delete_person, \
    update_person
from app.controllers.DefaultControllers import get_company, get_companies, create_company, \
    delete_company, update_company
from app.controllers.DefaultControllers import get_user, get_users, update_user, delete_user, create_user
from app.controllers.DefaultControllers import (get_user_profiles, get_user_profile, update_user_profile,
                                                delete_user_profile, create_user_profile)
from app.controllers.DefaultControllers import (get_permission, get_permissions, update_permissions, delete_permissions,
                                                create_permissions)
from app.controllers.DefaultControllers import (get_input_output_stocks, delete_input_output_stock,
                                                update_input_output_stock, create_input_output_stock,
                                                get_input_output_stock)
from app.controllers.DefaultControllers import (create_access_token, verify_token, SECRET_KEY,
                                                oauth2_scheme, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM)
from app.controllers.DefaultControllers import get_employees, get_employee, delete_employee, create_employee, update_employee

from app.controllers.DefaultControllers import get_logs, create_log, delete_log

from app.controllers.CustomControllers import (get_dynamic_entities, get_dynamic_entity,
                                               create_dynamic_entities,
                                               delete_dynamic_entity, update_dynamic_entity)
from app.controllers.CustomControllers import (get_dynamic_fields, update_dynamic_field,
                                               delete_dynamic_field,
                                               get_dynamic_field, create_dynamic_fields)
from app.controllers.CustomControllers import (get_dynamic_fields_values,
                                               create_dynamic_field_value,
                                               get_dynamic_field_value,
                                               delete_dynamic_field_value,
                                               update_dynamic_field_value)
