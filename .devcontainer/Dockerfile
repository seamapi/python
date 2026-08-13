ARG VARIANT="3"

FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

ARG NODE_VERSION="24"
ARG UV_VERSION="0.8.17"
ARG UV_SRC="https://astral.sh/uv"

# https://github.com/microsoft/vscode-dev-containers/blob/main/containers/go/.devcontainer/base.Dockerfile
ENV USERNAME=vscode
ENV LIBRARY_SCRIPTS_SRC="https://raw.githubusercontent.com/microsoft/vscode-dev-containers/main/containers/go/.devcontainer/library-scripts/node-debian.sh"
ENV NVM_DIR=/usr/local/share/nvm
ENV NVM_SYMLINK_CURRENT=true \
    PATH=${NVM_DIR}/current/bin:${PATH}
RUN mkdir /tmp/library-scripts \
 && curl -fsSL -o /tmp/library-scripts/node-debian.sh "${LIBRARY_SCRIPTS_SRC}"
RUN bash /tmp/library-scripts/node-debian.sh "${NVM_DIR}" "${NODE_VERSION}" "${USERNAME}" \
 && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
 && rm -rf /tmp/library-scripts

RUN apt-get update -y \
 && apt-get install -y --no-install-recommends just \
 && apt-get clean -y && rm -rf /var/lib/apt/lists/*

USER vscode
WORKDIR /home/vscode

RUN curl -fsSL "${UV_SRC}/${UV_VERSION}/install.sh" | sh

RUN mkdir -p .config/git \
 && echo ".vscode/*" >> .config/git/ignore \
 && echo "*.code-workspace" >> .config/git/ignore \
 && echo ".history/" >> .config/git/ignore
