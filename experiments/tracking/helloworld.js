/******************* 
 * Helloworld *
 *******************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.1.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'helloworld';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);



flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'Bonnen2015Conditions.csv', 'path': 'Bonnen2015Conditions.csv'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "Wait"
  WaitClock = new util.Clock();
  start_trial_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_trial_text',
    text: /* Press any button to continue */
  ,
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), 0.25], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  start_trial_mouse = new core.Mouse({
    win: psychoJS.window,
  });
  start_trial_mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  response_mouse = new core.Mouse({
    win: psychoJS.window,
  });
  response_mouse.mouseClock = new util.Clock();
  blob_0 = new visual.GratingStim({
    win : psychoJS.window,
    name : 'blob_0', units : undefined, 
    tex : np.ones([512, 512]), mask : 'gauss',
    ori : 45.0, pos : [0, 0],
    anchor : 'center',
    sf : 1.0, phase : 0.25,
    size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    contrast : 1.0, blendmode : 'add',
    texRes : 512.0, interpolate : true, depth : -1.0 
  });
  blob = new visual.GratingStim({
    win : psychoJS.window,
    name : 'blob', units : undefined, 
    tex : np.ones([512, 512]), mask : 'gauss',
    ori : 45.0, pos : [0, 0],
    anchor : 'center',
    sf : 1.0, phase : 0.25,
    size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    contrast : 1.0, blendmode : 'add',
    texRes : 512.0, interpolate : true, depth : -2.0 
  });
  cursor = new visual.Polygon({
    win: psychoJS.window, name: 'cursor', 
    edges: 100, size:[0.005, 0.005],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('red'),
    fillColor: new util.Color('red'),
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Bonnen2015Conditions.csv',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(WaitRoutineBegin(snapshot));
      trialsLoopScheduler.add(WaitRoutineEachFrame());
      trialsLoopScheduler.add(WaitRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function WaitRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Wait' ---
    t = 0;
    WaitClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Wait.started', globalClock.getTime());
    // setup some python lists for storing info about the start_trial_mouse
    // current position of the mouse:
    start_trial_mouse.x = [];
    start_trial_mouse.y = [];
    start_trial_mouse.leftButton = [];
    start_trial_mouse.midButton = [];
    start_trial_mouse.rightButton = [];
    start_trial_mouse.time = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    WaitComponents = [];
    WaitComponents.push(start_trial_text);
    WaitComponents.push(start_trial_mouse);
    
    for (const thisComponent of WaitComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function WaitRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Wait' ---
    // get current time
    t = WaitClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *start_trial_text* updates
    if (t >= 0.0 && start_trial_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_trial_text.tStart = t;  // (not accounting for frame time here)
      start_trial_text.frameNStart = frameN;  // exact frame index
      
      start_trial_text.setAutoDraw(true);
    }
    
    // *start_trial_mouse* updates
    if (t >= 0.0 && start_trial_mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_trial_mouse.tStart = t;  // (not accounting for frame time here)
      start_trial_mouse.frameNStart = frameN;  // exact frame index
      
      start_trial_mouse.status = PsychoJS.Status.STARTED;
      start_trial_mouse.mouseClock.reset();
      prevButtonState = start_trial_mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (start_trial_mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = start_trial_mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = start_trial_mouse.getPos();
          start_trial_mouse.x.push(_mouseXYs[0]);
          start_trial_mouse.y.push(_mouseXYs[1]);
          start_trial_mouse.leftButton.push(_mouseButtons[0]);
          start_trial_mouse.midButton.push(_mouseButtons[1]);
          start_trial_mouse.rightButton.push(_mouseButtons[2]);
          start_trial_mouse.time.push(start_trial_mouse.mouseClock.getTime());
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of WaitComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function WaitRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Wait' ---
    for (const thisComponent of WaitComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Wait.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('start_trial_mouse.x', start_trial_mouse.x);
    psychoJS.experiment.addData('start_trial_mouse.y', start_trial_mouse.y);
    psychoJS.experiment.addData('start_trial_mouse.leftButton', start_trial_mouse.leftButton);
    psychoJS.experiment.addData('start_trial_mouse.midButton', start_trial_mouse.midButton);
    psychoJS.experiment.addData('start_trial_mouse.rightButton', start_trial_mouse.rightButton);
    psychoJS.experiment.addData('start_trial_mouse.time', start_trial_mouse.time);
    
    // the Routine "Wait" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(15.500000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    // setup some python lists for storing info about the response_mouse
    // current position of the mouse:
    response_mouse.x = [];
    response_mouse.y = [];
    response_mouse.leftButton = [];
    response_mouse.midButton = [];
    response_mouse.rightButton = [];
    response_mouse.time = [];
    gotValidClick = false; // until a click is received
    blob_0.setContrast(.5*blobHeight);
    blob_0.setSize((blobWidth * np.ones([2])));
    blob_0.setTex(np.ones([512, 512]));
    blob.setContrast(.5*blobHeight);
    blob.setSize((blobWidth * np.ones([2])));
    blob.setTex(np.ones([512, 512]));
    // Run 'Begin Routine' code from code
    blob.setPos([0, 0]);
    response_mouse.setPos([0, 0]);
    response_mouse.setVisible(0);
    blob.x = [];
    blob.y = [];
    
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(response_mouse);
    trialComponents.push(blob_0);
    trialComponents.push(blob);
    trialComponents.push(cursor);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *response_mouse* updates
    if (t >= 0.0 && response_mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response_mouse.tStart = t;  // (not accounting for frame time here)
      response_mouse.frameNStart = frameN;  // exact frame index
      
      response_mouse.status = PsychoJS.Status.STARTED;
      response_mouse.mouseClock.reset();
      prevButtonState = response_mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 15.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (response_mouse.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      response_mouse.status = PsychoJS.Status.FINISHED;
        }
    if (response_mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = response_mouse.getPressed();
      _mouseXYs = response_mouse.getPos();
      response_mouse.x.push(_mouseXYs[0]);
      response_mouse.y.push(_mouseXYs[1]);
      response_mouse.leftButton.push(_mouseButtons[0]);
      response_mouse.midButton.push(_mouseButtons[1]);
      response_mouse.rightButton.push(_mouseButtons[2]);
      response_mouse.time.push(response_mouse.mouseClock.getTime());
    }
    
    if (blob_0.status === PsychoJS.Status.STARTED){ // only update if being drawn
      blob_0.setPos([0, 0], false);
    }
    
    // *blob_0* updates
    if (t >= 0 && blob_0.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blob_0.tStart = t;  // (not accounting for frame time here)
      blob_0.frameNStart = frameN;  // exact frame index
      
      blob_0.setAutoDraw(true);
    }
    
    frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (blob_0.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blob_0.setAutoDraw(false);
    }
    
    
    if (blob.status === PsychoJS.Status.STARTED){ // only update if being drawn
      blob.setPos((blob.pos + (sig * np.random.normal(size=[2]))), false);
    }
    
    // *blob* updates
    if (t >= 0.5 && blob.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blob.tStart = t;  // (not accounting for frame time here)
      blob.frameNStart = frameN;  // exact frame index
      
      blob.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 15.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (blob.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blob.setAutoDraw(false);
    }
    
    // Run 'Each Frame' code from code
    if ((response_mouse.status === PsychoJS.Status.STARTED)) {
        [x, y] = blob.pos;
        blob.x.push(x);
        blob.y.push(y);
    }
    
    
    if (cursor.status === PsychoJS.Status.STARTED){ // only update if being drawn
      cursor.setPos(response_mouse.getPos(), false);
    }
    
    // *cursor* updates
    if (t >= 0.0 && cursor.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cursor.tStart = t;  // (not accounting for frame time here)
      cursor.frameNStart = frameN;  // exact frame index
      
      cursor.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 15.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cursor.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cursor.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('response_mouse.x', response_mouse.x);
    psychoJS.experiment.addData('response_mouse.y', response_mouse.y);
    psychoJS.experiment.addData('response_mouse.leftButton', response_mouse.leftButton);
    psychoJS.experiment.addData('response_mouse.midButton', response_mouse.midButton);
    psychoJS.experiment.addData('response_mouse.rightButton', response_mouse.rightButton);
    psychoJS.experiment.addData('response_mouse.time', response_mouse.time);
    
    // Run 'End Routine' code from code
    trials.addData("blob.x", blob.x);
    trials.addData("blob.y", blob.y);
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
