lint-backend:
	(cd backend && .venv/bin/black .)

lint-frontend:
	(cd frontend && npm run lint)