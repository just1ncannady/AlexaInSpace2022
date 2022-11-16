.. raw:: html

   <div class="student-logo"> <img class="align-center" src="_static/MobileCSP-AFE-logo-white.png" width="400px" alt="mobile csp and amazon future engineers logo on space background"/> </div>
   	<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
   	<div align-center class="w3-show-inline-block">
		<div class="w3-bar w3-light-grey">
		<table style="width:100%">
			<tr>
			<td style="width:20%"><a href="index.html" class="w3-bar-item w3-button">Alexa in Space Overview</a></td>
			<td style="width:20%"><a href="lessons/01-01-stu-intro-to-ai-and-alexa.html" class="w3-bar-item w3-button">Lesson 1: Intro to AI and Alexa</a></td>
			<td style="width:20%"><a href="lessons/01-02-stu-biases-in-ai.html" class="w3-bar-item w3-button">Lesson 2: Biases in AI</a></td>
			<td style="width:20%"><a href="lessons/01-03-stu-ai-in-space-travel.html" class="w3-bar-item w3-button">Lesson 3: AI in Space Travel</a></td>
			<td style="width:20%"><a href="lessons/01-04-stu-artemis-alexa.html" class="w3-bar-item w3-button w3-dark-grey">Lesson 4: Artemis Brings Alexa</a></td>
			</tr>
		</table>
		</div>
	</div>
   
Lesson 4: Artemis Brings Alexa
======================================

.. raw:: html

    <style>    td { text-align: left; padding: 5px;}</style>


.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
        
        generateSummary(EKmapping['A.04']); /* Change the lesson number */
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

    <p>During this unit, you have examined the Artemis space program and worked with 2 Alexa skills: Good Morning, Space and Space Facts. In this lesson, you will explore other contexts in which AI would be helpful in space. You will also build an Alexa skill based on your previous brainstorm.</p>
    
    <p><strong>Learning Goals:</strong> At the end of this lesson, you will be able to:</p>
    <ul>
    	<li>Reuse components of existing programs for new programs.</li>
		<li>Create a new Alexa skill using MIT App Inventor.</li>
    </ul>
    
    <p><strong>Language Goals:</strong> At the end of this lesson, you will be able to:</p>
    <ul>
    	<li>Describe in writing the purpose of an Alexa skill.</li>
		<li>Explain in writing difficulties encountered while building a new Alexa skill.</li>
    </ul>

::::::::::::::::::

Learning Activities
--------------------

.. raw:: html

	<h3>Discussion: Introduction</h3>
	
	<p>In this lesson, you will be imagining how Alexa could be used in space travel. This video provides some examples of how voice AI could be used in space travel. As you watch, think about other Alexa function that could help with space travel.</p>

::::::::::::::::::
	
.. raw:: html

	<h3>Activity: Create Your Skill</h3>
	
	<p>In this activity, you will build an Alexa skill based on an idea that you have come up with in your brainstorm. Since you may be new to programming or the Alexa App Inventor environment, there are some examples of code blocks below to help you as you create your own. When you are ready, open the <a href="https://alexa.appinventor.mit.edu/?a=1#6280354029633536">New Skill starter</a>. The starter project has a skill (space helper) and intent (IntentHelpInSpace) already created for you.</p>
	
.. tabbed:: alexa-tabgroup-1-4

	.. tab:: Jokes
	
		.. raw:: html
		
			<p>In this skill, Alexa tells the user a joke. Alexa asks the question, waits for the user’s response, and then delivers the punchline.</p>
			<img src="_static/assets/img/jokesSkill.png" alt="Alexa Joke skill block code" />
			
	.. tab:: To-Do-List
	
		.. raw:: html
		
			<p>In this skill, Alexa tells the user a to-do list that has been programmed.</p>
			<img src="_static/assets/img/todoListSkill.png" alt="Alexa skill to read off a to-do list" />
			
	.. tab:: Space Facts
	
		.. raw:: html
		
			<p>In this skill, Alexa tells the user a random fact about space.</p>
			<img src="_static/assets/img/spaceFactsSkill.png" alt="Alexa skill to randomly read space fact from a list of facts" />


			
::::::::::::::::::

Reflection
-------------------------------

.. raw:: html

	<p>Congrats! You have successfully completed the Alexa in Space unit! Reflect on what you have learned in this lesson.</p>
	
.. shortanswer:: alexa-1-4-1

	Describe the purpose of your Alexa skill. In other words, what problem does your skill solve?
	
.. shortanswer:: alexa-1-4-2

	What was something you found challenging about building the skill?

::::::::::::::::::