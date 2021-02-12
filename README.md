### 02-parent-images
# Home Assignment - Part II

This python script does a recursive search for Dockerfiles in a directory passed as an argument. 
It prints the Dockerfile's base image and file path in this format: `<FILE PATH>: <BASEIMAGE>`

# Sample Usage and Output
```
$ ./02-parent-images.py .
./Dockerfile: alpine:3.12
./database/redis/cluster/Dockerfile: redis:5.9.11
./database/postgres/Dockerfile: postgres:14.5
./sample-app/Dockerfile: ubuntu:22.04
```
