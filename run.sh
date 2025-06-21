#!/bin/bash

# 🚀 LinkedIn AI Consultant - Build & Run Script
echo "🚀 LinkedIn AI Consultant - Docker Build & Run"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Check if API key is provided
if [ -z "$1" ]; then
    echo "❌ Usage: ./run YOUR_GOOGLE_API_KEY"
    echo "🔗 Get your API key from: https://aistudio.google.com/app/apikey"
    exit 1
fi

API_KEY="$1"
IMAGE_NAME="linkedin-ai-consultant"
CONTAINER_NAME="linkedin-consultant"

echo "🔧 Building Docker image..."
if docker build -t $IMAGE_NAME .; then
    echo "✅ Docker image built successfully!"
else
    echo "❌ Failed to build Docker image"
    exit 1
fi

# Stop and remove existing container if it exists
if docker ps -a | grep -q $CONTAINER_NAME; then
    echo "🛑 Stopping existing container..."
    docker stop $CONTAINER_NAME > /dev/null 2>&1
    echo "🗑️ Removing existing container..."
    docker rm $CONTAINER_NAME > /dev/null 2>&1
fi

echo "🚀 Starting new container..."
if docker run -d \
    --name $CONTAINER_NAME \
    -p 7860:7860 \
    -e GOOGLE_API_KEY="$API_KEY" \
    $IMAGE_NAME; then
    
    echo "✅ Container started successfully!"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🌐 Application URL: http://localhost:7860"
    echo "📊 Container Status: docker ps"
    echo "📋 View Logs: docker logs $CONTAINER_NAME"
    echo "🛑 Stop Container: docker stop $CONTAINER_NAME"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    # Wait a moment and check if container is running
    sleep 3
    if docker ps | grep -q $CONTAINER_NAME; then
        echo "🎉 LinkedIn AI Consultant is ready!"
        echo "💼 Open http://localhost:7860 to start consulting with Hayek!"
    else
        echo "⚠️ Container may have stopped. Check logs:"
        docker logs $CONTAINER_NAME
    fi
else
    echo "❌ Failed to start container"
    exit 1
fi