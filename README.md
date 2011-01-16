# AutoVI
These are some generic VI bindings for Linux using AutoKey

This isn't a replacement for proper bindings, like provided by Kate and QtCreator (or some browser plugins), it's just a bunch of key mappings for places, where no VI mode is available at all.
Also, if you're using Windows, there's already some stuff implemented in AutoHotKey.

Features
* The following commands are available:
* Complete (De-)Activation: super+v
* Insert Mode: i, a, escape
* Navigation: h, j, k, l, w, b, $, 0, gg, G
* Delete: dd, D, d+NavigationKey (not all)
* Change: cc, C, c+NavigationKey (not all)
* Other: o, O, J, x

Some bindings:
* :w → ctrl+s
* :q → ctrl+q (alt+f4 didn't work)
* / → ctrl+f
* u → ctrl+z (might or might not work as expected)
* Also some enumerated commands are supported, e.g. 4j and d2w (up to 9).

## Requirements

AutoKey 0.71.0 - older versions don't work.
notify-send - inform about de-/activation and insert mode through notifications

## Installing
Unpack the archive, change into the directory from a command line and type make. On the next start of your AutoKey GUI, there should be a folder called AutoVI.
