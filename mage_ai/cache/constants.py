from mage_ai.shared.enum import StrEnum

CACHE_KEY_BLOCKS_TO_PIPELINE_MAPPING = 'blocks_to_pipeline_mapping'
CACHE_KEY_BLOCK_ACTION_OBJECTS_MAPPING = 'block_action_objects_mapping'
CACHE_KEY_DBT_PROJECTS_PROFILES_MODELS = 'dbt_projects_profiles_models'
CACHE_KEY_FILES = 'files'
CACHE_KEY_PIPELINE_DETAILS_MAPPING = 'pipeline_details_mapping'
CACHE_KEY_TAGS_TO_OBJECT_MAPPING = 'tags_to_object_mapping'

MAGE_CACHE_DIRECTORY_DEFAULT = '.cache'
MAGE_CACHE_DIRECTORY_ENVIRONMENT_VARIABLE_NAME = 'MAGE_CACHE_DIRECTORY'


class CacheItemType(StrEnum):
    DBT = 'dbt'
