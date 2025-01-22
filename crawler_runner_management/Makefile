start:
	@echo "Starting Docker services..."
	@sudo docker-compose up -d --build

# Target to stop Docker services
end:
	@echo "Stopping Docker services..."
	@sudo docker-compose down

# Target to remove all Docker containers
clear:
	@echo "Removing all Docker containers..."
	@sudo docker rm -f $$(docker ps -a -q) || true