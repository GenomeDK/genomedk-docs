FROM ghcr.io/getzola/zola:v0.19.1 AS builder
WORKDIR /app
COPY . .
RUN ["zola", "build"]

FROM joseluisq/static-web-server:2
COPY --from=builder /app/public /public
ENV SERVER_PORT 8043
