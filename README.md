# What's this

Python3 script.

Create a large image by reducing multiple images and arranging them in a grid.

複数の画像を縮小して格子状に並べた大きな画像を作成する

# Usage

python3 tile_images.py output width heith column images

- output : path for output image
- width : width for output image
- height : height for output image
- column : grid counted horizontally
- images : path for input images

## Example1

```
$ python3 tile_images.py aa 1600 1200 5 images/*
```
```
$ ls
aathumb_0001.jpg
aathumb_0002.jpg
aathumb_0003.jpg
aathumb_0004.jpg
 ;
```

## Example2

```
$ python3 tile_images.py output_dir/ 1600 1200 5 images/*
```
```
$ ls
output_dir/thumb_0001.jpg
output_dir/thumb_0002.jpg
output_dir/thumb_0003.jpg
output_dir/thumb_0004.jpg
 ;
```

## Example3

```
$ python3 tile_images.py output_dir/aa 1600 1200 5 images/*
```
```
$ ls
output_dir/aathumb_0001.jpg
output_dir/aathumb_0002.jpg
output_dir/aathumb_0003.jpg
output_dir/aathumb_0004.jpg
 ;
```

