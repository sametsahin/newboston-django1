from core.core.utils.collections import deep_update
from core.core.utils.settings import get_settings_from_envoirement

deep_update(globals(),get_settings_from_envoirement(ENVVAR_SETTINGS_PREFIX)) # type: ignore