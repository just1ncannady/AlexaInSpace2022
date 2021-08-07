.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Paint Pot Projects
==================

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
            generateSummary(EKmapping['3.04']);
            generateHovers();
    
    
    
        });
    </script>
    <h3 id="est-length">Time Estimate: 90 minutes</h3>
    

Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <table><tbody>
    <tr>
		<td colspan=2><b><i>Be creative!</i></b> In this lesson you will complete several small programming projects that add enhancements to the Paint Pot app.  Hints and suggestions are provided.</td>
	</tr>
	<tr>
    <td valign="top">
    <iframe allowfullscreen="" frameborder="0" height="325" width="270" src="https://www.youtube.com/embed/2JIoJ-I3jH0">
    </iframe>
    </td>
    <td valign="top">
		<div><b>Learning Objectives:</b>&nbspI will learn to</div>
		  <ul>
          <li>program additional events into an existing mobile app</li>
          <li>solve simple programming problems</li>
          </ul>
          <div><b>Language Objectives:</b>&nbspI will be able to</div>
          <ul>
           <li>explain the advantages of collaboration when developing and improving an app using supporting details and examples</li>
		   <li>discuss errors in my program when I run my code, including how the errors could be fixed and tested</li>
		   <li>describe the functionality of an app using key vocabulary such as component, event, and pseudocode, out loud and in writing, with the support of <a href="https://docs.google.com/presentation/d/1n-K4AQ_maHcXekzcfERQ9dxj91nqv9ytwJx4ZkAp8zw/copy" target="_blank" title="">vocabulary notes</a> from previous lessons</li>       
          </ul>
    </td>
    
    </tr>
    </tbody></table>
    (<a href="http://www.teachertube.com/video/mobile-csp-paint-pot-projects-preview-438235" target="_blank" title="">Teacher Tube version</a>)<br/>
    

Learning Activities
--------------------

.. raw:: html

    <p><h3>Creative Mini Projects: Enhancing Paint Pot</h3>
    <p>To get started, open App Inventor with your completed Paint Pot app from lesson 3.2 in a separate tab, and then complete the programming 
      projects outlined below. Additional information is available in the 
      <a href="https://docs.google.com/document/d/1s7PTuvw0fg03iEVUIW11yvHb1TzZdk6T_woT4grvQZY/" target="_blank">text 
        version of this lesson</a>.
    </p>
    <ol>
    <li>Add a custom image to the app instead of using the cat image that is provided. 
        You can upload images to your project from either the Designer View  or Blocks Editor view.   
        Use the image as the Canvas background image.  Make sure the image doesn’t have any copyright restrictions.
      </li>
    <li>Add a button to support a 4th color option for the app.
      </li>
    <li>The app currently has a ButtonPlus and ButtonMinus. But, we only completed the code for ButtonPlus. Now that
        you understand how to increment variables by 1, implement an algorithm for ButtonMinus that will subtract 1 from
        dotsize. </li>
    <li><b>Test Cases:</b> It is important to test out code to make sure it does what is expected, especially for
      critical values or boundary values. Check if your program performs correctly in the following test
      cases and make note of which tests fail--we will fix those soon: </li>
    <div class="yui-wk-div" style="margin-left: 30px;">
    <table>
    <tbody>
    <tr>
    <td style="background-color: #cfe2f3;"><b>Test Name</b></td>
    <td style="background-color: #cfe2f3;"><b>Inputs</b></td>
    <td style="background-color: #cfe2f3;"><b>Expected Outputs</b></td>
    </tr>
    <tr>
    <td style="width: 120px;">Standard Plus Test </td>
    <td style="width: 300px;">With "Dot Size = 5", touch the canvas to draw a dot, press the + button, and 
                  touch the canvas to draw a second dot. </td>
    <td style="width: 300px;">The dotsize label should show "Dot Size = 6" and the second dot should be larger 
                  than the first dot. </td>
    </tr>
    <tr>
    <td>Standard Minus Test</td>
    <td>With "Dot Size = 5", touch the canvas to draw a dot, press the + button, and touch the canvas to draw 
                  a second dot.</td>
    <td>The dotsize label should show "Dot Size = 4" and the second dot should be smaller 
                  than the first dot.</td>
    </tr>
    <tr>
    <td>Lower Bounds Test </td>
    <td>With "Dot Size = 1", touch the canvas to draw a dot, then press the minus button, and touch the canvas 
                  to draw a second dot.</td>
    <td> The display should stay at "Dot Size = 1" and the second dot should be the same size as
                  the first dot. </td>
    </tr>
    </tbody>
    </table>
    </div>
    <li><b>If Block Exercise:</b> In computer programming, a bug is an error or defect, that prevents the app from
        working the way it is supposed to. The <i>Lower Bounds Test</i> above demonstrates a bug, the value of dotsize
        will eventually become negative. If dotsize is negative, what will be drawn when the user touches the screen?
        Try fixing this bug by adding an if/then algorithm to the ButtonMinus block. (Hint: The If/Then block is found
        under Control in the Toolbox. If you’ve done the I Have A Dream Part 2 lesson, you’ve already seen how to use an
        if/else block. You will need the = block from the Math drawer and to pull down its menu to get &lt;). Once you
        have fixed the bug, test case 3 should generate the given results.</li>
    <li><b>Program Requirement:</b> Naturally the dot size cannot be less than 1, but should there be an upper bound
        to the dot size? As an app designer, we can set an upper bound for the dot size and make this a program
        requirement. We will set a program requirement that the dot size cannot get larger than 25. Add an If block to
        the ButtonPlus block that will implement the new program requirement and satisfy the new test case we will
        define:</li>
    <div class="yui-wk-div" style="margin-left: 30px;">
    <table>
    <tbody>
    <tr>
    <td style="background-color: #cfe2f3;"><b>Test Name</b></td>
    <td style="background-color: #cfe2f3;"><b>Inputs</b></td>
    <td style="background-color: #cfe2f3;"><b>Expected Outputs</b></td>
    </tr>
    <tr>
    <td style="width: 120px;">Upper Bounds Test</td>
    <td style="width: 300px;">With "Dot Size = 25", touch the canvas to draw a dot, then press the plus button, 
                  and touch the canvas to draw a second dot.</td>
    <td style="width: 300px;"> The display should stay at "Dot Size = 25" and the second dot should be the same size as
                  the first dot. </td>
    </tr>
    </tbody>
    </table>
    </div>
    <li>Currently, if a user wants to use a larger dot and then use a smaller dot (or vice versus), they have to
        continually press the ButtonMinus (or ButtonPlus). If the current value of dotsize is 25, getting to a size of 4
        would be pain. For easier use, add a button that resets the size of the dot (circle) back to its original value.
        (HINT: You’ll need a second variable here to remember the original value of the dotsize.) </li>
    <li><b>Optional:</b> Instead of using an existing image, take a photo with the camera and use that as the Canvas 
        background image! (Hint: For this you’ll need to use a new Button, the Camera component from the Media drawer, and the Camera’s TakePicture command and the
        AfterPicture event handler where you can set the image returned by the camera as Canvas' background image.)  
      </li>
    <li><b>Optional:</b> Add a <a href="http://ai2.appinventor.mit.edu/reference/components/social.html#Sharing" target="_blank">Social/Sharing component</a> and a share button to email what is drawn on the canvas using the Sharing.ShareFile block with the <a href="http://ai2.appinventor.mit.edu/reference/components/animation.html#Canvas" target="_blank">Canvas.Save block</a>. You will have to set up an email account on your tablet to use the share component.  (This may not work yet on iOS devices). </li>
    <li><b>Optional:</b> Create one or more of your own enhancements for your app. Remember to write your ideas 
        down in pseudocode before you begin programming.
      </li>
    </ol>
    <!-- 
    &lt;h2&gt;Solutions&lt;/h2&gt; 
    
    &lt;p&gt;It is important to explore with App Inventor and become accustomed to 
      programming without explicit instructions. So try out the challenges listed above 
      and see how far you can get. If you get stuck -- or if, after you&#39;ve finished, you&#39;d like to compare 
      your solutions to ours --  check out the following videos, which show how we solved the problems.
    &lt;/p&gt;
    
    &lt;h3&gt;Solutions for Exercises 1, 2, and 3 above (&lt;a target=&quot;_blank&quot; href=&quot;http://www.teachertube.com/video/paintpot1solutions-347845&quot;&gt;TeacherTube version&lt;/a&gt;)&lt;/h3&gt; 
    &lt;gcb-youtube videoid=&quot;De4k1vPs3vU&quot; instanceid=&quot;qEivSJS4crpN&quot;&gt;&lt;/gcb-youtube&gt;    
      
    &lt;h3&gt;Solutions for Exercises 4, 5, and 6 above (&lt;a href=&quot;http://www.teachertube.com/video/mobile-csp-paint-pot-projects-solutions-part-2-438239&quot; target=&quot;_blank&quot; title=&quot;&quot;&gt;TeacherTube version&lt;/a&gt;) 
    &lt;gcb-youtube videoid=&quot;Pg5_khG7Zxk&quot; instanceid=&quot;D6Nq0YJjItKJ&quot;&gt;&lt;/gcb-youtube&gt;
      
    
    &lt;/h3&gt;
    -->
    <h3>AP CSP Pseudocode: If Statements</h3>
    <p>Selection with if statements is used in every programming language. The AP CS Principles Exam uses a text-based and a block-based pseudocode for questions that involve code. The <a href="https://drive.google.com/file/d/0B5ZVxaK8f0u9c1VlWFJDRHl0dEk/view" target="_blank">AP CSP reference sheet</a> is provided during the exam describing this pseudocode. The table below compares AP CSP pseudocode to App Inventor blocks for  if statements and relational operators. Note that the curly brackets { } are used in AP text pseudocode (and in many text-based programming languages) to indicate the start and end of a block of code.
      
      </p><p>The <b>relational operators</b> (=, ≠, &lt;, &gt;,&lt;=, &gt;=) are used inside if statements to compare variables with values or mathematical expressions, and they evaluate to a <b>Boolean</b> (true, false) value. For example, a = b evaluates to true if a and b are equal; otherwise, it evaluates to false. The logical operators NOT, AND, and OR can be used to combine conditions inside an if statement and also evaluate to a true or false Boolean value. </p>
    <p>If you have trouble telling &lt; and &gt; apart, think of a number line and think of &lt; and &gt; as arrows; &lt; (less than) points towards 0 and smaller numbers on the number line and &gt; (greater than) points towards the larger numbers on the number line. 
      </p>
    <table border="">
    <tbody><tr> <th>Function</th><th>Text Style</th> <th width="25%">Block Style</th><th>App Inventor</th></tr>
    <tr><td>Selection (else optional)</td> <td>IF (<em>condition</em>) <br/> {
        <br/>   <em>block of statements</em><br/> } <br/>
         ELSE <br/>  {
        <br/>   <em>block of statements</em><br/> } </td><td><div class="yui-wk-div" id="APblocks">
    <bl class="dark">IF <cond>condition</cond><br/>
    <bl> block of statements </bl><br/>ELSE<br/>
    <bl> block of statements</bl><br/>
    </bl></div></td>
    <td><img src="../_static/assets/img/ifelse.png" width="50%"/></td>
    </tr>
    <tr><td>Relational Operators</td><td>a = b<br/> a ≠ b<br/> a &lt; b <br/> a &gt; b<br/> a &lt;= b <br/> a &gt;= b 
        </td><td></td>
    <td><img src="../_static/assets/img/AppInvrelops.png" width="60%"/></td></tr>
    <tr><td>Logical Operators</td><td>
        NOT(<em>condition</em>) <br/> (condition AND condition) <br/>   (condition OR condition)
        </td><td></td>
    <td><img src="../_static/assets/img/logicblocks.png" width="60%"/></td></tr>
    </tbody></table>
    <p>
    We usually use if/else blocks to make a two way choice, but you can make a three way or even an unlimited number of choices with <b>nested else if statements</b>. In App Inventor, use the blue gear sign at the top of the if block and drag in as many else-if's as you need and end with an else block. For example, the block below will print out "Excellent" if your score is greater than 10, "Good job!" if your score is greater than 5, or "Keep Trying".  If the first condition is false (for example if score is 2), it will fall down to the next condition and so on until it reaches that last else. <br/>
    <img src="../_static/assets/img/ifelseif.png" width="450"/>
    </p>
    <p>In addition, some conditional statements can be written as equivalent Boolean expressions or vice versa. For example,
      </p><pre>  answer ← (x &gt; 0 AND x &lt; 10)
      
      is equivalent to
      
      IF (x &gt; 0 AND x &lt; 10)
      {
    
            answer ← true;
      }
    
      </pre>
    

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
	
	<h3>Check Your Understanding</h3>
    <p>Complete the following self-check exercises. 
	</p>
    
.. quizly:: mscp-3-4-7
    
    
    :quizname: quiz_initialize_variable
    
    <br/>
    
.. quizly:: mscp-3-4-8
    
    
    :quizname: quiz_incrementing
    
    <br/>
    
    
.. quizly:: mscp-3-4-9
    
    
    :quizname: quiz_simple_if_else
    <br/>
    <br/>
.. mchoice:: mcsp-3-4-1
    :random:
    :practice: T
    :answer_a: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
    :feedback_a: These values are in the middle of the legal range from 1 to 12, so they are not boundary values.
    :answer_b: 0 and 1, also 12 and 13
    :feedback_b: Since the valid values for a month is 1 to 12, these are examples of both valid and invalid boundary values.
    :answer_c: -99 and +99
    :feedback_c: While these are both invalid values, the are not on the boundary of the valid range of 1 to 12.
    :answer_d: 28, 29, 30, 31, and 32.
    :feedback_d: These are examples of boundary values for the day of the month, but not the month number which has a valid range of 1 to 12.
    :correct: b

    When testing software, it is important to test critical values or boundary values--both valid and invalid values at the extremes of a range of legal values. In an app where the user enters a number for the month of the year, what would be appropriate boundary values to check? 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

.. mchoice:: mcsp-3-4-2
    :random:
    :practice: T
    :answer_a: Not so good!
    :feedback_a: Sorry, "Not so good!" would only display if score is less than 5.
    :answer_b: Getting better!
    :feedback_b: That's right! Since score is not less than 5, it would fall down to the next condition, and since score is less than 10, it would print it out.
    :answer_c: Going strong!
    :feedback_c: Sorry, score is less than 10 so the condition before this one would work.
    :correct: b

    What would the following code print out if the score was 6?  

    .. raw:: html

        <img src="../_static/assets/img/ifelseifQ.png" width="400"/>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

.. mchoice:: mcsp-3-4-3
    :random:
    :practice: T
    :answer_a: "Not so good!"
    :feedback_a: No, 10 is not less than 5.
    :answer_b: "Getting better!"
    :feedback_b: No because 10 is not less than 10!&nbsp;
    :answer_c: "Going strong!"
    :feedback_c: Yes, since 10 is not less than 5 and is not less than 10, it would fall through to the last else statement.
    :correct: c

    What would the following code print out if the score was 10?  

    .. raw:: html

        <img src="../_static/assets/img/ifelseifQ.png" width="400"/>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

.. mchoice:: mcsp-3-4-4
    :random:
    :practice: T
    :answer_a:  II only
    :feedback_a: 
    :answer_b: (B) I and II only
    :feedback_b: 
    :answer_c: (C) I and III only
    :feedback_c: 
    :answer_d: (D) II and III only
    :feedback_d: 
    :correct: d

    AP 2021 Sample Question:  In a certain country, a person must be at least 16 years old to drive a car and must be at least 18 years old to vote. The variable age represents the age of a person as an integer. Which of the following expressions evaluates to true if the person is old enough to drive but not old enough to vote, and evaluates to false otherwise? I. (age ≥ 16) AND (age ≤ 18) II. (age ≥ 16) AND (NOT(age ≥ 18))III. (age &lt; 18) AND (NOT(age &lt; 16))


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

.. mchoice:: mcsp-3-4-5
    :random:
    :practice: T
    :answer_a:  x = 1, y = 2, z = 3
    :feedback_a: 
    :answer_b: (B) x = 1, y = 3, z = 2
    :feedback_b: 
    :answer_c: (C) x = 2, y = 3, z = 1
    :feedback_c: 
    :answer_d: (D) x = 3, y = 2, z = 1
    :feedback_d: 
    :correct: d

    .. raw:: html
    	
    	<p><b>AP 2021 Sample Question</b>: The following code segment is intended to set max equal to the maximum value among the integer variables x, y, and z. The code segment does not work as intended in all cases.</p>
        <p><img alt="" class="yui-img" src="../_static/assets/img/APExamPrepQ9image_question.PNG.jpg" title=""/></p>
        <p>Which of the following initial values for x, y, and z can be used to show that the code segment does not work as intended?</p>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

.. mchoice:: mcsp-3-4-6
    :random:
    :practice: T
    :answer_a: <img src="https://course.mobilecsp.org/mobilecsp/assets/img/APExamPrepQ18ChoiceA.PNG.jpg?seed=12167&amp;url=assets/img/APExamPrepQ18ChoiceA.PNG.jpg" class="yui-img" title="" alt="">
    :feedback_a: 
    :answer_b: <img src="https://course.mobilecsp.org/mobilecsp/assets/img/APExamPrepQ18ChoiceB.PNG.jpg?seed=4239&amp;url=assets/img/APExamPrepQ18ChoiceB.PNG.jpg" class="yui-img" title="" alt="">
    :feedback_b: 
    :answer_c: <img src="https://course.mobilecsp.org/mobilecsp/assets/img/APExamPrepQ18ChoiceC.PNG.jpg?seed=29728&amp;url=assets/img/APExamPrepQ18ChoiceC.PNG.jpg" class="yui-img" title="" alt="">
    :feedback_c: 
    :answer_d: <img src="https://course.mobilecsp.org/mobilecsp/assets/img/APExamPrepQ18ChoiceD.PNG.jpg?seed=36266&amp;url=assets/img/APExamPrepQ18ChoiceD.PNG.jpg" class="yui-img" title="" alt="">
    :feedback_d: 
    :correct: a,d

    .. raw:: html
    	
    	<p><b>AP 2021 Sample Question</b>: In the following statement, val1, val2, and result are Booleanvariables.</p>
    	<p><img alt="" class="yui-img" src="../_static/assets/img/APExamPrepQ18image_question.PNG.jpg" title=""/>
    	<p>Which of the following code segments produce the same result as the statement above for all possible values of val1 and val2?</p>
    	<p><b>Select <u>two</u> answers.</b></p>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1CcNfxNxoOI-Zr1tIEhpVJmMmYvczLVF-dZmBlmvou4I/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vT9q9RPeuFXRC4AjRmSm8MuCuiaRrX4yOba4CM0D5zRYxuTjAf4gcfMbKkHRjk8cU11CoC_uEEh_ACb/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--  &lt;p&gt;Create a page named &lt;i&gt;&lt;b&gt;Paint Pot Projects&lt;/b&gt;&lt;/i&gt; in your portfolio and give brief answers to the following questions:&lt;/p&gt;
      &lt;ol&gt;
        &lt;li&gt;For enhancement #5 above (the If Block Exercise) give a  brief descriptions of your solution
          to this problem. Provide a screenshot of your code -- the revised blocks  -- and 
          describe how the if/else block works to solve the problem in this case. If appropriate, 
          include a description of any significant problems or bugs you encountered in solving 
          this problem. The &lt;a href=&quot;https://support.microsoft.com/en-us/instantanswers/671b2932-1274-452a-905b-f7ed3c7d8818/open-snipping-tool-and-take-a-screenshot&quot; target=&quot;_blank&quot;&gt;Snipping Tool&lt;/a&gt; in Windows can be used to easily take screenshots of what&#39;s on your screen. App Inventor now has a &lt;em&gt;Download Blocks as Image&lt;/em&gt; feature (right click on the white space in the blocks editor to choose) that also can be used to take a screenshot of all of your code, see &lt;a href=&quot;https://www.youtube.com/watch?v=t7uhYaaflzg&quot;&gt;video tutorial&lt;/a&gt;.
          &lt;/li&gt;
        &lt;li&gt;When you use the Camera component to take a picture as the Canvas background, explain
          why the picture goes away when the app is restarted. HINT:  Think about the different
          hardware components we talked about in an earlier lesson and where on the device 
          the picture is stored.  What do you think could be done to prevent the picture from 
          disappearing when the app is restarted?
        &lt;/li&gt;
      &lt;/ol&gt;-->
    </div>
    </div>