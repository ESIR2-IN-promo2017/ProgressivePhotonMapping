#!python2
import os, sys, time, math

MITSUBA_PATH = 'C:/Program Files/Mitsuba 0.5.0/'

sys.path.append(MITSUBA_PATH + 'python/2.7')
os.environ['PATH'] = MITSUBA_PATH + os.pathsep + os.environ['PATH']

import mitsuba
import multiprocessing

from mitsuba.core import *
from mitsuba.render import SceneHandler, RenderQueue, RenderJob

fileResolver = Thread.getThread().getFileResolver()
fileResolver.appendPath('cbox/')

paramMap = StringMap()

scene = SceneHandler.loadScene(fileResolver.resolve("cbox.xml"), paramMap)

print(scene)

scheduler = Scheduler.getInstance()
for i in range(0, multiprocessing.cpu_count()):
    scheduler.registerWorker(LocalWorker(i, 'wrk%i' % i))

scheduler.start()

queue = RenderQueue()
scene.setDestinationFile('rendererResult_t'+sys.argv[1])

job = RenderJob('testJob', scene, queue)
job.start()

time.sleep(float(sys.argv[1]))

job.cancel()

queue.waitLeft(0)
queue.join()

print(Statistics.getInstance().getStats())
