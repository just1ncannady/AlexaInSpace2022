.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Cryptography Securing the Internet
==================================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
        generateSummary(EKmapping['6.07']);
        generateHovers();
        Tipped.create('.vocab', function(element) {
        var vocab = $(element).data('id');
        return vocabulary[vocab];
          }, {
            cache: false,
              position: 'topleft'
              });
      });
      
     /* var vocabulary = {
        "symmetric cipher" : "A symmetric cipher is one in which a single key is used for both encryption and decryption.",
        "asymmetric cipher" : "An asymmetric cipher is one in which separate but related keys are used for encryption and decryption.",
        "key exchange problem" : "The key exchange problem is the problem of sharing a secret cryptographic key between Alice and Bob without Eve being able to intercept it.",
        "public key cryptography" : "A cryptographic system that uses two keys -- a public key known to everyone and a private or secret key known only to the recipient of the message. When Bob wants to send a secure message to Alice, he uses Alice's public key to encrypt the message. Alice then uses her private key to decrypt it.",
        "diffie-hellman": "Diffie Hellman is an algorithm used to establish a shared secret between two parties. It is primarily used to exchange a symmetric cryptographic key among two parties, Alice and Bob, who wish to communicate securely.",
        "rsa" : "Rivest-Shamir-Adleman (RSA) is a cryptosystem for public-key encryption, and is widely used for securing sensitive data, particularly when being sent over an insecure network such as the Internet.", 
        "intractable":"A computational problem is intractable if the only known way to solve the problem depends on an exponential algorithm.",
        "https": "HTTPS is a  protocol for secure (trusted, encrypted) communication over the Internet.",
        "ssl": "SSL (Secure Socket Layer) is a protocol for establishing an encrypted link between a web server and a browser.",
        "certificate authority" : "In cryptography, a certificate authority (CA) is an entity that issues digital certificates.",
        "digital certificate":  "A digital certificate is a data packet that certifies the holder of a public key.",
        "trust model" : "The use of a trusted third party to verify the trustworthiness of a digital certificate.",
      };      */
    
    </script>
    <!-- can use: #self-check, #still-curious, .pogil, #portfolio -->
    <h3 id="est-length"><b>Time Estimate: 45 minutes</b></h3>
    

Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <p>This lesson focuses on the modern cryptographic systems that are used to 
      secure the Internet.  For all of the ciphers discussed in the
      <a href="https://course.mobilecsp.org/mobilecsp/unit?unit=25&amp;lesson=122" target="_blank" title="">Cryptography Basics</a>
      lesson,  the same key was used both for encrypting and decrypting messages.  Systems 
      that use the same key for both encryption and decryption are called <span class="hover vocab yui-wk-div" data-id="<span class="hover vocab yui-wk-div" data-id='symmetric cipher'>symmetric cipher</span>">symmetric ciphers</span>.
    </p>
    <p>
      Symmetric ciphers have a serious flaw, known as the 
      <span class="hover vocab yui-wk-div" data-id="<span class="hover vocab yui-wk-div" data-id='key exchange problem'>key exchange problem</span>"><span class="hover vocab yui-wk-div" data-id='key exchange problem'>key exchange problem</span></span>:  How can 
      Alice and Bob securely exchange the shared key needed to encrypt and decrypt their messages. Hopefully,
      you can see that sending the shared key across the Internet in an email message would not be a very secure
      system -- Eve could easily intercept the key, without Alice and Bob knowing, and would then be able to 
      read all their messages. 
    </p>
    <p>What's needed in order for cryptography to work on the Internet is an <span class="hover vocab yui-wk-div" data-id="<span class="hover vocab yui-wk-div" data-id='asymmetric cipher'>asymmetric cipher</span>">asymmetric system</span>, in which 
      the key can be broken into parts so that one key can be used for encrypting and another for decrypting without
      ever having to share a key. Such systems are examples of <span class="hover vocab yui-wk-div" data-id="<span class="hover vocab yui-wk-div" data-id='public key cryptography'>public key cryptography</span>"><span class="hover vocab yui-wk-div" data-id='public key cryptography'>public key cryptography</span></span> and we will look
      at two important algorithms,  the <span class="hover vocab yui-wk-div" data-id="<span class="hover vocab yui-wk-div" data-id='diffie-hellman'>diffie-hellman</span>"><span class="hover vocab yui-wk-div" data-id='Diffie-Hellman'>Diffie-Hellman</span></span> key exchange algorithm and the <span class="hover vocab yui-wk-div" data-id="<span class="hover vocab yui-wk-div" data-id='rsa'>rsa</span>">Rivest-Shamir-Adelman (<span class="hover vocab yui-wk-div" data-id='RSA'>RSA</span>)</span>
      <span class="hover vocab yui-wk-div" data-id='public key cryptography'>public key cryptography</span> algorithm.
    </p>
    <p>
      The discovery of a solution to the <span class="hover vocab yui-wk-div" data-id='key exchange problem'>key exchange problem</span> was one of the biggest 
      breakthroughs in modern cryptography -- and without this discovery it would simply be impossible to have an Internet
      today that we could use for banking, buying goods on Amazon, and so on. 
    </p>
    <p><span class="hover vocab yui-wk-div" data-id='Public key cryptography'>Public key cryptography</span> is a very technical topic, the mathematical details of which go beyond the scope of this course.
      However, it's important that you understand the basic ideas around how it works and are able to see that current
      cryptographic systems can be trusted to secure our private transactions on the Internet.
    </p>
    

Learning Activities
--------------------

.. raw:: html

    <p><h3>Doubly Locked Box Analogy</h3>
    <p>This video shows one helpful model for public key encryption, a <b><i>doubly-locked box</i></b>, in which Alice
      and Bob each have their own keys, both of which are used to securely transmit information.
      
.. youtube:: jJrICB_HvuI
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </p>
    <h3>Part 1: Diffie-Hellman Key Exchange Algorithm</h3>
    <p>This video (slides <a href="<span class="hover vocab yui-wk-div" data-id='https'>https</span>://docs.google.com/presentation/d/1O4fSXY7KwHj-e6LcU6_q4sx7yuY_Epad2rXuCBxGwnk/edit?ts=5f6b40b2#slide=id.p5" target="_blank" title="">here</a>) 
      includes video clips from Brit Cruise's great explanation
      of the <i><span class="hover vocab yui-wk-div" data-id='Diffie-Hellman'>Diffie-Hellman</span> key exchange algorithm</i>.  After watching
      the video, try using the widget below to play with the color-mixing
      analogy. 
    </p>
    <br/>
.. youtube:: oUvelH9ADjs
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <br/>
    <h3>Activity: Diffie-Hellman Exchange Secret Color Demo</h3>
    <p>This Web app provides an implementation of the <i>color-mixing analogy</i>
      presented in the Brit Cruise video.  You can select a shared public color and then your
      own private (secret) color.  When you click "Show Shared Secret!" the app will 
      display the secret color that it shares with you. 
    </p>
    <p>Give it a try.  Colors are represented by hexadecimal numbers as explained in the sidebar.
      (<a href="<span class="hover vocab yui-wk-div" data-id='https'>https</span>://mobile-csp.org/webapps/crypto/diffiehellmancolor.html" target="_blank">Open widget in a separate window</a>)
    </p>
    <table>
    <tbody><tr>
    <td>
    <iframe height="450" instanceid="k8nug819cUct" src="<span class="hover vocab yui-wk-div" data-id='https'>https</span>://mobile-csp.org/webapps/crypto/diffiehellmancolor.html" title="" width="550">
    </iframe>
    </td>
    <td>In the RGB system colors are represented by 6-digit hexadecimal numbers, 
          where the first two digits represent the amount of red, the next two represent 
          amount of green, and the last two represent amount blue.  Pure 
          <font color="red">red</font> is <font color="red">FF0000</font>, where FF is 
          the maximum amount of  red (equal to 255 in decimal).  Pure <font color="green">green</font>
          would be <font color="#00FF00">00FF00</font>.  
          If you mix lots of blue and green, <font color="#00FFFF">00FFFF</font>, you should 
          get <font color="#00FFFF">aqua</font>.  If you mix lots of red with some green, 
          <font color="#ff8500">FF8500</font>, you should get
          <font color="ff8500">orange</font>.
        </td>
    </tr>
    </tbody></table>
    <br/>
    <h3>Part 2: RSA Public Key Encryption</h3>
    <p>
      The Rivest-Shamir-Adleman (<span class="hover vocab yui-wk-div" data-id='RSA'>RSA</span>) algorithm is the most widely used public key encryption algorithm for
      securing the Internet. Like <span class="hover vocab yui-wk-div" data-id='Diffie-Hellman'>Diffie-Hellman</span>, it is an <span class="hover vocab yui-wk-div" data-id='asymmetric cipher'>asymmetric cipher</span>, in which the key is broken into
      two related parts using mathematical techniques.  And also, like <span class="hover vocab yui-wk-div" data-id='Diffie-Hellman'>Diffie-Hellman</span>, it depends on the use of a
      one-way function -- i.e., a mathematical function that is easy to compute in one direction, but <i><span class="hover vocab yui-wk-div" data-id='intractable'>intractable</span></i>
      to compute in the other.
    </p>
    <p>The following video (slides <a href="<span class="hover vocab yui-wk-div" data-id='https'>https</span>://docs.google.com/presentation/d/1O4fSXY7KwHj-e6LcU6_q4sx7yuY_Epad2rXuCBxGwnk/edit?ts=5f6b40b2#slide=id.g393395465_0254" target="_blank" title="">here</a>) 
      provides a high-level description of <span class="hover vocab yui-wk-div" data-id='RSA'>RSA</span> without out going too deeply into 
      the mathematical details.
    </p>
    
.. youtube:: Z6OCgIRt54g
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <br/>
    <h3>Part 3:  Securing the Internet</h3>
    <p>
      Now that we have some understanding of the algorithms used to encrypt data, we can take a look at how
      these algorithms work together in the system that secures the Internet.  
      The following video (slides <a href="<span class="hover vocab yui-wk-div" data-id='https'>https</span>://docs.google.com/presentation/d/1O4fSXY7KwHj-e6LcU6_q4sx7yuY_Epad2rXuCBxGwnk/edit?ts=5f6b40b2#slide=id.g393395465_0551" target="_blank" title="">here</a>) 
      describes the type of communication that takes place behind the scenes when the browser on your phone or 
      tablet or laptop computer makes a secure connection to Amazon or Google or some other Internet service. 
      
      
.. youtube:: 1BA9L3_7YJ8
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </p>
    

Still Curious?
---------------

.. raw:: html

    <p>
    <ul>
    <li><a href="<span class="hover vocab yui-wk-div" data-id='https'>https</span>://britcruise.com/2012/02/14/2000-years-of-cryptography-in-8-5min/" target="_blank">Brit Cruise</a> has made an entire series of videos explaining encryption. If you're curious about some of the mathematics involved, see his full videos on <a href="<span class="hover vocab yui-wk-div" data-id='https'>https</span>://www.youtube.com/watch?v=YEBfamv-_do" target="_blank"><span class="hover vocab yui-wk-div" data-id='Diffie-Hellman'>Diffie-Hellman</span></a> and <a href="<span class="hover vocab yui-wk-div" data-id='https'>https</span>://www.youtube.com/watch?v=wXB-V_Keiu8" target="_blank"><span class="hover vocab yui-wk-div" data-id='RSA'>RSA</span></a>.</li>
    <li>You can also read more about how encryption developed in <a href="http://www.bitsbook.com/wp-content/uploads/2008/12/chapter5.pdf" target="_blank">Chapter 5 of <i>Blown to Bits</i></a> (pg. 178+)</li>
    <li>The Khan Academy has incorporated the Cruise videos into an excellent interactive <a href="<span class="hover vocab yui-wk-div" data-id='https'>https</span>://www.khanacademy.org/computing/computer-science/cryptography" target="_blank">course on Cryptography</a>, from the Caesar cipher to public key encryption.</li>
    <li>The history of <a href="<span class="hover vocab yui-wk-div" data-id='https'>https</span>://en.wikipedia.org/wiki/History_of_cryptography" target="_blank">cryptography</a> is very interesting story of the battle between <i>cryptographers</i>, those who create ciphers, and <i>cryptanalysts</i>, those who try to break ciphers. Until the 1990s cryptographic algorithms were the considered armaments by the U.S. government and it was widely believed that the National Security Agency (NSA) could break all existing ciphers.  That's no longer believed to be true. Today, strong cryptography is available to us on our smart phones.  But we still see the battle playing out between the government and private individuals and corporations over whether the government should have access to the keys that protect the data on our phones.  If you're curious about this, see this article on the <a href="<span class="hover vocab yui-wk-div" data-id='https'>https</span>://en.wikipedia.org/wiki/FBI%E2%80%93Apple_encryption_dispute" target="_blank">dispute between Apple and the FBI</a>.</li>
    <li>The PBS News Hour video has a guest from the <b><a href="<span class="hover vocab yui-wk-div" data-id='https'>https</span>://www.eff.org/" target="_blank">Electronic Frontier Foundation</a></b>, an organization that defends civil liberties related to the digital world. What other issues from the course do they have positions on or have been involved with?</li>
    </ul>
    

Summary
--------

.. raw:: html

    <p>
    In this lesson, you learned how to:
      <div class="yui-wk-div" id="summarylist">
    </div>
    

Self-Check
-----------

.. raw:: html

    <p>
    Here is a table of some of the technical terms discussed in this lesson. Hover over the terms to review the definitions.
      <table align="center">
    <tbody>
    <tr>
    <td><span class="hover vocab yui-wk-div" data-id="symmetric cipher">symmetric cipher</span>
    <br/><span class="hover vocab yui-wk-div" data-id="asymmetric cipher">asymmetric cipher</span>
    <br/><span class="hover vocab yui-wk-div" data-id="key exchange problem">key exchange problem</span>
    <br/><span class="hover vocab yui-wk-div" data-id="public key cryptography">public key cryptography</span>
    </td>
    <td>
    <span class="hover vocab yui-wk-div" data-id="diffie-hellman">diffie-hellman</span>
    <br/><span class="hover vocab yui-wk-div" data-id="rsa">rsa</span>
    <br/><span class="hover vocab yui-wk-div" data-id="https">HTTPS</span>
    <br/><span class="hover vocab yui-wk-div" data-id="ssl">SSL</span>
    </td>
    <td>
    <span class="hover vocab yui-wk-div" data-id="certificate authority">certificate authority</span>
    <br/><span class="hover vocab yui-wk-div" data-id="digital certificate">digital certificate</span>
    <br/><span class="hover vocab yui-wk-div" data-id="trust model">trust model</span>
    <br/><span class="hover vocab yui-wk-div" data-id="intractable">intractable</span>
    </td>
    </tr>
    </tbody>
    </table>
    
.. mchoice:: mcsp-6-7-1
    :random:
    :practice: T
    :answer_a: is exemplified by RSA and Diffie-Hellman.
    :feedback_a: Right.
    :answer_b: was first discovered by Euclid 5 B.C.
    :feedback_b: Let me add new information to help you solve this; the idea of an asymmetric cipher was first conceived by British cryptographer, James Ellis, in 1970.  But his work was classified. Diffie-Hellman independently came up with the idea in 1976.
    :answer_c: Uses different keys for encryption and decryption.
    :feedback_c: Right. In RSA Bob would use Alice's <i>public key</i> is used to encrypt messages to her and Alice would use her <i>private key</i> to decrypt the message.
    :answer_d: Can be used to solve the <i>key exchange problem</i>.
    :feedback_d: Yes. The Diffie-Hellman algorithm was the first algorithm to be used solve the key exchange problem.
    :correct: a,c,d

    An asymmetric cipher________________ 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-6-7-2
    :random:
    :practice: T
    :answer_a: is a mapping from a integers to alphabetic characters.
    :feedback_a: This will be a challenging concept to learn, but we can all reach this goal. It is a function that is easy to compute in one direction but hard to compute in the opposite direction.  An example would be  y = x<sup>3</sup> mod 17. Given <i>x</i> it is easy to compute y.  But given <i>y</i> it is difficult to compute <i>x</i>.  This is an example of the function used (in different form) in both Diffie-Hellman and RSA.
    :answer_b: is a mathematical function that converts characters into numbers.
    :feedback_b: This will be a challenging concept to learn, but we can all reach this goal. It is a function that is easy to compute in one direction but hard to compute in the opposite direction.  An example would be  y = x<sup>3</sup> mod 17. Given <i>x</i> it is easy to compute y.  But given <i>y</i> it is difficult to compute <i>x</i>.  This is an example of the function used (in different form) in both Diffie-Hellman and RSA.
    :answer_c: is a mathematical function that is easy to compute one time only.
    :feedback_c: This will be a challenging concept to learn, but we can all reach this goal. It is a function that is easy to compute in one direction but hard to compute in the opposite direction.  An example would be  y = x<sup>3</sup> mod 17. Given <i>x</i> it is easy to compute y.  But given <i>y</i> it is difficult to compute <i>x</i>.  This is an example of the function used (in different form) in both Diffie-Hellman and RSA.
    :answer_d: is a function that is easy to compute in one direction but hard to compute in the other.
    :feedback_d: Right.  An example would be  y = x<sup>3</sup> mod 17. Given <i>x</i> it is easy to compute y.  But given <i>y</i> it is difficult to compute <i>x</i>.  This is an example of the function used (in different form) in both Diffie-Hellman and RSA.
    :correct: d

    One one-way function ________________


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-6-7-3
    :random:
    :practice: T
    :answer_a: is an example of an <i>open standard</i>.
    :feedback_a: This is part of the correct answer.  HTTPs is one of many open standards used on the Internet.
    :answer_b: uses <i>public key encryption</i> to exchange a <i>symmetric key</i> between a user's browser and a server.
    :feedback_b: This is part of the correct answer. A public key algorithm, such as RSA, is used to exchange a symmetric key between the browser and the server.
    :answer_c: uses a <i>symmetric cipher</i> to encrypt data between a user's browser and a server.
    :feedback_c: This is part of the correct answer. During an HTTPs session the actual data transferred between the browser and the server is encrypted using a <i>symmetric cipher</i> such as the <i>Advanced Encryption Standard</i>.
    :answer_d: uses a <i>Certificate Authority</i> to authenticate the identity of the server during the transaction. 
    :feedback_d: This is part of the correct answer. Certificate Authorities, such as Verisign, serve as <i>trusted third parties</i> to authenticate the identity of the server and its public key.
    :correct: a,b,c,d

    The HTTPs protocol _______________.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    

Sample AP CSP Exam Question
----------------------------

.. raw:: html

    <p>
    
.. mchoice:: mcsp-6-7-4
    :random:
    :practice: T
    :answer_a: (A) I
    :feedback_a: 
    :answer_b: (B) II
    :feedback_b: 
    :answer_c: (C) I and II
    :feedback_c: 
    :answer_d: (D) Neither I nor II
    :feedback_d: 
    :correct: a

    Which of the following are true statements about digital certificates in Web browsers? I. Digital certificates are used to verify the ownership of encrypted keys used in secured communication.  II. Digital certificates are used to verify that the connection to a Web site is fault tolerant.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/16_kQtNXciCBJGTVkdcxoN9odrEknY_qTl8Y4DhUL2Os/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vQYfjhwPzOeVj4G7kF6HDBpimuds7C9d-8fyxWArHJ4fEp8A0I0M8xsd_y3V8ot6cFtyK2zpgvTNBSU/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    </div>
    </div>