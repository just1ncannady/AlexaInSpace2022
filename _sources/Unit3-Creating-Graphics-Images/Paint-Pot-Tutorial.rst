.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Paint Pot Tutorial
==================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
        generateSummary(EKmapping['3.02']);
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
    <!--* var vocabulary = { 
        &quot;variable&quot;:&quot;A variable names a memory location to hold different values in your program.&quot;,
         &quot;assignment&quot;:&quot;Assignment sets a variable to a value or a mathematical expression.&quot;, 
        &quot;expression&quot;: &quot;A mathematical expression involves values, variables, and operators for example (a+b)/2&quot;,
        &quot;operator&quot;: &quot;Symbols like +,-,*,/ used for addition, subtraction, multiplication, division.&quot;,
        &quot;pseudocode&quot;: &quot;A blend of English and code used to write down an algorithm for a program.&quot;
    
      };    -->
    <h3 id="est-length">Time Estimate: 90 minutes</h3>
    

Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <table>
    <tbody>
    <tr>
    <td>
    <iframe allowfullscreen="" frameborder="0" height="420" src="https://www.youtube.com/embed/PWKGUzdiP44" width="315"></iframe>
        (<a href="http://www.teachertube.com/video/paintpot2preview-347830" target="_blank">TeacherTube Version</a>)
      </td>
    <td>
    <b><i>Paint Pot</i></b> is a basic “finger painting” app. It 
        simulates  dipping your finger in a pot of a paint and then 
        drawing with it on a canvas. The app uses buttons to change the paint colors 
        and uses App Inventor’s touch and drag event handlers to draw circles and lines
        on the canvas.
        <br/>
    <p>This tutorial also introduces the concept of a global <span class="hover vocab yui-wk-div" data-id='variable'>variable</span>.</p>
    <p>
    <b>Objectives:</b> In this lesson you will learn to:
        </p>
    <ul>
    <li>follow an instructor-led walkthrough to create the <i>PaintPot</i> app on a mobile device;
          </li><li>continue navigating the App Inventor programming platform;
          </li><li>develop your understanding of what an App Inventor program is;
          </li><li>deepen your understanding of event-driven programming;
          </li> <li>learn how to use a <span class="hover vocab yui-wk-div" data-id='variable'>variable</span> to make a program more general.</li>
    </ul>
    </td>
    </tr>
    </tbody>
    </table>
    

Learning Activities
--------------------

.. raw:: html

    <p><h3><br/>Tutorial Part 1: Painting and Drawing on a Canvas</h3>
    <p>To get started, <a href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit3/templates/PaintPotMediaOnly/PaintPotMediaOnly.asc" target="_blank">open App Inventor with the Paint Pot Template</a>
     in a separate tab and follow along with the following video or your teacher.
    <br/>
    Or  click <a href="https://docs.google.com/document/d/164sPOhgX0uaTCyrWL-zxxKv_DdAA-IgVvOlU5vpYPPc/edit?usp=sharing" target="_blank">here for the text version of the tutorial</a> or the <a href="https://docs.google.com/document/d/18thDoU6Ru3v9TTxhGfELuvwagm3bTNFYh-iXchDntGw/edit?usp=sharing" target="_blank">short handout</a>.  
      <br/>
      (<a href="https://teachertube.com/video/paint-pot-1-tutorial-476369" target="_blank">TeacherTube Version</a>)
    </p>
    
.. youtube:: OoA8Q5v2sWg
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    

Self-Check
-----------

.. raw:: html

    <p>
    
.. mchoice:: mcsp-3-2-1
    :random:
    :practice: T
    :answer_a: Vertically
    :feedback_a: 
    :answer_b: Horizontally
    :feedback_b: If it were easy, you wouldn’t be learning anything!
    :answer_c: Diagonally
    :feedback_c: If it were easy, you wouldn’t be learning anything!
    :answer_d: Randomly
    :feedback_d: If it were easy, you wouldn’t be learning anything!
    :correct: a

    By default, when you add components to the App Inventor Viewer they are laid out ___________.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-3-2-2
    :random:
    :practice: T
    :answer_a: Automatic
    :feedback_a: Try asking a classmate for advice—s/he may be able to explain/suggest some ideas or recommend some strategies.
    :answer_b: Fill parent
    :feedback_b: 
    :answer_c: Fill container
    :feedback_c: Try asking a classmate for advice—s/he may be able to explain/suggest some ideas or recommend some strategies.
    :answer_d: Max pixels
    :feedback_d: Try asking a classmate for advice—s/he may be able to explain/suggest some ideas or recommend some strategies.
    :correct: b

    Which value would you set the Width property to if you want your component, e.g., a Button, to fill its container? 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-3-2-3
    :random:
    :practice: T
    :answer_a: Button1
    :feedback_a: Don’t worry, it’s hard! Let’s go back and try it again.
    :answer_b: ButtonOne
    :feedback_b: Don’t worry, it’s hard! Let’s go back and try it again.
    :answer_c: ButtonRefresh
    :feedback_c: 
    :answer_d: B1
    :feedback_d: Don’t worry, it’s hard! Let’s go back and try it again.
    :answer_e: RefreshButton
    :feedback_e: 
    :correct: c,e

    Which of the following would be a good name for a button whose purpose was to allow the view to refresh the screen? 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
    
.. quizly:: mscp-3-2-10
    
    
    :quizname: quiz_background_color
    
    
    
.. quizly:: mscp-3-2-11
    
    
    :quizname: quiz_text_color
    
    

.. raw:: html

	<h3>Tutorial Part 2:  Varying the Size of the Dots</h3>
    <p>
    <p>Watch the video tutorial below or click <a href="https://docs.google.com/document/d/164sPOhgX0uaTCyrWL-zxxKv_DdAA-IgVvOlU5vpYPPc/edit?usp=sharing" target="_blank"> here for the text version</a> of the tutorial.
    <br/>
      (<a href="https://upload.teachertube.com/video/paintpot2-varying-the-dotsize-478432" target="_blank" title="">TeacherTube version</a>)</p>
    
.. youtube:: 7eY2aSeP9Oc
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

	<h3>AP CSP Pseudocode: Variables and Assignment Statements</h3>

    <p>
    <p>A <b><span class="hover vocab yui-wk-div" data-id='variable'>variable</span></b> provides a way to name a memory location in your program to hold different values. It is a <b>data abstraction</b> that exists in all programming languages. In App Inventor, we set up a <span class="hover vocab yui-wk-div" data-id='variable'>variable</span> using the <i>initialize global <span class="hover vocab yui-wk-div" data-id='variable'>variable</span></i> block. The <i>get</i> block is used to get the <span class="hover vocab yui-wk-div" data-id='variable'>variable</span>'s current value whenever needed in the program. The <i>set </i>block is used to assign or change the value of the <span class="hover vocab yui-wk-div" data-id='variable'>variable</span>.
    <br/> <img src="../_static/assets/img/initdotsize.png" width="20%"/>
    <img src="../_static/assets/img/getdotsize.png" width="20%"/> <img src="../_static/assets/img/setdotsize.png" width="20%"/>
    <br/>
    </p>
    <p> The AP CS Principles Exam does not have a designated programming language. It uses   <b><i><span class="hover vocab yui-wk-div" data-id='pseudocode'>pseudocode</span></i></b> which is a cross between computer code and everyday English. 
       <span class="hover vocab yui-wk-div" data-id='Pseudocode'>Pseudocode</span> is less precise than actual computer code, 
      such as Java or Python or App Inventor, but more precise and less wordy than everyday English. The <a href="https://drive.google.com/file/d/0B5ZVxaK8f0u9c1VlWFJDRHl0dEk/view" target="_blank">AP CSP reference sheet</a> is provided during the exam to help you understand the AP <span class="hover vocab yui-wk-div" data-id='pseudocode'>pseudocode</span> format used in the exam. It includes two <span class="hover vocab yui-wk-div" data-id='pseudocode'>pseudocode</span> styles: text-based and block-based.</p>
    <p>In the College Board AP CSP exam, App Inventor set blocks are called <b><span class="hover vocab yui-wk-div" data-id='assignment'>assignment</span> statements</b> and are represented as the left-pointing arrow (←). The following text and block style <span class="hover vocab yui-wk-div" data-id='pseudocode'>pseudocode</span> is used to assign values to variables:
        <br/>
    </p><table border="">
    <thead><tr> <th>Function</th><th>AP Text </th> <th width="25%">AP Block </th><th>App Inventor</th></tr></thead>
    <tbody>
    <tr><td><span class="hover vocab yui-wk-div" data-id='Assignment'>Assignment</span>:</td><td>a ← <em><span class="hover vocab yui-wk-div" data-id='expression'>expression</span></em></td><td><div class="yui-wk-div" id="APblocks">
    <bl>a ← <bl><span class="hover vocab yui-wk-div" data-id='expression'>expression</span></bl></bl></div></td><td><img src="../_static/assets/img/setdotsize.png" width="250px"/></td></tr>
    </tbody></table>
    <p>The DISPLAY statement is used to display <span class="hover vocab yui-wk-div" data-id='variable'>variable</span> values or the value resulting from mathematical expressions like (a+b)/2. <b>Expressions</b> are made up of values, variables, math operators, and sometimes mathematical procedures like getting a random number or squaring a number. In mathematical expressions, the <b>operators</b> * for multiplication, / for division, and the mod <span class="hover vocab yui-wk-div" data-id='operator'>operator</span> (remainder after division) are done before + and - like in math, unless there are parentheses that for example tell the computer to do (a+b) first before dividing by 2. Notice that * is used for multiplication instead of x, because x would get confused with a <span class="hover vocab yui-wk-div" data-id='variable'>variable</span> name. Expressions are evaluated to produce a single value.
    </p><table border="">
    <thead><tr> <th>Function</th><th>AP Text </th> <th width="25%">AP Block </th></tr></thead>
    <tbody><tr><td>Display:</td><td>DISPLAY(<em><span class="hover vocab yui-wk-div" data-id='expression'>expression</span></em>)</td><td><div class="yui-wk-div" id="APblocks">
    <bl>DISPLAY <bl><span class="hover vocab yui-wk-div" data-id='expression'>expression</span></bl></bl></div></td></tr>
    <tr><td>Expressions:</td><td>a + b, a - b, a * b, a/b </td><td><div class="yui-wk-div" id="APblocks">
    <bl>a + b</bl></div></td>
    </tr>
    </tbody></table>
    <p>
     For example, here is AP style <span class="hover vocab yui-wk-div" data-id='pseudocode'>pseudocode</span> to set the dotsize <span class="hover vocab yui-wk-div" data-id='variable'>variable</span> to 5 and then increment it (add one to it). The <span class="hover vocab yui-wk-div" data-id='variable'>variable</span> dotsize will have the value 6 after these two lines of code are executed. The value stored in a <span class="hover vocab yui-wk-div" data-id='variable'>variable</span> will be the most recent value assigned.
    </p>
    <table border="">
    <thead><tr> <th>Function</th><th width="25%">AP Text </th> <th width="25%">AP Block </th><th>App Inventor</th></tr></thead>
    <tbody>
    <tr><td>Set dotsize to 5</td><td>dotsize ← 5</td> <td> <div class="yui-wk-div" id="APblocks">
    <bl>dotsize ← <bl>5</bl></bl></div></td><td><img src="../_static/assets/img/initdotsize.png" width="250px"/></td></tr>
    <tr><td>Increment dotsize</td><td> dotsize ← dotsize + 1</td><td> <div class="yui-wk-div" id="APblocks">
    <bl>dotsize ← <bl>dotsize + 1</bl></bl></div></td><td><img src="../_static/assets/img/SetXToX1.png" width="350px"/></td></tr>
    </tbody></table>
    
    
    Some exercises involving AP <span class="hover vocab yui-wk-div" data-id='pseudocode'>pseudocode</span> for <span class="hover vocab yui-wk-div" data-id='assignment'>assignment</span> are below. More complex AP <span class="hover vocab yui-wk-div" data-id='pseudocode'>pseudocode</span> will be shown in Unit 4.
    

Summary
--------

.. raw:: html

    <p>
    In this lesson, you learned how to:
      <div id="summarylist">
    </div>
    

Self-Check
-----------

.. raw:: html
	<p>
    
    Here is a table of some of the technical terms we've introduced in this lesson. Hover over the terms to review the definitions.
    
    <table align="center">
    <tbody><tr>
    <td>
    <span class="hover vocab yui-wk-div" data-id="variable">variable</span>
    <br/><span class="hover vocab yui-wk-div" data-id="assignment">assignment</span>
    <br/><span class="hover vocab yui-wk-div" data-id="expression">expression</span>
    </td>
    <td>
    <span class="hover vocab yui-wk-div" data-id="operator">operator</span>
    <br/><span class="hover vocab yui-wk-div" data-id="pseudocode">pseudocode</span>
    </td>
    </tr>
    </tbody>
    </table>
    <p>
    
.. mchoice:: mcsp-3-2-4
    :random:
    :practice: T
    :answer_a: 5
    :feedback_a: Mistakes are welcome here! Try reviewing this; the value 5 is number.  Numbers cannot be used as variable names.  Try again
    :answer_b: -5
    :feedback_b: Mistakes are welcome here! Try reviewing this; the value -5 is number.  Numbers cannot be used as variable names.  Try again
    :answer_c: "user name"
    :feedback_c: Mistakes are welcome here! Try reviewing this; the text "user name" is a text value.  Text values cannot be used as variable names.
    :answer_d: userName
    :feedback_d: That's correct.  Variable names are alphanumeric symbols that must begin with a letter and can contain any combination of letters and digits. Other examples would be <i>name5, bigDot, passwd, smallDot.&nbsp;</i>
    :correct: d

    Which of the following would be a valid App Inventor variable name? 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-3-2-5
    :random:
    :practice: T
    :answer_a: 10
    :feedback_a: Mistakes are welcome here! Try reviewing this. 10 is a number.  It is a value not a variable.
    :answer_b: paintBrush
    :feedback_b: Yes, <i>paintBrush</i>&nbsp;is an abstract symbol for some particular value -- although we don't know what value it is referring to here.
    :answer_c: "hello"
    :feedback_c: Mistakes are welcome here! Try reviewing this. "hello" is a text value.  It is not a variable.  Text values are always represented in quote marks.
    :answer_d: true
    :feedback_d: Mistakes are welcome here! Try reviewing this. <i>true &nbsp;</i>is a <i>boolean value. &nbsp;</i>So it cannot be used as the name of a variable. &nbsp;The other boolean value is <i>false. &nbsp;</i>
    :answer_e: x
    :feedback_e: Yes. <i>x</i>&nbsp;is an abstract symbol that could be used for a variable name. &nbsp;We don't know what value it is referring to here.&nbsp;
    :correct: b,e

    A variable is an abstract symbol that refers to some particular value.  Which of the following symbols is a variable?


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-3-2-6
    :random:
    :practice: T
    :answer_a: <img src="../_static/assets/img/getdotsize.png" class="yui-img"><br>
    :feedback_a: OK, so you didn’t get it right this time. Let’s look at this as an opportunity to learn. Try reviewing this. This getter block, <img src="../_static/assets/img/getdotsize.png" class="yui-img">, can only be used to 'get' the variable's current value.  It cannot be used to change its value.
    :answer_b: <img src="../_static/assets/img/setdotsize.png" class="yui-img"><br>
    :feedback_b: Yes, a setter block, <img src="assets/img/setdotsize.png" class="yui-img">, is the correct block to use to change or 'set' a variable's value.
    :answer_c: <img src="../_static/assets/img/initdotsize.png" class="yui-img"><br>
    :feedback_c: OK, so you didn’t get it right this time. Let’s look at this as an opportunity to learn. Try reviewing this. The <img src="../_static/assets/img/initdotsize.png" class="yui-img">&nbsp;block can only be used to create and initialize a variable.  It cannot be used to change its value.
    :answer_d: None of the above.
    :feedback_d: 
    :correct: b

    Suppose you initialize dotsize with the block <img src="../_static/assets/img/initdotsize.png" class="yui-img"/>. Which of the following blocks would you use to change the value of dotsize?

    .. raw:: html

        <img class="yui-img selected" src="../_static/assets/img/initdotsize.png"/>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. fillintheblank:: mcsp-3-2-7

    What value will the variable dotsize have after the following sequence of blocks are executed?

    .. raw:: html

        <img class="yui-img" src="../_static/assets/img/dotsizesequence.png"/> |blank|

    - :18: <img src="../_static/assets/img/dotsizesequence.png" class="yui-img"><br>This sequence of blocks performs the following actions on <i style="font-weight: bold;">dotsize.</i>&nbsp;When the variable is created (initialized) its initial value is 5. &nbsp;Its value is then set to 10 by the second block in the sequence. &nbsp;Its value is then set to 20 (10 + 10) by the third block in the sequence. &nbsp;Its value is then set to 18 (20 - 2) by the last block in the sequence.&nbsp;
      :x: 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-3-2-8
    :random:
    :practice: T
    :answer_a: a variable is more general and more abstract than a specific value such as 5.
    :feedback_a: True. A variable, such as&nbsp;&nbsp;<i style="font-weight: bold;">dotsize</i>&nbsp;is more abstract than a value such as 5 because it can represent many different values.
    :answer_b: using a variable instead of a specific value makes an app more generally useful.
    :feedback_b: True. &nbsp;As we saw with&nbsp;<i style="font-weight: bold;">dotsize</i>&nbsp;using a variable made the program more useful.
    :answer_c: a variable is an abstract symbol that can represent lots of different values.
    :feedback_c: True. As we saw with<i style="font-weight: bold;">&nbsp;dotsize</i>&nbsp;a variable can take on many different values during the course of a program.
    :answer_d: using a variable instead of a specific value makes an app more vague.
    :feedback_d: Let me add new information to help you solve this. Variables are more general and more abstract, but that's not the same as being vague.  We can always determine precisely what value a variable represents during the course of a program. 
    :correct: a,b,c

    Using a variable is an example of abstraction because 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
    
.. quizly:: mscp-3-2-12
    
    
    :quizname: quiz_incrementing
    
    
.. mchoice:: mcsp-3-2-9
    :random:
    :practice: T
    :answer_a: 2 &nbsp;2
    :feedback_a: 
    :answer_b: 1 &nbsp;1
    :feedback_b: 
    :answer_c: 2 &nbsp;3
    :feedback_c: 
    :answer_d: 3 &nbsp;2
    :feedback_d: Yes, that's correct. At first a is 1 and b is set to a which is 1. &nbsp;Then, we add 1 to b and it becomes 2. &nbsp; Then, a adds b (which is currently 2) to its value (which is currently 1) and becomes 3.&nbsp;
    :correct: d

    What does the following AP CSP pseudocode display? Remember to trace through the code keeping track of the values in a and b after each line of code.a ← 1        (Set a to 1)b ← a        (Set b to the current value of a)b ← b + 1    (Add 1 to b)a ← a + b    (Set a to be the current value of a + b)DISPLAY(a)DISPLAY(b)


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <br/><br/><br/>
    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1X5TAmuqwe7soWYpuh39rZKvR2TcfEbE0rJqv9f5GcwA/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vRPC2TBmE49InvPhMK20fT8rYYOfKP9ZenSLfJkhgTxu8-H6u7cHZhgRk0YNv3b5T4TKUKRyb3q3Gdg/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--&lt;p&gt;Create a new page named &lt;i&gt;&lt;b&gt;Paint Pot Tutorial&lt;/b&gt;&lt;/i&gt; under the &lt;i&gt;Reflections&lt;/i&gt; category of your portfolio and write brief answers to the following questions.&lt;/p&gt;
    
      &lt;ol&gt;
        &lt;li&gt;Explain the meaning of the statements shown here, both in pseudocode and App Inventor. For 
          example, suppose the variable &lt;i&gt;X&lt;/i&gt; has the value 10 before the statement is executed.  What
          value would it have after the statement is executed. 
          &lt;table&gt;
            &lt;tbody&gt;&lt;tr&gt;
              &lt;td&gt;Set X to X + 1&lt;/td&gt;
              &lt;td&gt;&lt;img src=&quot;assets/img/SetXToX1.png&quot; width=&quot;350px&quot;&gt;&lt;/td&gt;
            &lt;/tr&gt;
          &lt;/tbody&gt;&lt;/table&gt;
        &lt;/li&gt;
        &lt;li&gt;One aspect of abstraction is that it helps to reduce details to focus on what&#39;s relevant. 
          How does the use of a variable, such as &lt;i&gt;dotsize&lt;/i&gt;, instead of a value, such as &#39;5&#39;, help
          to reduce detail and focus on what is essential in this program.
        &lt;/li&gt;
    --------------
        &lt;li&gt;How many different types of &lt;i&gt;events&lt;/i&gt; does this app respond to?  Name and describe each type of event.
        &lt;/li&gt;
        &lt;li&gt;What do the &lt;i&gt;X&lt;/i&gt; and &lt;i&gt;Y&lt;/i&gt; properties represent in the &lt;i&gt;Touched&lt;/i&gt;event handler?
        &lt;/li&gt;
        &lt;li&gt;Describe the difference between the &lt;i&gt;Start&lt;/i&gt; and &lt;i&gt;Previous&lt;/i&gt; properties in the &lt;i&gt;Dragged&lt;/i&gt; event handler.
        &lt;/li&gt;
        &lt;li&gt;One advantage of abstraction is that it allows us to make our apps more general. Describe how the use of the variable &lt;i&gt;dotsize&lt;/i&gt; is an example of abstraction in the Paint Pot app.
          &lt;/li&gt;
        &lt;li&gt;Abstraction is sometimes defined as &quot;reducing information and detail to focus on what&#39;s relevant&quot;.  In your opinion, does the use of the &lt;i&gt;dotsize&lt;/i&gt; variable fit this definition?  Why or why not?
          &lt;/li&gt;
    
      &lt;/ol&gt;-->
    </div>
    </div>