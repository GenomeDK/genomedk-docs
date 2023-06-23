FROM ghcr.io/getzola/zola:v0.17.2 AS builder

WORKDIR /app
COPY . .
RUN ["zola", "build"]

FROM pierrezemb/gostatic
COPY --from=builder /app/public /srv/http/
