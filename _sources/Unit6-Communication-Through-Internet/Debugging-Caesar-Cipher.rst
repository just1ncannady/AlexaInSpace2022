.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Debugging Caesar Cipher
=======================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
        generateSummary(EKmapping['6.08']);
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
        "syntax error" : "An error that results from a violation of the programming language grammatical rules. ",
        "semantic error":"An error in which the program is not working as it is designed to work.",
        "computer bug":"An informal term for error in computer hardware or software -- the term was coined by Grace Hopper.",
        "debugging":"The process of removing errors from computer hardware or software.",
       };    */
    </script>
    <h3 id="est-length">Time Estimate: 45 minutes</h3>
    

Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <p>In this lesson, we will learn more about the types of errors you might get in a program, including tips for identifying, fixing, and preventing them. First, watch the video below. After watching the video, try to identify and correct the errors in the Caesar Cipher app and then answer the questions about <span class="hover vocab yui-wk-div" data-id='debugging'>debugging</span>. When watching the video, look for these important terms and concepts: </p>
    <ul>
    <li><b>Bug</b> - In computer programming, a <span class="hover vocab yui-wk-div" data-id='computer bug'>bug</span> is an error or defect that prevents the app from working the way it is supposed to.
      </li><li><b><span class="hover vocab yui-wk-div" data-id='debugging'>Debugging</span></b> - The process of removing errors from computer hardware or software.
      </li><li><b>Logic Error</b> - A mistake in the algorithm or program that causes it to behave incorrectly or unexpectedly. Also referred to as a <span class="hover vocab yui-wk-div" data-id='semantic error'>semantic error</span>.</li>
	  <li><b><span class="hover vocab yui-wk-div" data-id='syntax error'>Syntax Error</span></b> - A mistake in the program where the rules of the programming language are not followed.
    </li></ul>
    
.. youtube:: g48gxSkOeik
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>	<div><b>Learning Objectives:</b>&nbspI will learn to</div>
	<ul>
	<li>identify and correct errors in a program</li>
	<li>explain the difference between <span class="hover vocab yui-wk-div" data-id="syntax error">syntax errors</span> and <span class="hover vocab yui-wk-div" data-id="semantic error">semantic errors</span></li>
	</ul>
	<div><b>Language Objectives:</b>&nbspI will be able to</div>
	<ul>
	<li>use target vocabulary, such as <span class="hover vocab yui-wk-div" data-id="syntax error">syntax error</span>, <span class="hover vocab yui-wk-div" data-id="semantic error">semantic error</span>, and <span class="hover vocab yui-wk-div" data-id="run-time error">run-time error</span> while fixing errors in an app, with the support of concept definitions and <a href="https://docs.google.com/presentation/d/1n-K4AQ_maHcXekzcfERQ9dxj91nqv9ytwJx4ZkAp8zw/copy" target="_blank" title="">vocabulary notes</a> from this lesson</li>
	</ul>

    (<a href="http://www.teachertube.com/video/359067" target="_blank">Teacher Tube version</a>)
    
	
    

Learning Activities
--------------------

.. raw:: html

    <p><h3>Activity</h3>
    <p>The activity for this lesson is to <span class="hover vocab yui-wk-div" data-id="debugging">debug</span> a version of the Caesar cipher app. There are at least <b>five errors</b> in 
    this version of the app. See if you can find and correct them all! To get started, 
    <a href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit5/templates/CaesarApp/CaesarCipherBuggy.asc" target="_blank">open App Inventor with the Caesar Cipher Buggy template</a>. 
    </p>
    <p>Here are some hints and suggestions.
      </p><ul>
    <li style="margin-bottom: 5px;">If you see a <span class="hover vocab yui-wk-div" data-id='run-time error'>run-time error</span> message, read it carefully - it's trying to tell you where the bug is. A <span class="hover vocab yui-wk-div" data-id='run-time error'>run-time error</span> is a mistake in the program that occurs during the execution of a program. Programming languages, such as MIT App Inventor, define their own run-time errors.  For example, if the <span class="hover vocab yui-wk-div" data-id='run-time error'>run-time error</span> complains about exceeding the length of the text, then the loop going through the text letter by letter did not stop at the end of the text.</li>
	<li style="margin-bottom: 5px;">The bugs can be in both the encryption and decryption steps.  So make sure you test the app thoroughly, with appropriate inputs. When you are testing this app, <b>only type in lowercase letters in the plaintext textbox to encrypt, and only type in uppercase letters in the Ciphertext textbox to decrypt</b>.</li>
    <li style="margin-bottom: 5px;">You are may see more problems if you encrypt longer rather than shorter messages.</li>
    <li style="margin-bottom: 5px;">If you are having trouble locating a problem, use a <i>Notifier</i> or use <i>Label1</i> to 
          display intermediate values of local or global variables.  
        </li><li style="margin-bottom: 5px;">You may also compare this code to your finished Caesar Cipher app from the previous lesson.</li>
    <li>Use App Inventor's Do It tool to evaluate expressions and intermediate values. Here's a short
          video on <a href="https://www.youtube.com/watch?v=Z4ceHVE_L_8" target="_blank">how to use Do It</a>.
        </li>
    </ul>
    

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
    
    Here is a table of some of the technical terms discussed in this
    lesson. Hover over the terms to review the definitions.
    
    <table align="center">
    <tbody>
    <tr>
    <td><span class="hover vocab yui-wk-div" data-id="debugging">debugging</span>
    <br/><span class="hover vocab yui-wk-div" data-id="computer bug">computer bug</span>
    <br/><span class="hover vocab yui-wk-div" data-id="syntax error">syntax error</span>
    <br/><span class="hover vocab yui-wk-div" data-id="semantic error">logic/semantic error</span>
    <br/><span class="hover vocab yui-wk-div" data-id="run-time error">run-time error</span>
    </td>
    </tr>
    </tbody>
    </table>
    
	
.. mchoice:: mcsp-6-8-1
    :random:
    :practice: T
    :answer_a: True
    :feedback_a: That's right! In fact, the term "bug" was used in an account by computer pioneer Grace Hopper regarding an error that was found to be related to a moth that was trapped in the machine.
    :answer_b: False
    :feedback_b: OK, so you didn’t get it right this time. Let’s look at this as an opportunity to learn. Try reviewing this; the term "bug" was actually used in an account by computer pioneer Grace Hopper regarding an error that was found to be related to a moth that was trapped in the machine.
    :correct: a

    .. raw:: html
    
    	<p><b>True or False</b>: In computer programming, a <b><i>bug</i></b> is an error or defect that prevents the app from working the way it is supposed to.</p>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-6-8-2
    :random:
    :practice: T
    :answer_a: programmer's knowledge 
    :feedback_a: Mistakes are welcome here! Try reviewing this; the programmer's knowledge can be used to determine if statements are formulated correctly, this is not what is meant by syntax.
    :answer_b: compiler 
    :feedback_b: Mistakes are welcome here! Try reviewing this; the compiler runs the program statements whether or not they are formulated correctly. If there is a syntax error, the compiler will inform you that there is an error.
    :answer_c: programming language 
    :feedback_c: Mistakes are welcome here! Try reviewing this; the programming language is the language the statements are written in. The programming language itself does not determine if the statements are formulated correctly. The programming language's syntax does this.
    :answer_d: set of rules
    :feedback_d: That's right! Programming languages all have syntax, a set of rules, that must be followed when writing code.
    :correct: d

    .. raw:: html
    
    	<p>In computer programming, <b><i>syntax</i></b> is the __________ that determines whether statements are correctly formulated.</p>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-6-8-3
    :random:
    :practice: T
    :answer_a: semantic
    :feedback_a: Mistakes are welcome here! Try reviewing this...Syntax errors occur when a programming language's rules for writing code are broken. The compiler can detect syntax errors and report an error message to the programmer.
    :answer_b: syntax
    :feedback_b: That's right! Syntax errors occur when a programming language's rules for writing code are broken. The compiler can detect syntax errors and report an error message to the programmer.
    :correct: b

    A ____________ error occurs when a programming language's rules are broken. This type of error can be detected by the compiler which will provide an error message. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-6-8-4
    :random:
    :practice: T
    :answer_a: Semantic
    :feedback_a: That's right! Semantic errors occur when the programmer unintentionally writes code that follows the syntax rules of the programming language, but their code works in a different way than what the programmer had intended it to.
    :answer_b: Syntax
    :feedback_b: OK, so you didn’t get it right this time. Let’s look at this as an opportunity to learn. Try reviewing this; semantic errors occur when the programmer unintentionally writes code that follows the syntax rules of the programming language, but their code works in a different way than what the programmer had intended it to.
    :correct: a

    A ____________ error occurs when a programmer inadvertently puts code that is syntactically correct, but does not do what the programmer intended it to do. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-6-8-5
    :random:
    :practice: T
    :answer_a: True
    :feedback_a: We’re in the learning zone today. Mistakes are our friends!
    :answer_b: False
    :feedback_b: That's right! Semantic errors cannot be detected by the compiler. Only the programmer knows what it wants the program to do.
    :correct: b

    .. raw:: html
    
    	<p><b>True or False</b>: Semantic errors can be detected by the compiler. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-6-8-6
    :random:
    :practice: T
    :answer_a: The PaintPot ButtonMinus.Click event adding 1 to dotsize. 
    :feedback_a: True. This would be syntactically correct, however based on the documentation (the name of the button) it would not do what the programmer had intended it to, which would be to decrease the dotsize by 1 when ButtonMinus is clicked.
    :answer_b: Coding duplicate Canvas1.Touched event handlers in PaintPot. 
    :feedback_b: We’re in the learning zone today. Mistakes are our friends!
    :answer_c: Attempting to set PaintPot's Canvas1.PaintColor to red using a text block. 
    :feedback_c: We’re in the learning zone today. Mistakes are our friends!
    :answer_d: The PaintPot ButtonRed.Click setting the Canvas1.PaintColor to blue. 
    :feedback_d: True. This would be correct syntactically, however, based on the documentation (the name of the button) it would not do what the programmer had intended it to, which would be to set the paint color to red when the ButtonRed is clicked.
    :correct: a,d

    .. raw:: html
    
    	<p>Which of the following are examples of <b><i>semantic errors</i></b> in App Inventor? Check all that apply. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-6-8-7
    :random:
    :practice: T
    :answer_a: Rebuild the app and then retest the app 
    :feedback_a: Here are some strategies to figure this out. The programmer should not rebuild their entire app just because there is a bug in it. They should take their time to examine the code and form a hypothesis about what the bug may be. Then they should design and implement an experiment, and then debug and retest their app.
    :answer_b: Form a hypothesis about what might be wrong, design an experiment to test their hypothesis, perform the experiment, debug, and then retest the app.  
    :feedback_b: That's right! When debugging a program, a programmer should form a hypothesis about what the bug might be, then design and implement an experiment to test their hypothesis. If their hypothesis was correct, then the programmer should debug the app and retest. If their hypothesis was wrong, the programmer should form a new hypothesis
    :answer_c: Form a hypothesis and then retest the app. 
    :feedback_c: Here are some strategies to figure this out. He/she should form a hypothesis about what could possible be wrong with the code, however, just forming a hypothesis and then retesting the app is not enough.
    :answer_d: Immediately start changing code and retest the app. 
    :feedback_d: Here are some strategies to figure this out. It is not recommended that he/she start changing code without first thinking about, and forming an hypothesis, about what could possible be wrong. The programmer should take their time, form a hypothesis, design and implement an experiment, and then debug and retest theirapp.
    :correct: b

    Your classmate discovers that their LightsOff app has a bug in it. What should he/she do to debug their app? 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. quizly:: mscp-6-8-8
    
    
    :quizname: quiz_loop_2_to_10th_power
    
    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1kaGzlMyliW4DjdcPIdvaipA_SCXYg2bXOkqqomQ1wFQ/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vR-wS8zGWHxS2k_ltRfYCEG73d9uIrcbL46VKKYtk5tMsqMQXBotTLUn060-bd3kQa8FCpOogXvDvS-/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--  &lt;p&gt;Create a page named &lt;i&gt;&lt;b&gt;Debugging&lt;/b&gt;&lt;/i&gt; under the &lt;i&gt;Reflections&lt;/i&gt; category of your portfolio and answer the following questions:&lt;/p&gt;
      &lt;p&gt;For each of the 5 bugs in the Caesar Cipher app, explain what the bug was, how to fix it, and the type of error (semantic or syntax).  If you wish, you can take a picture of your corrected blocks and then annotate it to identify and describe the bugs you fixed. 
        &lt;/p&gt; -->
    </div>
    </div>