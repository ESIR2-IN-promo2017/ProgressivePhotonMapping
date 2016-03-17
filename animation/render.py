#!python2
import os, sys, time, math, shutil

MITSUBA_PATH = 'C:/Program Files/Mitsuba 0.5.0/'

sys.path.append(MITSUBA_PATH + 'python/2.7')
os.environ['PATH'] = MITSUBA_PATH + os.pathsep + os.environ['PATH']

import mitsuba
import multiprocessing

from mitsuba.core import *
from mitsuba.render import SceneHandler, RenderQueue, RenderJob

fileResolver = Thread.getThread().getFileResolver()
fileResolver.appendPath('scenes/')

paramMap = StringMap()

scene = SceneHandler.loadScene(fileResolver.resolve("scene1.xml"), paramMap)

print(scene)

scheduler = Scheduler.getInstance()
for i in range(0, multiprocessing.cpu_count()):
    scheduler.registerWorker(LocalWorker(i, 'wrk%i' % i))

scheduler.start()

destinationFile = 'results/rendererResult'

queue = RenderQueue()
scene.setDestinationFile(destinationFile)

job = RenderJob('testJob', scene, queue)
job.start()

startTime = time.time()
renderInterval = 10
renderOutputDuration = 2;
renderLength = 5*60
lastRender = startTime

print("starting render for " + str(renderLength) + " seconds")

while time.time() < startTime + renderLength:
    currentTime = math.floor(time.time())
    if currentTime > lastRender + renderInterval:
        #time.sleep(1)
        lastRender = currentTime
        job.flush()
        time.sleep(renderOutputDuration)
        shutil.move(destinationFile+'.exr', destinationFile+'_'+str(currentTime - math.floor(startTime))+'.exr')
        print('----successfully moved to ' + destinationFile + '_' + str(currentTime - math.floor(startTime)) + '----')


job.cancel()

queue.waitLeft(0)
queue.join()

print(Statistics.getInstance().getStats())
