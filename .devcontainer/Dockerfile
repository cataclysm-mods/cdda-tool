# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.194.3/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3.9"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# Install any system dependencies required by this project.
# At this time, the only *direct* dependency is libvips: https://github.com/libvips/libvips
#
# However, this project has a build-time dependency on
# This in turn depends on `pycairo` and `PyGObject`, which in turn depend on
#
# See: https://pygobject.readthedocs.io/en/latest/getting_started.html#ubuntu-getting-started
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends libvips libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0

# Use Poetry to manage python dependencies
#
# Note: Previous commands are run as `root` while Poetry must be run as the development user (`vscode`)
USER vscode
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# This is a single project Docker image, so we have no need for Poetry to use
# Python virtualenvs to isolate dependencies
RUN . $HOME/.poetry/env && poetry config virtualenvs.create false
