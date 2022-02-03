.. raw:: html

   <div class="logo-header"  id="student-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>
   
Bias in AI
=======================

.. raw:: html

    <style>    td { text-align: left; padding: 5px;}</style>


.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
        
        generateSummary(EKmapping['A.02']); 
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
    <h3 id="est-length">Time Estimate: 90 minutes</h3>
 
Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <table><tbody>
    <tr><td valign="top" colspan=2><p><span class="hover vocab yui-wk-div" data-id="Alexa">Alexa</span> was first launched by Amazon in 2014. It is a smart speaker built with virtual assistant technology to respond to a <span class="hover vocab yui-wk-div" data-id="wake word">wake word</span> (in this case, the name “Alexa”) and capable of voice interaction. In 2017, Alexa was able to use third party applications so it could tie into everyday life on Earth such as ordering pizza or playing a radio station. Now, Alexa is being investigated as an option for astronauts to use in space. </p>
	<p>When visiting space, travelers need to be able to personalize their AI to their own particular requests. The Good Morning Space tutorial guides you through the basic steps in creating a new Alexa <span class="hover vocab yui-wk-div" data-id="skill">skill</span>. You will also explore bias that could exist within the world of <span class="hover vocab yui-wk-div" data-id="speech recognition">speech	recognition</span>. 
    </p></td></tr>
    <tr><td valign="top"><iframe allowfullscreen="" frameborder="0" height="365" src="https://www.youtube.com/embed/b8Iix4MyLGM" width="275"></iframe>
    <br/>(<a href="" target="_blank">Teacher Tube version</a>)</td>
    <td valign="top">
       <div><b>Learning Objectives:</b>&nbspI will learn to</div>
       <ul>
	   <li>Identify how Alexa’s <span class="hover vocab yui-wk-div" data-id="speech recognition">speech	recognition</span> works</li>
	   <li>Create a new Alexa <span class="hover vocab yui-wk-div" data-id="skill">skill</span> using <span class="hover vocab yui-wk-div" data-id="intent">intents</span>, <span class="hover vocab yui-wk-div" data-id="utterances">utterances</span>, and <span class="hover vocab yui-wk-div" data-id="endpoint function">endpoint functions</span></li>
	   <li>Recognize bias in AI</li>
       </ul>
       <div><b>Language Objectives:</b>&nbspI will be able to</div>
       <ul>
		<li>Explain the impact of using AI</li>
		<li>Describe how the Alexa <span class="hover vocab yui-wk-div" data-id="skill">skill</span> built in this lesson works by using target vocabulary such as <span class="hover vocab yui-wk-div" data-id="wake word">wake word</span>, <span class="hover vocab yui-wk-div" data-id="invocation">skill name/invocation</span>, <span class="hover vocab yui-wk-div" data-id="intent">intent</span>, <span class="hover vocab yui-wk-div" data-id="utterances">utterances</span>, and <span class="hover vocab yui-wk-div" data-id="endpoint function">endpoint function</span></li>
       </ul>
    </td>
    </tr>
    </tbody></table>
    <br/>    

Learning Activities
--------------------

.. raw:: html

	<ul align="center" style="list-style: none; margin: 0; padding: 0; background: lightgrey">
	<li style="display: inline"><a href="https://docs.google.com/document/d/1f08h6SKQGXgSMfNlBStFeK_OwEm9EICOHoBavpFqv9o/view" target="_blank" title="">Tutorial - Text Version</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline">Tutorial - Video</li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://docs.google.com/document/d/1fvoOQBwm9aDaUHVIiiEMyQEgBXEWyh2lUapk8XZAsaE/copy" target="_blank">Worksheet - Bias Activity</a></li>
	</ul> 
	
    <p>
    <h3>How Does Speech Recognition Work</h3>
    <p>In the previous lesson, you learned that Alexa uses <span class="hover vocab yui-wk-div" data-id="speech recognition">speech	recognition</span> and <span class="hover vocab yui-wk-div" data-id="speech synthesis">speech synthesis</span> to provide interactivity through voice. As a reminder, speech recognition involves interpreting and carrying out spoken commands.
	</p>
	
.. youtube:: iNbOOgXjnzE
	:width: 650
	:height: 415
	:align: center

.. raw:: html

	<p><i>Optional:</i> If your teacher has an Alexa in the classroom (a physical Alexa, the Alexa phone app, or the Alexa desktop app), try giving Alexa a few commands as <span class="hover vocab yui-wk-div" data-id="input">input</span>. Alexa will <span class="hover vocab yui-wk-div" data-id="output">output</span> a different result based on what you tell it. A few recommended inputs are:</p>
	<ul>
	<li>Alexa, tell me a joke.</li>
	<li>Alexa, do you have any pets?</li>
	<li>Alexa, what is the value of pi?</li>
	<li>Alexa, high five!</li>
	</ul>
	
	<h4>ACTIVITY: Understanding Alexa Dialogue</h4>
    <p>Before you build out an Alexa <span class="hover vocab yui-wk-div" data-id="skill">skill</span>, review this example of an <a href="https://docs.google.com/document/d/1Gg97OtfsyQlKI1d1mOC9W9q_fRDM0S-fKc75RQ0c6Kk/view" target="_blank">Alexa Dialogue</a> to get familiar with the interaction with Alexa in the tutorial. Here are some key words you should know for Alexa’s voice interaction using App Inventor:
	</p>

	<ul>
	<li><b>Wake word</b> - a phrase that causes the device to begin recording a user's request so it can be sent for processing.</li>
	<li><b>Skill</b> - a set of commands or questions that you can program to use with Alexa</li>
	<li><b>Skill name (also called an invocation)</b> - the phrase a user will speak to indicate to Alexa that they want to use your skill</li>
	<li><b>Intent</b> - the name of a command or question in your program (think of this like a variable or procedure name -- it’s not seen by the user, only the programmer)</li>
	<li><b>Utterance</b> - the command or question a user will speak to trigger a specific action as part of the skill</li>
	</ul>
	
	<p>{ {Insert diagram illustrating dialogue here} }</p>
	
	<h3>Tutorial: Good Morning, Space!</h3>
    <p>Now let’s build out an Alexa skill. Get together with a partner - we will be using <a href="https://www.youtube.com/watch?v=vgkahOzFH2Q" target="_blank">Pair Programming</a> to complete this program. To get started, open Alexa’s App Inventor and login with your Google account. Follow along with your teacher or the video tutorial to create the Good Morning Space Alexa Skill. Or, if you prefer, you can use the <a href="https://docs.google.com/document/d/1f08h6SKQGXgSMfNlBStFeK_OwEm9EICOHoBavpFqv9o/view" target="_blank">text version of the tutorial</a>.
	</p>
	
	<p>{ {Insert video tutorial here} }</p>
	
	<h4>ACTIVITY: Algorithmic Bias</h4>
    <p>Watch this brief video. What do you notice? What do you wonder?</p>
	
.. youtube:: nwPtcqcqz00
	:width: 650
	:height: 415
	:align: center

.. raw:: html

	<p>While comical, this video illustrates one pitfall of using voice activated AI. In this activity, you will investigate the bias present in speech recognition from different perspectives. Open the <a href="https://docs.google.com/document/d/1fvoOQBwm9aDaUHVIiiEMyQEgBXEWyh2lUapk8XZAsaE/copy" target="_blank">Bias Activity worksheet</a>. This can be completed either with a partner or on your own. Once finished, your teacher will lead a class discussion based on your findings. </p>

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>
    
Summary
--------

.. raw:: html

    <p>
    In this lesson, you learned how to:
      <div class="yui-wk-div" id="summarylist">
    </div>
    <br/>

Still Curious?
---------------

.. raw:: html

    <ul>
	<li><a href="https://www.techrepublic.com/article/amazon-alexa-the-smart-persons-guide/" target="_blank">Some background information about the evolution of Alexa</a></li>
	<li><a href="https://itchronicles.com/speech-to-text/speech-recognition-in-ai/" target="_blank">Speech Recognition in AI</a></li>
	<li><a href="https://www.nytimes.com/2019/11/19/technology/artificial-intelligence-bias.html" target="_blank">Dealing with Bias in Artificial Intelligence</a></li>
	<li><a href="https://www.businessinsider.com/what-does-google-know-about-me-search-history-delete-2019-10" target="_blank">What does Google know about you</a> - investigate your own background info</li>
	<li>Hello World is very commonly the first program that any programmer learns how to write! While the program you made for this lesson is modified for our space theme, you can find out more about the origins of Hello, World <a href="https://www.thesoftwareguild.com/blog/the-history-of-hello-world/" target="_blank">here</a>.</li>
	<li><a href="https://www.codedbias.com/" target="_blank">Coded Bias Movie</a></li>
	<li><a href="https://www.ted.com/talks/aicha_evans_your_self_driving_robotaxi_is_almost_here" target="_blank">Your self-driving robotaxi is almost here</a></li>
	</ul>
    
Self-Check
-----------

.. raw:: html

    <p>
    <h3>Vocabulary</h3>
	<p>Here is a table of the technical terms we've introduced in this lesson. Hover over the terms to review the definitions.</p>
    <table align="center">
    <tbody><tr>
    <td>
	<span class="hover vocab yui-wk-div" data-id="Alexa">Alexa</span>
	<br/><span class="hover vocab yui-wk-div" data-id="endpoint function">endpoint function</span>
	<br/><span class="hover vocab yui-wk-div" data-id="input">input</span>
	<br/><span class="hover vocab yui-wk-div" data-id="intent">intent</span>
	<br/><span class="hover vocab yui-wk-div" data-id="invocation">skill name/invocation</span>
	<br/><span class="hover vocab yui-wk-div" data-id="output">output</span>
	</td>
	<td>
	<br/><span class="hover vocab yui-wk-div" data-id="skill">skill</span>
	
	<br/><span class="hover vocab yui-wk-div" data-id="speech recognition">speech	recognition</span>
	<br/><span class="hover vocab yui-wk-div" data-id="utterances">utterances</span>
	<br/><span class="hover vocab yui-wk-div" data-id="wake word">wake word</span>
	<br/>
    </td>
    </tr>
    </tbody></table>
	
    <h3>Check Your Understanding</h3>
    <p>Complete the following self-check exercises. Please note that you should login if you want your answers saved and scored. In addition, some of these exercises will not work in Internet Explorer or Edge browsers. We recommend using Chrome.</p>

.. dragndrop:: mcsp-Alexa-2-1
    :feedback: Review the vocabulary and try again.
    :match_1: The name that users will say to open your skill|||invocation
    :match_2: The task you are asking your Alexa to complete|||intent
    :match_3: Anything the user says|||utterance
    :match_4: Contains the code for your intent|||endpoint function

    Drag the definition from the left and drop it on the correct concept on the right.  Click the "Check Me" button to see if you are correct

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>
	
.. mchoice:: mcsp-alexa-2-2
    :random:
    :practice: T
    :answer_a: To define a new variable called “temperature”
    :feedback_a: Sorry, try again
    :answer_b: To call an invocation called “home”
    :feedback_b: Not quite
    :answer_c: To return a number that represents the temperature
    :feedback_c: That's correct - great job!
    :answer_d: To access a skill in Alexa
    :feedback_d: Be a little more specific - what task does this command achieve?
    :correct: c

    If you say “Alexa, what is the temperature at home?”, the intent is:

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

.. mchoice:: mcsp-alexa-2-3
    :random:
    :practice: T
    :answer_a: Advertising that only shows recommendations based on your gender
    :feedback_a: 
    :answer_b: Recommended videos based on your searches
    :feedback_b: 
    :answer_c: Speech recognition that recognizes all languages 
    :feedback_c: 
    :answer_d: Only having conversations with people who share your interests
    :feedback_d: 
    :correct: a,b,d

    Which of these show an example of bias? Select all that apply.

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>
	

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/17lzd4Dqyau8hrupNGmK_371M5cVE4ewfaBdaBQariUM/copy" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vTGn8_ddjXscevpfJl_wDCdAZGV5ZPX6ddQY5EFW84-XdsR3-FquMS8l8lkYyrgDxh279PhvxDJ6xf0/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    </div>
    </img></div>