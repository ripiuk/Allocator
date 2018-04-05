## Image manual allocator

### Description
It's a mapping tool, which will help you to distribute images by their class manually.

### How to run
* Install python:
```bash
    make install
```

* Create/update virtual environment with all 
necessary libraries by this commands:
```bash
    make venv_init
    make venv_update
```

* Activate the virtual environment by command:
```bash
    source venv/bin/activate
```

* Run server by command:
```bash
    make runserver
```

* Place your images in the `media` folder in the project's core

* Go to http://127.0.0.1:8080