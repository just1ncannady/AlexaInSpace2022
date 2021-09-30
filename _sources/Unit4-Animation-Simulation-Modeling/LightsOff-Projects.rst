.. raw:: html 

   <div class="logo-header"  id="student-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

LightsOff Projects
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
            generateSummary(EKmapping['4.03']);
            generateHovers();
    
        });
    </script>
    <!-- can use: #self-check, #still-curious, .pogil, #portfolio -->
    <h3 id="est-length">Time Estimate: 45 minutes</h3>
    

Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <table>
    <tbody>
	<tr>
		<td colspan=2><b><i>Be creative!</i></b> In this lesson you will complete several small programming projects that add enhancements to the <i>LightsOff</i> app. Hints and suggestions are provided.</td>
	</tr>
    <tr>
		<td valign="top"> <img class="yui-img" src="../_static/assets/img/LightsOutPart2.png" height="185" width="400px"/> </td>
        <td valign="top">
			<div><b>Learning Objectives:</b>&nbspI will learn to</div>
			  <ul>
			  <li>iteratively develop a new app using Design Thinking</li>
			  <li>use programming concepts such as variables and conditional <i>if</i> blocks in more advanced ways to enhance an app's functionality</li>
			  </ul>
			  <div><b>Language Objectives:</b>&nbspI will be able to</div>
			  <ul>
			  <li>discuss how code changes will produce desired outputs in my app</li>
			  <li>describe the design process of an app using key vocabulary such as empathize, ideate, and prototype, out loud and in writing, with the support of <a href="https://docs.google.com/presentation/d/1YsJJ7IwEEpQGLqSizFhIFJVIw5TfDc5LqDtCSD-o42E/copy" target="_blank" title="">vocabulary notes</a> from previous lessons</li>			
			  </ul>
		</td>
    </tr>
    </tbody>
    </table>
    

Learning Activities
--------------------

.. raw:: html

    <ul align="center" style="list-style: none; margin: 0; padding: 0; background: lightgrey">
	<li style="display: inline"><a href="https://docs.google.com/document/d/1oKATe1UdK8JdRHzDUVdV7DgXNqvEx41ibnfES5Hijc8/" target="_blank" title="">text-version</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://www.youtube.com/watch?v=a7sEoEvT8l8" target="_blank">YouTube video</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://drive.google.com/open?id=1Qho7PgaSKt7zJhrxx100vFv4gV-voOE4" target="_blank">brainwriting template</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://docs.google.com/drawings/d/1M-DZITeDT9aiPZ7Oz-kXKEGkn0DiFOH1i8idBNlxwCA/" target="_blank" title="">prototypes template</a></li>
	</ul> 
	
    <br/><p>Personalize the LightsOff app by changing its socially useful theme to one that you like and adding new features to it. Your focus should be on understanding the development process. A development process can be incremental or iterative. For example, you might follow an <b>iterative thinking</b> process in which you process a limited number of steps repeatedly or use <b>step-wise refinement</b> to move one small step at a time when developing a program.  Within your development process, you may follow some of these commonly used phases: 
	  <ul>
	  <li> investigating and reflecting </li>
	  <li> designing </li>
	  <li> prototyping </li>
	  <li> testing</li>
	  </ul>
	
	For this lesson, you will focus on implementing <b> Design Thinking</b>. 
        </p>
	<h3>What is Design Thinking?</h3>
    <p>“Design Thinking is an iterative process in which we seek to understand the user, challenge assumptions, and
          redefine problems in an attempt to identify alternative strategies and solutions that might not be instantly
          apparent with our initial level of understanding.” (<a href="https://www.interaction-design.org/literature/article/what-is-design-thinking-and-why-is-it-so-popular" target="_blank">Interaction Design Foundation</a>)<br/>
    <br/>
          Watch this 2-minute introduction to Design Thinking<br/>
    
.. youtube:: a7sEoEvT8l8
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

    </p>
	
    <table border="0" style="width: 100%;">
    <tbody>
    <tr>
		<td style="width:65%">
			<b>Design Thinking Process</b><br/>
			<ol>
			<li><strong>Empathize: </strong>Investigate and understand your users to identify the program requirements</li>
			<ul><li>collect data through surveys</li>
			<li>conduct user testing</li>
			<li>conduct interviews </li>
			<li>make direct observations</li></ul>
			<li><strong>Define:</strong> Analyze the problem and determine the program specifications</li>
			<li><strong>Ideate:</strong> Brainstorm possible solutions</li>
			<ul><li>make a list of your ideas</li>
			<li><span class="yui-non">do a <a href="https://www.sciencedirect.com/science/article/pii/S1877042815027123" target="" title="">6-3-5 brainwriting activity</a> (<a href="https://drive.google.com/open?id=1Qho7PgaSKt7zJhrxx100vFv4gV-voOE4" target="_blank" title="">template</a>)</span></li>
			<li><span class="yui-non">draw paper prototypes (<a href="https://docs.google.com/drawings/d/1M-DZITeDT9aiPZ7Oz-kXKEGkn0DiFOH1i8idBNlxwCA/" target="_blank" title="">template</a>)</span></li></ul>
			<li><strong>Prototype:</strong> Creatively build simple solutions</li>
			<li><strong>Test:</strong> Evaluate the solutions</li>
			</ol>
		</td>
		<td valign=top><img alt="Design Thinking" class="yui-img" src="../_static/assets/img/DesignThinkingimage.png" title="Design Thinking"/><br/>    </td>
    </tr>
	<tr>
		<td colspan=2>When following the design thinking process, keep the following in mind:
	</tr>
	<tr>
		<td colspan=2><i>Program requirements</i> describe how a program functions which may include a description of user interactions that a program must provide. A <i>program’s specification</i> defines the requirements for the program. The <i>designing</i> part of the design thinking process (i.e. the define and ideate phases) is where you outline how to accomplish a given program specification.</td>
	</tr>
    </tbody>
    </table>
    
	<br/> <p>Now that you know about the Design Thinking Process, let's try it out. Use the <a href="https://docs.google.com/document/d/1oKATe1UdK8JdRHzDUVdV7DgXNqvEx41ibnfES5Hijc8/" target="_blank" title="">text-Version handout</a> to write in your answers to the questions in each iteration. </p>
	<h3>Iteration 1: Paper Prototyping</h3>
    <table style="width: 100%; border: 1px solid black;">
    <tbody>
    <tr>
    <td><img alt="DesignThinkingEmpathize" class="yui-img selected" src="../_static/assets/img/DesignThinkingEmpathize.png" style="width: 100px;" title="DesignThinkingEmpathize"/><br/>
    </td>
    <td>Think of a socially useful activity that your app can promote.<br/><br/>
                Who are the users of your app?</td>
    </tr>
    <tr>
    <td><img alt="Design Thinking Design" class="yui-img" src="../_static/assets/img/DesignThinkingDesign.png" style="width: 100px;" title="Design Thinking Design"/></td>
    <td>Define the problem or socially useful activity your app will address.</td>
    </tr>
    <tr>
    <td><img alt="Design Thinking Ideate" class="yui-img" src="../_static/assets/img/DesignThinkingIdeate.png" style="width: 100px;" title="Design Thinking Ideate"/> </td>
    <td>Brainstorm possible ideas for your app.<br/><br/>
                What type of background or sprite images would be good?<br/><br/>
                What would make the app more interesting?</td>
    </tr>
    <tr>
    <td><img alt="Design Thinking Prototype" class="yui-img selected" src="../_static/assets/img/DesignThinkingPrototype.png" style="width: 100px;" title="Design Thinking Prototype"/> </td>
    <td>Create paper prototypes of your app by drawing sample screens.<br/><br/>
                Are any buttons or other user interface elements needed?</td>
    </tr>
    <tr>
    <td><img alt="Design Thinking Test" class="yui-img" src="../_static/assets/img/DesignThinkingTest.png" style="width: 100px;" title="Design Thinking Test"/> </td>
    <td>Imagine users playing your app; does it promote the socially useful activity from your initial idea?<br/><br/>
                What should be changed in the app? </td>
    </tr>
    </tbody>
    </table>
    <h3>Iteration 2: App Inventor Prototyping</h3>
    <p>Start up <a href="http://ai2.appinventor.mit.edu/" target="_blank">App Inventor </a>and after opening your
          LightsOff project, rename it to something fitting your new app idea.<br/>
    </p>
    <table style="width: 100%; border: 1px solid black;">
    <tbody>
    <tr>
    <td><img alt="DesignThinkingEmpathize" class="yui-img" src="../_static/assets/img/DesignThinkingEmpathize.png" style="width: 100px;" title="DesignThinkingEmpathize"/> </td>
    <td>Revisit users of the app. Is the socially useful activity focused on users of a certain age, users doing
                certain activities, or users from specific cultures?<br/>
    <br/>
                Imagine showing your paper prototype to some possible user. They want the app to be more game-like, with a
                score display.</td>
    </tr>
    <tr>
    <td><img alt="Design Thinking Design" class="yui-img" src="../_static/assets/img/DesignThinkingDesign.png" style="width: 100px;" title="Design Thinking Design"/> </td>
    <td>Refine the problem or socially useful activity your app will address. Do you need to change the images use
                in the app?<br/><br/>
                What do you think the user means by adding a score to the app? What would you get points for?<br/>
    </td>
    </tr>
    <tr>
    <td><img alt="Design Thinking Ideate" class="yui-img" src="../_static/assets/img/DesignThinkingIdeate.png" style="width: 100px;" title="Design Thinking Ideate"/> </td>
    <td>Brainstorm ideas for new images for the app. Use <a href="https://www.google.com/imghp?tbm=isch" target="_blank">Google
                  Image search</a> to find possible images to use.<br/>
    <ul>
    <li>Find one or more background images and download these.</li>
    <li>Find one or more sprites and download these.</li>
    </ul>
    <blockquote style="font-size: 1.0em;"><i>Remember many images are copyrighted so use the Tools in Google Image Search to find images “Labeled for noncommercial reuse”</i></blockquote>
    Brainstorm ideas for scoring. Is there one sprite or multiple sprites worth different scores? Do you want good and bad sprites that both increment and decrement the score? </td>
    </tr>
    <tr>
    <td><img alt="Design Thinking Prototype" class="yui-img" src="../_static/assets/img/DesignThinkingPrototype.png" style="width: 100px;" title="Design Thinking Prototype"/> </td>
    <td>Upload the new background and sprite images into the media area for App Inventor. Change the Canvas and
                Sprites to use the new images.<br/>
                How will you add scoring to the app? Where will the score be displayed?<br/>
    <blockquote style="font-size: 1.0em;"><i>Hint: Use what you learned in the Paint Pot app about incrementing a variable to implement the score
                  feature.</i></blockquote></td>
    </tr>
    <tr>
    <td><img alt="Design Thinking Test" class="yui-img" src="../_static/assets/img/DesignThinkingTest.png" style="width: 100px;" title="Design Thinking Test"/> </td>
    <td>How does the new background and sprite images look? <br/>
    <div class="yui-wk-div" style="margin-left: 40px;"><i>The best sprites have a transparent background, so add “transparent” to
                    your image search to find these.</i></div>
                With the new images, when you click on a sprite does the sound still play?<br/>
                Does scoring work? What would be appropriate test cases for the score?</td>
    </tr>
    </tbody>
    </table>
    <h3>Iteration 3: Adding Features</h3>
    <p>Personalize the LightsOff app by changing its socially useful theme to one that you like and adding new features
          to it.</p>
    <table style="width: 100%; border: 1px solid black;">
    <tbody>
    <tr>
    <td><img alt="DesignThinkingEmpathize" class="yui-img" src="../_static/assets/img/DesignThinkingEmpathize.png" style="width: 100px;" title="DesignThinkingEmpathize"/> </td>
    <td>Imagine you talk to some users of your app and they ask for these features:<br/>
    <ol>
    <li> Add a winning score feature that stops the game and congratulates the user when they reach a certain
                    score.</li>
    <li> Add a Reset button to the app that allows the player to restart the game after it's been stopped.</li>
    </ol>
    </td>
    </tr>
    <tr>
    <td><img alt="Design Thinking Design" class="yui-img" src="../_static/assets/img/DesignThinkingDesign.png" style="width: 100px;" title="Design Thinking Design"/> </td>
    <td>Stopping the game when the user reaches the winning score should include stopping the ImageSprite from
                jumping around. Possible enhancement: <br/>
    <ul>
    <li> Use a Notifier component to pop up and congratulate the player.</li>
    <li> Use a TextToSpeech component and have it say something when the player reaches a certain score. </li>
    </ul>
                What do you want the app to do when the user reaches the winning score? What should the reset button do?</td>
    </tr>
    <tr>
    <td><img alt="Design Thinking Ideate" class="yui-img" src="../_static/assets/img/DesignThinkingIdeate.png" style="width: 100px;" title="Design Thinking Ideate"/> </td>
    <td>Brainstorm ways to implement the winning score. Remember you can use an if-block to only run code blocks
                under specific conditions.<br/><br/>
                What options do you have for stopping the game on a winning score and starting it back up with the reset
                button? Do you need any new variables? <br/><blockquote style="font-size: 1.0em;"><i>
                Hint, the <a href="http://ai2.appinventor.mit.edu/reference/components/sensors.html#Clock" target="_blank">Clock
                  component</a> has a Timer Enabled property that can be set to true or false in the program to start and
                stop the action.</i></blockquote></td>
    </tr>
    <tr>
    <td><img alt="Design Thinking Prototype" class="yui-img" src="../_static/assets/img/DesignThinkingPrototype.png" style="width: 100px;" title="Design Thinking Prototype"/> </td>
    <td>Try to implement the winning score and reset button.<br/><ul><li>
                Define a resetGame procedure to encapsulate the tasks involved in resetting the game. These would typically
                include setting the score back to 0 and getting the ImageSprite to start moving again. </li><li>
                In addition to calling the procedure from the reset button event handler, it should be called from the
                Screen1.Initialize handler. Make sure you use good naming conventions when you add a button to the app.</li></ul></td>
    </tr>
    <tr>
    <td><img alt="Design Thinking Test" class="yui-img" src="../_static/assets/img/DesignThinkingTest.png" style="width: 100px;" title="Design Thinking Test"/> </td>
    <td>What would be appropriate test cases for the winning score and the reset buttons? What would be good
                inputs and expected outputs to test?</td>
    </tr>
    </tbody>
    </table>
    <h3></h3>
    <p> </p>
    <p></p>
    <h3>Enhancements</h3>
    <p>Create one or more of your own enhancements or variations for this app. Here are some ideas:</p>
    <ol>
    <li style="margin-bottom: 5px;">Implement keeping track of the number of misses -- i.e., the number of times the player failed
            to touch the ImageSprite -- and factor this into your scoring algorithm.</li>
    <li style="margin-bottom: 5px;"><strong>Abstraction: </strong> Multiple sprites will share some common code and have some unique code. For
            example, all sprites may play the same sound when touched but have different scoring code. Use one of the
            following abstraction techniques on the common code:</li>
		<ul>
		<li style="margin-bottom: 5px;">Move the code common to all sprites into a procedure that is called by each sprite’s Touched event.</li>
		<li style="margin-bottom: 5px;">There is a new abstraction feature in App Inventor where you can take a block of code and make it generic to
              work for any sprite, button, or component. Just right-click on the "When LightBulb1.Touched" event handler and
              choose "Make Generic" to make it work for any sprite on the screen. This is a powerful abstraction feature.
              You will also need to add in moveTo blocks for the new sprites in moveRandom() to make them move.</li>
		</ul>
    <li style="margin-bottom: 5px;">Multiple sprites all have to be moved. You may need to define different versions of the moveRandom procedure for each sprite. </li>
	<li style="margin-bottom: 5px;"><strong>Challenge: </strong>Add another sprite or two. Ask the player to distinguish between "good"
            and "bad" sprites. For example, if your app had a nutrition theme, perhaps one image could be a picture of a
            healthy food item and the other a not-so-healthy item. Perhaps the player's score decreases if they touch the
            "bad" choice.</li>
	<li style="margin-bottom: 5px;"><strong>Challenge: </strong>Change the speed of the sprite when the player reaches a certain score. (Hint:
            Recall that in this app, the sprite's speed is controlled by the Clock timer.)</li>
    </ol>
    

Summary
--------

.. raw:: html

    <p>
    In this lesson, you learned how to:
      <div class="yui-wk-div" id="summarylist">
    </div>
    <p><br/>
    </p>
    

Self-Check
-----------

.. raw:: html

    <p>
    <div class="yui-wk-div" style="text-align: center;">
    .. quizly:: mscp-4-3-1
    
        :quizname: quiz_reset_score
     </div>
    
    .. quizly:: mscp-4-3-2
    
        :quizname: quiz_calculate_hit_rate
     <br/>
    
    .. quizly:: mscp-4-3-3
    
        :quizname: quiz_procedure_bug
    
    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also
            available in this <a href="https://docs.google.com/document/d/19WdMYdewt4Lp2z-lcDicmXOjbIQTlONqeqDIaBQbxa8/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vRPhvSnANzRZ8J3rf0W_SKeLHY09LjP1gog2NhdnlklmgSRCuLUssos-q9-gJ61KKO_IE4TqbPCqGJD/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--&lt;p&gt;Create a page named &lt;b&gt;&lt;i&gt;LightsOff Projects&lt;/i&gt;&lt;/b&gt; in your portfolio and answer the following questions.
    &lt;/p&gt; &lt;ol&gt;&lt;li&gt;Describe the purpose of each enhancement that you added to your app. Give brief descriptions of the enhancements and provide screen shots of important blocks and describe how you used them to solve certain programming problems.&lt;/li&gt;&lt;li&gt;When the user touches an ImageSprite, both the Canvas.Touched and ImageSprite.Touched events are triggered. This is important for more complex games. For instance, suppose there are &quot;good&quot; and &quot;bad&quot; sprites in your game. If you hit one, you earn a point. If you hit the other, you lose two points. If you hit the Canvas and don&#39;t hit the ImageSprite, you lose 1 point. How would you code this?&lt;/li&gt;&lt;li&gt;How do you speed up the movement of the ImageSprite? What is the fastest it could move?&lt;/li&gt;&lt;/ol&gt;-->
    </div>
    </div>