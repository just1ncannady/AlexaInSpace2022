.. raw:: html 

   <div class="logo-header"  id="student-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

Where is North: A Compass App (Optional)
=========================================

.. raw:: html

	
	
	<h3 id="est-length">Time Estimate: 45 minutes</h3> 
	
Preview
------------------------------

.. raw:: html

	<table><tbody><tr><td>
	
.. youtube:: AoxiklzmUMI
        :width: 650
        :height: 415
        :align: center

.. raw:: html

	(<a target="_blank" href="http://www.teachertube.com/video/whereisnorthpreview-348093">
	Teacher Tube version</a>)
	
	</td><td>
	<b><i>Where is North:</i></b> This app uses the orientation and
	location sensors to create a simple compass app.
	
	<p>
	<b>Objectives:</b> In this lesson you will learn to :
	</p><ul>
	<li>Create an app that
	<ul>
	<li>uses the Global Positioning System (GPS) to display your latitude and longitude,
	</li><li>uses the OrientationSensor to point to North,
	</li><li>uses the Canvas component for drawing,
	</li><li>uses an ImageSprite component to animate the arrow.
	</li></ul>
	</li><li>Think abstractly about the problem of placing labels on various sized screens.
	</li></ul>
	<p></p>
	</td></tr></tbody></table>
	
Some Preliminaries
------------------------------

.. raw:: html

	
	<p>Before we start the tutorial, there are some important concepts to talk about. 
	
	</p><h3>Orientation Sensor</h3>
	
	<p>App Inventor’s <a target="_blank" href="http://ai2.appinventor.mit.edu/reference/components/sensors.html#OrientationSensor">
	Orientation Sensor</a> 
	
	<a target="_blank" href="http://www.jdroid.ch/androidEnglish/index.php?inhalt_mitte=grundelemente/lagesensoren.inc.php">
	<img src="http://www.jdroid.ch/grundelemente/bilder/sensorwerte.png" align="right">
	</a>
	
	(in the Sensor drawer) is a non-visible component that provides information about 
	the device’s orientation in 3 dimensions:
	
	</p><ul>
	<li>Roll: 0 degrees when the device is level, increases to 90 degrees as the device is tilted 
	up on its left side, and decreases to -90 degrees when the device is tilted up on its 
	right side.
	</li>
	
	<li>Pitch: 0 degrees when the device is level, up to 90 degrees as the device is tilted 
	so its top is pointing down, up to 180 degrees as it gets turned over. Similarly, 
	as the device is tilted so its bottom points down, pitch decreases to -90 degrees, 
	then further decreases to -180 degrees as it gets turned all the way over.
	</li>
	
	<li>Azimuth: 0 degrees when the top of the device is pointing north, 90 degrees 
	when it is pointing east, 180 degrees when it is pointing south, 270 degrees when 
	it is pointing west, etc.
	</li>
	</ul>
	
	<p>For this compass app we will only be using the device’s azimuth, which tells us 
	the device’s position relative to due North.  Note that the azimuth is reported as 0 
	degrees when the top of the devices is pointing North.  You can read more about 
	the orientation sensor in App Inventor’s glossary.
	
	</p><h3>GPS and the Location Sensor</h3>
	
	<p>App Inventor’s <a target="_blank" href="http://ai2.appinventor.mit.edu/reference/components/sensors.html#LocationSensor">Location Sensor</a> (in the Sensor 
	drawer) is a non-visible component that provides location about the device’s 
	longitude, latitude, altitude and street address. It can also perform geocoding.   
	You can read more about the Location Sensor in App Inventor’s glossary.
	
	</p><p>A mobile device can detect its location in one of three ways:
	</p><ul>
	<li>Using its built-in <a target="_blank" href="http://en.wikipedia.org/wiki/Global_Positioning_System">GPS</a> 
	sensor.  This is the most accurate but, ideally, 
	requires that the phone have a clear shot of the sky so that it can receive 
	readings from at least 3 GPS satellites. This is accurate within a few meters 
	but uses the most battery power.
	</li>
	
	<li>Using a Wifi signal from surrounding Wifi router.  The phone’s location would be 
	the latitude and longitude of the router. This might work indoors and uses less 
	battery power.
	</li>
	
	<li>Using the Cell ID -- i.e., signals from surrounding cell towers. This is least 
	accurate but uses the least power.
	</li>
	</ul>
	
	<p>For this app we will just display the phone’s latitude and longitude in a label 
	whenever the phone’s location changes.
	
	
	</p><h3>Canvas Component</h3>
	
	<p>This app uses App Inventor's <a target="_blank" href="http://ai2.appinventor.mit.edu/reference/components/animation.html#Canvas">Canvas
	</a> 
	component (Graphics and Animation drawer).  
	
	<img src="../_static/assets/img/CanvasWithN.png" width="250" align="left">
	
	The Canvas is App Inventor’s 
	<i>graphics component</i>.  It is used for 
	drawing,  painting, and displaying 
	<a target="_blank" href="http://ai2.appinventor.mit.edu/reference/components/animation.html#ImageSprite">ImageSprites</a>.  
	The Canvas component has a 
	coordinate system that is similar to the Cartesian coordinate system that you might 
	have learned about in geometry, but it has some important differences.  Its main 
	characteristics are summarized in the  diagram shown here. 
	
	
	</p>
	<p>The Canvas’s origin, the point (0,0) is at its top-left. So its horizontal x-axis grows 
	positively from left to right.  Its vertical y-axis grows positively from top to bottom. 
	Coordinate values on the Canvas are represented as <i> pixels</i>, which is short for picture 
	elements. So, for example, the Width of the Canvas might be 300 pixels and its height 
	might be 450 pixels. 
	
	</p><p>The Canvas component has blocks that enable you to draw and paint on it.  For
	example, the <i>Canvas.DrawText</i> block lets you draw text on the canvas at
	coordinates (x,y).  Note that the letter's (x,y) coordinates are located at the
	top-left point of its enclosing rectangle,  as in many other graphics systems.
	</p>
	
	<br>
	<br>
	<br>
	<br>
	
Tutorial
------------------------------

.. raw:: html
	
	<p>To get started, <a href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit2/templates/WhereIsNorthTemplate/WhereIsNorthTemplate.asc" target="_blank">open App Inventor with the Where Is North Template</a>
	in a separate tab and follow along with the following video tutorial.
	
	
	If you prefer, you can 
	<a target="_blank" href="https://docs.google.com/document/d/1YQKOLLLrxUVFXm4yQrltVagSuGscAmKsCH_hXWEbRVY">
	click here for a text-based version</a> of the tutorial.
	</p>
	
	(<a target="_blank" href="http://www.teachertube.com/video/whereisnorthtutorial-348094">
	Teacher Tube version</a>)
	<gcb-youtube videoid="9HoIorx7hX0" instanceid="u4RT1hOX9jM4">
	</gcb-youtube>
	
	
Questions
------------------------------

.. raw:: html
	
	<question quid="5690820929781760" weight="1" instanceid="uFrTgZhBxgcu">
	</question>
	<br><br><question quid="5148883030114304" weight="1" instanceid="VfpI6193TKN2">
	</question><br>
	
	
Still Curious?
------------------------------

.. raw:: html
	
	<p>Want to learn more about the GPS system, how it came into being and more of the
	technical details about how it works?  Check out the <a target="_blank" href="http://en.wikipedia.org/wiki/Global_Positioning_System">Wikipedia article on GPS</a>. 
	</p>
	
Reflection
------------------------------

.. raw:: html
	
	<p>In your portfolio, create a new page named <i>Where is North Tutorial</i>&nbsp;under the Reflections category and answer the following questions:
	
	</p><ol>
	<li>What is the Orientation Sensor component? How is it used in the Where is 
	North tutorial?
	</li>
	
	<li>What is the Location Sensor component? How is it used in the Where is North tutorial? 
	Be sure to include how GPS works in your answer.
	</li>
	
	<li>In your opinion, is the Where is North app a good example of a location aware 
	app or can the location sensor be used in a better, more efficient way? Explain.
	</li>
	
	</ol>
	
	
