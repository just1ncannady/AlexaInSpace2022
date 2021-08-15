.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

The Pong Game (Optional) 
=========================

.. raw:: html

	
	
	<h3 id="est-length"><b>Time Estimate: 45 minutes</b></h3>

Preview
------------------------------

.. raw:: html

	<table><tbody><tr><td>
	
.. youtube:: robyGXwQ92U
        :width: 650
        :height: 415
        :align: center

.. raw:: html

	(<a target="_blank" href="http://www.teachertube.com/video/359085">Teacher Tube version</a>)
	
	</td>
	<td>
	
	<a href="http://en.wikipedia.org/wiki/Pong">Pong</a> was one of the first computer games. It consists of a paddle controlled 
	by the user and a ball. In its simplest form the ball bounces off the four walls 
	and the user tries to keep the ball from hitting the bottom wall.  When the ball 
	<img src="../_static/assets/img/Atari_Pong_240.jpg" width="180" align="right">
	hits the bottom wall, the game is over. Variations of the game include keeping 
	score, multiple lives, increasing the ball’s speed, sound effects, and so on.
	
	<br>
	<br>
	<br>
	<br>
	<p>
	<b>Objectives:</b> In this lesson you will learn to :
	</p><ul>
	
	<li>make incremental additions to an existing program;
	</li><li>understand that if/else is a selection control structures in algorithms;
	</li><li>define and use a procedure with a parameter;
	</li><li>define an if/else statement to evaluate more than one condition.
	</li></ul>
	
	</td></tr></tbody></table>
	
Tutorial or Basic Pong App
------------------------------

.. raw:: html
	
	<p>For this lesson <font color="red"><b><i>you have a choice</i></b></font>, you can follow some video tutorials
	that guide you through building the Pong game from scratch.  Or you can 
	start with a basic version of the game and add some enhancements.  No matter
	which option you choose, by the end of this lesson you will have built a pretty
	cool mobile Pong game that keeps score and plays sound effects.
	</p>
	
	<h3>Option 1: Build Pong from Scratch</h3>
	
	<p>To follow the video tutorials, open <a target="_blank" href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit5/templates/PongStarter/PongStarter.asc">
	App Inventor</a> in a separate tab and then 
	click on the top of the thumbnails to open each tutorial as full-screen videos. When finished with the basic app, add the enhancements listed after Option 2.
	
	</p><table>
	<tbody><tr><td>
	<a target="_blank" href="https://www.youtube.com/watch?v=2eLNwD4HivU&amp;list=PLsxoqvm6HPQV5XMPwN4N0tYIe7asB81PS">
	
.. youtube:: 2eLNwD4HivU
        :width: 650
        :height: 415
        :align: center

.. raw:: html

	</a>
	</td>
	<td>
	<a target="_blank" href="https://www.youtube.com/watch?v=2eLNwD4HivU&amp;list=PLsxoqvm6HPQV5XMPwN4N0tYIe7asB81PS">
	
.. youtube:: yvAGG19o
        :width: 650
        :height: 415
        :align: center

.. raw:: html

	</a></td>
	<td>
	<a target="_blank" href="https://www.youtube.com/watch?v=2eLNwD4HivU&amp;list=PLsxoqvm6HPQV5XMPwN4N0tYIe7asB81PS">
	
.. youtube:: pgREXeNHfRs
        :width: 650
        :height: 415
        :align: center

.. raw:: html

	</a></td>
	<td>
	<a target="_blank" href="https://www.youtube.com/watch?v=2eLNwD4HivU&amp;list=PLsxoqvm6HPQV5XMPwN4N0tYIe7asB81PS">
	
.. youtube:: 6juWVUy974Y
        :width: 650
        :height: 415
        :align: center

.. raw:: html

	</a></td>
	<td>
	<a target="_blank" href="https://www.youtube.com/watch?v=2eLNwD4HivU&amp;list=PLsxoqvm6HPQV5XMPwN4N0tYIe7asB81PS">
	
.. youtube:: 4IU9qdtwMpQ
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    </a></td>
	</tr>
	<tr>
	<td align="center">
	1. Moving the ball
	<br>5:29
	</td>
	<td align="center">
	2. Random movement
	<br>2:21
	</td>
	<td align="center">
	3. Bounce off edges
	<br>4:23
	</td>
	<td align="center">
	4. Moving the paddle
	<br>2:46
	</td>
	<td align="center">
	5. Keeping score
	<br>5:47
	</td>
	</tr>
	</tbody></table>
	
	
	<h3>Option 2: Enhance a Basic Pong App</h3>
	
	<p>If you take this route, we will start with a basic Pong app, in which a ball will
	move around the canvas, bouncing off the edges and the paddle.  You will add
	several enhancements to the game, such as keeping score and sound effects. 
	</p>
	
	
	<p>To begin, open the <a target="_blank" href="https://docs.google.com/document/d/1_ay9VcKsaX7gYL-5XaVcSgPtMd_dch-PJOKD3tAnkRg">
	notes for this lesson</a> in a separate tab.  Then open  
	<a target="_blank" href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit5/templates/PongBasic/PongBasic.asc">
	App Inventor with the Pong Basic template</a>. The notes provide an overview of 
	the code for the Basic Pong app.
	</p>
	
	<h3>Enhancements</h3>
	
	<p>Implement the following enhancements using the suggestions below.
	
	</p><ol>
	<li><b>Keeping Score:</b> Add a procedure with a parameter and other 
	statements to the code to perform score keeping tasks. (Note: already completed in Option 1.)
	
	</li><li><b>Ending the Game:</b> Modify the when Ball1.EdgeReached block to 
	end the game when the ball reaches the bottom edge.
	
	</li><li><b>Add Sound Effects:</b> Using the sound files included with the template, add effects for the ball hitting the bottom wall, an edge, and the paddle.
	
	</li><li><b>Advanced:</b> Allow the user turn the sound on/off. 
	</li></ol>
	
	
Self-Check
------------------------------

.. raw:: html

	<question quid="5084358662684672" weight="1" instanceid="6w4jpomlxYaN"></question>
	<question quid="5191002700644352" weight="1" instanceid="rUxnUyA2fwee"></question>
	<question quid="6203420981592064" weight="1" instanceid="ApztzKfHm5ca"></question>
	<question quid="6316902607486976" weight="1" instanceid="Qvts512Wt0m1"></question>
	<question quid="5123356965732352" weight="1" instanceid="YuQDw0axlU4a"></question>
	
	<quizly quizname="quiz_simple_if_else" preamble="" hasanswerbox="false" isrepeatable="false" hints="true" height="495" width="790" instanceid="scgF2VSCjUv8"></quizly>
	
	<quizly quizname="quiz_if_x_greater_than_y" preamble="" hasanswerbox="false" isrepeatable="false" hints="true" height="495" width="790" instanceid="JatcV7u6GOer"></quizly>
	
	
	<div id="portfolio">
	
Reflection: For Your Portfolio
------------------------------

.. raw:: html
	
	<p>In your portfolio, create a new page named <b><i>Pong</i></b> 
	under the <i>Reflections</i> category and answer the following questions:
	
	</p><ol>
	<li>Describe and provide pseudocode for the procedure you defined to keep score 
	(Enhancement #1).
	</li>
	<p></p><li>Describe and provide pseudocode for the algorithm you defined to handle 
	the sound on/off checkbox.
	</li>
	</ol>
	
	Be sure to provide screenshots along with your explanations for each of the 
	enhancements that you made.
	</div>