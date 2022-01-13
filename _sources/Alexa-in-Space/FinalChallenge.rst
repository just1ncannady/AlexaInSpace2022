.. raw:: html

   <div class="logo-header"  id="student-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>
   
Final Challenge
=======================

.. raw:: html

    <style>    td { text-align: left; padding: 5px;}</style>


.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
        
        generateSummary(EKmapping['X.XX']); /* Change the lesson number */
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
    <img height="25" src="../_static/assets/img/time.png" style="float:left" width="25"/>
    <h3 id="est-length">Time Estimate: 225-270 minutes</h3>
 
Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <table><tbody>
    <tr><td valign="top" colspan=2><p>Now it’s your turn to help space travelers navigate daily life in a microgravity environment! Using what you have learned and reviewing the resources below, what do you think will be some of the challenges space travelers will have to overcome and how might voice-powered artificial intelligence help them? </p>

	<p>For the final challenge, you will work with a partner to create an Alexa skill in MIT App Inventor that solves a problem for space travelers. You will submit your working program, a video or audio file demonstrating how the skill works, and written responses that explain the skill’s alignment to the challenge theme and how the algorithms in your code work. You may create an app to accompany the skill, similar to Lesson 5, however it is not required. Carefully review the criteria to make sure you understand them. </p>
	</p></td></tr>
    <tr><td valign="top"></td>
    <td valign="top">
       <div><b>Learning Objectives:</b>&nbspI will learn to</div>
       <ul>
	   
       </ul>
       <div><b>Language Objectives:</b>&nbspI will be able to</div>
       <ul>

       </ul>
    </td>
    </tr>
    </tbody></table>
    <br/>    

Learning Activities
--------------------

.. raw:: html

	<ul align="center" style="list-style: none; margin: 0; padding: 0; background: lightgrey">
	<li style="display: inline"><a href="" target="_blank" title="">Slides</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="" target="_blank">Video</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://drive.google.com/file/d/1Qho7PgaSKt7zJhrxx100vFv4gV-voOE4/view" target="_blank">Brainwriting Template</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://docs.google.com/document/d/16zZXzrw56HerqG_TmPDNw3nLx3RcAKGKwj3kZOlvi58/" target="_blank">Project Exemplar</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://docs.google.com/document/d/1HrkHitnELOOzd2mQ_taY0WKQj3quANhuJCdnpX2LD3U/" target="_blank">Final Challenge Rubric</a></li>
	</ul> 
	
    <p>
    <h4>Warm Up Activity</h4>
    <p>With your classmates, brainstorm a list of daily activities that you do on Earth such as taking a shower, brushing teeth, eating breakfast, etc. Then turn-and-talk to identify which of these activities might be the most difficult in a microgravity environment.</p>
	
	<h4>ACTIVITY: Grade Project Exemplar</h4>
    <p>Review the project requirements (slide deck/video). In groups of four students, review the <a href="https://docs.google.com/document/d/16zZXzrw56HerqG_TmPDNw3nLx3RcAKGKwj3kZOlvi58/" target="_blank">Project Exemplar</a> using the <a href="https://docs.google.com/document/d/1HrkHitnELOOzd2mQ_taY0WKQj3quANhuJCdnpX2LD3U/" target="_blank">Final Challenge Rubric</a>. Each group member should select a role from below. Complete the rubric and be prepared to discuss where you think the exemplar could use one area of improvement and one area where it exceeded expectations. </p>
	
	<p><b>Group Roles:</b></p>
	<ul>
	<li><i>Facilitator</i> - ensures everyone is participating and the group discussion is about the exemplar and rubric</li>
	<li><i>Rubric Completer</i> - fills out the rubric based on group discussion</li>
	<li><i>App Tester</i> - shares the App Inventor project on their screen and plays the audio/video of the skill being tested</li>
	<li><i>Reporter</i> - Represents the group during class discussion</li>
	</ul>
	
	<h4>ACTIVITY: Explore Project Ideas</h4>
    <p>Now that you understand the project requirements better, you will expand on your initial ideas for Alexa skills that might be useful in space. In your groups, each person should have a blank copy of the <a href="https://drive.google.com/file/d/1Qho7PgaSKt7zJhrxx100vFv4gV-voOE4/view" target="_blank">Brainwriting Template</a>. You will complete 4 rounds with 4 minutes for each round. Review these ground rules first:</p>
	<ul>
	<li>Defer judgement - there are no bad ideas</li>
	<li>Quantity - more is better</li>
	<li>Freewheel - wild ideas are good</li>
	<li>Piggyback ideas - play off each other’s ideas</li>
	<li>Write neatly & clearly</li>
	</ul>
	
	<p>In the first round, everyone should add an initial idea (or more!) of an Alexa skill that they would like to create for the project. For the second round, pass your brainwriting form to the person on your right. Review their ideas and add your own in the second row. Repeat this process for rounds 3 and 4. At the end, you should receive your own brainwriting form back with feedback from your group members. As you are writing in rounds 2 - 4, think about adding new ideas, combining ideas, adapting ideas to new areas, adding to ideas, or suggesting modifications.</p>

	
	<h3>Submission</h3>
    <p>To complete the challenge, provide the following three items in your portfolio: your program, a video or audio demonstration, and written response. You may complete the challenge on your own or in pairs. If you work individually, you should collaborate by asking student peers to help test your skill and/or review your code (to help debugging, for readability, etc.) If you work in pairs, each person should have responsibility for writing some of the code and each student should write their own written responses, however, both students can provide the same program and video/audio demonstration files. 
	</p>
	
	<ul>
	<li>Your Program -- Include your MIT App Inventor .aia file that includes your Alexa skill and a screenshot of your entire code.</li>
	<li>Video or Audio Demonstration -- Provide a video demonstrating the running of your skill in MIT App Inventor. Alternatively, if you have access to an Alexa device for testing, you could provide an audio recording using your skill. {Using Alexa app for testing}</li>
	<li>Written Response -- Provide a two paragraph response as a [PDF, Google Doc, Portfolio, etc.] that answers the following:</li>
		<ul>
		<li>Describe the purpose of your program. In other words, what problem does your skill and/or app solve related to space travel?</li>
		<li>Describe the functionality of the program demonstrated in your video/audio. How does your program solve the problem? Be sure to name your skill and include enough detail so that another person could recreate your skill.</li>
		<li>Include a screenshot of the code for your skill.</li>
		<li>Collaboration:</li>
			<ul>
			<li>If you worked on the challenge individually, describe how you used peer feedback through testing and code review to improve your skill.</li>
			<li>If you worked in pairs, describe your contributions to the challenge project and how working together improved the project.</li>
			</ul>
		<li> AI - {{to be added}} </li>
		</ul>
	</ul>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>
    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following written response questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1JXgsSdF0hSYI86Gj_B6LqdBP46o7U5wrlpO64Zz7tjU/copy" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vS29jCcI63pBREZXX0bTKp9MRZ5TqaiUIzW5-Wl_YrUGxrMnp8FvF_n2KYQVF-eJA4v1Xtv6_qvOYma/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    </div>
    </img></div>