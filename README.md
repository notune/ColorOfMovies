# ColorOfMovies
This is a small python script that can be used to generate images like this from movies or other video files:
## Examples
### Cloud Atlas (2012)
#### Skip-Rate: 100
![](/example/final_image_100.jpg)
#### Skip-Rate: 5000
![](/example/final_image_5000.jpg)

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

## License
See the [LICENSE](LICENSE) file.

## Credits
Inspired by the works of [lomoeffect](https://www.reddit.com/user/lomoeffect/) and [etherealpenguin](https://www.reddit.com/user/etherealpenguin/).
