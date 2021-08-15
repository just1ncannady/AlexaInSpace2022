.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Magic 8 Ball Tutorial and Projects (Optional)
=============================================

.. raw:: html

	
	
	<h3 id="est-length">Time Estimate: 90 minutes</h3>
	
Preview
-------

.. raw:: html

	<p></p>
	<table><tbody><tr><td>
	
	
	<iframe width="315" height="420" src="//www.youtube-nocookie.com/embed/rb33bA9K76Y?rel=0" frameborder="0" allowfullscreen="">
	</iframe>
	(<a target="_blank" href="http://www.teachertube.com/video/magic8ballpreview-347990">TeacherTube Version</a>)
	</td>
	<td>
	<b><i>Magic 8 Ball</i></b>  Magic 8-Ball is a mobile version of the classic 
	 fortune-telling game.  A user can ask a question, shake the phone, and 
	 hear the magic 8-ball’s prediction. This app uses the Accelerometer to 
	 handle the shaking event and the TextToSpeech component to have the phone speak 
	 the prediction, which is randomly selected from a list of predictions. 
	
	
	<p>
	<b>Objectives:</b> In this lesson you will learn to :
	</p><ul>
	<li>create an app that
	<ul>
	<li>uses the <i> Accelerometer sensor</i> to respond to shaking events,
	</li>
	<li>uses the <i>TextToSpeech</i> component to convert Text output to speech, and
	</li>
	<li>randomly selects the 8-Ball's responses from a list variable.
	</li>
	</ul>
	<p>
	</p></li><li>In the creative projects, you'll add enhancements to the app that:
	<ul>
	<li>use the <i>Speech Recognizer</i> component.
	</li>
	</ul>
	</li>
	</ul>
	
	<p></p>
	</td></tr></tbody></table>
	
Tutorial
--------

.. raw:: html

	
	<p>Follow the video tutorial to build an initial version of the Magic 8 Ball App.  
	If you prefer, there is a printable 
	<a target="_blank" href="https://docs.google.com/document/d/133cPONCoWoD389iaXbUFXwXRxk7hYZNE40ChXxykm-g">Text Version</a>
	of the tutorial.
	</p>
	
	<p>To begin the lesson 
	<a target="_blank" href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit3/templates/Magic8BallTemplate/Magic8BallTemplate.asc">
	open App Inventor with the Magic 8 Ball template</a>. 
	It provides the 
	media you need for this project and a partial version of the User Interface.  
	When the project opens -- be patient, it may take a moment -- use the Save As 
	option to rename it Magic8Ball.
	<br>(<a target="_blank" href="http://www.teachertube.com/video/magic8ball-347995">TeacherTube version</a>)</p>
	
	<gcb-youtube videoid="9EiBEFUU-xk" instanceid="iDCYaArzMplo"></gcb-youtube>
	
	
Mini Projects
-------------

.. raw:: html
	
	<p>Click here for a printable <a target="_blank" href="https://docs.google.com/document/d/1Lp-7hlE4hUifDhkAbir1YSFfSUuMRmY9EBRVKFP9EPk">Text Version</a> of the Mini Projects.
	</p>
	
	<p>Now that you've finished the tutorial, here are some creative projects.  Work with
	 your partner at implementing the following changes to the Magic 8 Ball App.
	</p>
	
	<ol>
	<li>Change the predictions that were used in the tutorial to include your own 
	 predictions, perhaps ones that are more humorous.
	</li>
	
	<li><b>If/Else Algorithm.</b> If you recall from the Tutorial video, one problem with the current 
	 version of the Shaking block is that it causes the Sound and the Voice to occur at the same time, 
	 making it hard to hear the prediction:
	
	
	<blockquote>
	<img src="../_static/assets/img/ShakingBlock.png">
	</blockquote>
	 
	<p>One way to fix this is to use an <i>if/else </i> algorithm to perform either
	   the speaking action or the sound action but not both.  Of course, the decision
	   to do one or the other has to depend on some <i>boolean condition</i>.  What 
	   could that be?</p>
	 
	<p>One idea is to add a feedback setting to your app, which controls the type of
	 feedback the user receives -- either a sound or a spoken prediction (in addition,
	 of course, to the written prediction in the Label). To allow the user to choose
	 which option they prefer, you can add a settings menu to your app that allows the user
	 to select between either Speaking the prediction or playing an alert sound.</p>
	 
	<p>A nice UI component for this type of menu is a <a target="_blank" href="http://ai2.appinventor.mit.edu/reference/components/userinterface.html#ListPicker">ListPicker</a>.
	 The ListPicker looks like a button but it has an <i>ElementsFromString</i> property that can be initialized 
	 in the Designer to a comma-separated list of choices.  For example, if you initialize it to <i>Speak, Sound</i>, 
	 then when you click on the ListPicker, it lets you select one of those two choices. The ListPicker
	 has an <i>AfterPicking</i> event handler:
	 
	</p><blockquote>
	<img src="../_static/assets/img/ListPickerAfterPicking.png" width="300px">
	</blockquote>  
	
	<p>What action should you take after the user has selected an option?  You will need to remember
	 what setting the user has selected. HINT:  Use a <i><b>global variable</b></i> to remember the 
	 setting and use an <i><b>if/else</b></i> block to test the value of that variable in the AccelerometerShaking
	 event handler.</p></li>
	
	<!-- 
	<p>One way to fix this is to put a delay between the Play and the Speak actions.   
	The Clock component (Sensor drawer) can be used for this purpose.  
	When the Clock is enabled, it generates a Timer event every so often 
	depending on the value of its TimerInterval property. The default 
	interval is 1000 milliseconds (i.e., 1 second).  Timer events are handled by the 
	Clock.Timer event handler:
	
	<blockquote>
	<img src="../_static/assets/img/Timer.png">
	</blockquote>
	
	
	<p>Using the timer correctly can be tricky. Here are some suggestions:
	
	</p><ul>
	<li> Initially the Timer should be disabled (Clock.enabled property is false).  
	This will prevent it from “ticking” -- i.e., it will prevent its Clock.Timer 
	block from firing.
	</li>
	
	<li>When you want to delay an action, say Action A, enable the Timer. 
	This will start the Timer “ticking”.  The Clock.Timer block will fire on 
	every TimerInterval -- i.e., by default, every second.
	</li>
	<li>When the Clock.Timer block fires, perform Action A and disable the Timer again. 
	</li>
	</ul>
	
	<p>You might also want to take a look a this 
	<a target="_blank" 
	href="http://www.youtube.com/watch?v=sdDcZfeCBXc">
	One Minute Lesson on the Clock Timer</a>.
	
	<p>Try to use these ideas to put a delay between the playing of the Sound and speaking of the prediction.
	</li>
	
	
	<li><b>Advanced: </b> Another shortcoming of the current app is that the Magic 8 Ball 
	provides a prediction whenever it is shaken, even if the user hasn’t asked a question.  
	To fix this, require the user to “speak” their question to the Magic 8-Ball before 
	Magic 8-Ball says its prediction. For this, you’ll need a SpeechRecognizer component (Media drawer).  
	Here’s a <a target="_blank" href="http://www.youtube.com/watch?v=hSLNx6-mYKY">One Minute 
	Lesson on the SpeechRecognizer</a> that you
	may find helpful.
	</li>
	-->
	<li><b>If/ElseIf Algorithm.</b> Modify your solution to the previous exercise to allow a 3-part menu 
	 that includes the following options:  Speak, Sound, Silent.   In the Silent case, the app should
	 silently display the prediction in the label.  HINT:  You'll need to <i>mutate</i> the if-block to 
	 include a second boolean condition.  To do so click the blue mutator widget on the if-block. Your 
	 block should look like one  of these.  Notice that there are 2 when slots where you can plug an
	 equals operator:
	 
	<blockquote>
	<img src="../_static/assets/img/IfElseIfBlocks.png" width="300px">
	</blockquote>   
	
	</li><li>Another shortcoming of the current app is that the Magic 8 Ball provides a prediction whenever 
	 it is shaken, even if the user hasn’t asked a question.  To fix this, require the user to “speak” 
	 their question to the Magic 8-Ball before Magic 8-Ball says its prediction. For this, you’ll need a 
	 <b>SpeechRecognizer</b> component (Media drawer).   Here’s a <a target="_blank" href="http://www.youtube.com/watch?v=hSLNx6-mYKY">One Minute Lesson on the SpeechRecognizer</a> that you may find helpful.  HINT:  To have the app "wait" for the user to speak, you'll
	 have to call the <i>SpeechRecognizer.GetText</i> procedure when the device is shaken.  And you'll have to use 
	 <i>SpeechRecognizer.AfterGettingText</i> to provide the feedback to the user. 
	 
	   
	 </li><li>Be Creative.  Come up with your own ideas to enhance your app or to create a variation of this app.
	</li>
	</ol>
	
Self-Check
----------

.. raw:: html

	<p></p>
	
	<question quid="5740423507083264" weight="1" instanceid="EkW9eUZd0MB1">
	</question>
	<question quid="5647308616105984" weight="1" instanceid="tfqOWeJEPKIA">
	</question>
	<question quid="5686306919153664" weight="1" instanceid="CNcscJO0265c">
	</question>
	<question quid="5758531089203200" weight="1" instanceid="LiXmP1gkuNGo">
	</question>
	<question quid="5725202142986240" weight="1" instanceid="0uXu0cYflIC1">
	</question><br>
	

Reflection: For Your Portfolio
------------------------------
	
	<p>Create a page named <i><b>Magic 8 Ball</b></i> under the <i>Reflections</i> 
	category of your portfolio and answer the following questions:</p>
	
	<ol>
	<li>This app is an <b><i>abstraction</i></b> of the real Magic 8 Ball game. 
	You’ve created a <b><i>model</i></b> of the real Magic 8 Ball game.  In the 
	real game you shake a real ball that contains messages that somehow float into 
	view when the shaking stops. Describe how the various features of your model 
	represent features of the the real game.
	</li>
	
	<li>This app makes use of <i><b>randomness</b></i> -- it picks a random 
	message from a list of options. Suppose you were going to create an app to 
	model a coin flip.  How might you use randomness in that case?
	</li>
	</ol>
	</div>