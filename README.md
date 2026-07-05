# What's this

Python3 script.

Create a large image by reducing multiple images and arranging them in a grid.

複数の画像を縮小して格子状に並べた大きな画像を作成する

## Example: 60 images to grid

### horizontally 3 （横３）

<img width="320" height="240" alt="Image" src="https://github.com/user-attachments/assets/98974ebb-40eb-40bc-9064-06ea179db05c" />
<img width="320" height="240" alt="Image" src="https://github.com/user-attachments/assets/f48b8e4c-33b1-4ae0-b92a-63dfd3e89978" />
<img width="320" height="240" alt="Image" src="https://github.com/user-attachments/assets/01453486-7339-40df-91a0-7122c82bc4ea" />
<img width="320" height="240" alt="Image" src="https://github.com/user-attachments/assets/797c42e7-518e-4d78-9291-e18af7acf815" />
<img width="320" height="240" alt="Image" src="https://github.com/user-attachments/assets/2c6ebb6e-33ea-437f-9d17-2409334cace4" />

### horizontally 4 （横４）

<img width="320" height="240" alt="Image" src="https://github.com/user-attachments/assets/7084ba54-9c02-4417-ae17-e722088b5115" />
<img width="320" height="240" alt="Image" src="https://github.com/user-attachments/assets/7f6127b1-b566-4318-8f82-a478075f8f83" />
<img width="320" height="240" alt="Image" src="https://github.com/user-attachments/assets/3292c898-7c68-4566-9a8c-10cb4c7a50b1" />

### horizontally 5 （横５）

<img width="320" height="240" alt="Image" src="https://github.com/user-attachments/assets/65c1fe10-4ba6-4cee-8542-355eb1d220c2" />
<img width="320" height="240" alt="Image" src="https://github.com/user-attachments/assets/2553fec3-9bcc-4910-8068-fa521e3f914f" />

### horizontally 6 （横６）

<img width="320" height="240" alt="Image" src="https://github.com/user-attachments/assets/b535f17e-5629-4119-9831-8cb3c2eddde6" />
<img width="320" height="240" alt="Image" src="https://github.com/user-attachments/assets/a1b58196-f482-485d-a3b6-e080132b664b" />

### horizontally 7 （横７）

<img width="320" height="240" alt="Image" src="https://github.com/user-attachments/assets/9e4207b2-fad5-4752-8cd4-763dc265150f" />


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
