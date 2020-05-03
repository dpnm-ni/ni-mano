# The name of the dashboard to be added to HORIZON['dashboards']. Required.
DASHBOARD = 'ni_mano'

# If set to True, this dashboard will not be added to the settings.
DISABLED = False

AUTO_DISCOVER_STATIC_FILES = True

# A list of applications to be added to INSTALLED_APPS.
ADD_INSTALLED_APPS = [
    'ni_horizon.openstack_dashboard.dashboards.ni_mano',
]
