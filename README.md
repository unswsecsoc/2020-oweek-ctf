2020 O-Week CTF
===============

Repository for challenges in the 2020 o-week ctf.

## Format
- Each challenge should be placed in a separate folder, either web, bin or other.
- All CTF platform related files should be placed in a subfolder named `_ctfd`
- Challenges placed in web or bin should be deployable, and should have a Dockerfile.
- Each challenge should have a `challenge.md` file with the format specified below.
- Optionally, each challenge can have a `files/` directory for storing files, and a
  `hints/` directory with markdown hints.
- See the `example_challenge` folder for an example.


## Deployment
Use the Container Optimzed OS image on Google Cloud. Also make sure to enable the necessary ports.

```sh
cd web
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v "$PWD:$PWD" -w="$PWD" docker/compose:1.24.0 up -d
cd ../binary # doesn't exist yet
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v "$PWD:$PWD" -w="$PWD" docker/compose:1.24.0 up -d
```
