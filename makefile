install-package:
	@read -p "Enter package name: " package; \
	docker compose exec mock_ws poetry add $$package

remove-package:
	@read -p "Enter package name: " package; \
	docker compose exec mock_ws poetry remove $$package