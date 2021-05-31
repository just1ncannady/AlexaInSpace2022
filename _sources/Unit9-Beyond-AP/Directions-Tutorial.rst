.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

My Directions Tutorial (Optional)
=================================

.. raw:: html

	<!-- Copy these 3 lines to the top of the lesson's HTML code.  -->
	<link rel="stylesheet" type="text/css" href="assets/lib/lessons/tipped.css">
	<link rel="stylesheet" type="text/css" href="assets/lib/lessons/lessons.css">
	<link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
	<!-- can use: #self-check, #still-curious, .pogil, #portfolio -->
	<h3 id="est-length">Time Estimate: 45 minutes</h3>
	
Preview
------------------------------

.. raw:: html

	<table><tbody><tr><td>
	
.. youtube:: j1eiu8Dy_SI
       :width: 650
       :height: 415
       :align: center

.. raw:: html
	
	</td><td>
	<b><i>My Directions</i></b> This tutorial shows how to use the Location Sensor 
	in combination with Google Maps to display directions from the user’s 
	current location to a selected destination.
	(<a target="_blank" href="http://www.teachertube.com/video/359114">Teacher Tube version</a>)
	
	<p>
	<b>Objectives:</b> In this lesson you will learn to :
	</p><ul>
	<li>create an app that
	<ul>
	<li>uses the Global Positioning System(GPS) to obtain the user's current location,
	</li><li>uses the Google Maps Application Programming Interface (API) to 
	obtain directions from the user's current location to a destination address;
	</li>
	</ul>
	</li><li>appreciate that Google Maps API is an abstraction that allows apps
	to leverage existing functionality;
	</li><li>obtain some additional experience working with lists and TinyDB to save user-generated information persistently.</li></ul>
	<p></p>
	</td></tr></tbody></table>
	
	
	
	<h3>Building the MyDirections App</h3>
	<p>To get started, <a href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit7/templates/MyDirections/MyDirectionsTemplate.asc" target="_blank">open App Inventor with the My Directions Template </a>&nbsp;in a separate tab and follow along with these tutorials.&nbsp;<br>
	<br>You can either click on the thumbnails to view the video or 
	<a target="_blank" href="https://docs.google.com/document/d/19q94J-fc9t4TjhrDOcl_skO-WAMg10Y8Y03-TaG64M8/edit?usp=sharing">
	click here</a> to read the tutorial.
	
	
	</p>
	
	<table><tbody><tr><td>
	<a target="_blank" href="https://www.youtube.com/watch?v=LdoJUouVWjw">

.. youtube:: LdoJUouVWjw
        :width: 650
        :height: 415
        :align: center

.. raw:: html

	</a></td>
	</tr>
	</tbody></table>
	
Enhancements: Creative Projects
-------------------------------

.. raw:: html

	
	There are a number of enhancements you could implement to improve this app.
	<ol>
	<li>In its current form, the destination addresses are created by the programmer. Add a Textbox and a Button to the UI to enable the user to input their own destination addresses. Addresses entered by the user should be added to the destinations list. This will make it possible to share the app with friends.
	</li><li><span class="yui-non">Improve the presentation of the search results by using or modifying one or more additional API arguments in the Map’s URL. &nbsp;Here is a complete list of the <a href="https://docs.google.com/document/d/1Rm4aXQRFBQf0i0jWHHqpkvhXrlm8GLcSJJbBqkXJmjA/edit" target="_blank" title="">Maps API arguments</a>. 
	 
	 </span></li><li><b>Advanced:</b> Add a TinyDb to the app so that the user’s destinations will persist. Addresses saved in the TinyDb will be there the next time the app is used.&nbsp;<span id="docs-internal-guid-c6e1980d-cbdb-7b60-9fc9-0e6a4f08b726"><span style="font-size: 15px; font-family: Arial; vertical-align: baseline; white-space: pre-wrap; background-color: transparent;">
	<br><img src="https://lh5.googleusercontent.com/yJ7te3jGckqeXrGW3IiJSd4QHqUiRfALH0oUaZFsK5q7zeJm-UOfFHTfXpCCETeBVP0T2XgwN0rEkwnrucEkJe9wmQtta2xhTqBgQ1O0jPEhn66WS3FkG4OWkjEoVPXvfw" width="624px;" height="100px;" style="transform: rotate(0rad); -webkit-transform: rotate(0rad);" alt="Screen Shot 2014-08-05 at 3.27.37 PM.png"></span></span><br><br>
	<b>HINT 1:</b>  Lists (as well as numbers and strings) can be stored in a TinyDb.  So you can store the entire destinations list as one element. Determine when and how to store the destinations. Then, determine when and how to retrieve the destinations.&nbsp;<span style="line-height: 1.22;">
	<br><br>
	<b>HINT 2:</b> The destinations should be retrieved from the TinyDb when the app is initialized.  Here’s how:&nbsp;</span><span style="line-height: 1.22;">
	<br><br>
	<i>NOTE:</i> This can be tricky to understand.  The first time the app is run, there definitely won’t be any ‘addresses’ stored in the TinyDb. You can specify how to handle the empty data situation with the valueIfTagNotThere parameter. In the example, we set global destinations to a default fixed list so the first time the app runs it will have some sample destinations You could also put a create empty list in valueIfTagNotThere if you wanted the destinations list empty to start. This problem won’t arise once the user has stored some addresses in the TinyDb.</span>
	</li></ol>
	<br>
	
Solutions
------------------------------

.. raw:: html

	<p>It is important to explore with App Inventor and become accustomed to programming without explicit instructions. So try out the challenges listed above and see how far you can get.<p>
	<p>If you get stuck -- or, after you've finished, to compare your solutions with ours -- check out the solutions video. </p>
	
.. youtube:: 0Wu_BvUVCM8
        :width: 650
        :height: 415
        :align: center

.. raw:: html
	
	<br>
    
Self-Check
------------------------------

.. raw:: html

	<question quid="5708573640228864" weight="1" instanceid="MsEJ0vmcqJrP">
	</question><br>
	<br><question quid="5155582105354240" weight="1" instanceid="yAc0ZsMnkuZh">
	</question>
	
	
Still Curious
------------------------------

.. raw:: html

	<p>
	In this lesson you used the Google Maps Application Programming Interface (API), an 
	abstraction that lets you specify commands to the Google Maps application.  This is a 
	nice example of <i>cloud computing</i>:  Google Maps is the cloud-based application
	that programmers can incorporated into their apps by learning the API.  This is also
	a nice example of how a program -- in this case a mobile app -- can leverage
	functionality that professional programmers have developed.
	
	</p><p>This example is not an isolated case. YouTube, Flickr, Twitter, and Amazon all provide APIs to use at least part of their services.
	
	</p>
	
	<div id="portfolio" class="yui-wk-div">

Reflection: For Your Portfolio
------------------------------

.. raw:: html

	 Create a new page named <i><b>My Directions</b></i> under the <i>Reflections</i> 
	 category of your portfolio and write brief answers to the following questions:
	 
	 <ol>
	   <li>What are the advantages of having a location aware app? What are the disadvantages?
	   </li>
	   <li>If you added any enhancements, post the screenshots to your portfolio and explain how you implemented the enhancements.
	   </li>
	 </ol>
	</div>
