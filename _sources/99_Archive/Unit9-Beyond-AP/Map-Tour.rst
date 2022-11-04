.. raw:: html 

   <div class="logo-header"  id="student-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

Map Tour Tutorial with Activity Starter and Google Maps
=========================================================

.. raw:: html

	
	
	<h3 id="est-length">Time Estimate: 45 minutes</h3>
	
	
Preview
------------------------------

.. raw:: html
		
	<table><tbody>
	<tr><td>
	<!-- <img src="../_static/assets/img/MapTourScreenShot.png" width="315">-->

.. youtube:: CfXWzE-EP58
        :width: 650
        :height: 415
        :align: center

.. raw:: html

	</td>
	<td>
	<p>The Map Tour allows a user to select a location from a list  and it then launches the device’s Google Maps app to show the selected location on the map.</p>
	
	<p>The app uses what’s known as the Google Maps Application Programming Interface (API) to enable the app to provide various forms of help and assistance such as:
	
	 </p><ul>
	   <li>Finding a location on a map.</li>
	<li>Getting directions (driving or walking) to a destination.</li>
	<li>Finding restaurants or other places of interest on a map.</li>
	 </ul>
	
	<p>Thus, by learning to use the maps API this lesson will open up a whole new view of the Internet that is available only to programmers.</p> 
	
	<p>
	 <b>Objectives:</b> In this lesson you will create an app that:
	</p><ul>
	 <li>uses the Google Maps API to perform different map-related functions;</li>
	<li>uses a List to store and access data;</li>
	<li>randomly selects items from a list.</li>
	 </ul>
	
	</td></tr></tbody></table>
	
APIs Extend Your Powers as a Programmer
------------------------------------------

.. raw:: html
		
	<p>In this app, you will make use (through Activity Starter) of Google Maps, an existing mobile app on your device. The Google Maps <a href="http://en.wikipedia.org/wiki/Application_programming_interface">Application Programming Interface</a> (API) is used to control the maps that were displayed in your app. The <a href="https://developers.google.com/maps/">Google Maps API</a> provides documentation for programmers and app developers on how to interact with its application. There are lots of APIs available to programmers. Their role is to specify exactly how programs and apps can interact with each other to perform certain tasks, like sending email or Twitter messages or displaying a map. The API specifies exactly what information you need to provide and in what specific format to provide it in order to interact with an existing application.</p>
	
	<p>One interesting implication is that APIs enable programmers to see the Internet and Web and their mobile devices in a very different way than other users. Rather than seeing it merely as something to use, APIs allow programmers to  control how they interact with their mobile devices and with applications provided by Google, Amazon, Twitter, and other software companies.</p>
	
	<p>The ActivityStarter component will be used to connect to the Google Maps API using a string of text that starts with "geo:0,0?q=". The <i>geo</i> portion indicates that the device should open Google Maps, instead of a different application. The <i>0,0</i> portion refers to the latitude and longitude coordinates - zeros specify to use the current device location. The <i>?q=</i> portion is a query, or question, to look for locations on the map that match. In the Map Tour app, we'll use a list to provide the portion that comes after the equals sign (e.g. <i>q=Mark Twain House</i>).</p>
	

Tutorial
------------------------------

.. raw:: html
		
	<p>To get started, <a href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit3/templates/MapTour2017/MapTourTemplate.asc" target="_blank">open App Inventor with the Map Tour Media Only Template</a>
	in a separate tab and follow along with the following tutorial.
	</p>
	
	<gcb-youtube videoid="S6DTiesNuQ4" instanceid="FYQnW28JjUcs"></gcb-youtube>
	
About Lists
------------------------------

.. raw:: html
		
	<p>The simplest data abstraction in programming is a <i>variable</i>, but there are more complex data structures 
	 available in all programming languages. Like most other programming languages, App Inventor has a data structure 
	 called <i><b>list</b></i> that allows  the storage of multiple items under one name in memory. The items are 
	 <i><b>indexed</b></i> which means they are <i><b>numbered from 1 to the length of the list</b></i>. 
	 To define a list, we can create a global variable that can be initialized to an <b><i>empty list</i></b> 
	 (a list with no items on it):
	
	 <br>
	 <img src="../_static/assets/img/EmptyList.png" width="400">
	 <br>
	 Or we can assign the variable a specific list of items using <b><i>make a list</i></b>: 
	 <br>
	 <img src="../_static/assets/img/DestinationsList.png" width="500">
	 
	 
	</p><p> The <i>Lists</i> drawer contains lots of blocks (<a target="_blank" href="http://appinventor.mit.edu/explore/ai2/support/blocks/lists.html">see the documentation here</a>) such as 
	 <i><b>insert item into list</b></i> and <i><b>select random item from list</b></i> that let you manipulate the 
	 items in the list. 
	
	</p><h3>AP Pseudocode</h3>
	<p>In the AP CSP pseudocode, lists are represented using square brackets [ ] as shown below.   
	 The assignment operator ← (the left-pointing arrow)  can be used to assign a list to a variable.   
	 So the initialization of the global destinations variable in App Inventor would look like this in the AP pseudocode:
	 </p><blockquote>
	 <pre>    destinations ← [ "Connecticut State Capitol Building", “Hartford Atheneum", “Trinity College”]
	</pre>
	</blockquote>
	
	<p>List items can be numbers or text or other lists.  Text items are sometimes called <i><b>strings</b></i>, which are usually 
	indicated by quotes "" to distinguish them from variables.
	
	
	</p>

Still Curious? Enhancements and Extensions
------------------------------------------------

.. raw:: html
	
	<p>Here are some enhancements that you can try: </p>
	<ol>
	   <li>Add your own map image to the UI and add your own locations to the destinations list. Directions: Click 
	     <a target="_blank" href="https://www.google.com/maps">here</a> to open Google Maps in your browser and 
	     search for your town or city.  Take a screenshot of a portion of the map of your vicinity.  On Mac you 
	     can use the Preview program to do this.  On Windows machines you can follow 
	     <a target="_blank" href="https://www.howtogeek.com/226280/how-to-take-screenshots-in-windows-10/">these instructions</a>.  
	     Save the screenshot on your computer.  Then upload the screenshot using the <i>Upload File</i> button in App Inventor's
	     Media panel. 
	   </li>
	   <li>Try some of the other commands that come with the Google Maps API.  Among other things, you can 
	     control the type of directions (by walking (mode=w)  or bicycle (mode=b) or public transit (mode=transit)),  the type of map (street view, satellite view, 
	     hybrid) and many other things.  Here’s a link to the 
	     <a target="_blank" href="https://developers.google.com/maps/documentation/urls/android-intents">API documentation</a>. 
	     And here are some example URIs to try:
	     <table border="1">
	       <tbody><tr border="1"><td>Find restaurants in the vicinity</td><td>geo:0,0?q=restaurants</td></tr>
	       <tr border="1"><td>Find restaurants in Hartford</td><td>geo:41.7618,-72.6806?q=restaurants</td></tr>
	       <tr border="1"><td>Display street view of Hartford</td><td>google.streetview:cbll=41.7618,-72.6806</td>
	         <tr border="1"><td>
	Directions to Hartford from your location by bicycle
	</td><td>google.navigation:q=Hartford&amp;mode=b</td>
	         </tr>
	     </tbody></table></li>
	 <li>Try using Google Maps Streetview, which uses the latitude and longitude coordinates. Instead of the current text string (geo=0,0?) used in the Set ActivityStarter1.DataUri block, the string should look like this: google.streetview:cbll=latitude,longitude. <a href="https://developers.google.com/maps/documentation/urls/android-intents" target="_blank">Google Maps API</a> gives a cool example of street view of Gaza pyramids with camera tilt: google.streetview:cbll=29.9774614,31.1329645&cbp=0,30,0,0,-15. Google maps will tell you the lat and long when you search for a location in <a href="https://maps.google.com" target="_blank">maps.google.com</a> and look at the url right after the @ sign (for example  <a href="https://www.google.com/maps/place/Paris,+France/@48.8589506,2.2768479,12z/" target="_blank">https://www.google.com/maps/place/Paris,+France/@48.8589506,2.2768479,12z/</a>).</li>
	</ol>
	
	
Self-Check
------------------------------

.. raw:: html
	
	<question quid="5718532058775552" weight="1" instanceid="F32XeNFWaYNT"></question>
	<question quid="5711832983535616" weight="1" instanceid="PT9wwDizOauu"></question>
	<question quid="5728415315394560" weight="1" instanceid="dFCgbh08jONl"></question>
	<question quid="5686306919153664" weight="1" instanceid="CNcscJO0265c">
	</question>
	<question quid="5758531089203200" weight="1" instanceid="LiXmP1gkuNGo">
	</question>
	<question quid="5725202142986240" weight="1" instanceid="0uXu0cYflIC1">
	</question><br>
	
	<div id="portfolio" class="yui-wk-div">

Reflection: For Your Portfolio
------------------------------

.. raw:: html
		
	 <p>Create a page named <i><b>Map Tour</b></i> under the <i>Reflections</i> category of your portfolio and answer the following questions:</p>
	
	 <ol>
	   <li>How is the ListPicker component used in this app?</li>
	   <li>How was the Activity Starter used in this app?</li>
	   <li>Pick an app that you use on your device (e.g. Snapchat, Twitter) and see whether it provides an API and some of the functions you can control with it.</li>
	 </ol>
	</div>