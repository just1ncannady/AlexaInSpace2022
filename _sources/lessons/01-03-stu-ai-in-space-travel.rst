.. raw:: html

   <div class="student-logo"> <img class="align-center" src="../_static/MobileCSP-AFE-logo-white.png" width="400px" alt="mobile csp and amazon future engineers logo on space background"/> </div>
   	<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
   	<div align-center class="w3-show-inline-block">
		<div class="w3-bar w3-light-grey">
		<table style="width:100%">
			<tr>
			<td style="width:20%"><a href="../index.html" class="w3-bar-item w3-button">Alexa in Space Overview</a></td>
			<td style="width:20%"><a href="01-01-stu-intro-to-ai-and-alexa.html" class="w3-bar-item w3-button">Lesson 1: Intro to AI and Alexa</a></td>
			<td style="width:20%"><a href="01-02-stu-biases-in-ai.html" class="w3-bar-item w3-button">Lesson 2: Biases in AI</a></td>
			<td style="width:20%"><a href="01-03-stu-ai-in-space-travel.html" class="w3-bar-item w3-button w3-dark-grey">Lesson 3: AI in Space Travel</a></td>
			<td style="width:20%"><a href="01-04-stu-artemis-alexa.html" class="w3-bar-item w3-button">Lesson 4: Artemis Brings Alexa</a></td>
			</tr>
		</table>
		</div>
	</div>
   
Lesson 3: AI in Space Travel
==================================================

.. raw:: html

    <style>    td { text-align: left; padding: 5px;}</style>


.. raw:: html

    <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
        
        //generateSummary(EKmapping['AiS.03']); 
        generateHovers();
    
        Tipped.create('.vocab', function(element) {
        var vocab = $(element).data('id');
        return vocabulary[vocab];
          }, {
            cache: false,
              position: 'topleft'
              });
      });
    </script>
    <p id="est-length" aria-label="time estimate icon"><b>Time Estimate: 45 minutes</b></p>
 
Introduction and Goals
-----------------------

.. raw:: html

	<p>Now that you’ve had a chance to explore the Alexa MIT App Inventor interface, you will have an opportunity to work closer with Alexa skill-building. During this lesson, you will examine some milestones being achieved by the Artmeis space program. You will also use that newfound knowledge to program Alexa to tell you some interesting facts.</p>
    	
    <p><strong>Learning Objectives:</strong> At the end of this lesson, you will be able to:</p>
    <ul>
    	<li>Identify 3 milestones that are happening with NASA’s Artemis space program.</li>
		<li>Modify an existing Alexa skill in MIT App Inventor by changing the utterances, intent, and function.</li>
    </ul>
    
    <p><strong>Language Objectives:</strong> At the end of this lesson, you will be able to:</p>
    <ul>
		<li>Describe in writing at least 3 facts about the Artemis space program.</li>
		<li>Orally discuss ideas for a new Alexa skill.</li>
    </ul>

::::::::::::::::::

Learning Activities
--------------------

.. raw:: html

	<h3>Discussion: Introduction</h3>
	
	<p>In this lesson, you will be exploring more about the milestones in the Artemis space program. After gathering information, you modify an Alexa skill to teach others about Artemis 1. This video will provide relevant facts you will need to complete the Alexa skill for this lesson. As you watch, write down at least 3 facts about the Artemis space program.</p>
	
.. youtube:: wKwoBudYIiI
	:width: 560
	:height: 315
	:align: center

.. shortanswer:: alexa-1-3-1
	
	What were at least 3 facts you have learned about the Artemis space program during this unit?
	
::::::::::::::::::

.. raw:: html

	<h3>Activity: Good Morning, Space!</h3>
	<p>In this activity, you will complete a build for an Alexa skill that will tell you a random space fact about the Artemis space program.</p>
	
	<ol>
		<li>Open <a href="http://space.appinventor.mit.edu/">Alexa’s App Inventor</a> and log in with your Google account.</li>
		<li>Next, you will need to open the <a href="https://alexa.appinventor.mit.edu/?a=1#4716304443375616">Space Facts skill starter</a>.</li>
		<li>Some of the skill has been created, but you will need to add or modify certain components to make the skill work.</li>
		<li>Walk through the learning object below to get your skill working!</li>
	</ol>
	
.. tabbed:: alexa-tabgroup-1-3

	.. tab:: Step 1: Designer Editor
	
		.. raw:: html
		
			<p>Add 3 utterances in the Designer Editor, under the Properties tab. Remember to click Add after typing each utterance.</p>
			<img src="../_static/assets/img/DesignEditor.png" alt="Adding utterances in the Properties for the IntentAboutSpace component" />
			
	.. tab:: Step 2: Creating Space Facts List
	
		.. raw:: html
			
			<p>Navigate to the Blocks Editor and add your Artemis space facts to the list. You may need to drag more <img src="_static/assets/img/blankStringBlock.png" alt="Blank String Block" style="width: 50px" /> blocks to fill in the empty spaces on the list. You can find those in the Text drawer on the left side of the browser.</p>
			<img src="../_static/assets/img/CreatingSpaceListBlocks.png" alt="Steps to create list for space facts" />
			
	.. tab:: Step 3: Randomize Fact Selection
	
		.. raw:: html
			
			<p>Using the <img src="_static/assets/img/getBlock.png" alt="get block" style="width: 75px" /> block, set the list for the <img src="_static/assets/img/pickRandomListItemBlock.png" alt="pick a random item in list block" style="width: 175px" /> block to be <span style="font-family: monospace;">global factsList</span>. Together, these blocks will pick a random space fact that Alexa will tell you each time you use the utterance.
			<img src="../_static/assets/img/FindGetBlock.png" alt="locating get block in code drawer" />
			
	.. tab:: Step 4: Congrats!
	
		.. raw:: html
		
			<p>Congrats! You’ve completed this Alexa skill! Test your new skill by clicking Send Updates and then with the utterances you created. By clicking the microphone button, you can speak to your Alexa. Alternatively, you can type your statement in the box.</p>
			<img src="../_static/assets/img/TestingAlexaSkill.png" alt="identifying microphone and textbox to send updates to the Alexa skills" />
	
::::::::::::::::::

.. raw:: html
	
	<h3>Discussion: Creating a New Skill</h3>
	
	<p><strong><em>What is an Alexa skill that you could program to solve a problem or be creative?</em></strong></p>
	
	<p>In the next class, you will work with a partner to create an Alexa skill in MIT App Inventor. In this discussion, you will brainstorm to come up with ideas that could be used for your Alexa skill. You will brainstorm in 2 separate activities:</p>
	
	<ol>
		<li><b>Individual Freewrite</b> - Allow your thoughts and ideas to flow freely. Write and draw different ideas that you could use.</li>
		<li><b>Group Idea Expansion</b> - Write some of your ideas on Post-It notes to be shared with your group. Write down any additional ideas that you think of after seeing your group’s ideas.</li>
	</ol>
	
::::::::::::::::::

Reflection
-------------------------------

.. raw:: html

    <p>In the next lesson, you will create an Alexa skill on your own with the ideas you generated today. For now, reflect on what you have learned in this lesson.</p>
    
.. shortanswer:: alexa-1-3-2

	What were some things you learned today about the Artemis space program?
	
.. shortanswer:: alexa1-3-3

	What ideas did you come up with as you brainstormed today for your Alexa skill?

::::::::::::::::::