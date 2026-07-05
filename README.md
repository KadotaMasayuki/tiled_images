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

## Example1 : 4 columns

```
$ python3 tile_images.py aa 320 240 4 images/*
```
```
$ ls
aathumb_0001.jpg
aathumb_0002.jpg
aathumb_0003.jpg
aathumb_0004.jpg
 ;
```

<img width="320" height="240" alt="Image" src="https://github.com/user-attachments/assets/9d8b0d7a-5275-477a-b28c-7050c0c5d1b4" />

## Example2 : 5 columns

```
$ python3 tile_images.py output_dir/ 320 240 5 images/*
```
```
$ ls
output_dir/thumb_0001.jpg
output_dir/thumb_0002.jpg
output_dir/thumb_0003.jpg
output_dir/thumb_0004.jpg
 ;
```

<img width="320" height="240" alt="Image" src="https://github.com/user-attachments/assets/8ad5a792-f7ad-4014-af9d-8481aca3da7b" />

## Example3 : 6 columns

```
$ python3 tile_images.py output_dir/aa 320 240 6 images/*
```
```
$ ls
output_dir/aathumb_0001.jpg
output_dir/aathumb_0002.jpg
output_dir/aathumb_0003.jpg
output_dir/aathumb_0004.jpg
 ;
```

<img width="320" height="240" alt="Image" src="https://github.com/user-attachments/assets/0a00e05f-bc59-4a7d-b9c1-ddb6a2b921c9" />
