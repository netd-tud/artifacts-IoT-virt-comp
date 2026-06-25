FROM ubuntu:24.04

# Prevent interactive prompts during package install
ARG DEBIAN_FRONTEND=noninteractive

# Install system packages
RUN apt-get update && apt-get install -y \
    sudo \
    curl \
    clang-20 \
    llvm-20 \
    libclang-rt-20-dev-wasm32 \
    lld-20 \
    clang-14 \
    libclang-14-dev \
    llvm-14 \
    llvm-14-dev \
    make \
    gcc-multilib \
    python3 \
    python3-pip \
    wget \
    unzip \
    git \
    openocd \
    gdb-multiarch \
    esptool \
    podman-docker \
    clangd \
    cmake \
    libssl-dev \
    pkg-config \
    gcc-arm-none-eabi \
    picocom \
    xxd \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

# There already is a ubuntu user -> give it sudo rights
RUN echo "ubuntu ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN update-alternatives --install /usr/bin/clang clang /usr/bin/clang-14 100  --slave /usr/bin/clang++ clang++ /usr/bin/clang++-14

# Switch to the ubuntu user
USER ubuntu
ENV HOME=/home/ubuntu
ENV CARGO_HOME=/home/ubuntu/.cargo
ENV RUSTUP_HOME=/home/ubuntu/.rustup
ENV PATH=/home/ubuntu/.cargo/bin:/home/ubuntu/.local/bin:$PATH

# Install Rust toolchain as non-root user
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
RUN rustup target add thumbv7em-none-eabihf \
    && cargo install c2rust --git https://github.com/immunant/c2rust --tag v0.19.0 --locked
    && cargo install rustfilt

# One rust dependency needs clang-14, form now on we use clang-20
RUN sudo update-alternatives --install /usr/bin/clang clang /usr/bin/clang-20 200  --slave /usr/bin/clang++ clang++ /usr/bin/clang++-20

WORKDIR /artifacts

COPY requirements.txt /requirements.txt

RUN pip install --user --ignore-installed --break-system-packages -r /requirements.txt

CMD ["/bin/bash"]
