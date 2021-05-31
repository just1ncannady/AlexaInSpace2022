.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Map Tour With TinyDB
====================

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
            generateSummary(EKmapping['3.09']);
            generateHovers();
    
    
    
        });
    </script>
    <h3 id="est-length">Time Estimate: 45 minutes</h3>
    

Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <table><tbody>
    <tr>
    <td>
    <!--
      &lt;img height=&quot;420&quot; src=&quot;assets/img/MapTourScreenshotPart2.png&quot;&gt;
    -->
    <iframe allowfullscreen="" frameborder="0" height="400" src="https://www.youtube.com/embed/PTWhgFo2e_Q?rel=0" width="300">
    </iframe>
    
    (<a href="https://teachertube.com/video/mobile-csp-map-tour-tinydb-revised-476367" target="_blank" title="">Teacher Tube version</a>)<br/>
    </td>
    <td>
    <p>  In this lesson we will extend the Map Tour App by adding two new features:
        </p><ol>
    <li><b>Adding Destinations to the Tour.</b>  
           We will allow users to click on the map to add new destinations to the map tour.
          </li>
    <li><b>Data Persistence.</b> We will incorporate  <i>TinyDB</i>, App Inventor's database component, which 
            will enable the app to save new destinations for the user.  New locations that are added to the destinations
            list will be saved to the database and re-loaded into the app when it starts up again. 
          </li>
    </ol>
    <p>
    <b>Objectives:</b> In this lesson you will:
    </p>
    <ul>
    <li>how to add items to lists;</li>
    <li>how to use a Notifier for input;</li>
    <li>basic concepts about databases and data persistence;</li>
    <li>
    how to use a TinyDB database component to permanently save app data on the device.
    
        </li>
    </ul>
    </td>
    </tr>
    </tbody></table>
    

Learning Activities
--------------------

.. raw:: html

    <p><h3>What is TinyDb?</h3></p>
    <p>Up until now, the data in our apps has been stored either in <b><i>global variables</i></b> or as the value of the <i><b>properties</b></i> of the app’s various components.  For example, when you store a piece of text in a Label, that data is stored in the computer’s main memory, in its RAM — random access memory.  And as we’ve learned, RAM is <b><i>volatile</i></b>,  meaning that any data stored there will be destroyed when the app is exited.
    </p>
    <p>By contrast, data stored in the computer’s long-term storage — e.g., on the phone’s flash drive — will <b><i>persist</i></b> as long as the app is kept on the device.  There are various ways to store data permanently on a computer.  For example, you could store it in a file, such as a document or image file.   Another way to store persistent data is in a <b><i>database</i></b>.  App Inventor provides us a very simple, easy-to-use database in its <b><i>TinyDb</i></b> component.  Any data that we store in the TinyDb, will not disappear when the app is exited.   Instead, it will persist between uses of the app -- even if you turn off the device.</p>
    <p>Before working on incorporating TinyDb into our app, the following video provides a brief overview of this very important component. (<a href="https://www.teachertube.com/videos/tiny-db-438788" target="_blank" title="">Teacher Tube version</a>)</p>
    
.. youtube:: qVJF-i5LqjQ
        :width: 650
        :height: 415
        :align: center


.. raw:: html

    <p><h3> Map Tour with TinyDB Tutorial</h3>
    <p>To get started, you can use the app you created in the previous lesson  and follow along with the video tutorial or the <a href="https://docs.google.com/document/d/1I01RYFHYLnNQZX9UN8Gc8dC2nAzAcXx9TLIkeEO8_Ug/edit?usp=sharing" target="_blank">Text Tutorial</a> or for an additional challenge, the <a href="https://docs.google.com/document/d/1LDIxFUhmRtmhc1Iyrow4PEsxu0qUuDeT5NDqBMZIvPM/edit?usp=sharing" target="_blank">Short Handout</a>.  </p>
    <iframe allow="autoplay; encrypted-media" allowfullscreen="" frameborder="0" height="500" src="https://www.youtube.com/embed/s6YZb3tfkq0?rel=0" width="100%"></iframe>
    (<a href="https://www.teachertube.com/videos/mobile-csp-map-tour-tinydb-revised-476367" target="_blank" title="">Teacher Tube version</a>)<br/>
    <h3>Enhancements </h3>
    Your instructor may ask you to do some or all  of the following enhancements for your Map Tour with TinyDB app.
    
    <ol>
    <li><b>Text To Speech:</b> Add a TextToSpeech component to the UI, and when the user picks an item from the list, call TextToSpeech.speak to say the selected item.</li>
    <li>
    <b>Delete Locations:</b> As you are testing your app, you may have added a lot of locations on your map tour that you do not want. You could delete the data stored for the installed app in your device under Settings/Applications Settings or by calling TinyDB.clearAll in your code, but in this enhancement you will add a Delete ListPicker button that lets you choose a location to remove from your lists and update the database. Here are the steps you need to do:
    <ul>
    <li>Add a ListPicker to the UI to Delete destinations.
    </li><li>In ListPicker.BeforePicking, set the ListPicker.Elements to the destinations list.
    </li><li>In ListPicker.AfterPicking, use the remove list item block from the Lists drawer to remove the item at the ListPicker.SelectedIndex from both of the lists (destinations and destinationsLatLong). Save both lists in TinyDB. Use Notifier.Alert to tell the user the destination was deleted.
    </li><li>Refactor your code to add a saveToDB procedure to save both lists in TinyDB and call it from ListPicker.AfterPicking and Notifier.AfterTextInput. 
    </li></ul></li>
    <li> <b>Add My Location:</b> If you have a device and location where GPS works. when you click on the My Location block, add that location to the destinationsLatLong lists using the Add Item to List block and use the Notifier.ShowTextDialog to get the location name for the destinations list (this will call the already written Notifier.AfterTextInput procedure).
    <br/></li>
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
    
.. mchoice:: mcsp-3-9-1
    :random:
    :practice: T
    :answer_a: a. Data stored in a TinyDb can easily be shared with other devices and users.
    :feedback_a: This is challenging, but rewarding!
    :answer_b: b. Data stored in a TinyDb will persist between different uses of the app.
    :feedback_b: That's right! Data stored in a TinyDb persist between uses of the app, but these data are stored on the device (not in the cloud) and cannot be shared with other devices or users. A TinyDb can store strings or numbers or lists.
    :answer_c: c. Data stored in a TinyDb disappears when you quit the app. 
    :feedback_c: This is challenging, but rewarding!
    :answer_d: d. Data stored in a TinyDb is stored in the cloud. 
    :feedback_d: This is challenging, but rewarding!
    :answer_e: e. Only strings (text) can be stored in a TinyDb. 
    :feedback_e: This is challenging, but rewarding!
    :correct: b

    Which of the following statements are true for a TinyDb component. Choose all that apply. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. fillintheblank:: mcsp-3-9-2
    :casei:

    What value would the global variable userName have after the blocks shown here are executed? Type your answer into the textbox. Spelling counts.

    .. raw:: html

        <img class="yui-img" src="../_static/assets/img/TinyDbSetUserName.png" width="350px"> |blank|

    - :Mary: Good. That's right! The StoreValue block stores the name "Mary" under the tag "name". So GetValue will retrieve "Mary" from the TinyDb and assign it to global variable userName. 
      :x: 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. fillintheblank:: mcsp-3-9-3
    :casei:

    What value would the global variable userName have after the blocks shown here are executed? Type your answer into the textbox. Spelling counts. 

    .. raw:: html

        <img class="yui-img" src="../_static/assets/img/TinyDbSetUsernameMary.png" width="350px"/> |blank|

    - :Mary: Good. That's right! The second StoreValue block stores the name "Bill" under the tag "Name", with an uppercase 'N'. Because tags are <b>case sensitive</b>, there are now two values stored in the database, "Mary" is associated with the tag "name" and "Bill" is associated with the tag "Name".   So GetValue will retrieve "Mary" from the TinyDb and assign it to global variable <i>userName</i>.
      :x: TinyDb tags are <i>case sensitive</i>, so the tags "name" and "Name" are two different tags associated with two different values. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-3-9-4
    :random:
    :practice: T
    :answer_a: a. Because that would be a bad score. 
    :feedback_a: OK, so you didn’t get it right this time. Let’s look at this as an opportunity to learn.
    :answer_b: b. Because that would be the value returned by TinyDb if nothing had yet been stored under the tag "highest". 
    :feedback_b: Good. If TinyDb does not find anything in the Db under the tag "highest" it will return the empty string. This is how you check that TinyDb does contain a value for a given tag. 
    :answer_c: c. Because TinyDb can only be used to store numbers, not strings. 
    :feedback_c: OK, so you didn’t get it right this time. Let’s look at this as an opportunity to learn.
    :answer_d: d. Because TinyDb returns an empty string whenever the network is not available. 
    :feedback_d: OK, so you didn’t get it right this time. Let’s look at this as an opportunity to learn.
    :correct: b

    In the block shown here why is it necessary to test whether the highestScore equals the empty string? 

    .. raw:: html

        <img class="yui-img" src="../_static/assets/img/getHighestScore.png"/>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


.. mchoice:: mcsp-3-9-5
    :random:
    :practice: T
    :answer_a: There are now two colleges, Trinity and Bowdoin, associated with the tag 'school'.
    :feedback_a: No. This is not the correct choice. Associating a value with a tag is not the same as adding new values to the tag. 
    :answer_b: This would cause an error because the tag 'school' has already been used.
    :feedback_b: No, this is a valid statement.
    :answer_c: The tag 'school' would now be associated with 'Bowdoin College' instead of 'Trinity College'.
    :feedback_c: Yes.  The value 'Bowdoin College' will now be associated with the tag 'school' in the TinyDb, replacing 'Trinity College' as the value of that tag. 
    :answer_d: The tag 'school' is still associated with 'Trinity College'. 
    :feedback_d: No, we are associating a new value with the tag 'school'. 
    :correct: c

    Consider the following depiction of the contents of a TinyDb for an app.TagsValuesschoolTrinity CollegetrinityTrinity CollegecollegeAmherst CollegeuniversityHarvardAnd suppose your app just executed the following block:Which of these statements best describes the current state of the database?

    .. raw:: html

        <img src="../_static/assets/img/StoreBowdoin.png" width="200"/>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-3-9-6
    :random:
    :practice: T
    :answer_a: True
    :feedback_a: Yes, a list can be empty. It's important in computer programming to be able to model a list with no elements. For many problems that is the list's initial state -- before items are added to it. A empty list has a length of 0.
    :answer_b: False
    :feedback_b: Mistakes are welcome here! Try reviewing this; in computer programming is it a list is often considered to be empty in it's initial state -- before items are added to it.
    :correct: a

    True or False: It is possible to have an empty list -- i.e., a list with no elements. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1sdliswlwSChrIo9xgIK-xP3qvL3d45BvHrwofEQoNic/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vSiaeUFtGF7GcQoI9DPm3AdsCLjLorYB9X2w3OvbgAIM1dNm6-MnLB4CHJUbvjkENRIKb-d62giEgMa/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--  &lt;p&gt;Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this &lt;a href=&quot;https://docs.google.com/document/d/1sdliswlwSChrIo9xgIK-xP3qvL3d45BvHrwofEQoNic/edit?usp=sharing&quot; target=&quot;_blank&quot;&gt;Google Doc&lt;/a&gt; where you may use File/Make a Copy to make your own editable copy.
    &lt;ol&gt;
    &lt;li&gt;What does it mean to say that data is &#39;persistent&#39;?&lt;/li&gt;
    &lt;li&gt;What&#39;s the difference in terms of &lt;i&gt;where&lt;/i&gt; data is located for data stored in a global variable vs. data stored in a database?&lt;/li&gt;
    &lt;li&gt;Include screenshots and explanations of your enhancements.&lt;/li&gt;
    
    &lt;/ol&gt;-->
    </div>
    </div>