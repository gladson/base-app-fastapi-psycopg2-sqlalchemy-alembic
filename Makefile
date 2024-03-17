p_add:
	poetry add $(pkg)

p_add_dev:
	poetry add --group=dev $(pkg)

p_remove:
	poetry remove $(pkg)

p_remove_dev:
	poetry remove --group=dev $(pkg)

p_update:
	poetry update

p_new:
	poetry new --src --name apps.$(name) backend

p_export:
	poetry export -f requirements.txt --output requirements.txt

# make a_migrate table='users'
a_migrate:
	alembic revision --autogenerate -m "create $(table) table"

a_up:
	alembic upgrade head