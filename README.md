[![Check and Lint](https://github.com/winsphinx/Toolbox/actions/workflows/check.yml/badge.svg)](https://github.com/winsphinx/Toolbox/actions/workflows/check.yml)
[![Build and Push Docker Image](https://github.com/winsphinx/toolbox/actions/workflows/docker.yml/badge.svg)](https://github.com/winsphinx/toolbox/actions/workflows/docker.yml)

# 7086 Tool Box
七零八落工具箱

## Docker 部署

```sh
docker run -d --name=toolbox --restart=unless-stopped -p 7086:7086 ghcr.io/winsphinx/toolbox:latest
```

或

```yaml
version: '3'
services:
  toolbox:
    image: ghcr.io/winsphinx/toolbox:latest
    container_name: toolbox
    restart: unless-stopped
    ports: 7086:7086
```
