2020 O-Week CTF
===============

Repository for challenges in the 2020 o-week ctf. Source code and everything included so that you can run it for yourself.

If you want to contribute to the writeups, feel free to make a pull request here.

## Deployment
Use the Container Optimzed OS image on Google Cloud. Also make sure to enable the necessary ports.

```sh
cd web
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v "$PWD:$PWD" -w="$PWD" docker/compose:1.24.0 up -d
cd ../binary
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v "$PWD:$PWD" -w="$PWD" docker/compose:1.24.0 up -d
```

If running on your local machine or other platforms, docker-compose will suffice.

```sh
cd web
docker-compose up -d
cd ../binary
docker-compose up -d
```

