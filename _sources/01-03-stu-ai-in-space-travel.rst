.. raw:: html

   <div class="student-logo"> <img class="align-center" src="../_static/MobileCSP-AFE-logo-white.png" width="400px"/> </div>

   
Lesson 3 - What's it like to be in space?
==================================================

.. raw:: html

    <style>    td { text-align: left; padding: 5px;}</style>


.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
        
        generateSummary(EKmapping['A.03']); 
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
    <h3 id="est-length">Time Estimate: 90 minutes</h3>
 
Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <table><tbody>
    <tr><td valign="top" colspan=2><p>You’ve been introduced to space travel, <span class="hover vocab yui-wk-div" data-id="artificial intelligence (AI)">artificial intelligence</span>, and the <span class="hover vocab yui-wk-div" data-id="Alexa">Alexa intelligent agent</span>. Now, let’s take a deeper dive into what daily life is really like in space. In this lesson, you will become more familiar with the daily activities of astronauts and space tourists/travelers, and learn how these activities are all affected by <span class="hover vocab yui-wk-div" data-id="microgravity">microgravity</span>. These new facts will become a <span class="hover vocab yui-wk-div" data-id="list">list</span> -- very useful structures in programming that can store a collection of related data. You will program an Alexa skill to access various items from your list in response to a voice command, or <span class="hover vocab yui-wk-div" data-id="utterances">utterance</span>.</p></td></tr>
    <tr><td valign="top"></td>
    <td valign="top">
       <div><b>Learning Objectives:</b>&nbspI will learn to</div>
       <ul>
	   <li>Recognize and give examples of the effects of <span class="hover vocab yui-wk-div" data-id="microgravity">microgravity</span> on peoples’ daily activities in space</li>
		<li> Create and add items to a <span class="hover vocab yui-wk-div" data-id="list">list</span> </li>
		<li>Select a random item from a <span class="hover vocab yui-wk-div" data-id="list">list</span> to be spoken as output</li>
       </ul>
       <div><b>Language Objectives:</b>&nbspI will be able to</div>
       <ul>
		<li>Explain the effects of microgravity on both daily activities and scientific experiments in space using target vocabulary such as microgravity out loud and in writing, with the support of the vocabulary notes from this lesson.</li>
		<li>Use target vocabulary, such as <span class="hover vocab yui-wk-div" data-id="utterances">utterance</span>, <span class="hover vocab yui-wk-div" data-id="intent">intent</span>, <span class="hover vocab yui-wk-div" data-id="invocation">invocation</span>, and <span class="hover vocab yui-wk-div" data-id="endpoint function">endpoint function</span>, to describe how an Alexa skill can respond to a request out loud and in writing, with the support of the vocabulary notes from this lesson.</li>
       </ul>
    </td>
    </tr>
    </tbody></table>
    <br/>    

Learning Activities
--------------------

.. raw:: html

	<ul align="center" style="list-style: none; margin: 0; padding: 0; background: lightgrey">
	<li style="display: inline"><a href="https://docs.google.com/document/d/1gXTLiOCspw8bfdq1Fyuic5OhevNqGeikplist5mug68/view" target="_blank" title="">Tutorial - Text Verison</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://youtu.be/MymcQP6UJDg" target="_blank" title="">Tutorial - Video</a></li>
	</ul> 
	
    <p>
    <h4>ACTIVITY: Daily Life in Space</h4>
    <p>The resources below detail the daily activities of astronauts on the International Space Station, or ISS. Remember microgravity? Microgravity (very weak gravity) affects each and every part of an astronaut’s <b>daily routine</b>. Imagine yourself as an astronaut or space tourist. How might your daily activities be changed by microgravity?</p>
	
	<p align="center"><i>Try this thought exercise and discuss as a class: 
	<br/>If you were placed in the middle of a room in a microgravity environment, 
	how would you move to another place in that room? 
	<br/>Hint: Newton’s Third Law -- for every action, there is an equal and opposite reaction. </i></p>
	
	<ul>
	<li><a href="https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Astronauts/Daily_life" target="_blank">ESA - Daily Life </a></li>
	<li><a href="https://youtu.be/-Y04Zic1-r4" target="_blank">Life Inside the International Space Station (ISS)</a></li>
	<li><a href="https://www.breezyscroll.com/technology/a-day-in-the-life-of-an-astronaut-in-space/ " target="_blank">A day in the life of an astronaut</a></li>
	</ul>
	
	
	<h4>ACTIVITY: Scientific Research in Space</h4>
    <p>Aside from daily routines, a good part of an astronaut’s time is taken up with <b>scientific research</b>, much of which includes collecting and analyzing data like we discussed earlier in this unit. Read through the variety of research topics</p>
	<ul>
	<li>Experiments in space: Space Station Research Explorer on NASA.gov - Which of the experiments sound the most interesting to you? What kind of data was collected during the experiment? <a href="https://www.nasa.gov/mission_pages/station/research/experiments/explorer/" target="_blank">Read more</a>.</li>
	<li>Thinking about going into space as a <b>tourist</b>, instead of as an astronaut? You will find that microgravity will have just as much of an impact on your experience as it does for astronauts! <a href="https://www.travelandleisure.com/trip-ideas/space-astronomy/what-space-tourists-should-know-before-traveling-to-space-according-to-astronauts" target="_blank">Read more about what to expect as a space tourist here</a>.</li>
	<li>Our understanding of space and microgravity will be important to future missions such as NASA’s Artemis program, designed to return astronauts to the moon by 2025, and potentially prepare for future Mars missions. The Artemis program includes plans for a mini space station to orbit the moon. There are even plans to include Alexa in the mission! Everything we can learn now will help the Artemis program to be successful in the future. <a href="https://www.cnn.com/2022/01/05/tech/amazon-alexa-artemis-orion-launch-scn/index.html" target="_blank">Check out this CNN article on Amazon Alexa in the Artemis program</a>.</li>
	</ul>

	<p>Complete the <a href="https://docs.google.com/document/d/1Yc7RaSNibIBS5NZ8zpl0-zlQFrcM-q4ARs7am2XgiKo/copy" target="_blank">Space Facts Worksheet</a> and record the responses to the following in your portfolio: </p>
	<p><b><i>[Portfolio]</b></i> List 4 daily activities that must be done in space. How are they different in an environment of microgravity?</p>
	<p><b><i>[Portfolio]</b></i> List 2 interesting science experiments being done in space. Why is it important to understand the results of these experiments in microgravity?</p>
	<p><b><i>[Portfolio]</b></i> What are 2 ways that microgravity could affect space tourists?</p>
	
	<h3>Tutorial: Space Facts</h3>
    <p>Now that you’ve had a chance to explore what it’s like to be in space, you can appreciate how small tasks become extremely difficult without special adaptations. An example of a helpful adaptation would be using an AI program with speech recognition, like Alexa, to access needed information that normally would be accessed by typing directly on a device. In this exercise, you’ll get the opportunity to work with an Alexa skill, and adapt it for use with multiple <span class="hover vocab yui-wk-div" data-id="intent">intents</span>. The list of items you developed in the previous activity will be used to create a list of space facts.</p>
	<p>This tutorial will use programming constructs that allow for data abstraction. We will use a list, which is a special type of variable. 
	
	<h4>Variable</h4>
    <p>A <span class="hover vocab yui-wk-div" data-id="global variable">global variable</span> provides a way to name a memory location in your program to hold different values. It is a data abstraction that exists in all programming languages. In MIT App Inventor, we set up a variable using the initialize global variable block. The get block is used to get the variable's current value whenever needed in the program. The set block is used to assign or change the value of the variable.</p>
	
	<h4>List</h4>
    <p>Like most other programming languages, MIT App Inventor has an abstract data type (ADT) called <span class="hover vocab yui-wk-div" data-id="list">list</span> that allows the storage of an ordered sequence of elements under one name in memory. Lists are sometimes called arrays in other programming languages. Data abstractions manage complexity in the program by giving a collection of data a name that can be used without knowing the specific details of its representation. The elements in a list are indexed which means they are numbered from 1 to the length of the list.</p>
	<p>Before starting the tutorial, brainstorm as a class several <span class="hover vocab yui-wk-div" data-id="utterances">utterances</span> that you might use to ask Alexa for a random fact about space. </p>
	<p>After brainstorming, complete the <a href="https://docs.google.com/document/d/1gXTLiOCspw8bfdq1Fyuic5OhevNqGeikplist5mug68/view" target="_blank">Space Facts tutorial</a>.</p>
	
.. youtube:: MymcQP6UJDg
	:width: 650
	:height: 415
	:align: center

.. raw:: html
	
	<h3>Enhancements</h3>
    <ol>
	<li>Add 4 additional facts to the list of “space facts”.</li>
	<li>Program the skill to remove an item from the list once it’s been used</li>
	</ol>

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

    <p><a href="https://www.usatoday.com/story/money/2019/07/08/space-race-inventions-we-use-every-day-were-created-for-space-exploration/39580591/" target="_blank">This article</a> lists inventions that many of us use every day. You may never have realized that they were initially invented to be used by astronauts in space. 
	</p>
    
Self-Check
-----------

.. raw:: html

    <h3>Vocabulary</h3>
	<p>Here is a table of the technical terms we've introduced in this lesson. Hover over the terms to review the definitions.</p>
    <table align="center">
    <tbody><tr>
    <td>
    <span class="hover vocab yui-wk-div" data-id="Alexa">Alexa</span>
	<br/>
	<span class="hover vocab yui-wk-div" data-id="artificial intelligence (AI)">artificial intelligence</span>
	<br/>
	<span class="hover vocab yui-wk-div" data-id="endpoint function">endpoint function</span>
	<br/>
	<span class="hover vocab yui-wk-div" data-id="global variable">global variable</span>
	<br/>
	<span class="hover vocab yui-wk-div" data-id="list">list</span>
	<br/>
	</td>
	<td>
	<span class="hover vocab yui-wk-div" data-id="microgravity">microgravity</span>
	<br/>
	<span class="hover vocab yui-wk-div" data-id="randomness">randomness</span>
	<br/>
	<span class="hover vocab yui-wk-div" data-id="intent">intent</span>
	<br/>
	<span class="hover vocab yui-wk-div" data-id="invocation">invocation</span>
	<br/>
	<span class="hover vocab yui-wk-div" data-id="utterances">utterances</span>
	<br/>
    </td>
    </tr>
    </tbody></table>
	
    <h3>Check Your Understanding</h3>
    <p>Complete the following self-check exercises. Please note that you should login if you want your answers saved and scored. In addition, some of these exercises will not work in Internet Explorer or Edge browsers. We recommend using Chrome.</p>
    
.. mchoice:: mcsp-alexa-3-1
    :random:
    :practice: T
    :answer_a: Shampoo cannot be brought into space
    :feedback_a: Sorry, try again
    :answer_b: Microgravity prohibits the use of water to rinse shampoo or conditioner out of hair.
    :feedback_b: Correct!
    :answer_c: There is no water in space.
    :feedback_c: Sorry, try again.
    :answer_d: There is no time for personal hygiene in space.
    :feedback_d: Astronauts do have access to a water supply and shampoo, and do make time for personal hygiene each day. However, there is no way to rinse normal shampoo out of your hair in space, so a special “dry” shampoo was developed.
    :correct: b

    The best explanation for having a difficult time washing your hair in space would be:

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>
	
.. mchoice:: mcsp-alexa-3-2
    :random:
    :practice: T
    :answer_a: Space provides a unique vantage point for data collection
    :feedback_a: Sorry, try again
    :answer_b: It’s important to study the risks to human health inherent in space travel from space itself.
    :feedback_b: Sorry, try again
    :answer_c: Astronauts don’t have a lot to do in space, and need things to keep them busy.
    :feedback_c: Correct!
    :answer_d: Cell and tissue growth for various organisms can be very different in space due to microgravity, and it’s important to understand the differences.
    :feedback_d: Scientific experiments of all types are being done in space because space provides a unique opportunity to study the effects of microgravity on everything from complex living things to inanimate objects, and to see if any learned information can be applied to helping people on Earth, as well as in space.
    :correct: c

    Which of the following are NOT reasons why it is important to do scientific experiments in space:

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

.. mchoice:: mcsp-alexa-3-3
    :random:
    :practice: T
    :answer_a: use multiple phrases (utterances) to define one intent.
    :feedback_a: 
    :answer_b: follow a specific path to retrieve a value
    :feedback_b: 
    :answer_c: speak an intent
    :feedback_c: Sorry, try again
    :answer_d: eliminate bias from the skill
    :feedback_d: This does not require a list to be present in the Alexa skill. Actually, in this case, a list could actually increase the bias of the skill, depending on the data contained in the list and how that data is processed.
    :correct: a,b

	Lists can be useful when building an Alexa skill because they allow the programmer to (choose two):

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

.. mchoice:: mcsp-alexa-3-4
    :random:
    :practice: T
    :answer_a: 2
    :feedback_a: Sorry, try again
    :answer_b: 5
    :feedback_b: Correct! In App Inventor, lists are indexed starting at 1. The last index is the same number as the length of the list. In this case, with 4 items in the list, the last index is 4. Therefore, an index of 5 would be out of bounds.
    :answer_c: 1
    :feedback_c: Sorry, try again
    :answer_d: 3
    :feedback_d: Sorry, try again
    :correct: b

    Which of the following is NOT a possible index for a random fact that Alexa could say?

    .. raw:: html

        <img class="yui-img" src="../_static/assets/img/factsIndex.PNG"/>   


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/16Hx7qg_xpJEodi60gZksV95wZrZWi8d0GSypuOZf97Y/copy" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vSR9qrA9WiHALOoO6wy9a5ZXJ5koUrH-cPNyQMUhHPQHQcqKQhHL7Xc2fguUf1ACIo5ksRybW3OHB0n/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    </div>
    </img></div>