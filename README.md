
create docker group to use it without sudo
```sh
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```