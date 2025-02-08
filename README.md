# NoMedia

Program to control whether Android files should appear in media or not

In the Android operating system, it is commonly configured so that folders containing a ".nomedia" file do not have their contents displayed in the device's public gallery.

In certain cases, applications or even the user himself may have many images and videos in the device's memory, but the user does not want to see them in the cell phone's media. With this in mind, this tool was developed for Termux.

With a single command, you can hide all the contents of a folder, so that they no longer appear in the media.

`nomedia folder`

if you do not specify a folder, it will always assume the current folder by default. If you want all subfolders in that directory to also be hidden, add the argument `-r`

`nomedia -r folder`

And if you want to revert or make a folder visible to the cell phone's media, just add the parameter `-u` or `--unhide`

`nomedia -r -r folder`

Need help? Try running `nomedia --help`

## Limitations

- This program was made to work on Android operating systems, together with Termux
- Not all programs and systems support the .nomedia file, some require extra configuration and some others are simply not compatible.
