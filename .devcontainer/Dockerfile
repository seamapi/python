ARG VARIANT="3"

FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

ARG NODE_VERSION="20"
ARG POETRY_VERSION="1.8.2"
ARG POETRY_SRC="https://install.python-poetry.org"

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

USER vscode
WORKDIR /home/vscode

RUN curl -fsSL -o install-poetry.py "${POETRY_SRC}" \
 && python install-poetry.py --version $POETRY_VERSION \
 && rm install-poetry.py

RUN mkdir -p .config/git \
 && echo ".vscode/*" >> .config/git/ignore \
 && echo "*.code-workspace" >> .config/git/ignore \
 && echo ".history/" >> .config/git/ignore
