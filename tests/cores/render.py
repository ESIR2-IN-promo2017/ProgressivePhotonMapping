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

#print(scene)

for nb_cores in range(1, multiprocessing.cpu_count()):

    scheduler = Scheduler.getInstance()
    for i in range(0, nb_cores):
        scheduler.registerWorker(LocalWorker(i, 'wrk%i' % i))

    scheduler.start()

    queue = RenderQueue()
    scene.setDestinationFile('rendererResult_c'+str(nb_cores))

    job = RenderJob('testJob', scene, queue)
    job.start()

    time.sleep(60)

    job.cancel()

    queue.waitLeft(0)
    queue.join()

    scheduler.stop()

#print(Statistics.getInstance().getStats())
