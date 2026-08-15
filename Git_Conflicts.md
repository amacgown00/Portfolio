# Handling Git Merge Conflicts/Other CMD/Unix Commands 

### Searching for files 
<!-- current folder-->
```bash
$ find . -name file_name
```

### Starting from home directory 
```bash
$ find ~/ -name file_name
```

### Starts with 
```bash
$ find ~/ -name file*
```

CTRL + R 
Recursive search on past commands  



### Text content within a file
```bash 
$ grep -r "word 
```

### Auto-complete with spaces



Onedrive - Company

```$ cd Onedrive\ ``` + space +  TAB - 


My Folder
My Photos 
```bash
$ cd My\ F
```

Tab 

## grep - searching for values 

### Values in all files 
```bash
$ grep -r "word"
```

### Values in one file 
```bash
$ grep "word" file_name.txt
```

### Remove from stage
```bash
git restore --staged file_name
```

### Edit a file in terminal
```bash
$ vim file_name
```

```i``` - Edit mode 
```ESC``` - Read mode

Save 
`ESC` + `:wq`


```python
print(str(len(list)))
```

ffmpeg -loop 1 -t 1.33 -i IMG_1420.jpg -loop 1 -t 1.33 -i IMG_1419.jpg -loop 1 -t 1.34 -i IMG_1418.jpg -filter_complex "[0][1][2]concat=n=3:v=1:a=0" -r 30 summer_sound.mp4

ffmpeg -loop 1 -t 1.33 -i IMG_1420.jpg \
       -loop 1 -t 1.33 -i IMG_1419.jpg \
       -loop 1 -t 1.34 -i IMG_1418.jpg \
       -filter_complex "[0:v]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,setsar=1[v0]; \
                        [1:v]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,setsar=1[v1]; \
                        [2:v]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,setsar=1[v2]; \
                        [v0][v1][v2]concat=n=3:v=1:a=0[outv]" \
       -map "[outv]" -r 30 -c:v libx264 -pix_fmt yuv420p summer_sound.mp4

ffmpeg -loop 1 -t 1.33 -i IMG_1420.jpg \
       -loop 1 -t 1.33 -i IMG_1419.jpg \
       -loop 1 -t 1.34 -i IMG_1418.jpg \
       -filter_complex "[0:v]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,setsar=1[v0]; \
                        [1:v]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,setsar=1[v1]; \
                        [2:v]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,setsar=1[v2]; \
                        [v0][v1][v2][v0][v1][v2][v0][v1][v2]concat=n=9:v=1:a=0[outv]" \
       -map "[outv]" -r 30 -c:v libx264 -pix_fmt yuv420p summer_sound1.mp4

ffmpeg -loop 1 -t 1.33 -i IMG_1420.jpg -loop 1 -t 1.33 -i IMG_1419.jpg -loop 1 -t 1.34 -i IMG_1418.jpg -filter_complex "[0:v]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,setsar=1[v0];[1:v]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,setsar=1[v1];[2:v]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,setsar=1[v2];[v0][v1][v2][v0][v1][v2][v0][v1][v2]concat=n=9:v=1:a=0[outv]" -map "[outv]" -r 30 -c:v libx264 -pix_fmt yuv420p summer_sound.mp4

ffmpeg -loop 1 -t 0.333 -i IMG_1420.jpg -loop 1 -t 0.333 -i IMG_1419.jpg -loop 1 -t 0.333 -i IMG_1418.jpg -filter_complex "[0:v]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,setsar=1,split=3[v0a][v0b][v0c];[1:v]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,setsar=1,split=6[v1a][v1b][v1c][v1d][v1e][v1f];[2:v]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,setsar=1,split=3[v2a][v2b][v2c];[v0a][v1a][v2a][v1b][v0b][v1c][v2b][v1d][v0c][v1e][v2c][v1f]concat=n=12:v=1:a=0[outv]" -map "[outv]" -r 30 -c:v libx264 -pix_fmt yuv420p summer_sound3.mp4

### Remove a file checked into Git 
```bash
$ git rm --cached file_name
```

### Remove all .env files
```bash
$ git rm --cached *.env
```

### Ignore untracked files 
```bash

```