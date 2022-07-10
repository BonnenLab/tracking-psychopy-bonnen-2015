#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on Tue Jul  5 11:24:10 2022
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
expName = 'Bonnen2015_2afc'  # from the Builder filename that created this script
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
    originPath='/Users/kathrynbonnen/Documents/psychopy-exp/Bonnen2015_2afc_lastrun.py',
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
    text="Press left or right to continue",
    font='Arial',
    pos=(-0.3, 0.25), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
start_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "trial" ---
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
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=0.0)
noise.buildNoise()
noise_2 = visual.NoiseStim(
    win=win, name='noise_2',
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
noise_2.buildNoise()
blob_1 = visual.GratingStim(
    win=win, name='blob_1',
    tex=np.ones((512,512)), mask='gauss', anchor='center',
    ori=45.0, pos=[0,0], size=1.0, sf=1.0, phase=0.25,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='add',
    texRes=512.0, interpolate=True, depth=-2.0)
blob_2 = visual.GratingStim(
    win=win, name='blob_2',
    tex=np.ones((512,512)), mask='gauss', anchor='center',
    ori=45.0, pos=[0,0], size=1.0, sf=1.0, phase=0.25,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='add',
    texRes=512.0, interpolate=True, depth=-3.0)
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Wait" ---
continueRoutine = True
# update component parameters for each repeat
start_key_resp.keys = []
start_key_resp.rt = []
_start_key_resp_allKeys = []
# keep track of which components have finished
WaitComponents = [start_trial_text, start_key_resp]
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'start_trial_text.started')
        start_trial_text.setAutoDraw(True)
    
    # *start_key_resp* updates
    waitOnFlip = False
    if start_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_key_resp.frameNStart = frameN  # exact frame index
        start_key_resp.tStart = t  # local t and not account for scr refresh
        start_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'start_key_resp.started')
        start_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = start_key_resp.getKeys(keyList=['left','right'], waitRelease=False)
        _start_key_resp_allKeys.extend(theseKeys)
        if len(_start_key_resp_allKeys):
            start_key_resp.keys = _start_key_resp_allKeys[-1].name  # just the last key pressed
            start_key_resp.rt = _start_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
# check responses
if start_key_resp.keys in ['', [], None]:  # No response was made
    start_key_resp.keys = None
thisExp.addData('start_key_resp.keys',start_key_resp.keys)
if start_key_resp.keys != None:  # we had a response
    thisExp.addData('start_key_resp.rt', start_key_resp.rt)
thisExp.nextEntry()
# the Routine "Wait" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Bonnen2015Conditions2AFC.csv'),
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
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    if not noise_2._needBuild:
        noise_2.updateNoise()
    blob_1.setContrast(.5*blobHeight)
    blob_1.setSize([blobWidth*np.ones((2,))])
    blob_1.setTex(np.ones((512,512)))
    blob_2.setContrast(.5*blobHeight)
    blob_2.setSize([blobWidth*np.ones((2,))])
    blob_2.setTex(np.ones((512,512)))
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [noise, noise_2, blob_1, blob_2, key_resp]
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *noise* updates
        if noise.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
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
            if tThisFlipGlobal > noise.tStartRefresh + .75-frameTolerance:
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
        
        # *noise_2* updates
        if noise_2.status == NOT_STARTED and tThisFlip >= .75-frameTolerance:
            # keep track of start time/frame for later
            noise_2.frameNStart = frameN  # exact frame index
            noise_2.tStart = t  # local t and not account for scr refresh
            noise_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noise_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'noise_2.started')
            noise_2.setAutoDraw(True)
        if noise_2.status == STARTED:
            if noise_2._needBuild:
                noise_2.buildNoise()
        
        # *blob_1* updates
        if blob_1.status == NOT_STARTED and tThisFlip >= .1-frameTolerance:
            # keep track of start time/frame for later
            blob_1.frameNStart = frameN  # exact frame index
            blob_1.tStart = t  # local t and not account for scr refresh
            blob_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blob_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blob_1.started')
            blob_1.setAutoDraw(True)
        if blob_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blob_1.tStartRefresh + .25-frameTolerance:
                # keep track of stop time/frame for later
                blob_1.tStop = t  # not accounting for scr refresh
                blob_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blob_1.stopped')
                blob_1.setAutoDraw(False)
        if blob_1.status == STARTED:  # only update if drawing
            blob_1.setPos((0,0), log=False)
        
        # *blob_2* updates
        if blob_2.status == NOT_STARTED and tThisFlip >= 0.45-frameTolerance:
            # keep track of start time/frame for later
            blob_2.frameNStart = frameN  # exact frame index
            blob_2.tStart = t  # local t and not account for scr refresh
            blob_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blob_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blob_2.started')
            blob_2.setAutoDraw(True)
        if blob_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blob_2.tStartRefresh + .25-frameTolerance:
                # keep track of stop time/frame for later
                blob_2.tStop = t  # not accounting for scr refresh
                blob_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blob_2.stopped')
                blob_2.setAutoDraw(False)
        if blob_2.status == STARTED:  # only update if drawing
            blob_2.setPos((offset,0), log=False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= .75-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
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
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
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
