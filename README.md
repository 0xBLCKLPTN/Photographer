<div align="center">
  <img src="https://github.com/0xBLCKLPTN/Photographer/blob/master/screenshots/camera.png?raw=True" height='64px'/>
  <h1>Photographer</h1>
  <p>Cross-platform utility for creating beautiful screenshots.</p>
  <img src="https://github.com/0xBLCKLPTN/Photographer/blob/master/screenshots/final_image.png?raw=True"/>
</div>

## Install dependencies
```sh
poetry install     # If you are using poetry.
pip3 install -r requirements.txt   # default pip3
```

## Run
```sh
poetry run python3 main.py ./bg.png -s    # with poetry
python3 main.py ./bg.png -s               # with python
```

### Flags
| Flag |     description                      |
|------|--------------------------------------|
|  -s  | show image with default photo editor after save |
|  -b  | copy to buffer. currectly not works  |
|------|--------------------------------------|
