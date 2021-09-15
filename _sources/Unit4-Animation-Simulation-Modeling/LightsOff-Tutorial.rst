.. raw:: html 

   <div class="logo-header"  id="student-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

LightsOff Tutorial
==================

.. raw:: html

    <!-- Custom Scripts -->
    <script src="../_static/assets/lib/lessons/tipped.js" type="text/javascript"></script>
    <script src="../_static/assets/lib/lessons/Framework2020.js" type="text/javascript"></script>
    <link href="../_static/assets/lib/lessons/tipped.css" rel="stylesheet" type="text/css"></link>
    <link href="../_static/assets/lib/lessons/lessons.css" rel="stylesheet" type="text/css"></link>
    <link href="../_static/assets/css/custom.css" rel="stylesheet" type="test/css"></link>
    <script src="../_static/assets/lib/lessons/vocabulary.js" type="text/javascript"></script>
    <style>    td { text-align: left; padding: 5px;}</style>


.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
        $(document).ready(function() {
            generateSummary(EKmapping['4.02']);
            generateHovers();
          });
    </script>
    <h3 id="est-length">Time Estimate: 45 minutes</h3>
    

Introduction and Goals
-----------------------

.. raw:: html

    <p>
	The <i>LightsOff</i> app is a variation of the classic Whack-a-Mole game  -- this one promoting the socially useful message of saving electricity.  In the game, a light bulb pops up at random positions on the screen. The player can score by touching the light bulb before it disappears and pops up in a new position. This tutorial guides you through the basic steps in creating the game.
	<table><tbody>
	<tr><td valign="top">
		<!-- 
		&lt;img width=&quot;315&quot; src=&quot;assets/img/LightsOutPart1.png&quot; /&gt; 
		-->
		<iframe allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/bWLkchEpy6w" width="285"></iframe>
		(<a href="https://teachertube.com/video/lightsoff-tutorial-preview-476362" target="_blank">Teacher Tube version</a>) 
    </td>
    <td valign="top">
		<div><b>Learning Objectives:</b>&nbspI will learn to</div>
		<ul>
		<li>use the <i>Canvas</i> and <i>ImageSprite</i> components in AppInventor</li>
		<li>further develop an understanding of procedures and procedural abstraction</li>
		<li>use timing, animation, and randomness as part of an event-driven program</li>
		</ul>
		<div><b>Language Objectives:</b>&nbspI will be able to</div>
		<ul>
		<li>discuss in detail the benefits of writing procedures in programming</li>
		<li>describe the functionality of an app using key vocabulary such as event, timer, and sprite, out loud and in writing, with the support of <a href="https://docs.google.com/presentation/d/1YsJJ7IwEEpQGLqSizFhIFJVIw5TfDc5LqDtCSD-o42E/copy" target="_blank" title="">vocabulary notes</a> from previous lessons</li>
		</ul>
	</td>
	</tr>
	<tr>
		<td colspan="2"><b>Acknowledgement: </b> The socially useful theme for this app -- helping to save electricity -- was suggested by Boston Latin Academy students Adam Vardaro and Daniel Rodriguez through their teacher, Ms. Ingrid Roche.</td>
    </tr>
    </tbody></table>
    

Learning Activities
--------------------

.. raw:: html

    <ul align="center" style="list-style: none; margin: 0; padding: 0; background: lightgrey">
	<li style="display: inline"><a href="https://docs.google.com/document/d/1hS57DObILtWguAbc6NSrJC6MSHDMow8Y7KzeCc63jPs/" target="_blank" title="">text-version</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://docs.google.com/document/d/1CbF1qvDy9KcpUYYJvFRndJxCGbj190Q0UEWixlzQ0uw/edit?usp=sharing" target="_blank">short handout</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://www.youtube.com/watch?v=_zsR2gxFEhk" target="_blank">YouTube video</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://teachertube.com/video/lightsoff-tutorial-476364" target="_blank" title="">TeacherTube video</a></li>
	</ul> 
	
	<p><h3>Tutorial</h3>
    <p>To get started, open App Inventor with the<a href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit4/templates/LightsOffTemplate/TurnOffLightsTemplate.asc" target="_blank"> LightsOff Template</a> in a separate tab.  Rename the project to <i>LightsOff</i> or something similar. If the template does not open, download the <a href="http://templates.appinventor.mit.edu/trincoll/csp/unit4/templates/LightsOffTemplate/TurnOffLightsTemplate.aia" target="_blank">.aia file</a>, go to <a href="http://ai2.appinventor.mit.edu" target="_blank">App Inventor</a> and do File/Import and import in the downloaded .aia file.</p>
    <p>Follow along with your teacher or the video tutorial. Or, if you prefer, click on the <i>Text Version</i> button above to use the written version of the tutorial or use the <i>Short Handout</i> for more of a challenge.</p>
    
.. youtube:: _zsR2gxFEhk
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


     (<a href="https://teachertube.com/video/lightsoff-tutorial-476364" target="_blank">Teacher Tube version</a>) 
    
    <p></p>
    

Summary
--------

.. raw:: html

    <p>
    In this lesson, you learned how to:
      <div id="summarylist">
    </div>
    

Self-Check
-----------

.. raw:: html

    <p>
    
.. mchoice:: mcsp-4-2-1
    :random:
    :practice: T
    :answer_a: Label
    :feedback_a: Try asking a classmate for advice—s/he may be able to explain/suggest some ideas or recommend some strategies.
    :answer_b: Button
    :feedback_b: Try asking a classmate for advice—s/he may be able to explain/suggest some ideas or recommend some strategies.
    :answer_c: Ball
    :feedback_c: Try asking a classmate for advice—s/he may be able to explain/suggest some ideas or recommend some strategies.
    :answer_d: Canvas
    :feedback_d: That's correct! Image sprites and balls can only be added within a Canvas component (found under Drawing and Animation) and not directly on screen
    :correct: d

    An ImageSprite component can only be inserted into what other component?


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-4-2-2
    :random:
    :practice: T
    :answer_a: True
    :feedback_a: Try asking a classmate for advice—s/he may be able to explain/suggest some ideas or recommend some strategies.
    :answer_b: False
    :feedback_b: That's correct! In order to use an ImageSprite component, you must have a Canvas component to put it on.
    :correct: b

    True or False: You can drag and drop the ImageSprite Component from Animation tab directly onto the screen? 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-4-2-3
    :random:
    :practice: T
    :answer_a: When the user shakes the phone.
    :feedback_a: Programming what happens when the user shakes the phone would require the use of the Accelerometer Sensor. 
    :answer_b: When the user tilts the phone. 
    :feedback_b: Programming what happens when the user tilts the phone would require the use of the Orientation Sensor. 
    :answer_c: When the Clock.Timer ticks. 
    :feedback_c: Correct! Each time the Clock's Timer fires, the Mole moves to a new random location.
    :answer_d: When the Sound beeps.
    :feedback_d: The Sound will beep only after the player has successfully touched the ImageSprite. 
    :correct: c

    What event causes the ImageSprite to move to a new random location?


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-4-2-4
    :random:
    :practice: T
    :answer_a: 1.5
    :feedback_a: Recall that the TimerInterval property requires that you specify an amount of time in milliseconds.
    :answer_b: 15
    :feedback_b: Recall that the TimerInterval property requires that you specify an amount of time in milliseconds.
    :answer_c: 150
    :feedback_c: Recall that the TimerInterval property requires that you specify an amount of time in milliseconds. 
    :answer_d: 1500
    :feedback_d: That's correct! The TimerInterval property requires that you specify an amount of time in milliseconds. 1.5 seconds is equivalent to 1500 milliseconds.
    :correct: d

    What value would you give the Clock's TimerInterval property to have the ImageSprite move every 1.5 seconds? 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1kPPfVeuev9CcGdO-6miswHJeDo00m_E8zo_LLE6ONLE/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vTdeN2tFAWjAMcEc_hslJemuBUiiH2LfJ65lhhj37DckY5IOmAoDq6MN6MrXXMLKNnPGjKHlf9oYhlJ/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--&lt;p&gt;Create a page named &lt;b&gt;&lt;i&gt;LightsOff Tutorial&lt;/i&gt;&lt;/b&gt; under the
      &lt;i&gt;Reflections&lt;/i&gt; category of your portfolio and answer the following questions.&lt;/p&gt;
      &lt;ol&gt;
        &lt;li&gt;This app presents a new type of event which you haven&#39;t encountered before. What is that new event? How often is it triggered?&lt;/li&gt;
        &lt;li&gt;Consider the apps you&#39;ve developed so far. Can you list all the different events your apps have responded to? What other events do you think an app can respond to? Explore some of the components in App Inventor and see what event handlers they have.&lt;/li&gt;
        &lt;li&gt;What are the advantages of writing procedures in programming? Consider the procedures you wrote for this app.&lt;/li&gt;
      &lt;/ol&gt;-->
    </div>
    </div>