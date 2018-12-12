# About
PySharp is a scripting language with the purpose of providing a simple framework to create scales (A,B,C,D,E,F,G) with different types (Melodic, Harmonic, Natural)

## Motivation
On the music industry, becoming a professional requires a lot of practice. To achieve this goal, people should start at a young age but also practice a lot. When musicians have a great basic knowledge on music and its time to go to the next level, they are taught what is called the Circle of Fifths. This Circle of Fifths is a special tool to practice not just theoretical music, but also practical. The concept is based on the existing musical notes (C, G, D, A, E, B, F#). The purpose of this exercises is to let the musician play the scale for each of the musical notes but with different alterations. Each of the musical notes has its own scale. There are 3 types of scales: Natural, Harmonic and Melodic. 

<img class="aligncenter wp-image-41065" src="https://www.musical-u.com/wp-content/uploads/2017/07/MU-Circle-of-Fifths-3-with-Key-Signatures-1024x1024.png" alt="Circle of Fifths With Major Keys and Their Key Signatures Shown" width="600" height="600" srcset="https://www.musical-u.com/wp-content/uploads/2017/07/MU-Circle-of-Fifths-3-with-Key-Signatures-1024x1024.png 1024w, https://www.musical-u.com/wp-content/uploads/2017/07/MU-Circle-of-Fifths-3-with-Key-Signatures-150x150.png 150w, https://www.musical-u.com/wp-content/uploads/2017/07/MU-Circle-of-Fifths-3-with-Key-Signatures-300x300.png 300w, https://www.musical-u.com/wp-content/uploads/2017/07/MU-Circle-of-Fifths-3-with-Key-Signatures-768x768.png 768w, https://www.musical-u.com/wp-content/uploads/2017/07/MU-Circle-of-Fifths-3-with-Key-Signatures-1080x1080.png 1080w" sizes="(max-width: 600px) 100vw, 600px">


### Language Features
PySharp Features:

Note Control: Allows alteration of the notes with which the scale is created.

Scale Creation: Allows creation of scales and their starting point. 

Scale Alteration: Allows Scale alteration using one of the following.

- Harmonic 
- Melodic
- Natural

Scale Demonstration: Plays the created Scale

<iframe width="560" height="315" src="https://www.youtube.com/embed/SXIZRwJNH4M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

This video shows how to run PySharp.
It goes through creating a scale using the createScale function, then playing that last created scale with the playScale function.

We then run the playScale function with the createScale as argument as this function returns the scale created to then play it.

Next, we show the creation of scales and how we store them and play them from variables.

Lastly, we show the HELP function, and exit using the EXIT function.

