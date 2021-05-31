.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

No Texting While Busy Tutorial (Optional)
============================================

.. raw:: html

	<!-- Copy these 3 lines to the top of the lesson's HTML code.  -->
	<link rel="stylesheet" type="text/css" href="assets/lib/lessons/tipped.css">
	<link rel="stylesheet" type="text/css" href="assets/lib/lessons/lessons.css">
	<link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
	<!-- can use: #self-check, #still-curious, .pogil, #portfolio -->
	
	<h3 id="est-length"><b>Time Estimate: 90 minutes</b></h3>
	

Preview
------------------------------

.. raw:: html
	
	<table><tbody><tr><td>

.. youtube:: Al82272L8tw
        :width: 650
        :height: 415
        :align: center

.. raw:: html

	(<a target="_blank" href="http://www.teachertube.com/video/359113">Teacher Tube version</a>)
	
	<br></td>
	<td><b><i>No Texting While Busy</i></b> uses the App Inventor 
	Texting Component to receive and send text messages.  
	This version is a variation of the 
	<a target="_blank" href="http://appinventor.mit.edu/explore/content/no-text-while-driving.html">
	No Text While Driving</a> tutorial 
	and it shows how to use the 
	<a target="_blank" href="http://appinventor.mit.edu/explore/content/google-voice.html">
	Texting component over Wifi</a> 
	(for devices with no Sim card or Mobile service plan). The app itself 
	is bare bones. <b style="background-color: rgb(255, 255, 0);">IMPORTANT NOTE: Google Voice has been updated and is no longer working for use with the texting component. In order to test apps that require the texting component, disable Google Voice in App Inventor and use an Android device that has cellular service (e.g. an Android cellphone). </b> This app is designed to respond automatically to messages 
	received while the user is busy.  The app simply displays the message 
	in a log and sends an automatic response.  
	
	<p>The lesson contains several 
	suggestions for enhancements.
	
	<br>
	<br>
	<br>
	<br>
	</p><p>
	<b>Objectives:</b> In this lesson you will learn to :
	</p><ul>
	<li>use App Inventor's Texting component;
	</li><li>work with <i>Google Voice</i>, both the mobile app and the <i>Google Voice</i> account;
	</li><li>handle received text messages in App Inventor.
	</li></ul>
	<p></p>
	</td></tr></tbody></table>
	
Tutorial
------------------------------

.. raw:: html
	
	<p>To get started, <a href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit7/templates/NoTextingWhileBusy/NoTextingWhileBusy.asc" target="_blank">open App Inventor with the No Texting While Busy Template</a>
	in a separate tab and follow along with the following tutorial.
	
	<br><br>
	If you prefer, you can 
	<a target="_blank" href="https://docs.google.com/document/d/1NwBaKgSkpW18titqPSnlKINEUykb67il4IfTa9umYDI">
	click here for a text-based version</a> of the tutorial.
	<br><br><span id="docs-internal-guid-baab3ed7-0753-e853-ff76-b2f017be9731"><span style="font-size: 14.6667px; font-family: Arial; font-weight: 700; vertical-align: baseline; white-space: pre-wrap; background-color: rgb(255, 255, 0);">NOTE: To test this app, it is necessary to package and install it on your device.</span><span style="font-size: 14.6667px; font-family: Arial; vertical-align: baseline; white-space: pre-wrap; background-color: transparent;"> 
	</span></span><b style="background-color: rgb(255, 255, 0);">IMPORTANT NOTE: Google Voice has been updated and is no longer working for use with the texting component. In order to test apps that require the texting component, disable Google Voice in App Inventor and use an Android device that has cellular service (e.g. an Android cellphone).&nbsp;</b><br></p>
	
	<gcb-youtube videoid="821nlCBewEQ" instanceid="xRWAkRvI17aX">
	</gcb-youtube>
	<br>
	
	
Enhancements: Creative Projects
--------------------------------

.. raw:: html

	<p>Here are some ideas for programming projects.
	
	
	
	</p><ul>
	<li><b>Customization:</b> Add a feature that allows the user to input the 
	message that gets sent automatically while busy.   For a simple version of this, 
	a <i>Textbox</i> and a <i>Button</i> could be used.
	
	</li><li><b>Customization:</b> A more sophisticated version of the above 
	enhancement might be to add a <i>Listpicker</i> that lets the user choose the 
	category of ‘busyness’ and then sets the outgoing message to one that 
	is appropriate for that category. For example, the categories might by 
	[driving, studying, working]  and the corresponding messages might be 
	[“Driving, TTYL”, “Gotta study now sorry”, “I’m at work now and can’t 
	respond. I’ll get back to you soon..”].
	
	</li><li><b>Look and Feel: </b> Improve the overall appearance of the app by using layouts,
	images, and other UI features.
	
	</li><li><b>Persistence:</b>  Add a TinyDb component to the app so that their custom 
	replies will persist between uses of the app.
	
	</li><li><b>Settings Screen (Advanced):</b> Add a second Settings screen that allows 
	the user to set certain Texting and/or app properties.  For example, for the 
	Texting component, let the user control whether GoogleVoice is enabled 
	and when the app is receiving messages (Off, Always, Foreground).   
	For the app, maybe the custom message setting could be done on this screen?  
	
	<br><i>HINT</i>: You may need to use the 
	<a target="_blank" href="https://docs.google.com/document/d/1lnYq4Fuw6DPKohEv1gdqpzNdyugERrw3aI_GPYBh8Y4">
	How to: Pass Information Between Screens</a> tutorial.
	</li></ul>
	
	
	<p></p>

Self-Check
------------------------------

.. raw:: html
	
	<question instanceid="KDlzYkuYGVuk" weight="1" quid="5415703544856576">
	</question>
	<question instanceid="amefRsT8OKEL" weight="1" quid="6028020389249024">
	</question>
	
	<div id="portfolio" class="yui-wk-div">

Reflection: For Your Portfolio
------------------------------

.. raw:: html
		
	<p>Create a new page named 
	<i><b>No Texting While Busy</b></i> under the <i>Reflections</i> category of your 
	portfolio and write
	brief answers to the following questions.</p>
	
	<ol>
	<li>What is the main functionality of this app? Which block(s) control the primary 
	function of this app? 
	</li>
	
	<li>Describe briefly how the <i>MessageReceived</i> event handler works.
	</li><li>Describe one of your enhancements and how it works.</li>
	
	
	</ol></div>