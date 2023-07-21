FROM rust:slim AS zola-builder

RUN apt-get update -y && \
    apt-get install -y make g++ libssl-dev zip wget && \
    rustup target add x86_64-unknown-linux-gnu

RUN wget -q https://github.com/getzola/zola/archive/refs/heads/next.zip && \
    unzip -q next.zip -d /app/
WORKDIR /app/zola-next
RUN cargo build --release --target x86_64-unknown-linux-gnu

FROM gcr.io/distroless/cc AS site-builder
COPY --from=zola-builder /app/zola-next/target/x86_64-unknown-linux-gnu/release/zola /bin/zola
WORKDIR /app
COPY . .
RUN ["/bin/zola", "build"]

FROM joseluisq/static-web-server:2
COPY --from=site-builder /app/public /public
ENV SERVER_PORT 8043
