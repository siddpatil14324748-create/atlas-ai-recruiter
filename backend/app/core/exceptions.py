class AtlasAIError(Exception):
    """Base exception for Atlas AI application errors."""


class ConfigurationError(AtlasAIError):
    """Raised when configuration is invalid."""
