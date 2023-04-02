Used for loading and validating BRUV data.

# Project structure

```
docs/
├─ This is where github gets static content from
myapp/
├─ main.py (used to run main logic)
├─ app.py (configure shiny app)
├─ load_bruv_training.py (useful functions for formatting and validating)
```

# Running

Most of the commands to get setup and generate the static website are in the makefile:

### Install dependencies:

```
make install_dependencies
```

### Generate static website:

```
make generate_static_app
```

#### Serve website locally for debugging etc.:

```
make serve_app
```

