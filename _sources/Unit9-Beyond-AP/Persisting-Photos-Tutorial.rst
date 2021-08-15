.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Persisting Photos Tutorial and Projects (Optional)
==================================================

.. raw:: html

	
	
	<h3 id="est-length">Time Estimate: 90 minutes</h3>
	
Preview
-------

.. raw:: html

	<p></p>
	<table><tbody>
	<tr>
	<td>
	
.. youtube:: TqvgyVRETcY
        :width: 650
        :height: 415
        :align: center

.. raw:: html
	</td>
	<td>
	
	<p>In PaintPot projects, we added a Camera button to take a photo with the device’s <b><i>Camera</i></b> and use that 
	 photo as the Canvas’s background image.  In this tutorial, we will learn how to save that photo to a database on the device,   
	 so that whenever the app is run, the photo can be retrieved from the database. 
	 </p>
	 
	<p>By using a database in this way we will turn the photo into an example of <i><b>persistent data</b></i> -- 
	 i.e., data that persists between different uses of the app.  We will use App Inventor’s <b><i>Tiny DB</i></b> 
	 component to allow the app to save the user’s photos on the device. 
	 </p>
	<p>
	<b>Objectives:</b> In this lesson you will:
	</p>
	 <ul>
	   <li>create an app that saves images between sessions;
	   </li>
	   <li>learn about the concept of persistent data;
	   </li>
	   <li>learn how to access App Inventor’s simple TinyDB database component;
	   </li>   
	   <li>learn to use Lists and the ListPicker component.
	 </li></ul>
	
	</td>
	</tr>
	</tbody></table>
	(<a href="http://www.teachertube.com/video/mobile-csp-paint-pot-tinydb-preview-438786" target="_blank" title="">Teacher Tube version</a>)<br>
	
	
Introduction:  What is TinyDb?
------------------------------

.. raw:: html
	
	<p>Up until now, the data in our apps has been stored either in <b><i>global variables</i></b> or as the value of the <i><b>properties</b></i> of the app’s various components.  For example, when you store a piece of text in a Label, that data is stored in the computer’s main memory, in its RAM — random access memory.  And as we’ve learned, RAM is <b><i>volatile</i></b>,  meaning that any data stored there will be destroyed when the app is exited.
	</p>
	
	<p>By contrast, data stored in the computer’s long-term storage — e.g., on the phone’s flash drive — will <b><i>persist</i></b> as long as the app is kept on the device.  There are various ways to store data permanently on a computer.  For example, you could store it in a file, such as a document or image file.   Another way to store persistent data is in a <b><i>database</i></b>.  App Inventor provides us a very simple, easy-to-use database in its <b><i>TinyDb</i></b> component.  Any data that we store in the TinyDb, will not disappear when the app is exited.   Instead, it will persist between uses of the app -- even if you turn off the device.</p>
	
	<p>Before working on incorporating TinyDb into our app, the following video provides a brief overview of this very important component.</p>
	<gcb-youtube videoid="qVJF-i5LqjQ" instanceid="8fLzUtvqvYcM"></gcb-youtube>&nbsp;(<a href="http://www.teachertube.com/video/tiny-db-438788" target="_blank" title="">Teacher Tube version</a>)<br>
	 
	 
	
Incorporating TinyDb into Paint Pot
--------------------------------------

.. raw:: html
	
	<p>To get started, click here to open App Inventor with the 
	 <a target="_blank" href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit3/templates/PaintPotTinyDbTemplate/PaintPotTinyDbTemplate.asc">
	   PaintPotTinyDbTemplate</a>
	 in a separate tab and follow along with the video tutorial.  Once the template project opens use Save As to rename your project <b><i>PaintPotTinyDb</i></b>. Note: If the blocks don’t appear well in the Blocks Editor, right-click on the background and use the Arrange Vertically option.</p>
	<p>If you prefer, you can follow the <a target="_blank" href="https://docs.google.com/document/d/1yoF4jgL4NQd9_imMZtvDZpm506URCit0z3WyIGcstFU">text version of this lesson</a>.</p>
	<gcb-youtube videoid="pMfuz6fYnJE" instanceid="2ivkTidNbS6R"></gcb-youtube>&nbsp;(<a>Teacher Tube version</a>)
	<br>
	
Lists
--------------------------------------

.. raw:: html
	
	<p>In the projects below, you will extend this version of PaintPot to save multiple photos for the canvas background in a <em>list</em> in TinyDB.  The simplest data abstraction in programming is a  <em>variable</em>, but there are more complex data structures available in all programming languages. App Inventor has a data structure called <em>list</em> which allows the storage of multiple items under one name in memory. The items are <em>indexed</em> which means they are numbered from 1 to the length of the list. The <em>Lists</em> drawer contains all the blocks available for manipulating lists. We first create a global variable to hold a list which can be an <em>empty list</em> or a list of items using <em>make a list</em>:
	 <br>
	 <img src="../_static/assets/img/listVariable.png" width="70%">
	 
	</p><p>In the projects below, you will use <a href="http://appinventor.mit.edu/explore/ai2/support/blocks/lists.html" target="_blank">List blocks</a> such as <em>insert item into list</em> and <em>select random item from list</em>.</p>
	
	<p>In the AP CSP exam pseudode, lists are represented using square brackets [ ] like below. The assignment operator ← can be used to assign a list to a variable. The list items can be numbers or text which are called <em>strings</em>; strings are usually indicated by quotes "" to distinguish them from variables.
	 </p><pre>  list ← [ "kitty.png", "android.png" ]
	 </pre>
	
	 <br>
	
Creative Mini Projects
----------------------

.. raw:: html
	
	<p>Now that you've learned the basics of using TinyDb,  it's time to add some additional features and enhancements to
	 the Paint Pot app.  Working in pairs, implement each of the following enhancements.
	</p>
	<ol>
	 <li>As we saw in the overview video, one can also store lists of data in TinyDb.  So rather than just having a single photo to
	   use as the Canvas background, we could have a selection of photos to choose from.   As a first step, initialize a global variable for this list of backgrounds to the <em>create empty list</em> block from the <em>Lists</em> drawer. In the <em>When Camera1.AfterPicture</em> event handler,   add the photo that's taken to that list using the <em>add items to list</em> block. Store the variable for the whole list  in the TinyDb.  Don't forget!  You'll need a unique tag to
	   associate with the list.</li>
	 <li><b>If/else Algorithm.</b> What about when the app starts up? This can be a little tricky because now you'll be retrieving a
	   list of photos, rather than a single photo.  (What should the default value be when you are retrieving a list from TinyDb?) 
	   So you can't assign the list as the background image. You could select a 
	   random item (photo) from the list and make that your background.  But what if this is the first time the app runs?  When the
	   list is empty?  This would be a good place for an <b>if/else algorithm</b> controlled by whether or not the list retrieved from
	   the TinyDb is empty or not.  To solve this problem, you'll have to look through the <i>Lists</i> drawer in the Blocks Editor for
	   some useful functions to use. 
	 </li>
	 
	 <li>Add a <i><b>ListPicker</b></i> component to the app's user interface to let the user select the background image. Read more about the <a href="http://appinventor.mit.edu/explore/content/basic.html#ListPicker" target="_blank">Listpicker component here</a>. The ListPicker looks like a button but it displays a list of items to choose from. In its blocks, it has a <em>BeforePicking</em> and an <em>AfterPicking</em> event handler. One of the
	   ListPicker properties is the <i><b>Elements</b></i> property which is the list of choices shown to the user.  You can set this Elements property to your list of background photos in the <em>BeforePicking</em> event handler. Note that what will appear in the ListPicker are the file paths of the images, not the images themselves.
	   There's no easy way around this. After the user has picked an element from the ListPicker, their choice will be in <em>ListPicker1.Selection</em> and can be put on the Canvas background. 
	 </li>
	 
	</ol>
	
Self-Check
----------

.. raw:: html
	
	<question quid="4919153316069376" weight="1" instanceid="vjSaPuUiLVsN">
	</question>
	
	<question quid="5187793219223552" weight="1" instanceid="o3SX2UMr2ZEJ">
	</question>
	
	<question quid="6268469368586240" weight="1" instanceid="qB3SgPjhp1hh">
	</question>
	
	<question quid="6277220263788544" weight="1" instanceid="j7wmJhW0AsmS">
	</question><question quid="5142460119384064" weight="1" instanceid="ZMyrrQMnKSl4"></question>
	
	<question quid="5647308616105984" weight="1" instanceid="tfqOWeJEPKIA">
	</question>
	
Reflection: For Your Portfolio
------------------------------

.. raw:: html

	 <p>Create a page named <i><b>Persistent Photos Tutorial</b></i> in your portfolio and give brief answers to the following questions:</p>
	 <ol>
	   <li>What does it mean to say that data is 'persistent'?</li>
	   <li>What's the difference in terms of <i>where</i> data is located between data stored in a global variable and data stored in a database?</li>
	   <li>When and how often does App Inventor's <i>Screen1.Initialize</i> block fire and what is its purpose?</li>
	   <li>Include a screenshot of your if/else algorithm for retrieving photos from TinyDB.</li>
	 </ol>
	</div>
