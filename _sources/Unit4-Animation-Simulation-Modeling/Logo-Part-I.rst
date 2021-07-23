.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Logo Part I
===========

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
        $(document).ready(function() {
            generateSummary(EKmapping['4.04']);
            generateHovers();
    
        });
    </script>
    <h3 id="est-length">Time Estimate: 90 minutes</h3>
    

Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <table>
    <tbody><tr>
    <td>
    <iframe allowfullscreen="" frameborder="0" height="420" src="https://www.youtube.com/embed/9vTB4J0go2A" width="315">
    </iframe>
    (<a href="http://www.teachertube.com/video/mobile-csp-logo-1-preview-438790" target="_blank">Teacher Tube version</a>)
    </td>
    <td width="20px"></td>
    <td>In this lesson you will design, implement, and 
    test algorithms to draw simple shapes using simple commands.
    For example, you will write an algorithm to draw a face made up of
    squares and lines like the one in the picture on the left.     
    <br/>
    <p>
    <b>Objectives:</b> In this lesson you will learn to:
    </p><ul>
    <li>use primitive <i>Logo</i> commands to draw simple shapes;
    </li><li>define simple procedures to simplify the drawing process.
    </li>
    <li>use loops to replace repeated commands.</li></ul>
    <p>In our implementation of Logo, we’ve replaced the Turtle with an Android.
    Here are the drawing commands you can use:
    
    </p><ul>
    <li>The <b>forward</b> command moves the Android <b>forward by 10 pixels</b>.  
    </li><li>The <b>turn</b> command causes the Android to <b>turn right by 90 degrees</b>. 
    </li><li>The <b>penUp</b> and <b>penDown</b> commands puts 
    the Android's pen on or off the canvas.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>
    

Learning Activities
--------------------

.. raw:: html

    <p><h3>Introduction</h3></p>
    <img align="left" hspace="10" src="../_static/assets/img/spiral.png" width="180"/>
    <a href="http://en.wikipedia.org/wiki/Logo_(programming_language)" target="_blank">Logo</a>
    is a programming language that was invented in the 1960s by Seymour Papert primarily
    for educational use.   Papert believed that we learn best when we are building 
    our own knowledge and ideas –  when we build tangible objects 
    that help us create our own mental models to understand the world around us. 
    
    <p>In this lesson the tangible objects you will build are algorithms for drawing 
    simple shapes.
    
    </p><p>Logo’s best known feature is its turtle, an actual picture of a turtle,
    that the user can control by telling it how to move.  As the turtle moves 
    it leaves behind a trail, in other words it draws.  Imagine the trail left behind 
    by an animal as it moves around in the sand on a beach.  
    Logo can be used to create very sophisticated algorithms and  
    very sophisticated drawings, such as the pattern on the left.
    
    </p>
    <p>
    </p><h3>Logo Commands</h3>
    
    The Logo programming language consists of a set of primitive commands that 
    control the turtle.  You saw something like these commands in 
    the Blockly Maze exercises that you did. Taken together these commands constitute
    an <i>abstraction</i> – a language – for drawing shapes. The App Inventor template below has these Logo Commands already written for you. 
    <p>      Existing code segments that you can use are often called <b>libraries</b>.  A software library contains procedures that may be used in creating new programs. The use of libraries already written for you simplifies the task of creating complex programs. You can also write your own libraries of code to use in other App Inventor projects using the backpack feature to share them.
    
    
    </p><p>In this lesson we have
    deliberately created a fairly <i>weak abstraction</i> – one that lets you
    draw shapes, but only with some difficulty.  As you're working on the shapes, 
    think about how you would improve the drawing language;  that is, help us 
    think about a <i>better abstraction</i> for drawing shapes.
    
    </p>
    <h3>Tutorial</h3>
    <p>To get started, 
    <a href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit5/templates/Logo1/Logo1Template.asc" target="_blank">open App Inventor with the Logo 1 Template</a> in a separate tab and follow along with the tutorial below. If the template does not open, download the <a href="http://templates.appinventor.mit.edu/trincoll/csp/unit5/templates/Logo1/Logo1Template.aia" target="_blank">.aia file</a>, go to <a href="http://ai2.appinventor.mit.edu" target="_blank">App Inventor</a> and do File/Import and import in the downloaded .aia file. If you are using iOS companion, please change the Canvas Height property to Fill Parent instead of 100% so it does not cover the buttons.</p>
    When the template opens, you will see a lot of collapsed blocks. <span id="docs-internal-guid-39ef5219-64db-37ef-3dde-eeaa1ea5a99e">
    <span class="yui-tag-span yui-tag" style="font-size: 13px;" tag="span"><b><u>DO NOT OPEN OR EDIT THESE BLOCKS!</u></b></span></span><br/>
    <br/>You can either watch the video tutorial or 
    <a href="https://drive.google.com/open?id=1YXRlbOiAaKvb281YDn-XGI4ZNWDYv4iCRgR1cN7TE0s" target="_blank">
    click here</a> to read the tutorial or use <a href="https://drive.google.com/open?id=1McHT42xH7YT-_rV-Cu3a7l8LYGTM-Fr3NyVxI-wIX8o" target="_blank">the short handout </a>.<p></p>
    
.. youtube:: 8I4bGQRLqPw
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <p> 	(<a href="http://www.teachertube.com/video/mobile-csp-logo-1-438792" target="_blank" title="">Teacher Tube version</a>)
    
    <p>There are three basic types of control structures in designing algorithms:  sequence, selection, and repetition.  Just about any algorithm you can think of can be built using these three types of controls. 
    As you saw in the tutorial, procedures and loops made drawing a square much easier than using a list of commands. Note the big difference between the two algorithms below.  The algorithm on the left uses a simple sequence with copies of the forward and turn blocks to draw a square, whereas the algorithm on the right uses repetition, a for-each counting loop, a much more practical and general approach. The for-each block in this case repeats the statements in its do-slot 4 times.   </p>
    <img src="../_static/assets/img/logoLoop.png" width="50%">
    <h3>Exercises (Pair Programming)</h3>
    <p>After doing the tutorial above, you have drawn 20x20 square using a loop and then refactored the code to use <b>procedural abstraction</b> to create the procedure <b>square20</b>.
     
    </p><p>        For these exercises below, before coding your solution in App Inventor, it would be a good idea  to first write out the solution in pseudocode and discuss it with your coding partner. Download and print <a href="https://drive.google.com/file/d/0B5ZVxaK8f0u9NjNuaTZ5S0Z4OUE/edit?usp=sharing">this graph paper</a>         to use when designing your algorithms in the following exercises.
    </p>
    <ol>
    <li><b>40x40 Square:</b> Design an algorithm for drawing a 40-by-40 square.  Then         implement your algorithm by defining a procedure named <i>square40</i> that         draws a 40-by-40 square. Then modify the <i>ButtonDraw.Click</i> handler so that it calls         the <i>square40</i> procedure.
    To simplify this algorithm, use a <i><b>for-each</b></i> loop to repeat the commands      needed to draw a square.</li>
    <li><b>Line40:</b> Define a procedure name <b><i>line40</i></b>  that draws a <b>line</b> of length 40. Test it by calling it     from the ButtonDraw.Click handler.       </li>
    <li>
    <b><i>Refactor</i></b> your square40 procedure to use a for-each loop and the line40 procedure to draw a 40-by-40 square.  As we learned in an earlier lesson, refactoring means to revise your code         without changing the basic functionality of your app.   Test your algorithm by calling it from the <i>ButtonDraw.Click</i> handler.  </li>
    <li><b>Draw a Face:</b> Design an algorithm for drawing a face with a large square for the head, 2 small squares for eyes, and a line for the mouth, as shown below.   Design and define any other procedures         you need  to help simplify this problem -- e.g., the outline of the head, the eyes, and so on.  Make appropriate use of loops in your algorithm.
        
    <br/><img src="../_static/assets/img/face.png" width="150px"/>
    <p><b>Design first, then code:</b>  This algorithm will be quite a bit more complex than 
    any of the others you’ve done.  You’ll have to use the <i>penUp</i> procedure to 
    lift the Android off of the drawing canvas.  And you’ll have to plan how far 
    to move forward to get the eyes and mouth placed properly.  You will definitely 
    want to plan and test this algorithm on paper or on the board before trying to 
    program it. <b><i>Use your graph paper</i></b> to help figure the distances.
    </p>
    <p>Once you’ve designed a correct algorithm, implement it by defining a 
    procedure named drawFace that draws the face.  Then test your code to 
    make sure you got it right. Post a screenshot of your face drawing on your portfolio. 
    </p>
    <p>Here is a plan to follow:
    </p>
    <ul>
    <li>First,  draw a <b><i>scale model</i></b>  of your face.  For this you need to decide what 
    each square on the graph paper represents -- e.g., is each square 10 pixels?  5 pixels?
    </li>
    <li>Based on your model, write out the commands for drawing the face using <b>pencil 
    and paper</b> -- i.e., write out your algorithm right on the graph paper.
    </li>
    <li>Code your face-drawing algorithm and test it.  <b>Define a procedure named drawFace and 
    call it in the ButtonDraw.Click procedure</b>.  Keep testing and refining your algorithm until it 
    correctly draws a face. 
    </li>
    <li><b>Abstraction:</b>  Once you can successfully drawn the face, <b>refactor your code</b> to 
    make good use of procedures that break the face into parts, e.g., head,           left eye, right eye, mouth, moves.
    </li>
    </ul>
    </li>
    <li><b>Refactor</b>  your drawFace procedure by breaking it up into smaller procedures.  
    This will make it easier to understand.   For example, here’s a possible algorithm you might use:
    <br/>
    <table>
    <tbody><tr>
    <td>
    <pre> To drawFace do:
    square100
    positionAndDrawLeftEye
    positionAndDrawRightEye
    positionAndDrawMouth
    returnToStartOfFace
    </pre>
    </td>
    <td>
    <img src="../_static/assets/img/DrawFace.png" width="200px"/>
    </td>
    </tr>
    </tbody></table>
              
        
    As their names suggest, the sub-procedures will include the various penUp, penDown, and move 
    commands to position the eyes and mouth correctly and to return the Android to its starting 
    position (at the bottom left corner of the face).  Remember: Ideally, your algorithms should 
    leave the Android in the same state when it is finished drawing the head as when it started.
    </li>
    </ol>
    <!--
    &lt;h2&gt;Some Solutions &amp;amp; Hints&lt;/h2&gt;
    &lt;gcb-youtube videoid=&quot;G8dLsWZnYAQ&quot; instanceid=&quot;B2CUBJnVbJe3&quot;&gt;&lt;/gcb-youtube&gt;&amp;nbsp;(&lt;a href=&quot;http://www.teachertube.com/video/mobile-csp-logo-1-project-solutions-438793&quot; target=&quot;_blank&quot; title=&quot;&quot;&gt;Teacher Tube version&lt;/a&gt;)
    -->
    <h3>AP CSP Pseudocode: Control Structures</h3>
    <p>In the AP CSP exam, there are questions that involve a robot moving in a grid following simple commands similar to our Logo App. The commands used in the exam are:
    </p>
    <ul>
    <li> <b>MOVE_FORWARD()</b> : The robot moves 1 square forward in the direction it is facing.
    </li><li> <b> ROTATE_RIGHT() </b>: The robot turns right 90 degrees, staying in the same square but facing right.
    </li><li><b> ROTATE_LEFT()</b> : The robot turns left 90 degrees, staying in the same square but facing left.
    </li><li><b> CAN_MOVE( <em>direction</em> )</b> : This command can be used with 4 possible directions: <b>left, right, forward,</b> and <b>backward</b>. It returns true if there is an open square in the specified direction from the square that the robot is in. 
    </li></ul>
    <p>  The AP CS Principles Exam uses a text-based and a block-based pseudocode for questions that involve code. The <a href="https://drive.google.com/file/d/0B5ZVxaK8f0u9c1VlWFJDRHl0dEk/view" target="_blank">AP CSP reference sheet</a> is provided during the exam describing this pseudocode. The AP CSP pseudocode for  basic control structures compared to App Inventor blocks is shown below:
    </p><table border="">
    <tbody><tr> <th>Function</th><th>Text Style</th> <th width="25%">Block Style</th><th>App Inventor</th></tr>
    <tr><td>Assignment</td><td>a ← <em>expression</em></td><td><div class="yui-wk-div" id="APblocks">
    <bl>a ← <bl>expression</bl></bl></div></td> <td><img src="../_static/assets/img/setexpr.png" width="70%"/></td></tr>
    <tr><td>Display</td><td>DISPLAY(<em>expression</em>)</td><td><div class="yui-wk-div" id="APblocks">
    <bl>DISPLAY <bl>expression</bl></bl></div></td>
    </tr>
    <tr><td>Expressions</td><td>a + b, a - b, a * b, a/b, a mod b </td><td><div class="yui-wk-div" id="APblocks">
    <bl>a + b</bl></div></td>
    <td><img src="../_static/assets/img/setexpr2.png" width="70%"/></td></tr>
    <tr><td>Selection (else optional)</td> <td>IF (<em>condition</em>) <br/> {
    <br/>   <em>block of statements</em><br/> } <br/>
    ELSE <br/>   {
    <br/>   <em>block of statements</em><br/> } </td><td><div class="yui-wk-div" id="APblocks">
    <bl class="dark">IF <cond>condition</cond><br/>
    <bl> block of statements </bl><br/>
    ELSE<br/>
    <bl> block of statements</bl><br/>
    </bl></div></td>
    <td><img src="../_static/assets/img/ifelse.png" width="50%"/></td>
    </tr>
    <tr><td>Condition</td><td>a = b, a ≠ b, a &lt; b, a &gt; b,a &lt;= b,a &gt;= b <br/>        NOT(<em>condition</em>), (condition AND condition),   (condition OR condition)
    </td><td></td>
    <td><img src="../_static/assets/img/logicblocks.png" width="60%"/></td></tr>
    <tr><td>Repetition</td> <td>REPEAT n times  <br/>{
    <br/>   <em>block of statements</em><br/> }
    </td><td>
    <div class="yui-wk-div" id="APblocks"><bl class="dark">REPEAT n times<br/>
    <bl> block of code </bl><br/>
    </bl></div></td>
    <td><img src="../_static/assets/img/forloop.png" width="80%"/></td>
    </tr>
    <tr><td>Repetition</td> <td>REPEAT UNTIL (<em>condition</em>)   <br/> {
    <br/>   <em>block of statements</em><br/> }</td><td>
    <div class="yui-wk-div" id="APblocks">
    <bl class="dark">REPEAT UNTIL <cond>condition</cond><br/>
    <bl>block of code</bl><br/>
    </bl></div></td>
    <td><img src="../_static/assets/img/whilenot.png" width="60%"/></td>
    </tr>
    </tbody></table>
    <p>The AP pseudocode robot navigation commands can be used within selection and repetition control structures like below:
    
    </p><pre>REPEAT UNTIL ( GoalReached() )
    {
        IF (CAN_MOVE(forward))
        {
            MOVE_FORWARD()
        }
    }
    </pre>
    <p>In the REPEAT UNTIL(condition) loop:
      </p><ul>
    <li>The code inside the loop is repeated until the boolean condition evaluates to true. </li>
    <li> If the condition evaluates to true initially, the loop body is not executed at all.</li>
    <li>There can be an <b>infinite loop</b> if the ending condition never evaluatea to true.</li>
    </ul>
    Note that the curly brackets { } are used to indicate the start and end of a block of code, for example the repetition control structure. The parenthesis () are used after a procedure name to indicate that it is a procedure and to give it any data it might need inside the parentheses. Some practice problems using these commands are below.
    
    <p>
    </p>

Summary
--------

.. raw:: html

    <p>
    In this lesson, you learned how to:
    <div class="yui-wk-div" id="summarylist">
    </div><br/>
    <p></p>

Self-Check
-----------

.. raw:: html

    <p>
    
.. fillintheblank:: mcsp-4-4-1
    :casei:

    What is the name of the computer language that uses a turtle to implement drawing algorithms? Type your answer into the textbox (spelling counts).  |blank|

    - :Logo: Logo is a programming language invented in the 1960s by Seymour Papert and used mostly for educational purposes.  It can be used to draw simple and complex geometric shapes. 
      :x: 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-4-4-2
    :random:
    :practice: T
    :answer_a: True
    :feedback_a: Mistakes are welcome here! Try reviewing this...An algorithm can indeed be expressed in a programming language, such as App Inventor or Logo, but it can also be expressed in English or pseudocode.
    :answer_b: False
    :feedback_b: Correct.  An algorithm can indeed be expressed in a programming language, such as App Inventor or Logo, but it can also be expressed in English or pseudocode.
    :correct: b

    True or False? An algorithm is a precise sequence of statements that must be expressed in a computer language. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-4-4-3
    :random:
    :practice: T
    :answer_a: A square 
    :feedback_a: Don’t worry, it’s hard! Let’s go back and try it again. Notice that there are two forwards followed by a turn followed by one forward and so on.  This algorithm draws a rectangle.
    :answer_b: A right angle 
    :feedback_b: Don’t worry, it’s hard! Let’s go back and try it again. This algorithm draws a rectangle.
    :answer_c: A rectangle
    :feedback_c: That's right. This algorithm would draw a rectangle whose length is twice as long as its width. 
    :answer_d: A circle 
    :feedback_d: Don’t worry, it’s hard! Let’s go back and try it again. This algorithm draws a rectangle.
    :correct: c

    .. raw:: html
    
    	<p>Assuming that forward tells the Android to move forward by 10 pixels and turn tells it to turn right by 90 degrees, what shape would be drawn by this algorithm?</p>
		forward<br />
		forward<br />
		turn<br />
		forward<br />
		turn<br />
		forward<br />
		forward<br />
		turn<br />
		forward<br />
		turn<br />


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


.. mchoice:: mcsp-4-4-4
    :random:
    :practice: T
    :answer_a: x = 0
    :feedback_a: Yes, if x is 0 or a negative number, the loop would keep subtracting 1 from it and x would never be greater than 0, so it would be an infinite loop.
    :answer_b: x = 1
    :feedback_b: Since 1 is greater than 0, the loop would never run.
    :answer_c: x = 10
    :feedback_c: Since 10 is greater than 0, the loop would never run.
    :correct: a

    .. raw:: html
    
    	<p>Given the following code segment, which value of x would cause an infinite loop?</p>
    	<pre>REPEAT UNTIL (x &gt; 0)
    	{
    	   x ← x - 1
    	}
    	</pre>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. quizly:: mscp-4-4-9
    
    
    :quizname: quiz_scrambled_dollars_loop
    
    
.. quizly:: mscp-4-4-10
    
    
    :quizname: quiz_loop_stars
    <br/>
    

Sample AP CSP Questions
------------------------

.. raw:: html

    <p>
    
.. mchoice:: mcsp-4-4-5
    :random:
    :practice: T
    :answer_a: &nbsp;<br><div style="text-align: left;"><img src="../_static/assets/img/Q17A1.png" class="yui-img" title="" alt="" style="line-height: 1.22;"></div>
    :feedback_a: 
    :answer_b: &nbsp;<br><img src="../_static/assets/img/Q17A2.png" class="yui-img" title="" alt=""><br>
    :feedback_b: 
    :answer_c:  <br><img src="../_static/assets/img/Q17A3.png" class="yui-img" title="" alt=""><br>
    :feedback_c: 
    :answer_d:  <br><img src="../_static/assets/img/Q17A4.png" class="yui-img" title="" alt=""><br>
    :feedback_d: 
    :correct: a

    .. raw:: html
    
    	<p>The following question uses a robot in a grid of squares. The robot is represented as a triangle, which is initially in the bottom left square of the grid and facing right.</p>
    	<img alt="" class="yui-img selected" src="../_static/assets/img/Q17SquareQuestion.png" style="line-height: 1.22;" title=""/>
    	<p>Consider the following code segment, which moves the robot in the grid.</p>
    	<img alt="" class="yui-img selected" src="../_static/assets/img/Q17Code.png" style="line-height: 1.22;" title=""/>
    	<p>Which of the following shows the location of the robot after running the code segment?</p>

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-4-4-6
    :random:
    :practice: T
    :answer_a: &nbsp;<img src="../_static/assets/img/APExamPrepQ14ChoiceA.png" class="yui-img selected" title="" alt="" align="center" style="display: block;">
    :feedback_a: 
    :answer_b:  <img src="../_static/assets/img/APExamPrepQ14ChoiceB.png" class="yui-img selected" title="" alt="" align="center" style="display: block;">
    :feedback_b: 
    :answer_c: &nbsp;<img src="../_static/assets/img/APExamPrepQ14ChoiceC.png" class="yui-img" align="center" style="display: block;" title="" alt="">
    :feedback_c: 
    :answer_d: &nbsp;<img src="../_static/assets/img/APExamPrepQ14ChoiceD.png" class="yui-img" align="center" style="display: block;" title="" alt="">
    :feedback_d: 
    :correct: d

    The program segment below is intended to move a robot in a grid to a gray square. The program segment uses the procedure GoalReached, which evaluates to true if the robot is in the gray square and evaluates to false otherwise. The robot in each grid is represented as a triangle and is initially facing left. The robot can move into a white or gray square, but cannot move into a black region.For which of the following grids does the program NOT correctly move the robot to the gray square?

    .. raw:: html

        <img alt="" class="yui-img" src="../_static/assets/img/APExamPrepQ14.png" style="width: 200px;" title=""/>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


.. mchoice:: mcsp-4-4-7
    :random:
    :practice: T
    :answer_a:  Changing line 6 to IF(item = count)
    :feedback_a: 
    :answer_b:  Changing line 6 to IF(myList[item] = val)
    :feedback_b: 
    :answer_c:  Moving the statement in line 5 so that it appears between lines 2 and 3
    :feedback_c: 
    :answer_d:  Moving the statement in line 11 so that it appears between lines 9 and 10
    :feedback_d: 
    :correct: c

    .. raw:: html
    
    	<p><b>AP 2021 Sample Question</b>:  The following procedure is intended to return the number of times the value val appears in the list myList. The procedure does not work as intended.</p>
    	
    	<pre>
    	Line 1: PROCEDURE countNumOccurences(myList, val)
    	Line 2: {
    	Line 3: FOR EACH item IN myList
    	Line 4: {
    	Line 5: count 0
    	Line 6: IF(item = val)
    	Line 7: {
    	Line 8: count count + 1
    	Line 9: }
    	Line 10: }
    	Line 11: RETURN(count)
    	Line 12: }
   		</pre>
   		
   		<p>Which of the following changes can be made so that the procedure will work as intended?</p>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


.. mchoice:: mcsp-4-4-8
    :random:
    :practice: T
    :answer_a: &nbsp;<img src="../_static/assets/img/APExamPrepQ17ChoiceA.PNG.jpg" class="yui-img" title="" alt="">
    :feedback_a: 
    :answer_b: &nbsp;<img src="../_static/assets/img/APExamPrepQ17ChoiceB.PNG.jpg" class="yui-img" title="" alt="">
    :feedback_b: 
    :answer_c: &nbsp;<img src="../_static/assets/img/APExamPrepQ17ChoiceC.PNG.jpg" class="yui-img" title="" alt="">
    :feedback_c: 
    :answer_d: &nbsp;<img src="../_static/assets/img/APExamPrepQ17ChoiceD.PNG.jpg" class="yui-img" title="" alt="">
    :feedback_d: 
    :correct: b,c
    
    .. raw:: html
    
    	<p><b>AP 2021 Sample Question</b>: Consider the following procedure.</p>
    	<table border="1"><tbody>
    	<tr>
    		<th>Procedure Call</th>
    		<th>Explanation</th>
    	</tr>
    	<tr>
    		<td width="40%" style="padding:2px">drawCircle(xPos, yPos, rad)</td>
    		<td>Draws a circle on a coordinate grid with center (xPos, yPos) and radius rad</td>
    	</tr>

    	</tbody>
    	</table>
 		<br />
 		<p>The drawCircle procedure is to be used to draw the following figure on a coordinate grid.</p>
 		<p><img alt="" class="yui-img" src="../_static/assets/img/APExamPrepQ17Question.png" title="" /></p>
 		<br />
 		<p>Which of the following code segments can be used to draw the figure?</p>
 		<p><b>Select <u>two</u> answers.</b></p>

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1M1fuADAP1re1FZrmaY_P8m0Uz7RE3Gbi3YXHH5ULEV8/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vTmOjmUgG_8I1xBV49qd_Pv15Tk2sedyycqNvVAT6xpFcpOhGAsoFDpD0zOsFmvtWcPP-toQ6P6-pkE/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--&lt;p&gt;Create a new page named &lt;i&gt;&lt;b&gt;Logo 1&lt;/b&gt;&lt;/i&gt; under the &lt;i&gt;Reflections&lt;/i&gt; category of your portfolio and write brief answers to the following questions. &lt;/p&gt;
      &lt;ol&gt;
    &lt;li&gt;Include a screenshot of your app&#39;s face drawing and the code involved showing the use of a loop and a procedure. You can take a screenshot on most Android devices by pressing the power button and the volume down button at the same time and then emailing the photo from the gallery to yourself.
        &lt;/li&gt;&lt;li&gt;Can you draw a triangle with this set of Logo commands?  Discuss how or why not. &lt;br&gt;&lt;i&gt;Note: &quot;...this set of Logo commands&quot; refers to the commands available in the app (forward, turn, penUp, penDown, etc.)&lt;/i&gt;&lt;/li&gt;
        &lt;li&gt;If you were designing the Logo language, how would you change some of our basic commands so that it would be easy to draw a triangle and easier to draw other shapes — i.e., what should the basic commands do that would make drawing easier?&lt;/li&gt;
        &lt;li&gt;What weaknesses do you find in using the procedures (the abstractions) we gave you — forward, turn — for drawing simple shapes?   How would you change the definitions of these procedures to make it easier to draw shapes?  Give a specific example that illustrates how a more powerful set of procedures would improve the app.&lt;/li&gt;
      &lt;/ol&gt;-->
    </div>
    </img></div>