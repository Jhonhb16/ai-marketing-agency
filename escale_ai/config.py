"""
Configuration constants for the AI Marketing Agency project.

Centralizing these values makes it easy to adjust sending limits,
allowed countries and default brand settings in one place.
"""

# Maximum number of cold emails the base team should send per day
EMAIL_LIMIT_PER_DAY: int = 50

# Country where operations are allowed; clients must be within this region
ALLOWED_COUNTRY: str = "United States"

# Default brand kit settings used when creating a new client workspace
DEFAULT_BRAND_KIT: dict[str, str] = {
    "logo_path": "assets/default_logo.png",
    "primary_color": "#0066CC",
    "secondary_color": "#CCCCCC",
}
