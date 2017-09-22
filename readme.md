# Soundify : Transform your pictures into sound and vice versa!

## The Idea

The idea to transform pictures into sounds comes from [this great video](https://www.youtube.com/watch?v=3s7h2MHQtxc) by [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw). I was very interested by this topic, and said to myself : "why not do the opposite as well?". To see what our music looks like as an image. I know we already have a visual representation for music with the spectrum, but still, I think it's a fun project !

## More about The Project

This project is at stage of development for now. 
Idealy, this little software would:
 - Convert square pictures (2^n x 2^n sized) into a sound texture
 - Convert sound into pictures (with 44,100Hz sampling rate, we can create a 4096x4096 picture out of a 6:30 music)
 - Convert video into music (each frame would be transformed into sound)
 - Convert music into video (get the music spectrum every 60ms would give us a ~16 fps video)

### Implementation

The idea is to use [Hilbert Curves](https://en.wikipedia.org/wiki/Hilbert_curve) to unfold the pixels of the picture because it preserve locality.

### What does that means ?

It means that two points close from eatch other on the picture will be close on the spectrum as well. Also, it means that if we scale up the picture, the spectrum we get will be close to the first one.
As explained in [the video](https://www.youtube.com/watch?v=3s7h2MHQtxc), this will also allow our ears to train and learn without relearning everytime we scale up the picture.
