.. raw:: html

   <div class="logo-header"  id="student-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>
   
Lesson 4 - Meals in Space
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
    <h3 id="est-length">Time Estimate: 90 minutes</h3>
 
Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <table><tbody>
    <tr><td valign="top" colspan=2><p>When you are experiencing <span class="hover vocab yui-wk-div" data-id="microgravity">microgravity</span>, the need arises for space travelers to increase their <span class="hover vocab yui-wk-div" data-id="calorie intake">calorie intake</span> everyday. In space, your <a href="https://www.nasa.gov/audience/foreducators/stem-on-station/ditl_eating" target="_blank">food options</a> can be limited and sometimes astronauts can become bored with the meal options. </p>
	<p>In this lesson, you will create an <span class="hover vocab yui-wk-div" data-id="Alexa">Alexa</span> skill where Alexa can select your meal for you and track your calories. The purpose of this skill is to help someone in space to make a decision about what food they will have for breakfast and track the amount of calories a user has eaten that day, starting with their breakfast meal. </p>
	</td></tr>
    <tr><td valign="top"></td>
    <td valign="top">
       <div><b>Learning Objectives:</b>&nbspI will learn to</div>
       <ul>
	   <li>Use multiple intents</li>
		<li>Use <span class="hover vocab yui-wk-div" data-id="slot">slots</span></li>
		<li>Use <span class="hover vocab yui-wk-div" data-id="parallel lists">parallel lists</span></li>
		<li>Use a procedure with a <span class="hover vocab yui-wk-div" data-id="parameters">parameter</span></li>
		<li>Perform math calculations using <span class="hover vocab yui-wk-div" data-id="Alexa">Alexa</span></li>
       </ul>
	   
       <div><b>Language Objectives:</b>&nbspI will be able to</div>
       <ul>
		<li>Explain how <span class="hover vocab yui-wk-div" data-id="Alexa">Alexa</span> uses variables to store data</li>
		<li>Explain how a <span class="hover vocab yui-wk-div" data-id="parameters">parameter</span> can be useful in a procedure</li>
		<li>Describe how <span class="hover vocab yui-wk-div" data-id="procedural abstraction">procedural abstraction</span> can manage complexity</li>
       </ul>
    </td>
    </tr>
    </tbody></table>
    <br/>    

Learning Activities
--------------------

.. raw:: html

	<ul align="center" style="list-style: none; margin: 0; padding: 0; background: lightgrey">
	<li style="display: inline"><a href="https://docs.google.com/document/d/16dGhZqbFQ_QonbLIPQd2825sFQ9JKvcaKcBeEIBqC-E/view" target="_blank" title="">Tutorial - Text Version</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://youtu.be/E1gIkzIjJ6M" target="_blank" title="">Tutorial Part 1 - Video</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://youtu.be/ct9Cf7y73g0" target="_blank" title="">Tutorial Part 2 - Video</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://youtu.be/O1q63nAUNc8" target="_blank" title="">Tutorial Part 3 - Video</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://www.nasa.gov/sites/default/files/atoms/files/stemonstrations_nutrition.pdf" target="_blank">Activity</a></li>
	</ul> 
	
    <h4>ACTIVITY: Breakfast Calories</h4>
    <p>When experiencing <span class="hover vocab yui-wk-div" data-id="microgravity">microgravity</span>, space travelers need to ingest more calories than on Earth, sometimes an extra <a href="https://phys.org/news/2018-03-astronauts-extra-calories-space.html" target="_blank">1000-1500 calories per day</a>. Keeping track of their diet can be tricky, so you will develop an Alexa skill to help space travelers make a decision about their meal options and track their <span class="hover vocab yui-wk-div" data-id="calorie intake">calorie intake</span>. </p>
	
	<p>As an example, here are the daily energy needs for two astronauts aboard the ISS. The basal metabolic rate (BMR) is calculated from data on the astronaut’s gender, age, height, and mass. The calorie needs vary by the activity level of the astronaut. Calories are often measured in kilocalories (1 kcal = 1,000 calories).</p>
	
	<table>
	<th><td><b>Astronaut A</b></td> <td><b>Astronaut B</b></td></th>
	<tr>
	<td><b>Data</b></td>
	<td>Gender: Female, Age: 38, <br/> Height: 157 cm, Mass: 55 kg</td>
	<td>Gender: Male, Age: 40, <br/> Height: 183 cm, Mass: 93 kg</td>
	</tr>
	<tr>
	<td><b>BMR (base kcal)</b></td>
	<td>1,294</td>
	<td>1,989</td>
	</tr>
	<tr>
	<td><b>No exercise (x1.2)</b></td>
	<td>1,552</td>
	<td>2,387</td>
	</tr>
	<tr>
	<td><b>Moderate exercise (x1.55)</b></td>
	<td>2,006</td>
	<td>3,083</td>
	</tr>
	<tr>
	<td><b>Heavy exercise (x1.9)</b></td>
	<td>2,459</td>
	<td>3,779</td>
	</tr>
	</table>
	
	<br/>
	<p>Using the <a href="https://www.nasa.gov/sites/default/files/atoms/files/stemonstrations_nutrition.pdf" target="_blank">ISS Standard Menu (pg. 10-18)</a>, work with a partner to create a menu for one of the astronauts. You can select their exercise amount for the day and the corresponding calorie needs. Think about three meals (breakfast, lunch, dinner) as well as snacks and beverages throughout the day.</p>
	
	<h3>Tutorial: Meals in Space</h3>
    <p>For <a href="https://docs.google.com/document/d/16dGhZqbFQ_QonbLIPQd2825sFQ9JKvcaKcBeEIBqC-E/view" target="_blank" title="">this tutorial</a>, you will program a skill where Alexa will read the <span class="hover vocab yui-wk-div" data-id="list">list</span> of breakfast options and the user will be able to select one of the options to eat. Alexa will then let you know how many calories that item contains and add that amount to your total <span class="hover vocab yui-wk-div" data-id="calorie intake">calorie intake</span> for the day. You will also create a procedure that takes in the number of calories already consumed for the day, subtracts from the daily requirement, and sets the calorie variable to the new number.</p>
	
	<h4>Parallel Lists</h4>
	<p>The Meals in Space skill has two essential <span class="hover vocab yui-wk-div" data-id="list">lists</span>: one list contains three breakfast options and another list contains the calorie count for each breakfast option. The first food in the food list corresponds to the first calorie in the calories list. This is known as a <span class="hover vocab yui-wk-div" data-id="parallel lists">parallel list</span> construction. This parallel setup allows you to use an <span class="hover vocab yui-wk-div" data-id="index">index</span> to associate each food with its corresponding calorie value. Indexing of lists in App Inventor starts at 1. </p>

.. youtube:: E1gIkzIjJ6M
	:width: 650
	:height: 415
	:align: center

.. raw:: html

	<h4>Multiple Intents</h4>
	<p>In the previous lessons you learned how to create a skill that involves Alexa responding to a direct command using one intent. However, for the Meals in Space skill two intents are needed: one intent to trigger the reading of the breakfast options and another intent to trigger the logging of a food and its calories. After an utterance for one intent is made, you can use the “ask” block shown below to have Alexa respond and ask the user what they would like to do next. When using the “ask” block, Alexa will wait eight (8) seconds for the user to respond with another intent.</p>

	<h4>Slots</h4>
	<p>A <span class="hover vocab yui-wk-div" data-id="slot">slot</span> is like a variable in an utterance. You use slots when you want to store something that a user said, like a particular date, place, or number. Slot blocks tell Alexa what part of the utterance it should store. For example, if you want to ask Alexa how far away a planet is from earth, then you might say something like “How far is Mars from Earth?” Without your help, Alexa won’t know which part of the sentence needs to be stored (which, in this case, is “Mars”). To tell Alexa which part of the sentence is important, we use slots. For the Meals in Space skill, you use a slot for collecting the food option selected by the user. </p>

	<p>Note: Slots that are numbers can only be whole numbers, not decimal numbers.</p>

	<h4>Procedural Abstraction</h4>
	<p>As part of this skill, you will use procedural abstraction. <span class="hover vocab yui-wk-div" data-id="procedural abstraction">Procedural abstraction</span> is the ability to name a block of code in a procedure and call it whenever needed, is a very important concept in programming. We are abstracting away from the details of that block of code and just using its name to do its job. We only need to know what it does, not how it does it. Procedural abstraction allows us to reuse code that is already written instead of rewriting the code and repeating it. And it allows programmers to change the internals of the procedure (to make it faster, more efficient, use less storage, etc.) without needing to notify users of the change as long as what the procedure does is preserved. In addition, it helps with debugging, code readability, and maintenance since changes to that block of code only need to happen in one place. </p>

	<p>Using a procedure that inputs a <span class="hover vocab yui-wk-div" data-id="parameters">parameter</span> allows the programmer to have even more control over the execution of the parameter. You are able to take in a specific input to be used inside of the procedure in order to produce a different output. Parameters are especially useful if you have very similar code with some variance. Parameters allow you to manage the complexity of your code by allowing your procedure more control over the input and output. </p>
	
.. youtube:: ct9Cf7y73g0
	:width: 650
	:height: 415
	:align: center

.. raw:: html	
	
	<h4>Incrementing a Variable</h4>
	<p>The totalCalorieIntake variable should increase whenever the user logs a food they have eaten. You can use the global variable to track the total calories and add the new number of calories each time the user logs their food. The algorithm for this is: </p>
	<p align="center"> totalCalorieIntake = totalCalorieIntake + the calorie value of the food being logged
	</p>
	
.. youtube:: O1q63nAUNc8
	:width: 650
	:height: 415
	:align: center

.. raw:: html

	<h3>Enhancements</h3>
    <ol>
	<li>Program an intent that acts as a reset command for Alexa to reset the totalCalorieIntake variable at the end of the day.</li>
	<li>Since there are limited meal options available, space travelers might get bored and have a hard time selecting their breakfast meal. Create another intent as a random option where <a href="https://docs.google.com/document/d/14jWn8GyMpHwFdFqNbE4ZRc4rnXR_WtDsIai97U6TGwo/" target="_blank">Alexa will decide</a> on the breakfast meal to eat.</li>
	<li>Looking back to your Eat Intent. If the user says they will eat a food item from the list of foods, that food item’s calories are added to the daily calorie eaten total. Test what happens when you respond with a food that is not in your food list. As is, if the user eats that food, it would not be counted toward their daily <span class="hover vocab yui-wk-div" data-id="calorie intake">calorie intake</span>. Modify your procedure to include selection (i.e. an if/else block) that would make your intent produce two possible outputs: one for food that is in the list and one for food not in the list. (Hint: the List drawer contains a block that can be used to check if an item is in a list.)</li>
	<li>Right now the foods in the list are only breakfast options. Update your Options Intent to have a slot that listens for the meal the user wants to know food options for. Add in two more lists (one for lunch options and another for the corresponding lunch calories).</li>
	<li>Program an intent with a slot for setting the daily calorie total for the user.</li>
	<li>Challenging: Create another intent where Alexa reads only the breakfast items with calorie amounts greater than 200. What is your new intent and how will the utterances change from the first enhancement? </li>
	<li>You may have noticed that finding the calorie value of the food eaten is a complex piece of code that is repeated multiple times in the skill. This is a great place to use a <b>procedure with a result</b> also known as a <b>function</b>. Refactor your code to use a function to calculate the calorie value of the food item.</li>
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

    <ul>
	<li><a href="https://www.businessinsider.com/do-astronauts-age-slower-than-people-on-earth-2015-8" target="_blank">Do astronauts age differently than people on earth?</a></li>
	<li><a href="https://www.scientificamerican.com/article/how-does-spending-prolong/" target="_blank">Prolonged effects of microgravity on astronauts</a></li>
	<li>What do astronauts eat for breakfast? <a href="https://www.youtube.com/watch?v=AGR3FiEkBwA" target="_blank">Eat Like An Astronaut</a>; <a href="https://www.myrecipes.com/extracrispy/what-do-astronauts-eat-for-breakfast" target="_blank">Breakfast in Space</a></li>
	</ul>
    
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
	<span class="hover vocab yui-wk-div" data-id="arguments">arguments</span>
	<br/>
	<span class="hover vocab yui-wk-div" data-id="calorie intake">calorie intake</span>
	<br/>
	<span class="hover vocab yui-wk-div" data-id="index">index</span>
	<br/>
	<span class="hover vocab yui-wk-div" data-id="list">list</span>
	</td>
	<td>
	<span class="hover vocab yui-wk-div" data-id="microgravity">microgravity</span>
	<br/>
	<span class="hover vocab yui-wk-div" data-id="parameters">parameters</span>
	<br/>
	<span class="hover vocab yui-wk-div" data-id="parallel lists">parallel lists</span>
	<br/>
	<span class="hover vocab yui-wk-div" data-id="procedural abstraction">procedural abstraction</span>
	<br/>
	<span class="hover vocab yui-wk-div" data-id="slot">slot</span>
    </td>
    </tr>
    </tbody></table>
	
    <h3>Check Your Understanding</h3>
    <p>Complete the following self-check exercises. Please note that you should login if you want your answers saved and scored. In addition, some of these exercises will not work in Internet Explorer or Edge browsers. We recommend using Chrome.</p>
    
    <p>{ {insert self-check questions here} }</p>

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1HNTuieyef7DRTccR6N7cwZpmaVemRYfwoNMWVw6XREo/copy" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vS3CLqWF_oybBjSSlXdCCnkCJ6hkUaefuO82XO4_wmPxwwWSvSHYokDAKvzB_s65kP-EACxieR35gCz/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    </div>
    </img></div>