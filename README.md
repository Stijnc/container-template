# Sample project for docker - GH actions - ACR integration

The sample focusses on the docker build, helm and ACR integration.

2 pipelines exist, but share the same principles.

1. build docker
2. push to acr
3. push helm chart
4. lock docker image for immutability

the ci_acrtask pipeline replaces the docker build for an acr build, enabling automatic base image update triggers.

<!-- As a version the the commit short sha is used. -->

## todo

### linting

- [x] add superlinter

### docker - local validation

- [x] generate docker meta data
- [x] setup QEMU
- [x] setup dokcer buildx
- [x] docker build
- [] inspect digest

### docker - sinple build and push (local)

- [ ] include job services (local registry)
- [x] generate docker meta data
- [x] setup QEMU
- [x] setup dokcer buildx
- [x] docker build and push
- [x] inspect image and digest

### docker - simple build and push

- [x] generate docker meta data
- [x] setup QEMU
- [x] setup dokcer buildx
- [ ] docker login
    - [ ] github registry
- [x] docker build and push
- [x] inspect image and digest

### docker - advanced build and push

- [ ] include registry matrix (ghcr, acr)
- [x] generate docker meta data
- [x] setup QEMU
- [x] setup dokcer buildx
- [ ] docker login (multiple registries)
- [x] docker build and push
- [x] inspect image and digest

### docker - advanced bake file

- [ ] include registry matrix (ghcr, acr)
- [x] generate docker meta data
- [x] setup QEMU
- [x] setup dokcer buildx
- [ ] docker login (multiple registries)
- [x] docker bake
    - [ ] multi-arch (arm64, amd64, armv6, armv7)
- [x] inspect image and digest

### docker - advanced bake file and scanning

- [ ] include registry matrix (ghcr, acr)
- [x] generate docker meta data
- [x] setup QEMU
- [x] setup dokcer buildx
- [ ] docker login (multiple registries)
- [x] docker bake
    - [] multi-arch (arm64, amd64, armv6, armv7)
- [x] inspect image and digest
- [ ] scan image (aqua / anchor)
- [ ] security center integration?
