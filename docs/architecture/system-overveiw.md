# System Overview

## Components

- CI/CD Pipeline
- OTA Server
- Edge Device Agent

## Flow

1. Developer pushes code
2. CI/CD signs firmware
3. Server stores firmware
4. Device downloads firmware
5. Device verifies signature
6. If valid → install update
