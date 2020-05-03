# ni_horizon
Horizon integrated web GUI to ni-mano.

# Installation
Note: Should install into an environment where Openstack Horizon is all ready installed.

```bash
    cd ~
    git clone https://github.com/dpnm-ni/ni-mano
    # edit ni_client endpoints
    vi ni-mano/ni_horizon/openstack_dashboard/api/config/config.yaml
    # install ni_horizon as pip module
    pip install --user -e ni_mano/ni_horizon
    # enable ni_horizon dashboard in Openstack horizon
    cp ni-mano/ni_horizon/ni_horizon/enabled/_50_ni_mano.py horizon/openstack_dashboard/enabled/
    # collect & compress horizon static files, then reboot apache server
    cd horizon && echo yes | ./manage.py collectstatic && ./manage.py compress
    sudo service apache2 restart
```

