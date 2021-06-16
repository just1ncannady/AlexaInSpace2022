.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Artificial Intelligence and Machine Learning
============================================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
        generateSummary(EKmapping['7.07']);
        generateHovers();
        Tipped.create('.vocab', function(element) {
        var vocab = $(element).data('id');
        return vocabulary[vocab];
          }, {
            cache: false,
              position: 'topleft'
              });
      });
    
    /*  var vocabulary = { 
        "artificial intelligence (AI)":"A branch of computer science that works on creating machines and programs that exhibit human-like intelligence.",
        "machine learning":"Algorithms that learn intelligent behavior from lots of training data.",
         "neural network":"A computer system modeled on simple neurons in the human brain.",
        "back propagation":"Back propagation is an algorithm that repeatedly adjusts the connections (weights) between the nodes in the neural network",
        "deep learning":"A type of very successful machine learning algorithm using neural networks with many layers to learn data representations on its own from massive amounts of data.",
      };      */
    </script>
    <h3 id="est-length">Time Estimate: 45 minutes</h3>

Introduction and Goals
-----------------------

.. raw:: html

    <p><h3>Can a computer recognize your doodles?</h3>
    <p><b><i>Artificial intelligence (AI)</i></b> is sometimes described as getting a computer to do complex tasks that humans find easy.  Examples would be walking, seeing, and understanding speech.  These activities, which come naturally to us, are very difficult to develop traditional step-by-step algorithms for.</p>
    <p>But AI researchers have developed an approach known as <i><b><span class="hover vocab yui-wk-div" data-id='machine learning'>machine learning</span></b></i> that enables computers to perform these complex tasks.  With <span class="hover vocab yui-wk-div" data-id='machine learning'>machine learning</span> a computer <i><b>learns</b></i> how to perform a task or solve a problem not by being given a traditional program to solve the problem, but by being given lots of examples of correct and incorrect solutions to the problem.  

Learning Activities
--------------------

.. raw:: html
    
    </p><a href="https://quickdraw.withgoogle.com/" target="_blank"><img src="../_static/assets/img/FlagDoodle.png" style="float:left;" width="200"/></a>To give you a sense of what such a <i>trained</i> computer can do, here's an interactive Google application that has learned (and is continuing to learn) how to recognize doodles -- i.e., free-hand drawn images of typical objects. Certainly, the ability to recognize a person's doodles, is something we humans do quite easily.  But it is a skill that would be very nearly impossible to specify by means of a traditional algorithm.</p>
    <p>Give it a try yourself!  Click on the <a href="https://quickdraw.withgoogle.com/" target="_blank">flag doodle</a> here to see how well the computer can recognize your doodles. 
    </p>
    <h3>Video: What is Machine Learning?</h3>
    <p>Hopefully you enjoyed that activity and are curious now about <span class="hover vocab yui-wk-div" data-id='machine learning'>machine learning</span>.  The following short (7:48) tutorial was created by an undergraduate student from Texas A&amp;M University. It is one of many good tutorials that you can find online. 
      
    
.. youtube:: DG5-UyRBQD4
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </p>
    <p>
      As you learned, <i><span class="hover vocab yui-wk-div" data-id='machine learning'>machine learning</span></i> is based on an algorithm called <i><span class="hover vocab yui-wk-div" data-id='back propagation'>back propagation</span></i> that repeatedly adjusts the connections (weights) between the nodes in the <i><span class="hover vocab yui-wk-div" data-id='neural network'>neural network</span></i>. To summarize, the <span class="hover vocab yui-wk-div" data-id='machine learning'>machine learning</span> algorithm consists of the following steps:
    </p><h4>Machine Learning Algorithm</h4>
    <ul>
    <li>Initialize the <span class="hover vocab yui-wk-div" data-id='neural network'>neural network</span> by assigning random weights to connections between its nodes.</li>
    <li>Repeat until there is little to no difference between the network's actual outputs and the desired outputs.</li>
    <ul>
    <li>Present the <span class="hover vocab yui-wk-div" data-id='neural network'>neural network</span> with a set of inputs.</li>
    <li>Compare the network's output with the desired output and calculate the difference (the error).</li>
    <li>Adjust the weights on the hidden nodes using <i><span class="hover vocab yui-wk-div" data-id='back propagation'>back propagation</span></i>.
        </li></ul>
    </ul>
    <p>
      By performing these steps for lots of examples, the network will eventually be trained to associate its inputs with the desired outputs. As the tutorial explained, neural networks are <b>slow learners</b>.  But they have improved over time and as you will experience in this next activity, some networks can be trained now with dozens of examples (rather than "millions" as the video suggested).
    </p>
    <h3>Important Qualifications</h3>
    <p>Don't be misled by this basic overview of simple neural networks and our simple explanation of <span class="hover vocab yui-wk-div" data-id='machine learning'>machine learning</span>.  Designing and implementing successful neural networks and <span class="hover vocab yui-wk-div" data-id='machine learning'>machine learning</span> algorithms to address problems like speech recognition (Siri, Alexa), computer vision (Face Recognition software), natural language understanding (Google Translate), and the many other tasks that are simple and natural for humans is an extremely complex and challenging research field. </p>
    <p>It has taken AI researchers many years of hard work to accomplish some of the examples you are seeing in this lesson.  In contrast to the simple networks shown in the video, current approaches AI are based on <i><b><span class="hover vocab yui-wk-div" data-id='deep learning'>deep learning</span></b></i> networks, which are networks that contain multiple layers in between the input and output layers. The additional <i>hidden</i> layers enable the network to learn abstract representations.</p>
    <p>Now, let's have some fun with AI by training our own <span class="hover vocab yui-wk-div" data-id='neural network'>neural network</span> using Google's Teachable Machine software.</p>
    <h3>Activity: Google's Teachable Machine Experiments</h3>
    
    In this activity you will use your browser to train a <span class="hover vocab yui-wk-div" data-id='neural network'>neural network</span> to associate inputs from the camera on your computer or tablet or phone camera with certain sounds and images.  Before you get started, here's a short (3:20) video demo that shows you how it works. 
    
    
.. youtube:: 3BhkeY974Rg
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <p>As you saw in the video, you can train a simple <span class="hover vocab yui-wk-div" data-id='neural network'>neural network</span> to distinguish between three classes: green, purple, and orange.  The network will associate a certain inputs from your video camera (hand up, funny face) with certain GIF images (cat, dog) or sounds (hello, hey). Once you've trained the network to make the desired associations, you have created a <i><b>model</b></i>. </p>
    <p>Now it's your turn to try it. If your computer does not have a camera, use your tablet or phone for this activity. When you click on the <a href="https://teachablemachine.withgoogle.com/v1/" target="_blank">link to the Teachable Machine Version 1</a>, you should see the following interface (note there is also a version 2 that you could try by deleting /v1 from the URL):
      <br/>
    <a href="https://teachablemachine.withgoogle.com/v1/" target="_blank"><img src="../_static/assets/img/TeachableMachine.png" style="float:center;" width="400"/></a>
    <br/>
      
      Here are some exercises and experiments to try:</p>
    <ol>
    <li>First, just to make sure everything is working properly, do the tutorial by clicking on the "Let's Go!" button.  The tutorial will lead you through creating the model that you saw in the demo video (hand up, funny face).</li>
    <li>Next, tweak the model by replacing the GIFs with sounds, creating your own sounds.</li>
    <li>Next, customize a model with your own inputs and outputs.</li>
    <li>Here's an experiment to try:  Does it take more training cycles to train a model to distinguish between (left-hand-up, right-hand-up) than a model that distinguishes between (hand-up, no-hand-up)? </li>
    <li><b>Facial recognition?</b> Pair up with one or two of your classmates and explore whether the network can be trained to distinguish between your faces.
      </li><li>Design your own experiment(s) with or without classmates.  For example, can you find two or three inputs that the machine cannot distinguish between no matter how many learning cycles you do? 
    </li></ol>
    <h3>Negative Impacts: Bias in Algorithms</h3>
    <p>How do you explain the following riddle? 
      
      </p><blockquote><b>A father and son are in a horrible car crash that kills the dad. The son is rushed to the hospital. Just as he’s about to go under the knife, the surgeon says, 'I can’t operate. That boy is my son.'</b>
    </blockquote>
    <p>If you were puzzled by that riddle, you are not alone. The vast majority of people are. Check out <a href="https://www.wtsp.com/article/news/local/challenging-stereotypes-in-the-workplace-with-a-riddle/450749550" target="_blank">this news report</a> in which a reporter put the riddle to 15 Floridians, only two of whom figured it out.
    </p>
    <p>As the news story illustrated, we humans are full of unconscious biases -- assumptions and generalizations we've learned just by growing up.  Some of these have been embedded in our languages. Consider, for example, all of the various "man" terms for occupations that today at least aren't just for males:  "mailman", "fireman", "repairman", "foreman". 
    </p>
    <p>Can an algorithm be biased? Perhaps you might think algorithms cannot be biased because they are not human. But algorithms (and computer interfaces and all other aspects of computer systems) are designed and implemented by humans.  So it's perfectly reasonable to expect that apps and computer programs would display some of the biases that their designers have.</p>
    <p> Computing innovations can reflect existing human biases because of biases written into the algorithms at all levels of software development or biases in the data used by the innovation. <span class="hover vocab yui-wk-div" data-id='Machine learning'>Machine learning</span> and data mining have enabled innovation in medicine, business, and science, but information discovered in this way could be biased depending on the data source and the information can also be used to discriminate against groups of individuals. Programmers need to take action to reduce bias in algorithms used for computing innovations as a way of combating existing human biases.</p>
    <h3>Activity: Bias in an AI Program</h3>
    <p>Here's a little experiment you can do to see an example of bias in an AI program.  <a href="https://translate.google.com/" target="_blank">Google Translate</a> is a <span class="hover vocab yui-wk-div" data-id='machine learning'>machine learning</span> application that Google has created that automatically translates words or sentences from one language to another. It learns languages <a href="https://en.wikipedia.org/wiki/Google_Neural_Machine_Translation" target="_blank">by looking at millions of examples</a>.</p>
    <p>
      Type the English sentence "The nurse is happy" into <a href="https://translate.google.com/" target="_blank">Google Translate</a> and translate into Spanish.  It will translate it into "La enferma estaba feliz," which assumes that the nurse is female (the term "la enferma" is feminine is Spanish).  Now change the English sentence to "The nurse is happy because today is <b>his</b> day off"  and translate that into Spanish.  You should get "La enfermera estaba feliz porque es su día libre," which still assumes the nurse is a female.  Now switch the order, translating from Spanish to English and translate "La enfermera estaba feliz porque es su día libre" to English. You will get "The nurse was happy because it's <b>her</b> day off."</p>
    <p>So, Google Translate got the translation wrong because it has allowed some bias to creep into its peformance.  While that was a fairly mild example of the type of bias that can occur, this has become a significant issue in <span class="hover vocab yui-wk-div" data-id='machine learning'>machine learning</span>.  Perhaps the most famous example of what can go very wrong was Micrsoft's disasterous experiment with Tay, its <a href="https://www.youtube.com/watch?v=Lr4yi9onykg" target="_blank">chatbot that was released on Twitter</a> and quickly learned a wide range of racist, sexist, and anti-semitic views.</p>
    <p>For more information about bias in AI algorithms, you may want to watch:
    </p><ul>
    <li>a Ted Talk video on <a href="https://www.youtube.com/watch?v=UG_X_7g63rY" target="_blank">Bias in Facial Recognition</a> by Joy Buolamwini,</li>
    <li><a href="https://www.youtube.com/watch?v=7lpCWxlRFAw" target="_blank">a report on police crime prediction software and bias</a></li>
    </ul>
    <h3>Optional: App Inventor Artificial Intelligence Tutorials</h3>
    
    Check out these <a href="http://appinventor.mit.edu/explore/ai-with-mit-app-inventor" target="_blank">AI tutorials in MIT App Inventor</a>. The Image Classifier tutorials require an AI extension that some mobile devices can use (<a href="http://appinventor.mit.edu/explore/ai-compatible-devices" target="_blank">list of compatible devices and an apk</a> that you can test on your device to see if it can use these extensions).  The Therapist Bot tutorial and the Rock-Paper-Scissors Tutorials do not require this AI extension and can be implemented on any device. They are a lot of fun! 
    
    
Summary
--------

.. raw:: html

    <p>
    In this lesson, you learned how to:
      <div id="summarylist">
    </div>
    
Still Curious?
---------------

.. raw:: html

    <p>
    <p> There are lots of interesting videos and presentations online to help you learn more about AI and the impact it is having in the world.  Here's a selection:
      </p><ul>
    <li>In this video two Googlers, Nat and Lo, interview a couple of Google AI researchers who describe <a href="https://www.youtube.com/watch?time_continue=1&amp;v=bHvf7Tagt18" target="_blank">how <span class="hover vocab yui-wk-div" data-id='machine learning'>machine learning</span> works</a>. This video was made as part of their "20% project".  One of the cool features of working at Google and other technology companies is that employees get to spend part of their time (1 day per week in this case) working on projects that they themselves choose.   
        </li>
    <li>The <a href="https://www.youtube.com/watch?time_continue=1&amp;v=tiwVMrTLUWg" target="_blank">Google Self-Driving Car</a> is an example of the being done by car industry researchers to create fully autonomous vehicles.  As the video points out, an autonomous vehicle is much different than the computer-assisted vehicles that are currently available today.  
        </li>
    <li>Computer vision is a long-standing AI research area. In this TED talk, Wei-wei Li from Stanford University describes how she used <span class="hover vocab yui-wk-div" data-id='machine learning'>machine learning</span> and crowd source to to <a href="https://www.youtube.com/watch?time_continue=1&amp;v=tiwVMrTLUWg" target="_blank">teach a computer to understand pictures</a>.
        </li>
    <li>Here is a Ted Talk video on <a href="https://www.youtube.com/watch?v=UG_X_7g63rY" target="_blank">Bias in Facial Recognition</a> by Joy Buolamwini and another on <a href="https://www.ted.com/talks/cathy_o_neil_the_era_of_blind_faith_in_big_data_must_end" target="_blank">Blind Faith in Big Data Must End</a> by Cathy O'Neil.</li>
    <li>This <a href="https://www.youtube.com/watch?v=Fq1SEqNT-7c" target="_blank">video</a> is on the use of Facial Recognition in China and privacy concerns.</li>
    <li>This is <a href="https://www.youtube.com/watch?v=7lpCWxlRFAw" target="_blank">a report on police crime prediction software and bias.</a></li>
    <li>The history of Artificial Intelligence goes back to the 1950s. You can read about it <a href="https://en.wikipedia.org/wiki/Artificial_intelligence" target="_blank">here</a>. One interesting feature of this history is the so-called <i>AI effect</i>, whereby the problems that make up the discipline have changed over time.  For example, the ability to recognize numbers and characters -- <i>optical character recognition</i> -- used to be considered an AI problem. But today it has become a routine part of ATM machines and other computers.  Another interesting AI area that has evolved is chess playing.  In the 50s some researchers predicted that a computer would be able to beat the best human chess player.  For years the failure of computers to beat top humans was used as "proof" that AI would never succeed.  This changed in 1997 when an IBM computer known as Deep Blue <a href="https://en.wikipedia.org/wiki/Deep_Blue_versus_Garry_Kasparov" target="_blank">beat Gary Kasparov</a>, the reigning world chess champion, in a six game match.  Since then computer chess programs have only gotten better and humans are no longer competitive against chess programs, which today <a href="https://en.wikipedia.org/wiki/World_Computer_Chess_Championship" target="_blank">have their own computer-only championships</a>.   
    </li>
    <li>The <a href="https://machinelearningforkids.co.uk/" target="_blank">machinelearningforkids.co.uk/</a> site uses IBM's <span class="hover vocab yui-wk-div" data-id='machine learning'>machine learning</span> processors online to train and use models in Scratch and in an App Inventor extension. Using these materials does require setting up accounts with IBM and some set up time.</li> </ul>

Self-Check
-----------

.. raw:: html

    <p>
    <p>Here is a table of the technical terms we've introduced in this lesson. Hover over the terms to review the definitions.</p>
    <table align="center">
    <tbody>
    <tr>
    <td><span class="hover vocab yui-wk-div" data-id="artificial intelligence (AI)">artificial intelligence</span>
    <br/><span class="hover vocab yui-wk-div" data-id="machine learning">machine learning</span>
    <br/><span class="hover vocab yui-wk-div" data-id="neural network">neural network</span>
    <br/><span class="hover vocab yui-wk-div" data-id="back propagation">back propagation</span>
    <br/><span class="hover vocab yui-wk-div" data-id="deep learning">deep learning</span>
    </td>
    </tr>
    </tbody>
    </table>
    
.. mchoice:: mcsp-7-7-1
    :random:
    :practice: T
    :answer_a: Computer vision
    :feedback_a: Yes that's one.
    :answer_b: Natural language understanding
    :feedback_b: That's one example but there are others.&nbsp;
    :answer_c: Speech recognition
    :feedback_c: That's one example but there are others.&nbsp;
    :answer_d: Robot navigation
    :feedback_d: That's one example but there are others.&nbsp;
    :answer_e: All of the above.
    :feedback_e: That's correct. All of these are examples of AI.
    :correct: e

    Which of the following application areas would be considered an example of artificial intelligence? 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-7-7-2
    :random:
    :practice: T
    :answer_a: an axon
    :feedback_a: An axon is that part of the nerve cell (or neuron) that transmits signals from one neuron to another.
    :answer_b: a neuron
    :feedback_b: Yes, that is correct.&nbsp; The nodes in a neural network are simplified representations of the brain's nerve cells, which are called neurons.&nbsp;
    :answer_c: a synapse
    :feedback_c: In the brain synapses are the junctions between the neurons or nerve cells. 
    :answer_d: A neurotransmitter
    :feedback_d: A neurotransmitter is a chemical substance that causes the transfer of signals from one nerve cell to another across a synapse.&nbsp; It is not directly represented in an artificial neural network.&nbsp;
    :correct: b

    An artificial neural network (ANN) is meant to be a simplified model of the human brain.  In an ANN, each node of the network is meant to represent _____________.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <!--
    &lt;h3&gt;Sample AP CSP Exam Questions&lt;/h3&gt;
    &lt;question instanceid=&quot;6CfVDBYD9eg6&quot; weight=&quot;1&quot; quid=&quot;5150886206636032&quot;&gt;&lt;/question&gt;
    -->
    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/13P2M8j-1CfDMHwS2Oi6xzsjUlwBi8Yjwc6N6B3x1q3M/edit?usp=sharing" target="_blank" title="">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vRoxAxWILNc_nvCafnIUm_DEvyQ8E8U4PXHMcq7pPil43FNLmfhdR4pY2ZmaEvwuACsNehbeyPgw1Hd/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!-- 
    &lt;p&gt;In your portfolio, create a new page named &lt;i&gt;&lt;b&gt;Artificial Intelligence&lt;/b&gt;&lt;/i&gt; under the &lt;i&gt;Reflections&lt;/i&gt; category of your portfolio (we recommend also including the lesson number. Check with your instructor) and answer the following questions:&lt;/p&gt;
      &lt;ol&gt;
        &lt;li&gt;In the Teachable Machine activity, what inputs were easy for the program to learn to distinguish and what inputs were more difficult?
        &lt;/li&gt;
        &lt;li&gt;Search online and identify another application area for AI or machine learning besides the ones described in this lesson. Is this task hard easy for humans but hard for computers to do? &lt;/li&gt;
        &lt;li&gt;In this lesson you saw some examples of &lt;i&gt;gender bias&lt;/i&gt; in a machine translation program.  Identify another form of &lt;i&gt;unconscious bias&lt;/i&gt; and give an example of how it could affect a computer program. Explain how that could be a harmful effect on society, economy, or culture. &lt;/li&gt;
      &lt;/ol&gt; -->
    </div>
    </div>