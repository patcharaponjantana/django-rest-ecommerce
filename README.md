
create docker group to use it without sudo
```sh
sudo groupadd docker
sudo usermod -aG docker $USER
sudo gpasswd -a $USER docker
newgrp docker
```