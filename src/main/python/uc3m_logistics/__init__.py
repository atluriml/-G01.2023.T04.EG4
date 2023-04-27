"""UC3M Care MODULE WITH ALL THE FEATURES REQUIRED FOR ACCESS CONTROL"""

from uc3m_logistics.exceptions.order_management_exception import OrderManagementException
from .order_manager import OrderManager
from .order_manager_config import JSON_FILES_PATH, JSON_FILES_RF2_PATH, Config
from .singleton_metaclass import SingletonMeta
