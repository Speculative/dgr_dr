Dgr_dr
======

Dgr_dr (pronouned "degrader" or "DAH GURR DURRRRR", if you are so inclined) is a
hack/art site/"totally serious counterculture app that's meant to challenge your ideas
of like, images, and permanence, man" created during Y-Hack 2013.

The interesting bits are in /wsgi/app/

It uses Flask to serve images and PIL to "degrade" images. Corruption of images is achieved
by picking parts of random rows/columns of pixels and arbitrarily performing or/xor with the surrounding
rows/columns.

The intent is that the more an image is viewed, the less it will get to be viewed in the future. We think
this makes for an interesting dynamic in the permanence of uploaded images. Also it was fun.

See it Live
-----------
[Dgr_dr](http://dgrdr.enigmasm.com/)

Created by the guys at [EnigmaSM](http://enigmasm.com/)