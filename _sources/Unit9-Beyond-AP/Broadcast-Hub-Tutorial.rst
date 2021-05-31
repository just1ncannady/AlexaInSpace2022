.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Socially Aware App: Broadcast Hub Tutorial 
====================================================

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
		
	<table>
	  <tbody>
	    <tr>
	      <td>

.. youtube:: 8hGirBMNo-4
        :width: 650
        :height: 415
        :align: center

.. raw:: html

	        (<a target="_blank" href="http://www.teachertube.com/video/359112">Teacher Tube version</a>)
	        <br>
	      </td>
	      <td>
	        
	        <b><i>BroadcastHub</i></b> The Broadcast Hub app uses email and texting to broadcast messages to a group of members who join the hub. This useful technology is used in many places that have unreliable internet access but do have mobile phones, for example in this <a href="https://www.youtube.com/watch?v=zGCxiD4qREM&amp;feature=youtu.be" target="_blank">PBS video on broadcast hubs in Africa</a>.  
	
	This tutorial uses the App Inventor Texting Component and the ActivityStarter Component for email to send messages to the list of registered members.  
	
	        </p><p><b style="font-color:red">Requirements:</b> This tutorial requires that an email address and email app are set up on the device to be able to send email messages. If you want to use texting, you need a device with an SMS service plan (e.g. an Android phone with service including texting). Google Voice no longer works with the App Inventor Text Component to receive text messages (although it does work to send them). However, you can do this tutorial with just using email over a WiFi connection and skip the sections that require texting.
	        </p>
	        
	    
	        <p>
	          <b>Objectives:</b> In this lesson you will learn to :
	        </p>
	        <ul>
	          <li>create an app that
	            <ul>
	              <li>uses the Texting component or email to create a hub for group messages,</li>
	              <li>follows a complex algorithm with loops, ifs, and lists for processing members and incoming texts,</li>
	
	             
	            </ul>
	          </li>
	          <li>gain additional experience using procedures to organize an app.
	          </li>
	        </ul>
	      </td>
	    </tr>
	  </tbody>
	</table>
	
	
Building the BroadcastHub app
------------------------------

.. raw:: html
		
	<p>The Broadcast Hub app allows people to join the hub by texting or entering their contact information. Messages are broadcast to all members of the hub:</p>
	<br><img src="../_static/assets/img/BroadcastHubConcept.png" width="300px">
	
	<p>To get started open <a href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit7/templates/BroadcastHub/BroadcastHubEmailTextTemplate.asc" target="blank">App Inventor with the new BroadcastHubEmailText Template</a>&nbsp;in a separate tab and follow along with the 
	  <a target="_blank" href="https://docs.google.com/document/d/1Kl03xcvO15R8I25wQmOXdJfvvHKVnNt1onvz3YbGKnc/edit">revised text tutorial</a> 
	  or the revised video below.
	  <br><gcb-youtube videoid="https://youtu.be/Uj6v4zk469Q" instanceid="O2WUPSbQimCJ"></gcb-youtube>
	</p>
	<!--
	<table>
	  <tbody>
	    <tr>
	      <td><a target="_blank" href="https://www.youtube.com/watch?v=LdoJUouVWjw">
	        
.. youtube:: nSZy0yK7F-M
        :width: 650
        :height: 415
        :align: center
	    
.. raw:: html

	        </a>
	      </td>
	      <td>
	        <a target="_blank" href="https://www.youtube-nocookie.com/embed/YGaqFGICRc0?rel=0">

.. youtube:: YGaqFGICRc0
        :width: 650
        :height: 415
        :align: center

.. raw:: html
	       
	        </a>
	      </td>
	    </tr>
	  </tbody>
	</table>
	-->

Enhancements: Creative Projects
------------------------------

.. raw:: html
	
	<p>Here are some ideas for programming projects.</p>
	<ul>
	  <li>  <b>Abstraction:</b> refactor your code to add more procedures with parameters, for example sendText(number, message), sendEmail(emailAddresses,message), addMember(member) which will add to the list and display the list, addMessage(message), etc.
	  </li>
	  <li>
	    <b>Persistence:</b> Add a TinyDb so that the members of the hub can persist from one use of the app to another. 
	  </li>
	  <li><b>Deleting Members:</b> Modify the app so that a member can be removed from the hub using the User Interface. If you are able to receive text messages, you can also have a protocol that deletes a user based on a received text message like “remove me”.
	  </li>
	  <li><b>Longer-term (Advanced) Project:</b>  Come up with your own variations of this app. For example, one variation might be to extend the app to have multiple types of hubs -- family, friends, etc.  And, allow members to tag their messages with certain prefixes to indicate which distribution list should receive the message -- e.g. “family: The picnic is at 1 PM’. Another variation might be to use the Social/Twitter component to tweet messages to your member list.  
	  </li>
	
	
	 
	
	</ul>
	
Still Curious?
------------------------------

.. raw:: html
	
	<p>Learn more about how mobile phones are used in Africa. How is their experience similar to yours? How is it different?<br><gcb-youtube videoid="https://youtu.be/zGCxiD4qREM" instanceid="LPW0RuROyNZy"></gcb-youtube><br></p>
	
Self-Check
------------------------------

.. raw:: html
		
	<question instanceid="plake0926166" weight="1" quid="6541603451699200">
	</question>
	<question instanceid="plake0926167" weight="1" quid="5959747320676352">
	</question>
	<question instanceid="plake0926168" weight="1" quid="6285036869386240" qu_type="mc" student_email="">
	</question>
	<question instanceid="plake0926169" weight="1" quid="5941684030406656">
	</question>
	
	
	
	
	<div id="portfolio" class="yui-wk-div">

Reflection: For Your Portfolio
------------------------------

.. raw:: html
	
	<p>Create a new page named <i><b>Broadcast Hub</b></i> under the <i>Reflections</i> category of your portfolio 
	  and write brief answers to the following questions:</p>
	  <ol>
	    <li>How is the For Each loop used in this app? What is the significance of this loop? 
	    </li>
	    <li>Besides Texting and the For Each loop, what programming concept plays a significant 
	      role in the functionality of this app? Explain.
	    </li>
	  </ol>
	</div>