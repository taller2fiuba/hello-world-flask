#! /usr/bin/env bash
set -e

export LISTEN_PORT=$PORT
exec "$@"
