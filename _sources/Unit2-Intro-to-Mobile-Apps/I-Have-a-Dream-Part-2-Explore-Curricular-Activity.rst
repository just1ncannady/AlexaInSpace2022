.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

I Have a Dream Part 2  Explore Curricular Activity
==================================================

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
        generateSummary(EKmapping['2.04']);
        generateHovers();
        Tipped.create('.vocab', function(element) {
        var vocab = $(element).data('id');
        return vocabulary[vocab];
          }, {
            cache: false,
              position: 'topleft'
              });
      });
     /*
      var vocabulary = { 
        "Computing Innovation" : "includes a program as an integral part of its function. A computing innovation can be physical, non-physical computing software, or non-physical computing concepts. For example, self-driving cars, picture editing software, e-commerce, a mobile app",
        "If/Else" : "Selection or conditional algorithm that allows a program to choose between different actions. ",
        "UI Components" : "Parts of the user interface such as Buttons, Labels, etc.",
        "Horizontal Arrangement" : "A component used to display a group of components laid out from left to right."
       
        
      };*/
    </script>
    <h3 id="est-length">Time Estimate: 45 minutes</h3>

Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <table><tbody>
    <tr><td>
    <iframe allowfullscreen="" frameborder="0" height="400" src="https://www.youtube.com/embed/CykBbRvB0lk" width="400"></iframe><br/>(<a href="http://www.teachertube.com/video/358484" target="_blank">Teacher Tube version</a>)</td>
    <td><b><i>Enhancing I Have a Dream. </i></b>The I Have a Dream app only had one picture and speech, and it didn't allow you to pause the speeches. In part 2, you'll add a speech of Malcolm X to show the contrast of these two great leaders, and you'll code it so each speech can be paused. <br/><br/>
    This tutorial introduces the concept of an <i><b>if-else condition</b></i>, which enables an app (an example of a computing innovation) to ask questions and make decisions-- it's one of the fundamentals of "artificial intelligence".
        
    <p><b>Objectives:</b> In this lesson you will learn to:</p>
    <ul>
    <li>Follow an instructor-led walkthrough to create the <i>I Have a Dream </i>app on a mobile device.
    </li><li>Use a selection <i>if-else</i> block to pause and start the speeches. 
      </li><li>Reuse code efficiently by using the copy and paste blocks feature in App Inventor Blocks Editor
      </li><li>Use a horizontal arrangement to layout buttons side-by-side
      </li><li>Name components in a standard format (description followed by component type, e.g. MalcolmButton)
      </li><li>Understand what a computing innovation is</li></ul>
    <p></p>
    </td></tr></tbody></table>
    

Learning Activities
--------------------

.. raw:: html

    <p><h2></h2><h3>If/Else Selection Blocks</h3>
    <p>The <a href="http://appinventor.mit.edu/explore/ai2/support/blocks/control.html#if" target="_blank">if block</a> in App Inventor can be used to choose between different actions.  All programming languages have something like if blocks, called selection or conditional algorithms, to make decisions based on a condition. In this version of the app, we want to use the buttons to toggle playing and pausing the speeches. When a button is clicked, if that speech is already playing, we want to pause the speech. If it is paused, we want to start playing it again. To do this, we need to use an If block from the Control drawer of the block editor. This block has a blue mutator button where we can drag in an else block to make the block into an If/Else block which will allow us to choose between 2 actions (pause or play) depending on if the speech is already playing.</p><p>
    <img src="../_static/assets/img/IfElseAnimated.gif" style="width:60%"/>
    <br/>
    </p><h3>Tutorial</h3>
    <p><img src="../_static/assets/img/changeEmbeddedTutorial.gif" style="width:180px;float:right;"/>
      To get started, <a href="http://ai2.appinventor.mit.edu" target="_blank">open App Inventor</a>
     in a separate tab and log in and open your own project from the previous I Have a Dream lesson. Follow along with your teacher or the following video tutorial or the <a href="https://drive.google.com/open?id=142GsbdyLdww30yb5WLqA-Nmej53povgD4eCStG69ESg" target="_blank" title="">text tutorial</a> or the <a href="https://docs.google.com/document/d/1-mEg1OTpFWDq2UF86NWNwNozlU-roQYCxzovpcT88jU/edit?usp=sharing" target="_blank" title="">short handout</a>. You could also use <a href="https://www.youtube.com/watch?v=vgkahOzFH2Q" target="_blank">Pair Programming</a> to do this tutorial in teams of two. If you'd like to use an embedded tutorial for this App Inventor project, scroll down in your Screen properties to find the <b>TutorialURL</b> property and paste in http://templates.appinventor.mit.edu/trincoll/csp/tutorials/IHaveADreamPart2.html or change IHaveADream.html to IHaveADream<b>Part2</b>.html. </p>
    <br/>
.. youtube:: Qs8NJbCoD9c
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

    <h3>Explore Curricular Activity: Computing Innovations and Collaboration</h3>Discuss the following two paragraphs with your classmate(s) and/or a friend. You can use this <a href="https://docs.google.com/document/d/1Y_LDNnjXkmj-RzOM3dlIkcvmUjP8KUWlSlE2aVdiCJY/copy" target="_blank" title="">Notes Worksheet</a> to help guide your discussion. Check with your instructor to see if they have additional worksheets or activities for you to complete.<br/><br/>With the expansion of computers and the Internet, every day new computing innovations are being developed. A <b>computing innovation</b> includes a program as an integral part of its function. The purpose of computing innovations is to solve problems or to pursue interests through creative expression. Understanding the purpose of a computing innovation provides developers with an improved ability to develop that computing innovation. Additionally, a computing innovation can be physical, non-physical computing software, or non-physical computing concepts. For example, self-driving cars, picture editing software, e-commerce. In this lesson, we're also creating a mobile app, which is certainly an example of a computing innovation. Can you think of other examples of computing innovations? Can you identify the function or purpose of each of those computing innovations?<br/><br/>Computing innovations, such as the I Have a Dream mobile app, are often improved through collaboration. Most computing innovations are developed by groups or teams of developers. Effective collaboration can take many forms. It can range from working with a diverse group of people to create or modify the computing innovation to consulting and communicating with users as part of the development process of the computing innovations (e.g. gathering information from potential users of your app to help understand the program from diverse perspectives). In the end, effective collaboration produces a computing innovation that reflects the diversity of talents and perspectives of those who designed it. Collaboration that includes diverse perspectives is important because it helps avoid bias in the development of computing innovations. One model to help facilitate collaboration is <a href="https://www.youtube.com/watch?v=vgkahOzFH2Q" target="_blank">Pair Programming</a>. This course emphasizes collaboration, so there will be plenty of opportunities for pair programming when developing apps in the course. <br/>
    

Summary
--------

.. raw:: html

    <p>
    In this lesson, you learned how to:
      <div class="yui-wk-div" id="summarylist">
    </div>
    

Self-Check
-----------

.. raw:: html

    <p>
    Vocabulary:<br/>
    <table align="center">
    <tbody><tr>
    <td>
    <span class="hover vocab yui-wk-div" data-id="Computing Innovation">Computing Innovation</span>
    <br/><span class="hover vocab yui-wk-div" data-id="If/Else">If/Else</span>
    <br/><span class="hover vocab yui-wk-div" data-id="UI Components">UI Components</span>
    <br/><span class="hover vocab yui-wk-div" data-id="Horizontal Arrangement">Horizontal Arrangement</span>
    </td></tr>
    </tbody></table>
    
.. mchoice:: mcsp-2-4-1
    :random:
    :practice: T
    :answer_a: A mobile app
    :feedback_a: A computing innovation includes a program as an integral part of its function.  Mobile apps surely count as such.
    :answer_b: Self-driving cars
    :feedback_b: A computing innovation includes a program as an integral part of its function. Self-driving cars depend on computer programs to make them work.
    :answer_c: Office software (used to create spreadsheets or word documents)
    :feedback_c: A computing innovation includes a program as an integral part of its function.  Office software is an example of computer software. 
    :answer_d: Bar codes
    :feedback_d: A computing innovation includes a program as an integral part of its function.  A bar code itself does not contain a program - it is an image. 
    :correct: a,b,c

    A computing innovation includes a program as an integral part of its function. Which of the following would be considered computing innovations?    Choose all that apply.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

.. mchoice:: mcsp-2-4-2
    :random:
    :practice: T
    :answer_a:  "if" blocks are used because there are two speeches to choose from.
    :feedback_a: Don’t worry, it’s hard! Let’s go back and try it again.
    :answer_b: "if" blocks are used to determine, when the buttons are clicked, whether a speech is already playing. 
    :feedback_b: 
    :answer_c: "If" blocks are used to determine which speech is playing.
    :feedback_c: Don’t worry, it’s hard! Let’s go back and try it again.
    :answer_d: "if" blocks are used to ask if the user wants to close the app
    :feedback_d: Don’t worry, it’s hard! Let’s go back and try it again.
    :correct: b

    Why are "if" blocks used in the "I Have a Dream" app?


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-2-4-3
    :random:
    :practice: T
    :answer_a: Button1
    :feedback_a: Mistakes are welcome here! Try reviewing this; it is best to give buttons names that help you understand their function. 
    :answer_b: Clear
    :feedback_b: Mistakes are welcome here! Try reviewing this; this choice tells us what is happening, but it doesn't tell us what is making something clear. Therefore a better option would also tell us that it was a button. 
    :answer_c: ClearButton
    :feedback_c: Correct! 
    :answer_d: ButtonA
    :feedback_d: Mistakes are welcome here! Try reviewing this; it is best to give buttons names that help you understand their function.
    :correct: c

    Which of the following is the best name for a button whose function is to clear another component?


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-2-4-4
    :random:
    :practice: T
    :answer_a: True
    :feedback_a: 
    :answer_b: False
    :feedback_b: We’re in the learning zone today. Mistakes are our friends!
    :correct: a

    A horizontal arrangement allows buttons (and other components) to be placed side-by-side in the user interface.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
    .. quizly:: mscp-2-4-6
    
        :quizname: quiz_stop_player_if_playing
    
    
    .. quizly:: mscp-2-4-7
    
        :quizname: quiz_if_else_stop_start_player
    
    

Sample AP CSP Exam Question
----------------------------

.. raw:: html

    <p>
    In the sample AP exam below, <span style="font-style: italic;">absent </span>and <span style="font-style: italic;">onTime</span> are variables that can be true or false, just like <i>Player1.IsPlaying </i>could be true or false in the if blocks in the I Have a Dream app. They are both false in this question. This question uses nested if blocks where a second if block is inside the else of the first if block. <br/>
.. mchoice:: mcsp-2-4-5
    :random:
    :practice: T
    :answer_a: (A) Is anyone there?
    :feedback_a: This would only display if absent was true, but absent is false.
    :answer_b: (B) Better late than never.
    :feedback_b: That's correct!
    :answer_c: (C) Hello. Is anyone there?
    :feedback_c: Hello would only display if onTime was true, but onTime is false.
    :answer_d: (D) Hello. Better late than never.
    :feedback_d: Hello would only display if onTime was true, but onTime is false.
    :correct: b

    Consider the code segment below.If the variables onTime and absent both have the value false, what is displayed as a result of running the code segment?

    .. raw:: html

        <img alt="" class="yui-img selected" src="../_static/assets/img/APExamPrepQ13.PNG" style="width: 400px;" title=""/>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1B2qxsUuLSFAHF9l42VqOQ41195zucIGqqHiribB800Q/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vSdP9MMLFaLbyv1GstC1eYRerx9KvPX1TxUWL11gwI1_-BCEFS8II63C0NESq1H1Hdk7MLPP3WX_XBH/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--
      &lt;p&gt;In your portfolio, create a new page named &lt;i&gt;I Have a Dream Part 2&lt;/i&gt; (If you are using the Mobile CSP Student portfolio template, this page has already been created for you)  and answer the following questions:&lt;/p&gt;
      &lt;ol&gt;
        &lt;li&gt;What components make up the &lt;b&gt;&lt;i&gt;User Interface (UI)&lt;/i&gt;&lt;/b&gt; for this enhanced version of the &lt;i&gt;I Have A Dream&lt;/i&gt; app?&lt;/li&gt;
        &lt;li&gt;A&amp;nbsp;&lt;b&gt;computing innovation&lt;/b&gt; includes a program as an integral part of its function. We&#39;ve just created a mobile app, which is certainly an example of a computing innovation. Give at least 3 examples from your own experience of computing innovations that you&#39;ve used or seen and describe the function/purpose of each.&lt;/li&gt;
      &lt;/ol&gt; -->
    </div>
    </div>