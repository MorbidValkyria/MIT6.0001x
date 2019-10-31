# Installing Anaconda and Spyder


## What is Anaconda?

Anaconda is not an IDE but a set of tools/packages meant for Data Science, Machine Learning and Plotting. Most of these packages are for Python and R programming languages. Anaconda includes an IDE called Spyder and the optional Text Editor called Visual Studio Code.


## What is Spyder?

Spyder is an IDE (Integrated Development Environment) for Python. Main tool we use in the class.

## Downloading Anaconda:
Go to the [Anaconda main site](https://www.anaconda.com/distribution/ "Anaconda distribution"):
![alt text][Anaconda logo]

[Anaconda logo]: https://www.anaconda.com/wp-content/uploads/2018/06/cropped-Anaconda_horizontal_RGB-1-600x102.png

Once you scroll down, the website should detect which OS you're working on.
### Linux:
Make sure you have the required packages:
```shell
## Red Hat Linux/ Fedora/ CentOS:
yum install libXcomposite libXcursor libXi libXtst libXrandr alsa-lib mesa-libEGL libXdamage mesa-libGL libXScrnSaver

## Debian and Debian based distros(Ubuntu, Mint, Elementary, etc):
apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

## Gentoo:
emerge x11-libs/libXau x11-libs/libxcb x11-libs/libX11 x11-libs/libXext x11-libs/libXfixes x11-libs/libXrender x11-libs/libXi x11-libs/libXcomposite x11-libs/libXrandr x11-libs/libXcursor x11-libs/libXdamage x11-libs/libXScrnSaver x11-libs/libXtst media-libs/alsa-lib media-libs/mesa

## Arch Linux and Arch based distros(Manjaro and such):
pacman -Sy libxau libxi libxss libxtst libxcursor libxcomposite libxdamage libxfixes libxrandr libxrender mesa-libgl  alsa-lib libglvnd

## OpenSuse and other Suse based distros:
zypper install libXcomposite1 libXi6 libXext6 libXau6 libX11-6 libXrandr2 libXrender1 libXss1 libXtst6 libXdamage1 libXcursor1 libxcb1 libasound2  libX11-xcb1 Mesa-libGL1 Mesa-libEGL1

```

Once you have the necesary dependencies download the .sh Anaconda installer. It should be version *Python 3*.

Open a terminal window and type:

```shell
~/Downloads/Anaconda3-2019.10-Linux-x86_64.sh
```
Unless you know what you're doing install on the *default install location* and once it asks you: “Do you wish the installer to initialize Anaconda3 by running conda init?” type "yes".
Restart the shell and type:

```shell
conda --ver
```

This should display the current version of the Anaconda distribution, if done correctly, you should see something like ```conda 4.7.11``

After try to launch Spyder, open your terminal and type:
```shell
spyder

```
If you see the Spyder IDE, everything installed correctly.
### Macintosh:



### Windows:



