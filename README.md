# Sample project for docker - GH actions - ACR integration

The sample focusses on the docker build, helm and ACR integration.

2 pipelines exist, but share the same principles.

1. build docker
2. push to acr
3. push helm chart
4. lock docker image for immutability

the ci_acrtask pipeline replaces the docker build for an acr build, enabling automatic base image update triggers.

As a version the the commit short sha is used.