# BVHsmooth
Apply smoothening filters to an animation in BVH format.

## Usage
To smoothen the **rotations** of the animation run: 

```python code/smooth_rotation.py -i <input_file> -o <output_file> --filter <filter> <params>```

To smoothen the **positions** of the animation run: 

```python code/smooth_position.py -i <input_file> -o <output_file> --filter <filter> <params>```

## Filters:

### Butterworth (frquency domain)

`--filter butterworth --border <border> --u0 <u0> --order <order>`

### Central Moving Average (time domain)

`--filter average -m <m>`

### Gaussian (frquency domain) - Not recomended, poor results.

`--filter gaussian --border <border> --sigma <sigma>`

## Example

You can see the results using [BVH Player](http://www.akjava.com/demo/bvhplayer/).

Let's use the provided sample BVH file **bvh_files/sample01.bvh**. The sample file was created by kinect capture method at CENA (Centro de Tecnologias Narrativas) laboratory, located at the Insituto Politécnico (IPRJ/UERJ).

First, apply the smoothening in rotations:

```python code/smooth_rotation.py -i bvh_files/sample01.bvh -o bvh_files/out.bvh --filter butterworth --border 100 --u0 60 --order 2```

Then, apply the smoothening in positions:

```python code/smooth_position.py -i bvh_files/out.bvh -o bvh_files/out.bvh --filter butterworth --border 100 --u0 60 --order 2```

Now you can compare the files **bvh_files/sample01.bvh** and **bvh_files/out.bvh**.
