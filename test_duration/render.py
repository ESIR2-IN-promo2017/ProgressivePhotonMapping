#!/bin/python3

import mitsuba
from mitsuba.core import *
from mitsuba.render import SceneHandler

fileResolver = Thread.getThread().getFileResolver()
fileResolver.appendPath('cbox/')

paramMap = StringMap()

scene = SceneHandler.loadScene(fileResolver.resolve('cbox.xml'), paramMap)

#print(scene)
print('ok')
