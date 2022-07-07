# ColorOfMovies
This is a small python script that can be used to generate images like this from movies or other video files:
## Examples
### Cloud Atlas (2012)
#### Skip-Rate: 100
![](/example/color_of_cloud_atlas_100.jpg)

### Matrix (1999)
#### Skip-Rate: 100
![](/example/color_of_matrix_100.jpg)

## Installation
```
git clone https://github.com/leumon/ColorOfMovies.git
pip install opencv-python
```

## Usage
```
python colorofmovies.py <optional: movie path> <optional: skip rate>
```
Default values:
`movie_path="movie.mp4"` and `skip_rate=100`

### Example
```
python colorofmovies.py cloud_atlas.mp4
python colorofmovies.py matrix.mp4 30
```

## License
See the [LICENSE](LICENSE) file.

## Credits
Inspired by the works of [lomoeffect](https://www.reddit.com/user/lomoeffect/) and [etherealpenguin](https://www.reddit.com/user/etherealpenguin/).
