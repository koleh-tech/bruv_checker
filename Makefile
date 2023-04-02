generate_static_app:
	shinylive export myapp docs

install_dependencies:
	pip install -r myapp/requirements.txt

serve_app:
	python3 -m http.server --directory docs --bind localhost 8008
