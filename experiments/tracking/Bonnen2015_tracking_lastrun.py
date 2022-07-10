#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on Sat Jul  9 15:15:21 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.1'
expName = 'helloworld'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/kathrynbonnen/Documents/work-repos/tracking-bonnen-2015-psychopy/experiments/tracking/Bonnen2015_tracking_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Wait" ---
start_trial_text = visual.TextStim(win=win, name='start_trial_text',
    text="Press any button to continue",
    font='Arial',
    pos=(-0.3, 0.25), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
start_trial_mouse = event.Mouse(win=win)
x, y = [None, None]
start_trial_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "trial" ---
response_mouse = event.Mouse(win=win)
x, y = [None, None]
response_mouse.mouseClock = core.Clock()
noise_0 = visual.NoiseStim(
    win=win, name='noise_0',
    noiseImage=None, mask=None,
    ori=0.0, pos=(0, 0), size=(1, 1), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=None, blendmode='add', contrast=0.5,
    texRes=512, filter=None,
    noiseType='White', noiseElementSize=[0.0625], 
    noiseBaseSf=8.0, noiseBW=1.0,
    noiseBWO=30.0, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-1.0)
noise_0.buildNoise()
noise = visual.NoiseStim(
    win=win, name='noise',
    noiseImage=None, mask=None,
    ori=0.0, pos=(0, 0), size=(1, 1), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=None, blendmode='add', contrast=0.5,
    texRes=512, filter=None,
    noiseType='White', noiseElementSize=[0.0625], 
    noiseBaseSf=8.0, noiseBW=1.0,
    noiseBWO=30.0, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-2.0)
noise.buildNoise()
blob_0 = visual.GratingStim(
    win=win, name='blob_0',
    tex=np.ones((512,512)), mask='gauss', anchor='center',
    ori=45.0, pos=[0,0], size=1.0, sf=1.0, phase=0.25,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='add',
    texRes=512.0, interpolate=True, depth=-3.0)
blob = visual.GratingStim(
    win=win, name='blob',
    tex=np.ones((512,512)), mask='gauss', anchor='center',
    ori=45.0, pos=[0,0], size=1.0, sf=1.0, phase=0.25,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='add',
    texRes=512.0, interpolate=True, depth=-4.0)
cursor = visual.ShapeStim(
    win=win, name='cursor',
    size=(0.005, 0.005), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-6.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Bonnen2015Conditions.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Wait" ---
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the start_trial_mouse
    start_trial_mouse.x = []
    start_trial_mouse.y = []
    start_trial_mouse.leftButton = []
    start_trial_mouse.midButton = []
    start_trial_mouse.rightButton = []
    start_trial_mouse.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    WaitComponents = [start_trial_text, start_trial_mouse]
    for thisComponent in WaitComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Wait" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *start_trial_text* updates
        if start_trial_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_trial_text.frameNStart = frameN  # exact frame index
            start_trial_text.tStart = t  # local t and not account for scr refresh
            start_trial_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_trial_text, 'tStartRefresh')  # time at next scr refresh
            start_trial_text.setAutoDraw(True)
        # *start_trial_mouse* updates
        if start_trial_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_trial_mouse.frameNStart = frameN  # exact frame index
            start_trial_mouse.tStart = t  # local t and not account for scr refresh
            start_trial_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_trial_mouse, 'tStartRefresh')  # time at next scr refresh
            start_trial_mouse.status = STARTED
            start_trial_mouse.mouseClock.reset()
            prevButtonState = start_trial_mouse.getPressed()  # if button is down already this ISN'T a new click
        if start_trial_mouse.status == STARTED:  # only update if started and not finished!
            x, y = start_trial_mouse.getPos()
            start_trial_mouse.x.append(x)
            start_trial_mouse.y.append(y)
            buttons = start_trial_mouse.getPressed()
            start_trial_mouse.leftButton.append(buttons[0])
            start_trial_mouse.midButton.append(buttons[1])
            start_trial_mouse.rightButton.append(buttons[2])
            start_trial_mouse.time.append(start_trial_mouse.mouseClock.getTime())
            buttons = start_trial_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    
                    continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WaitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Wait" ---
    for thisComponent in WaitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('start_trial_mouse.x', start_trial_mouse.x)
    trials.addData('start_trial_mouse.y', start_trial_mouse.y)
    trials.addData('start_trial_mouse.leftButton', start_trial_mouse.leftButton)
    trials.addData('start_trial_mouse.midButton', start_trial_mouse.midButton)
    trials.addData('start_trial_mouse.rightButton', start_trial_mouse.rightButton)
    trials.addData('start_trial_mouse.time', start_trial_mouse.time)
    # the Routine "Wait" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the response_mouse
    response_mouse.x = []
    response_mouse.y = []
    response_mouse.leftButton = []
    response_mouse.midButton = []
    response_mouse.rightButton = []
    response_mouse.time = []
    gotValidClick = False  # until a click is received
    blob_0.setContrast(.5*blobHeight)
    blob_0.setSize([blobWidth*np.ones((2,))])
    blob_0.setTex(np.ones((512,512)))
    blob.setContrast(.5*blobHeight)
    blob.setSize([blobWidth*np.ones((2,))])
    blob.setTex(np.ones((512,512)))
    # Run 'Begin Routine' code from code
    blob.setPos((0,0))
    response_mouse.setPos((0,0))
    response_mouse.setVisible(0)
    blob.x = []
    blob.y = []
    # keep track of which components have finished
    trialComponents = [response_mouse, noise_0, noise, blob_0, blob, cursor]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    while continueRoutine and routineTimer.getTime() < 15.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *response_mouse* updates
        if response_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response_mouse.frameNStart = frameN  # exact frame index
            response_mouse.tStart = t  # local t and not account for scr refresh
            response_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('response_mouse.started', t)
            response_mouse.status = STARTED
            response_mouse.mouseClock.reset()
            prevButtonState = response_mouse.getPressed()  # if button is down already this ISN'T a new click
        if response_mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response_mouse.tStartRefresh + 15.5-frameTolerance:
                # keep track of stop time/frame for later
                response_mouse.tStop = t  # not accounting for scr refresh
                response_mouse.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('response_mouse.stopped', t)
                response_mouse.status = FINISHED
        if response_mouse.status == STARTED:  # only update if started and not finished!
            x, y = response_mouse.getPos()
            response_mouse.x.append(x)
            response_mouse.y.append(y)
            buttons = response_mouse.getPressed()
            response_mouse.leftButton.append(buttons[0])
            response_mouse.midButton.append(buttons[1])
            response_mouse.rightButton.append(buttons[2])
            response_mouse.time.append(response_mouse.mouseClock.getTime())
        
        # *noise_0* updates
        if noise_0.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            noise_0.frameNStart = frameN  # exact frame index
            noise_0.tStart = t  # local t and not account for scr refresh
            noise_0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noise_0, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'noise_0.started')
            noise_0.setAutoDraw(True)
        if noise_0.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noise_0.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                noise_0.tStop = t  # not accounting for scr refresh
                noise_0.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'noise_0.stopped')
                noise_0.setAutoDraw(False)
        if noise_0.status == STARTED:
            if noise_0._needBuild:
                noise_0.buildNoise()
            else:
                if (frameN-noise_0.frameNStart) %         1==0:
                    noise_0.updateNoise()
        
        # *noise* updates
        if noise.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            noise.frameNStart = frameN  # exact frame index
            noise.tStart = t  # local t and not account for scr refresh
            noise.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noise, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'noise.started')
            noise.setAutoDraw(True)
        if noise.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noise.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                noise.tStop = t  # not accounting for scr refresh
                noise.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'noise.stopped')
                noise.setAutoDraw(False)
        if noise.status == STARTED:
            if noise._needBuild:
                noise.buildNoise()
            else:
                if (frameN-noise.frameNStart) %         1==0:
                    noise.updateNoise()
        
        # *blob_0* updates
        if blob_0.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            blob_0.frameNStart = frameN  # exact frame index
            blob_0.tStart = t  # local t and not account for scr refresh
            blob_0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blob_0, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blob_0.started')
            blob_0.setAutoDraw(True)
        if blob_0.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blob_0.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                blob_0.tStop = t  # not accounting for scr refresh
                blob_0.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blob_0.stopped')
                blob_0.setAutoDraw(False)
        if blob_0.status == STARTED:  # only update if drawing
            blob_0.setPos((0,0), log=False)
        
        # *blob* updates
        if blob.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            blob.frameNStart = frameN  # exact frame index
            blob.tStart = t  # local t and not account for scr refresh
            blob.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blob, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blob.started')
            blob.setAutoDraw(True)
        if blob.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blob.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                blob.tStop = t  # not accounting for scr refresh
                blob.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blob.stopped')
                blob.setAutoDraw(False)
        if blob.status == STARTED:  # only update if drawing
            blob.setPos([blob.pos+sig*np.random.normal(size=(2,))], log=False)
        # Run 'Each Frame' code from code
        if response_mouse.status == STARTED:
            x,y = blob.pos
            blob.x.append(x)
            blob.y.append(y)
        
        # *cursor* updates
        if cursor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cursor.frameNStart = frameN  # exact frame index
            cursor.tStart = t  # local t and not account for scr refresh
            cursor.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cursor, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cursor.started')
            cursor.setAutoDraw(True)
        if cursor.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cursor.tStartRefresh + 15.5-frameTolerance:
                # keep track of stop time/frame for later
                cursor.tStop = t  # not accounting for scr refresh
                cursor.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cursor.stopped')
                cursor.setAutoDraw(False)
        if cursor.status == STARTED:  # only update if drawing
            cursor.setPos([response_mouse.getPos()], log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('response_mouse.x', response_mouse.x)
    trials.addData('response_mouse.y', response_mouse.y)
    trials.addData('response_mouse.leftButton', response_mouse.leftButton)
    trials.addData('response_mouse.midButton', response_mouse.midButton)
    trials.addData('response_mouse.rightButton', response_mouse.rightButton)
    trials.addData('response_mouse.time', response_mouse.time)
    # Run 'End Routine' code from code
    trials.addData('blob.x', blob.x)
    trials.addData('blob.y', blob.y)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-15.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
