.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Map Tour Tutorial
=================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
        generateSummary(EKmapping['3.08']);
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
        "list":"In computer science, a list  stores multiple items under one variable name and uses an index to number and access them.",
        "index":"The index of a list is the number or position of an element in the list.",
        "data abstraction":"A data abstraction provides a general way to access a collection of data.",
        "string":"A sequence of characters that can be stored in a variable or list.", 
        "concatenation": "Putting two strings together to make a new string.",
        "data type": "The type of data stored in a variable, for example number, string, boolean, or list.",
        "ADT":"An abstract data type (ADT) defines a general data type like list that describes a collection of data without worrying about the specific implementation.",
        "API":"The Application Programming Interface (API) for a program or web service defines how other programs can communicate with it and use it.",
        "GPS": "The Global Positioning System (GPS) allows people to pinpoint their geolocation (geographic location) on Earth using satellites."
        
       
      };     */
    </script>
    <h3 id="est-length">Time Estimate: 45 minutes</h3>
    

Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <table><tbody>
	<tr><td colspan=2>The Map Tour App tutorial showcases some features of the <a href="http://ai2.appinventor.mit.edu/reference/components/maps.html#Map" target="_blank">Map component</a> in MIT App Inventor  to create a map tour of different destinations. You will learn about an important <span class="hover vocab yui-wk-div" data-id='data abstraction'>data abstraction</span> called <b>Lists</b> to keep track of the destinations.</td></tr>
    <tr>
	<td valign=top><iframe allowfullscreen="" frameborder="0" height="275px" src="https://www.youtube.com/embed/JyqhNvOtQfA?rel=0" width="250px"></iframe>       
    (<a href="https://www.teachertube.com/video/mobile-csp-map-tour-preview-revised-476365" target="_blank">TeacherTube Version</a>)
    </td>
    <td valign=top>
		<div><b>Learning Objectives:</b>&nbspI will learn to</div>
		<ul>
		<li>use the <i>Map</i>, <i>ListPicker</i>, and <i>WebViewer</i> UI components in MIT App Inventor</li>
		<li>use <span class="hover vocab yui-wk-div" data-id='list'>lists</span> to store and access destinations on the map</li>
		<li>use an <span class="hover vocab yui-wk-div" data-id='API'>API</span> (Application Programming Interface) to display Wikipedia pages of destinations</li>
		</ul>
        <div><b>Language Objectives:</b>&nbspI will be able to</div>
		<ul>
		<li>use target vocabulary, such as <span class="hover vocab yui-wk-div" data-id=list>list</span>, <span class="hover vocab yui-wk-div" data-id=index>index</span>, <span class="hover vocab yui-wk-div" data-id=string>string</span>, <span class="hover vocab yui-wk-div" data-id=concatenation>concatenation</span>, and <span class="hover vocab yui-wk-div" data-id=API>API</span> while describing app features and UI components, with the support of concept definitions and <a href="https://docs.google.com/presentation/d/1Pfrv_g1AGKNFPmgir1uGApfHtkhB783Te5kzVz5FZ8c/copy" target="_blank" title="">vocabulary notes</a> from this lesson</li>
		</ul>
    </td>
	</tr>
	</tbody></table>
    

Learning Activities
--------------------

.. raw:: html

    <p><h3>Tutorial</h3>
    <p>To get started, <a href="http://ai2.appinventor.mit.edu/" target="_blank">open MIT App Inventor</a> and start a new project and name it Map Tour.  Follow along with the following video or the <a href="https://drive.google.com/open?id=1yuKxS3XcFXpVDPqSUm9_I_9buKmrl4rshR07TKCCqz4" target="_blank">text tutorial</a> or the <a href="https://drive.google.com/open?id=1qOJQYsqISwD54UDRLPGTgbU2Ywe_ZqYM94-UmCepdfU" target="_blank">short handout</a> for more of a challenge.
    <br/>
.. youtube:: -pl9xYAK17I
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


      (<a href="https://teachertube.com/video/mobile-csp-map-tour-tutorial-revised-476368" target="_blank">TeacherTube Version</a>)
      <br/></p>
    <h3>Enhancements</h3>
    <p>Your instructor may ask you to do some or all  of the following enhancements for your Map Tour app. Be creative!</p>
    <ol>
    <li style="margin-bottom: 5px;">Add more destinations to your map tour.  Make sure you have at least 3 destinations.
      </li><li style="margin-bottom: 5px;"><b>MapType ListPicker:</b> Add a ListPicker to choose the Map Type with the Elements Roads, Aerial, and Terrain. These elements can be set in the UI or in the code in the BeforePicking event handler. After picking, use the user’s Selection to set the Map.MapType to 1 for Roads, 2 for Aerial, and 3 for Terrain. You could do this with an if block using the blue mutator button to add if/elseif/else parts to make a 3 way choice.</li>
    <li style="margin-bottom: 5px;"><b>Zoom Slider: </b>Add a slider to your UI to control the zoom level in the map. You may want a horizontal arrangement to arrange these new controls.  In the slider’s properties, set the MaxValue to 20, MinValue to 1, and ThumbPosition to 13. The slider has a When Slider Position Changed event handler that is called when the user slides the slider. Inside this event, you can change the Map1’s Zoom property to value in the Slider’s ThumbPosition.</li>
    <li><b>My Location button and <span class="hover vocab yui-wk-div" data-id='GPS'>GPS</span>:</b> OpenStreetMap keeps track of the user’s location using <span class="hover vocab yui-wk-div" data-id='GPS'>GPS</span> (the Global Positioning System which uses satellites orbiting the earth to allow us to pinpoint our locations on earth). The Map’s properties UserLatitude and UserLongitude will give the latitude and longitude of the device currently running your app if the device has <span class="hover vocab yui-wk-div" data-id='GPS'>GPS</span> capabilities. Add a button called My Location. When it is clicked, use the Map.PanTo procedure to go the the Map’s UserLatitude, UserLongitude, Map.ZoomLevel. <b>Note:</b> This enhancement is very dependent on the type of device you have and where you are -- being indoors in a classroom is not optimal. So to get this part of the app working you may want to package the app and take the device outdoors. Also, make sure that the device’s <a href="https://www.droid-life.com/2013/01/30/how-to-enable-gps-and-other-location-services-beginners-guide/" target="_blank">location sensing setting</a> is turned on. 
    
     </li>
    </ol>
    <h3>Data Abstraction: Lists</h3>
    <p>The simplest <span class="hover vocab yui-wk-div" data-id='data abstraction'>data abstraction</span> in programming is a <i>variable</i>, but there are more complex data structures 
      available in all programming languages. Like most other programming languages, MIT App Inventor has an <span class="hover vocab yui-wk-div" data-id='ADT'>abstract data type (ADT)</span> called <span class="hover vocab yui-wk-div" data-id='list'>list</span> that allows the storage of an ordered sequence of elements under one name in memory. <span class="hover vocab yui-wk-div" data-id='list'>Lists</span> are sometimes called arrays in other programming languages. Data abstractions manage complexity in the program by giving a collection of data a name that can be used without knowing the specific details of its representation.
      
      The elements in a <span class="hover vocab yui-wk-div" data-id='list'>list</span> are 
      <span class="hover vocab yui-wk-div" data-id='index'>indexed</span> which means they are numbered from <b><i>1</i></b> to the <b><i>length</b></i> of the <span class="hover vocab yui-wk-div" data-id='list'>list</span>. 
      To define a <span class="hover vocab yui-wk-div" data-id='list'>list</span>, we can create a global variable that can be initialized to an <b><i>empty</i></b> <span class="hover vocab yui-wk-div" data-id='list'>list</span> 
      (a <span class="hover vocab yui-wk-div" data-id='list'>list</span> with no items in it):
    
      <br/>
    <img src="../_static/assets/img/EmptyList.png" width="400"/>
    <br/>
      Or we can assign the variable a specific <span class="hover vocab yui-wk-div" data-id='list'>list</span> of items using <b><i>make a <span class="hover vocab yui-wk-div" data-id='list'>list</span></i></b>: 
      <br/>
    <img src="../_static/assets/img/DestinationsList.png" width="500">
    </img></p><p> The <i>Lists</i> drawer contains lots of blocks (<a href="http://appinventor.mit.edu/explore/ai2/support/blocks/lists.html" target="_blank">see the documentation here</a>) such as 
      <i><b>insert item into <span class="hover vocab yui-wk-div" data-id='list'>list</span></b></i> and <i><b>select random item from <span class="hover vocab yui-wk-div" data-id='list'>list</span></b></i> that let you manipulate the 
      items in the <span class="hover vocab yui-wk-div" data-id='list'>list</span>. 
    
    </p>
    <p>Notice that a <b>variable</b> in MIT App Inventor can hold a single data item like a number or a whole <span class="hover vocab yui-wk-div" data-id='list'>list</span> containing many items. Actually, variables in MIT App Inventor can hold a variety of <b>data types</b> including:
      </p><ul>
    <li>Numbers: integers or decimal numbers, </li>
    <li> Strings: text, any sequence of characters you can type on a keyboard, represented inside quotes like "Hello World! 123". </li>
    <li>Booleans: like true or false </li>
    <li> <span class="hover vocab yui-wk-div" data-id='list'>Lists</span>: a collection of related elements given a name. The elements can be any <span class="hover vocab yui-wk-div" data-id='data type'>data type</span> but they are usually all the same <span class="hover vocab yui-wk-div" data-id='data type'>data type</span>, for example all strings or all numbers, and they are numbered with an <span class="hover vocab yui-wk-div" data-id='index'>index</span>. </li>
    </ul>
    <p>We also used <span class="hover vocab yui-wk-div" data-id='string'>string</span> <span class="hover vocab yui-wk-div" data-id='concatenation'>concatenation</span> in this app to <b>join</b> together two strings to make a new <span class="hover vocab yui-wk-div" data-id='string'>string</span>. We joined together the wikipedia web site url with the destination name to make a new url. Another term used with strings is <span class="hover vocab yui-wk-div" data-id='substring'>substring</span> which is part of a <span class="hover vocab yui-wk-div" data-id='string'>string</span>; for example, "cat" is a <span class="hover vocab yui-wk-div" data-id='substring'>substring</span> of "catalog".
      
    </p><h3>AP Pseudocode</h3>
    <p>In the AP CSP pseudocode, <span class="hover vocab yui-wk-div" data-id='list'>lists</span>are represented using square brackets [ ] as shown below.   
      The assignment operator ← (the left-pointing arrow)  can be used to assign a value to a variable. This value can be any <span class="hover vocab yui-wk-div" data-id='data type'>data type</span> including a number, a <span class="hover vocab yui-wk-div" data-id='string'>string</span>, a boolean, or a <span class="hover vocab yui-wk-div" data-id='list'>list</span>.  
      So the initialization of the global  variable for the empty <span class="hover vocab yui-wk-div" data-id='list'>list</span> or a <span class="hover vocab yui-wk-div" data-id='list'>list</span> of destinations would look like this in the AP pseudocode:
      </p><blockquote>
    <pre>   
      destinations ← []
      destinations ← [ "Statue of Liberty", "Chichen Itza" ]
    </pre>
    </blockquote>
    <span class="hover vocab yui-wk-div" data-id='list'>Lists</span> can also be copied into one another, newlist ← destinations.  In a program, if the <span class="hover vocab yui-wk-div" data-id='index'>index</span> is less than 1 or greater than the length of the <span class="hover vocab yui-wk-div" data-id='list'>list</span>, the program will have an error and stop running.
      
      
    
    <h3>APIs: Extend Your Powers as a Programmer</h3>
    <p>In this app, you will make use of an <a href="http://en.wikipedia.org/wiki/Application_programming_interface">Application Programming Interface</a> (<span class="hover vocab yui-wk-div" data-id='API'>API</span>) to communicate with and use Wikipedia from inside your app. An <span class="hover vocab yui-wk-div" data-id='API'>API</span> for a program or web service defines how other programs can communicate with it and use it. There are lots of APIs available to programmers. The APIs specify exactly how programs and apps can interact with each other to perform certain tasks, like sending email or retrieving some data or displaying a particular web page. </p>
    <p>APIs enable programmers to see the Internet and Web and their mobile devices in a very different way than other users. Rather than seeing it merely as something to use, APIs allow programmers to  control how they interact with their mobile devices and with applications provided by Google, Wikipedia, and other software companies.</p>
     

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
	<h3>Vocabulary</h3>
    Here is a table of the technical terms introduced in this lesson. Hover over the terms to review the definitions.
	<table align="center">
    <tbody>
    <tr>
    <td><span class="hover vocab yui-wk-div" data-id="list">list</span>
    <br/><span class="hover vocab yui-wk-div" data-id="index">index</span>
    <br/><span class="hover vocab yui-wk-div" data-id="string">string</span>
    <br/><span class="hover vocab yui-wk-div" data-id="concatenation">concatenation</span>
    <br/><span class="hover vocab yui-wk-div" data-id="substring">substring</span>
    </td>
    <td>
    <span class="hover vocab yui-wk-div" data-id="data type">data type</span>
    <br/> <span class="hover vocab yui-wk-div" data-id="data abstraction">data abstraction</span>
    <br/> <span class="hover vocab yui-wk-div" data-id="ADT">Abstract Data Type (ADT)</span>
    <br/><span class="hover vocab yui-wk-div" data-id="API">API</span>
    <br/><span class="hover vocab yui-wk-div" data-id="GPS">GPS</span>
    </td></tr>
    </tbody>
    </table>
	<p>
    
	<h3>Check Your Understanding</h3>
    <p>Complete the following self-check exercises. 
	</p>
	
.. fillintheblank:: mcsp-3-8-1
    :casei:

    In order for this block to work, the global destinations variable must be what type of data (number, string, list, etc.)? Type your answer into the text box. Spelling counts. 

    .. raw:: html

        <img src="../_static/assets/img/listpickerelements.png"/> |blank|

    - :list: Good. That's right! This statement assumes that global destinations is a <b>list</b> of strings.  When the List Picker is clicked, the list will be presented to the user, who may then select one of the items on the list.
      :x: 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. fillintheblank:: mcsp-3-8-2

    Lists have a length property that keeps track of how many items or elements are in a given list. What is the length of this list? Type your answer into the text box. 

    .. raw:: html

        <img class="yui-img selected" src="../_static/assets/img/ListLength.png?seed=93691&amp;url=assets/img/ListLength.png"/> |blank|

    - :4: That's right! The list has 4 items/elements, so its length is 4.
      :x: The list has 4 items/elements, so its length is 4.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. fillintheblank:: mcsp-3-8-3

    Lists are indexed, or numbered, starting with 1, which means that you can retrieve any item from a list by giving its index. For the list below, what is the index of "No way"? Type your answer into the text box. 

    .. raw:: html

        <img class="yui-img" src="../_static/assets/img/makealist8.png"/> |blank|

    - :3: That's right! The text "No way" occurs as the third item in the list, so its index is 3.
      :x: The text "No way" occurs as the third item in the list, so its index is 3.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-3-8-4
    :random:
    :practice: T
    :answer_a: It would give you the last item in the list.  
    :feedback_a: If it were easy, you wouldn’t be learning anything! Unfortunately the app would probably crash because you did not use a valid index.
    :answer_b: It would give you the first item in the list. 
    :feedback_b: If it were easy, you wouldn’t be learning anything! Unfortunately the app would probably crash because you did not use a valid index.
    :answer_c: It would crash because there is no item with that index. 
    :feedback_c: That's right! When you are referring to an item in a list using an index, you must make sure to use a valid index. For this list the valid indexes are 1 through 8. Using any other index is sometimes called an Index out of bounds error.
    :answer_d: It would ignore your request. 
    :feedback_d: If it were easy, you wouldn’t be learning anything! Since there is no index of 10, MIT App Inventor wouldn't ignore your request. Instead it would unfortunately probably crash the app because you did not use a valid index.
    :answer_e: It would give you a random item from the list. 
    :feedback_e: If it were easy, you wouldn’t be learning anything! Unfortunately the app would probably crash because you did not use a valid index.
    :correct: c

    What do you suppose would happen if your app asked MIT App Inventor for the item at index 10 in the list shown here? 

    .. raw:: html

        <img class="yui-img" src="../_static/assets/img/makealist8.png"/>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1WONX7hPohAnBxVUsfaCnY5c7qkUe_ZS_kHRdper1Dyk/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vRgIhKX2pbpqXGDClZyqJ576Esw3oEppPeOIxORfeNh4_D8qkc7VZC2t-vST4TdNI5xF7wF7Oiqp2EO/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--  &lt;p&gt;Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this &lt;a href=&quot;https://docs.google.com/document/d/1WONX7hPohAnBxVUsfaCnY5c7qkUe_ZS_kHRdper1Dyk/edit?usp=sharing&quot; target=&quot;_blank&quot;&gt;Google Doc&lt;/a&gt; where you may use File/Make a Copy to make your own editable copy.&lt;/p&gt;
    
      &lt;ol&gt;
          &lt;li&gt;How are lists used in this app? Why is a list a useful data abstraction or an abstract data type (ADT) in programming?&lt;/li&gt;
        &lt;li&gt;How do APIs simplify complex programming tasks? Pick an app that you use on your device (e.g. Snapchat, Twitter) and see whether it provides an API and some of the functions you can control with it. &lt;/li&gt;
      &lt;li&gt; How is GPS used in this app? Do some research to find out how GPS works and describe it here in a couple sentences.&lt;/li&gt;
    &lt;li&gt;Insert screenshots of the enhancements that you made below and describe how they work.
        &lt;/li&gt;
      &lt;/ol&gt;-->
    </div>
    </div>