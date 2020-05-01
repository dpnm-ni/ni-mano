# ni-mano
Dev: [![Build Status](http://141.223.82.61:9010/api/badges/dpnm-ni/ni-mano/status.svg?ref=refs/heads/dev)](http://141.223.82.61:9010/dpnm-ni/ni-mano)

Master: [![Build Status](http://141.223.82.61:9010/api/badges/dpnm-ni/ni-mano/status.svg?ref=refs/heads/master)](http://141.223.82.61:9010/dpnm-ni/ni-mano)

Monorepo for the ni-mano related modules.
Browse each sub folders for detailed README.

NI-MANO architecture documentation on google doc: [link](https://docs.google.com/document/d/1mPfyjV3OFvtscQvKekPSgNlGsp_RAB2p5eQLtXOguFU)

# Local testing with drone CI
- Install [Drone CLI](https://docs.drone.io/cli/install/)
- If `ufw` is used, need to allow local traffic
    ``` bash
    sudo ufw allow from 172.0.0.0/8
    sudo ufw allow from 192.0.0.0/8
    ```
- Add `secret.txt` file, then run
    ``` bash
    drone exec --secret-file secret.txt --pipeline ni-tests__dev .drone.yml
    ```

