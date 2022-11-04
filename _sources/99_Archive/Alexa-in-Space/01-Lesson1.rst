.. raw:: html

   <div class="logo-header"  id="student-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>
   
Lesson 1 - Introduction to AI in Space
================================

.. raw:: html

    <style>    td { text-align: left; padding: 5px;}</style>


.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
        
        generateSummary(EKmapping['A.01']); /* Change the lesson number */
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
    <tr><td valign="top" colspan=2><p>In this lesson you will learn about <span class="hover vocab yui-wk-div" data-id="artificial intelligence (AI)">artificial intelligence (AI)</span>. Although AI has been around since the 1950s, it is widely recognized now as one of the fastest-growing fields in technology. From ELIZA to <span class="hover vocab yui-wk-div" data-id="Alexa">Alexa</span>, AI has become something we interact with every day, and will be a part of our daily life for the foreseeable future. Navigation apps, 3D photography, facial recognition, and smart assistants are just a few of the everyday uses for AI, and you’ll be introduced to more examples. But how can we define AI? And why is the use of AI being extended into space?</p></td></tr>
    <tr><td valign="center"><img src="../_static/assets/img/AlexaInSpace.png" style="float:left"/>
    <td valign="top">
       <div><b>Learning Objectives:</b>&nbspI will learn to</div>
       <ul>
	   <li>Explain the importance of data in the process of developing <span class="hover vocab yui-wk-div" data-id="artificial intelligence (AI)">AI</span> and <span class="hover vocab yui-wk-div" data-id="machine learning">machine learning</span>, and recognize how data can lead to <span class="hover vocab yui-wk-div" data-id="bias">bias</span> in AI. </li>
	   <li>Explain how <span class="hover vocab yui-wk-div" data-id="Alexa">Alexa</span> is an example of <span class="hover vocab yui-wk-div" data-id="artificial intelligence (AI)">AI</span> </li>
		<li> Identify how Alexa can be used to perform basic tasks. </li>
		<li> Describe why AI could be useful in space and other contexts. </li>

       </ul>
       <div><b>Language Objectives:</b>&nbspI will be able to</div>
       <ul>
		<li>Use target vocabulary such as <span class="hover vocab yui-wk-div" data-id="artificial intelligence (AI)">artificial intelligence (AI)</span>, <span class="hover vocab yui-wk-div" data-id="machine learning">machine learning</span>, <span class="hover vocab yui-wk-div" data-id="machine learning">bias</span>, <span class="hover vocab yui-wk-div" data-id="Alexa">Alexa</span> and <span class="hover vocab yui-wk-div" data-id="microgravity">microgravity</span> to describe the impact that AI has had on society out loud and in writing, with the support of vocabulary notes from this lesson.</li>
       </ul>
    </td>
    </tr>
    </tbody></table>
    <br/>    

Learning Activities
--------------------

.. raw:: html

	<ul align="center" style="list-style: none; margin: 0; padding: 0; background: lightgrey">
	<li style="display: inline"><a href="https://docs.google.com/presentation/d/1sUbh5EfF6WqKufugb2J2shWlx0GZsGZErjIr6dGd3Y4/" target="_blank" title="">Slides</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://www.youtube.com/watch?v=-eQXJ6hdy7c" target="_blank">video</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://docs.google.com/document/d/1oJVBhjrigBKQVC4gpA4w9mSFpHebPcJeRuuDRP7N1T8/copy" target="_blank">Worksheet - Guided Notes</a></li>
	</ul> 
	
    <p>
    <h3>Hook Activity</h3>
    <p><span class="hover vocab yui-wk-div" data-id="artificial intelligence (AI)">Artificial intelligence (AI)</span> has made its way into popular culture through movies, literature, and commerce. Examples include Star Wars, Marvel movies, Siri, <span class="hover vocab yui-wk-div" data-id="Alexa">Alexa</span> and literary works such as I, Robot. Can you think of others? <b>Discussion:</b> share your ideas with the class. </p>
	
	<h3>Lecture</h3>
    <p>This lecture is based on the slides by Jessica Van Brummelen, Tommy Heng, and Viktoriya Tabunshchyk from MIT. </p> 

.. youtube:: -eQXJ6hdy7c
	:width: 650
	:height: 415
	:align: center

.. raw:: html

	<p>AI, in general, is a computer program designed to simulate human intelligence. AI can be difficult to define in detail, but there are <b>5 Big Ideas</b> that can help us to understand it.</p>
	
	<p align="center"><img src="https://i0.wp.com/ai4k12.org/wp-content/uploads/2020/07/AI4K12_Five_Big_Ideas_Graphic-1160958986-1594515160405.png?ssl=1" width="400" height="400" alt="5 Big Ideas of AI Wheel"></p>
	<p align="center"><i>Source: <a href="https://ai4k12.org/resources/big-ideas-poster/" target=_blank">https://ai4k12.org/resources/big-ideas-poster</a></i></p>
	
	<ol>
	<li><b>Perception</b> - Computers can use sensors to perceive information about their environment, and the programs that run them can use this data to create meaning.</li>
	<li><b>Representation and Reasoning</b> - Once information has been gathered, it can be used to create a data structure that represents the problem, and reasoning algorithms can be applied to solve it. While these reasoning algorithms can be very complex, they are not “thinking” as a human thinks.</li>
	<li><b>Learning</b> - With enough data (think thousands or, more likely, millions of input samples), computer algorithms can make inferences about patterns in data that allow it to “learn” something new. </li>
	<li><b>Natural Interaction</b> - An “intelligent agent” must be able to interact with humans. This means not only mimicking appropriate human responses, but also recognizing human expressions, emotions and intentions. These can all be very complex to interpret when one takes into account differences in language, culture, and social conventions.</li>
	<li><b>Societal Impact</b> - As AI becomes more of an influence on our daily lives, <span class="hover vocab yui-wk-div" data-id="bias">biases</span> in the data and/or the algorithms can lead to flawed learning. This flawed learning can lead to unintentional discrimination, marginalization and under- or overrepresentation of certain groups of people. Different types of bias that can affect the reliability of intelligent agents are reporting bias, selection bias, group attribution bias, and implicit bias. The likelihood of bias in AI means that we need to be keenly aware of the need for criteria to ensure that the models are ethical and have a beneficial impact on society.</li>
	</ol>
	
	<h4>ACTIVITY: Is it AI?</h4>
	<p>Consider <a href="https://docs.google.com/presentation/d/e/2PACX-1vSKBRcT4EiUe07l0yxIKH6oi0xgnJnpkPffkVgvFvhlponEY8tjbeflLef5nr_OxtAPVNKhcfULMc4y/pub?start=true&loop=false&delayms=3000&slide=id.g8cab8164ef_0_1055" target=_blank"> these examples</a>. <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSKBRcT4EiUe07l0yxIKH6oi0xgnJnpkPffkVgvFvhlponEY8tjbeflLef5nr_OxtAPVNKhcfULMc4y/embed?start=false&loop=false&delayms=3000" frameborder="0" width="650" height="415" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
	
	<br/> In a small group of 2-3 students, discuss and document whether these examples can be considered AI. Document your group’s answers on <a href="https://docs.google.com/document/d/1oJVBhjrigBKQVC4gpA4w9mSFpHebPcJeRuuDRP7N1T8/copy" target="_blank">this worksheet</a>. The following questions may be helpful to consider:</p>
	<ul>
	<li>Does the example perceive/understand its environment?</li>
	<li>Does the example continue to learn?</li>
	<li>Does the example make plans or decisions on its own?</li>
	<li>Does the example interact with its environment?</li>
	<li>Who is doing the thinking? Where is the intelligence - with the humans who programmed it or with the device/program?</li>
	</ul>

	<p>Taking it a step further, if it’s AI, can it be considered “conversational AI?”</p>
	<ul>
	<li>Does the example understand natural (human) language?</li>
	<li>Can the example respond in natural (human) language?</li>
	</ul>
	
	<h3>Video: What is Machine Learning?</h3>
	<p>Did you realize it is difficult to know if a machine is learning?  Watch this short video (2 minutes) introducing <span class="hover vocab yui-wk-div" data-id="machine learning">machine learning</span>.</p>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/QghjaS0WQQU?controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    
	<h3>Alexa as AI</h3>
    <p>Amazon’s smart assistant, Alexa, uses AI to build on the skills it already knows, and <span class="hover vocab yui-wk-div" data-id="speech recognition">speech	recognition</span> (an application of AI technology that interprets and carries out spoken commands and/or aims to identify an individual based on their speech patterns) and <span class="hover vocab yui-wk-div" data-id="speech synthesis">speech synthesis</span> (the artificial production of human speech) to interact with humans to improve their productivity. This video offers a glimpse into Alexa’s capabilities.</p>
	
.. youtube:: V9Zkw-0SDZU
	:width: 650
	:height: 415
	:align: center

.. raw:: html

	<h4>ACTIVITY: Alexa as AI</h4>
	<p>Reflecting independently, brainstorm 1-2 ways that <span class="hover vocab yui-wk-div" data-id="Alexa">Alexa</span> could help you be more productive in the classroom. Document your reflections in your portfolio about the following:</p>
	<ul>
	<li>How would you ask Alexa to help you with that particular task?</li>
	<li>How might Alexa “learn” to help you with that skill if you continue to use it regularly?</li>
	<li>What problems might you encounter as you attempt to use Alexa for this purpose?</li>
	</ul>
	
	<h3>Space Travel</h3>
    <p>Now that you understand the vast capability of AI to help with productivity here on Earth, you can appreciate how this technology is being used in space.</p>
	
	<p>We have been sending people into space since 1961, when Alan Shepard became the first US man in space. Most of the people who have travelled outside of the Earth’s atmosphere have been trained astronauts, but there have been exceptions. In 1985 US Senator Jake Garn flew on a seven day space shuttle mission. Recently, in September of 2021, the Inspiration4 flight saw four civilians orbit the earth for three days. Check out William Shatner’s reaction to his trip to space!</p>

.. youtube:: Q9UzJTNKJ9A
	:width: 650
	:height: 415
	:align: center

.. raw:: html

	<p>Referred to by some as “space tourism,” more civilian space travel seems to be on the horizon. Independently explore these resources to learn more about space tourism.</p>
	
	<ul>
	<li><a href="https://www.businessinsider.com/spacex-inspiration4-first-space-tourists-return-to-earth-2021-9" target="_blank">https://www.businessinsider.com/spacex-inspiration4-first-space-tourists-return-to-earth-2021-9</a></li>
	<li><a href="https://www.space.com/space-tourism-is-finally-ready-for-launch" target="_blank">https://www.space.com/space-tourism-is-finally-ready-for-launch</a></li>
	<li><a href="https://www.space.com/space-tourism-risk-safety-regulations " target="_blank">https://www.space.com/space-tourism-risk-safety-regulations </a></li>
	</ul>
	
	<p>People travel into space for various reasons, including scientific discovery, economic benefit, national security, and curiosity. Whatever the reason for space travel, all people encounter an environment very different from the one here on Earth. The further away from Earth one gets, the less effect gravity has on people and other objects. The name for the phenomenon of being affected by only a small amount of gravity is <span class="hover vocab yui-wk-div" data-id="microgravity">microgravity</span>. As astronauts and space tourists go through their daily routines and responsibilities, they must find ways to cope with objects not responding as they would on Earth and their own physiology (the body and how it works) behaving differently. The resources above offer some insight into just how different daily life is in space with the effects of microgravity. </p>
	
	<h4>ACTIVITY: Exploring Microgravity</h4>
	<p>Independently explore one of these two resources to learn more about <span class="hover vocab yui-wk-div" data-id="microgravity">microgravity</span> in space. Identify at least 2-3 ways that microgravity impacts daily life. Then, share what you learned with a shoulder partner.</p>
	
	<ul>
	<li><a href="https://www.nasa.gov/audience/forstudents/k-4/stories/MicrogravityImageGallery.html" target="_blank">NASA Microgravity Image Gallery</a></li>
	<li><a href="https://youtu.be/yqHiShYGkZQ " target="_blank">Microgravity Explained Video</a></li>
	</ul>
	
	<h3>AI in Space</h3>
    <p>One way for humans to deal with the difficulties of space travel is to rely on AI platforms like Alexa for help. For the reasons mentioned in the previous activity, AI is uniquely suited to assisting space travelers in monitoring their equipment, health statistics, daily tasks, navigation and more. Each role, from Commander to Flight Engineer, Science Officer to individual space flight participants could benefit. <b>Maybe the best ways to use Alexa in space haven’t even been discovered yet…maybe that will be up to you! At the end of this unit, you’ll get the opportunity to develop your own Alexa skill!</b></p>

	<p><a href="https://drive.google.com/file/d/1pnvRuDFg-RfVgIm_H6teWFFxi5vVX8Hl/view" target="_blank">Here</a> is just an idea about how AI could be used in space in the future! (<a href="https://docs.google.com/document/d/1bZuXdUXPrvLz_FuBCh4qiKnOTI0kuYDiBvQbh9oCGk4/" target="_blank">Audio transcript</a>)</p>

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>
	
	<p>
	<audio controls>
	<source src="../_static/assets/img/ExampleStudentProduct_EpsilonEridani.mp3" type="audio/mpeg">
	Your browser does not support the audio element.
	</audio>
	</p>

    
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
	<li><a href="https://web.njit.edu/~ronkowit/eliza.html" target="_blank">ELIZA was one of the first natural language processing programs.</a></li>
	<li><a href="https://deepmind.com/" target="_blank">DeepMind</a> is a project run by Google and a team of engineers and computer scientists working to “help society find answers to some of the world’s most pressing and fundamental scientific challenges.</li>
	<li><a href="https://www.lucidpix.com/10-examples-of-artificial-intelligence-in-our-everyday-lives/" target="_blank">Curious about AI in our everyday lives?</a></li>
	<li>AI can be used for creating <a href="https://www.zdnet.com/article/nixons-grim-moon-disaster-speech-is-a-now-a-warning-about-the-deepfake-future/?ftag=TRE-03-10aaa6b&bhid=%7B%24external_id%7D&mid=%7B%24MESSAGE_ID%7D&cid=%7B%24contact_id%7D&eh=%7B%24CF_emailHash%7D" target="_blank">“deep fake” videos</a>, which can be confusing and misleading for those who are unaware that they are not real.</li>
	<li>Build your own voice AI with <a href="https://wiki.almond.stanford.edu/" target=_blank">Stanford's Genie.</a></li>
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
	<br/><span class="hover vocab yui-wk-div" data-id="artificial intelligence (AI)">artificial intelligence (AI)</span>
    <br/><span class="hover vocab yui-wk-div" data-id="bias">bias</span>
	<br/><span class="hover vocab yui-wk-div" data-id="machine learning">machine learning</span>
	<br/><span class="hover vocab yui-wk-div" data-id="microgravity">microgravity</span>
    <br/><span class="hover vocab yui-wk-div" data-id="speech recognition">speech	recognition</span>
	<br/><span class="hover vocab yui-wk-div" data-id="speech synthesis">speech synthesis</span>
    </td>
    </tr>
    </tbody></table>
	
    <h3>Check Your Understanding</h3>
    <p>Complete the following self-check exercises. Please note that you should login if you want your answers saved and scored. In addition, some of these exercises will not work in Internet Explorer or Edge browsers. We recommend using Chrome.</p>
	
.. mchoice:: mcsp-alexa-1-1
    :practice: T
    :answer_a: Perceive information about its environment
    :feedback_a: 
    :answer_b: Create a representation of the problem at hand, and draw reasonable conclusions based on the data
    :feedback_b: 
    :answer_c: Learn from additional data
    :feedback_c: 
    :answer_d: Interact with humans
    :feedback_d: 
    :answer_e: All of the above
    :feedback_e: Without each of these, a computer program would not be considered AI, it would just be a program.
    :correct: e

    The best definition of AI would be a computer program with the ability to:


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


.. mchoice:: mcsp-alexa-1-2
    :random:
    :practice: T
    :answer_a: True 
    :feedback_a: Unfortunately, AI is prone to bias due to problems with the data, algorithms, or both. We have to be very careful to identify possible sources of bias before they impact society.
    :answer_b: False 
    :feedback_b: That's right!
    :correct: b

        Due to the fact that AI is a computer program with no opinions, there is no possibility of bias in its performance.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>
	
	
.. fillintheblank:: mcsp-Alexa-1-3
    :casei:

    The force that affects human ability to function and interact with objects in space is called ___________. (Spelling counts)

    |blank|

    - :Microgravity: Correct! Although not technically “Zero” gravity, microgravity makes people and objects appear to be weightless.
      :Gravity: Close - try again.

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>
    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/12IxFUadeAoyMYWO9ueI1PgjFLohu0aB3tEZ_0X8WWVc/copy" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/12IxFUadeAoyMYWO9ueI1PgjFLohu0aB3tEZ_0X8WWVc/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    </div>
    </img></div>