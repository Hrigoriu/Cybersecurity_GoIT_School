#!/bin/bash

# Quick Start Script for Pokemon Collection App
# Run this to start both frontend and backend

echo "🎮 Starting Pokemon Collection App..."
echo ""

# Start backend
echo "Starting Backend (port 3001)..."
npm start &
BACKEND_PID=$!

# Give backend time to start
sleep 2

# Start frontend
echo ""
echo "Starting Frontend (port 3000)..."
echo ""
cd frontend
echo "Frontend ready at: http://localhost:3000"
echo "Backend ready at: http://localhost:3001"
echo ""
echo "Serving frontend..."

# Use Python for HTTP server if available, otherwise npx
if command -v python3 &> /dev/null; then
  python3 -m http.server 3000
else
  npx http-server -p 3000
fi

# Cleanup
trap "kill $BACKEND_PID" EXIT
