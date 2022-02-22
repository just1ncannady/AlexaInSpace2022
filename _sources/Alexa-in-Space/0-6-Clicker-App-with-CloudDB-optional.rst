.. raw:: html 

   <div class="logo-header"  id="student-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

7.6 Clicker App with CloudDB (optional)
=======================================

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
            generateSummary(EKmapping['7.06']);
            generateHovers();
    
    
        });
    </script>
    <h3 id="est-length">Time Estimate: 90 minutes</h3>
    

Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <table>
    <tbody>
    <tr>
    <td colspan=2>
		<p>In earlier apps that we designed in this course, we used TinyDB to store and retrieve data on our physical device (phone or tablet). In this lesson, we will build a simple Clicker App that will store and retrieve data from a cloud database on the web.</p>
        <p> Imagine a teacher asking the class a question and students voting on it. We want to design an app that can not only store the results from each student in one central place but also allow the teacher and the students to view the results in real time.</p>
	</td>
	</tr>
    <tr>
		<td valign=top>
		<iframe allowfullscreen="" frameborder="0" height="300" src="https://www.youtube-nocookie.com/embed/TD0B60NsMz8" width="275"></iframe>
		<!-- (&lt;span class=&quot;yui-non&quot;&gt;TeacherTube Version&lt;/span&gt;)-->
		</td>
		<td valign=top>
        <div><b>Learning Objectives:</b>&nbspI will learn to</div>
		<ul>
		<li>differentiate between synchronous and asynchronous operations</li>
		<li>create an app using the CloudDB component to store data on the web so it can be shared by different users</li>
		</ul>
		<div><b>Language Objectives:</b>&nbspI will be able to</div>
		<ul>
		<li>describe and give examples of syncrhonous and asyncronous operations</li>
		<li>describe how using a database helps reduce detail in an app</li>
		<li>use target vocabulary while describing app features and User Interface with the support of concept definitions from this lesson</li>
		</ul>
		</td>
	</tr>
    </tbody>
    </table>
    

Learning Activities
--------------------

.. raw:: html

    <p><h3>Introduction:  Abstracting an App's Data</h3>
    <p>We will create a polling app that enables students to answer a yes/no question then display the poll results in real time. When your code is completed, you will have a clicker app that stores all 
      of its data on the Web using a cloud database for a high-level <b>data abstraction</b>.</p>
    <h3>Database Concepts: TinyDB vs.  CloudDBs</h3>
    <p>
      Before working on the app itself, it is important to understand what <i>CloudDB</i> is and how it differs from <i>TinyDB</i>.  As you know from a 
      <a href="../Unit3-Creating-Graphics-Images/Map-Tour-With-TinyDB.html" target="_blank">previous lesson</a>, 
      we can use a TinyDB component to <i><b>persist</b></i> data.  TinyDB stores its data on the
      device itself—the phone or tablet—and access to the data is <i><b>synchronous</b></i>, 
      which means that access to the data is immediate. It's good for sharing data between uses of the app on the same device, but it is not good for sharing data among users on different devices.
    </p>
	<p>
	<img src="../_static/assets/img/diary.png" width="125" style="float:right;padding-left:5px"/>
	For example, consider a diary app which enables a user to record entries that contain personal information. The synchronous storage of a TinyDB would be effective for storing entries in this app that a user does not want to share with anyone on a different device. 
	Next, consider a messaging app intended to allow users to communicate with other users of the app. If a TinyDB was used to store the messages, users of the app on different devices would not be able to access the messages and the app would not work as intended. For this app, a CloudDB would be a better choice.
	</p>
	<p> <b>CloudDB</b> is a web-based database service. It is a non-visible App Inventor component that can be used to store and retrieve data values in a database located on the Web.  It can be found in the palette’s <b>Storage</b> drawer. Whereas TinyDB stores data only on the device running the app, a CloudDB is shared among users on multiple devices running the same app because it stores data online, in the cloud. 
	Access to the web data is <i><b>asynchronous</b></i>, which means storing and retrieving data may not happen immediately. Your program must request the data operation, and the CloudDB will signal the program when it is completed. The app can continue running other commands at the same time as the web database is doing the data operation, until it is interrupted by the event that the data operation is complete. 
    </p>
    <p>Note that App Inventor also has <b>TinyWebDB</b> and <b>FirebaseDB</b> which are also web databases that can be used the same way as CloudDB with slight differences in the blocks. TinyWebDB does not have a <i>when data changed</i> block to push updates to all the shared devices. FirebaseDB  is a Google product and charges for some services. CloudDB is based on FirebaseDB with all the same blocks but it is hosted at MIT. </p>
	<p style="color:red">CloudDB is currently having connection problems due to server overload. If you get a socket connection error, switch to using the Experimental/FirebaseDB and its associated blocks for this tutorial! </p>
    <p>The following video explains the basic concepts of using a web-based database like CloudDB.</p>
    <iframe allowfullscreen="" frameborder="0" height="470" src="https://www.youtube-nocookie.com/embed/TrxBrGq0c2U" width="630"></iframe>
    <br/>
        (<a href="https://www.teachertube.com/video/mobile-csp-database-fundamentals-485235" target="_blank" title="">TeacherTube Version</a>)
      <br/>
    </p>
    <p>
    CloudDB stores two types of records, individual data items in variables or lists. In this app, we will only be using it to store individual data items. Note that the tags are case sensitive in a CloudDB. 
      
    </p><h3>Getting Ready</h3>
    <p>Start App Inventor with <a href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit6/templates/ClickerApp/ClickerWebDBtemplate.asc" target="_blank">Clicker App Template</a>.  Once the project opens use Save As to rename your project <i>ClickerCloudDB</i>. 
    </p>
    <p>Follow along with the video tutorial or the <a href="https://drive.google.com/open?id=1ovmfYBEnTdLSD5JnVVEvmMrtJcONSaYdwLHgn6Rv-08" target="_blank">text version</a> or use the <a href="https://docs.google.com/document/d/10wiCYVDcvVUsmBnTJWsIJicaOhAOZD8nsS-_Wh_oHd4/" target="_blank">short handout</a> to complete this app.</p>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/25WJLbsgIrM?controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	
	<p style="color:red">CloudDB is currently having connection problems due to server overload. If you get a socket connection error, switch to using the Experimental/FirebaseDB and its associated blocks for this tutorial! </p>

	<h3>Testing the App</h3>
    <p>
    This app is best tested by forming a group of students where everyone in the group loads one student's app using <b>Build/App (provide QR code for apk)</b>.   Make sure that as each person's app loads, that the most recent data stored in the database shows up on their device. When one of student in your group votes, the latest data should update on everyone’s screen. Because this app is more easily tested using .apk files, we recommend it be built (and tested) on Android devices until iOS .apk files become available in App Inventor.</p>
    <h3>Exercises and Enhancements</h3>
    <p>To appreciate the increased flexibility and generality that we get from centralizing data on the web, here are
      some exercises to try. </p><ol>
    <li style="padding-bottom:5px"><b>Create a Percentage Display Using the Thumb Switches<br/></b>
		<ul>
			<li style="padding-bottom:5px">Read the <a href="http://ai2.appinventor.mit.edu/reference/components/userinterface.html#Slider" target="_blank" title="">documentation on Thumb Sliders </a>before proceeding.</li>
			<li style="padding-bottom:5px">The sliders or thumb switches are most frequently used to allow the user to set the value of some property by moving their thumb on a sliding scale. For our Clicker app, we will be using this component in reverse - to create a percentage display based on the ratio of “Agree” and “Disagree” votes recorded by the app.</li>
			<li style="padding-bottom:5px"><a href="https://www.youtube.com/watch?v=cm2-kVcWTuw&amp;feature=youtu.be" target="_blank" title="">This video</a> provides additional details on how to program the sliders to display percentages.</li>
		</ul>
	</li>
    <li style="padding-bottom:5px"><b>Allow Users to Vote Only Once<br/></b>
	<ul>
		<li style="padding-bottom:5px">Modify the app so that the app only allows the user to vote once (hint: there is an <i>Enabled</i> property for buttons). Votes will still be updated by the <i>DataChanged</i> procedure which is called automatically when the data in the database is updated. 
		<li style="padding-bottom:5px">Add re-enabling the voting buttons when the user hits reset. Note: For testing purposes, it might be easier to disable the "vote only once" feature while testing other enhancements.</li>
	</ul>
    <li style="padding-bottom:5px"><b>Build a Teacher Version<br/></b> This special version of the app, the “Teacher” version, will update the question displayed on the screen in real time. 
     First in the student app.
      <ul>
    <li style="padding-bottom:5px">Change the student version of the app to accept new questions while the app is running. This will involve adding code to the <i>CloudDB.DataChanged</i> event handler to see if the question was changed in the database and changing the question label accordingly and re-enabling the voting buttons. Use the tag name "question". Note that the question data will consist of a string, whereas the agree and disagree data were numbers.</li>
    <li style="padding-bottom:5px">Remove the RESET button from the UI of the student side so that only the teacher can reset the counters. </li>
    </ul>
    <p>Build a separate version of the app called "ClickerTeacher" (use Projects/Save As). Allow only this version to change the questions. Note that when you use Projects/Save As, the CloudDB token and ProjectID will both stay the same, so the student app and the teacher app can share the same database. Also, when testing the app, it may be easier to use QR codes to load the two versions of the app instead of trying to use the Companion.</p> <p style="color:red"> Note: If using Projects/Save As does not copy the CloudDB token, you may need to copy and paste the token from the student version into a text editor (e.g. a Google doc) and then copy and paste the token from the text editor into the teacher version.</p>
	<ul>
    <li style="padding-bottom:5px">
    Replace the question label in the teacher version of the app with a <i>TextBox</i> to allow the teacher to update the question field in real time. 
      </li>
    <li style="padding-bottom:5px">Add an “Update Question” button to the teacher app that will store the new question into the CloudDB from where it will get pushed to all the users. Remember the tag name you used (question)! Also, reset the counters and store them in the database too. </li>
    <li style="padding-bottom:5px">Test with your group with one student using the teacher app and the rest using the corresponding student apps.</li>
    </ul> </li>
    </ol>
    

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
    
.. mchoice:: mcsp-7-6-1-copy
    :random:
    :practice: T
    :answer_a: that it can be completed immediately. 
    :feedback_a: OK, so you didn’t get it right this time. Let’s look at this as an opportunity to learn. Try reviewing this; synchronous means "at the same time".  So synchronous operations are performed instantaneously, whereas asynchronous operations are not.  Operations over the Internet are asynchronous.
    :answer_b: that the request cannot be completed at the same time as it was made and may take an unpredictable amount of time. 
    :feedback_b: Right.  Synchronous means "at the same time".  So synchronous operations are performed instantaneously, whereas asynchronous operations are not.  Operations over the Internet are asynchronous.
    :answer_c: that it must be performed on a clock.
    :feedback_c: OK, so you didn’t get it right this time. Let’s look at this as an opportunity to learn. Try reviewing this; synchronous means "at the same time".  So synchronous operations are performed instantaneously, whereas asynchronous operations are not.  Operations over the Internet are asynchronous.
    :answer_d: that it cannot be performed on a clock.
    :feedback_d: OK, so you didn’t get it right this time. Let’s look at this as an opportunity to learn. Try reviewing this; synchronous means "at the same time".  So synchronous operations are performed instantaneously, whereas asynchronous operations are not.  Operations over the Internet are asynchronous.
    :correct: b

    .. raw:: html
    
    	<p>To say that the operation of requesting data from a CloudDB is <b><i>asynchronous</i></b> means</p>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-7-6-2-copy
    :random:
    :practice: T
    :answer_a: a. Data stored in a CloudDB can easily be shared with other devices and users. 
    :feedback_a: That's right! Data stored in a CloudDB is stored on the Web and that's why it can easily be shared with other devices or users.
    :answer_b: b. Data stored in a CloudDB will persist between different uses of the app. 
    :feedback_b: That's right! Data stored in a CloudDB persists between uses of the app. 
    :answer_c: c. Data stored in a CloudDB disappears when you quit the app. 
    :feedback_c: No, data stored in a CloudDB persists between uses of the app so they do not disappear. 
    :answer_d: d. Data stored in a CloudDB are stored on the Internet.
    :feedback_d: Right.  Unlike TinyDB, which stores data on the mobile device, CloudDB data are stored on the Internet and downloaded into the app at run time. 
    :correct: a,b,d

    Which of the following statements are true for a CloudDB component. Choose all that apply. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-7-6-3-copy
    :random:
    :practice: T
    :answer_a: a. Because data stored in a CloudDB is stored on the phone's hard drive.
    :feedback_a: We’re in the learning zone today. Mistakes are our friends!
    :answer_b: b. Because data stored in a CloudDB can store bigger chunks of data.
    :feedback_b: We’re in the learning zone today. Mistakes are our friends!
    :answer_c: c. Because CloudDB data are stored on the Web and retrieved over the Internet whereas TinyDb data are stored on the device.
    :feedback_c: Good. Because CloudDB data are stored on the Web, attempts to retrieve it depend on the availability of the Internet and other factors and may take considerable time. So an event handler is used to tell the app when the requested data has arrived. 
    :answer_d: d. Because CloudDB data are stored in a complicated database whereas TinyDb data are stored in a simple database. 
    :feedback_d: We’re in the learning zone today. Mistakes are our friends!
    :correct: c

    .. raw:: html
    
    	<p>A <b><i>TinyDb</i></b> component does not have an event handler. Why do <b><i>CloudDB</i></b> need a GotValue event handler?</p>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-7-6-4-copy
    :random:
    :practice: T
    :answer_a: a. When the data needs to persist between uses of the app.
    :feedback_a: Both, CloudDB and TinyDb are able to persist data between different uses of the app.  So this is not the best answer.
    :answer_b: b. When the data needs to be shared among different devices running the app.
    :feedback_b: Right.  CloudDB store data on the Web and retrieve it over the Internet. So it can be shared among many devices.  TinyDb stores data on the device.  So it can't be shared among different devices. 
    :answer_c: c. When you need to retrieve the data quickly. 
    :feedback_c: It is true that data stored on a TinyDb is retrieved instantaneously, which will always be faster than data retrieved asynchronously from a CloudDB. But we are talking about a difference of a few milliseconds, assuming the app has a reasonable Internet connection.  So this is not a main reason to choose between TinyDb and a Web-based database.
    :answer_d: d. When you need to store lists of data.
    :feedback_d: Both CloudDB and TinyDB can store lists of data.  So this is not a distinguishing feature. 
    :correct: b

    .. raw:: html
    
    	<p>When should an app's data be stored in a <b><i>CloudDB</i></b> as opposed to a <b><i>TinyDb</i></b>?


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1l7qXqMXYcrrzvBdatwPggcHdURra_dGMHcFryB8jSIY/copy" target="_blank" title="">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vTUklOMKnldChJ-iVIcwAXQ1ipPo5OgPRRcNVjFnY_qZekzKXo23tQ0S-z-7s7zmvp9DnNHWgymVmkT/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--  &lt;p&gt;Create a new page named &lt;i&gt;&lt;b&gt;Clicker App with CloudDB&lt;/b&gt;&lt;/i&gt; in your portfolio and write brief answers to the following questions.&lt;/p&gt;
    
      &lt;ol&gt;
        &lt;li&gt;Describe and give an example of the difference between &lt;i&gt;synchronous&lt;/i&gt; and &lt;i&gt;asynchronous&lt;/i&gt; data operations.
        &lt;/li&gt;
        &lt;li&gt;True or False.  When an app retrieves data from CloudDB, it first requests the data and then it stops
          whatever it is doing and waits for the  data to arrive.  Explain. 
        &lt;/li&gt;
        &lt;li&gt;One aspect of abstraction is that it helps to reduce details to focus on what&#39;s relevant. 
          How does the use of an external database in this app help reduce detail in the program?  
        &lt;/li&gt;
    
      &lt;/ol&gt;-->
    </div>
    </div>