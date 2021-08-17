.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Caesar Cipher App
=================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
        generateSummary(EKmapping['6.05']);
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
        "cipher" : "A cipher is a system for creating secret messages.",
        "cryptography":"Cryptography means, literally, 'secret writing'.  The art and science of writing secret messages.",
        "encryption": "Encryption is the process of using a secret key to convert plaintext into ciphertext.",
        "plaintext" : "Plaintext is the unencrypted, readable message.",
        "ciphertext" : "Ciphertext is an unreadable, secret message.",
        "decryption" : "Decryption is the process of using a secret key to convert ciphertext into plaintext.",
        "encryption key" : "The encryption key is a piece of secret data used in by encryption and decryption algorithms.",
        "encryption algorithm" : "The encryption algorithm uses a secret key to encrypt messages.",
        "substitution cipher" : "In a substitution cipher letters from a ciphertext alphabet are substituted for the letters in a plaintext message in a systematic way.",
        "function" : "A procedure that computes and returns a value.",
        "local variables" : "Variables that are declared and exist only inside a procedure or function (this is called their scope)."
       };    */
    </script>
    <h3 id="est-length">Time Estimate: 90 minutes</h3>
    

Introduction and Goals
-----------------------

.. raw:: html

    <p></p>
    <table><tbody>
	<tr>
	<td colspan=2>This lesson describes some basic terminology from the field of <span class="hover vocab yui-wk-div" data-id='cryptography'>cryptography</span>, and then introduces the Caesar Cipher, one of the earliest and simplest examples of a <span class="hover vocab yui-wk-div" data-id='substitution cipher'>substitution cipher</span>.</p>
    <p>Once we understand how the Caesar algorithm works, we will implement it in a simple app that encrypts and decrypts messages.</p>	
	</td>
	</tr>
	
	
	<tr><td valign="top">
    <!-- 
      &lt;img src=&quot;assets/img/Preview.png&quot; alt=&quot;Preview of Caesar <span class="hover vocab yui-wk-div" data-id='cipher'>Cipher</span>&quot; width=&quot;240px&quot;&gt;
    -->
    <iframe allowfullscreen="" frameborder="0" height="350" src="https://www.youtube.com/embed/U_Lg56Dvg2s" width="250"></iframe>
    </td>
    <td valign="top">
		<div><b>Learning Objectives:</b>&nbspI will learn to</div>
		<ul>
		<li>describe the fundamentals of <span class="hover vocab yui-wk-div" data-id='cryptography'>cryptography</span>
		<li>follow an instructor-led walkthrough to create an app that implements Caesar Cipher <span class="hover vocab yui-wk-div" data-id='encryption'>encryption</span> and <span class="hover vocab yui-wk-div" data-id='decryption'>decryption</span></li>
		<li>learn how to use <span class="hover vocab yui-wk-div" data-id='local variables'>local variables</span></li>
		<li>learn how to use a <span class="hover vocab yui-wk-div" data-id='function'>function</span></li>
		<li>use parameters with both procedures and functions <span class="hover vocab yui-wk-div" data-id='function'>functions</span></li>
		</ul>
		<div><b>Language Objectives:</b>&nbspI will be able to</div>
		<ul>
		<li>explain the difference between <span class="hover vocab yui-wk-div" data-id='local variables'>local</span> and global variables</li>
		<li>use target vocabulary, such as <span class="hover vocab yui-wk-div" data-id="encryption key">encryption key</span>, <span class="hover vocab yui-wk-div" data-id="encryption algorithm">encryption algorithm</span>, and <span class="hover vocab yui-wk-div" data-id="substitution cipher">substitution cipher</span> while describing app features and User Interface with the support of concept definitions and <a href="https://docs.google.com/presentation/d/1n-K4AQ_maHcXekzcfERQ9dxj91nqv9ytwJx4ZkAp8zw/copy" target="_blank" title="">vocabulary notes</a> from this lesson</li>
		</ul>
    </td>
    </tr>
    </tbody></table>
    

Learning Activities
--------------------

.. raw:: html

    <p><h3>Part I: Introduction to Cryptography and the Caesar Cipher</h3>
    <p><span class="hover vocab yui-wk-div" data-id='cryptography'>Cryptography</span> means secret writing. It is the art and science of sending secret  messages and it has been used by generals and governments and everyday people practically  since the invention of written language.  As we will see in upcoming lessons, modern cryptographic techniques are essential to guaranteeing the security of our transactions on the Internet. </p>
    <p><span class="hover vocab yui-wk-div" data-id='cryptography'>Cryptography</span> plays a role whenever you make an online purchase at Amazon or provide  your password to Google.  Whenever you see the <i><b>https protocol</b></i> in your browser, you can rest assured that your communications are secure because they are being encrypted with strong, unbreakable <span class="hover vocab yui-wk-div" data-id='encryption'>encryption</span>.   If we couldn't rely on those transactions being secure we really wouldn't have the Internet as we know it today.</p>
    <p>In upcoming lessons we will look at several different versions of <span class="hover vocab yui-wk-div" data-id='cryptography'>cryptography</span>, including the strong <span class="hover vocab yui-wk-div" data-id='encryption'>encryption</span> that protects our Internet transactions.  But let’s begin here with a simple <span class="hover vocab yui-wk-div" data-id='cipher'>cipher</span>, the <b><i>Caesar Cipher</i></b>, so named because it was used by Julius Caesar in 1st century B.C. The following video will explain the basics of the Caesar Cipher.  Click below to watch this presentation on Caesar Cipher.<br/>(<a href="https://docs.google.com/presentation/d/1GOzrwChWLjWbYi_yqKpLi2T60dwM8Yv2CaX2qGPzuV8/" target="_blank" title="">Slides - use 1-12</a>)</p>
    
.. youtube:: mXx4G_x6OuY
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <br/>
    <h3>Activity: Caesar Cipher</h3>
    (<a href="https://www.mobile-csp.org/webapps/crypto/caesar.html" target="_blank">Open widget in separate window</a>)
    
    <iframe height="300" src="https://www.mobile-csp.org/webapps/crypto/caesar.html" style="border: 0;" title="Caesar <span class="hover vocab yui-wk-div" data-id='Cipher'>Cipher</span>" width="650"></iframe>
    <ol>
    <li>Use the Caesar cipher to encrypt your name by hand using the cipher_alphabet below that is shift 3. Then use the widget above to check your answer.
      <pre>PLAIN_ALPHABET:   abcdefghijklmnopqrstuvwxyz
    CIPHER_ALPHABET:  DEFGHIJKLMNOPQRSTUVWXYZABC</pre>
    </li>
    <li style="margin-bottom: 5px;">Encrypt a short message for your partner by hand using the cipher alphabet with shift 3 above. Trade the encrypted messages and decrypt them by hand. Use the widget to check your answer.   </li>
    <li style="margin-bottom: 5px;">Create the CIPHER_ALPHABET that would result from a Caesar shift of 5. Use the widget above on some letters with shift 5 to check your answer.</li>
    <li>Try the self-check exercises below.</li>
    </ol>
    
.. mchoice:: mcsp-6-5-1
    :random:
    :practice: T
    :answer_a: a person who makes up secret codes
    :feedback_a: This is challenging, but rewarding!
    :answer_b: an algorithm that is used to scramble text so that it can be passed in secret
    :feedback_b: That's right! A cipher, such as the Caesar cipher, is an algorithm that is used to encrypt or scramble text so that it is unreadable unless one knows how to descrypt it. A cipher converts plaintext into ciphertext and vice versa.
    :answer_c: a lock that can be used to lock a message in a lock box
    :feedback_c: This is challenging, but rewarding!
    :answer_d: any puzzle, such as a crossword or Sudoku puzzle
    :feedback_d: This is challenging, but rewarding!
    :correct: b

    A cipher is _________________________.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <br/>
    
.. fillintheblank:: mcsp-6-5-2
    :casei:

    .. raw:: html
    
    	<p>Encrypt the word <b>alphabet</b> using a Caesar cipher with a shift of 3. Type your answer into the Textbox.</p>

    - :doskdehw: That's right! With a Caesar shift of 3, the 'alphabet' is encrypted into 'doskdehw'.
      :x: You're not quite there, yet. Give it another try; with a little more work you can figure this out! 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <br/>
    
.. mchoice:: mcsp-6-5-3
    :random:
    :practice: T
    :answer_a: transposition cipher
    :feedback_a: Don’t worry, it’s hard! Let’s go back and try it again...
    :answer_b: bimodal cipher
    :feedback_b: Don’t worry, it’s hard! Let’s go back and try it again...
    :answer_c: substitution cipher
    :feedback_c: That's right! A cipher, such as the Caesar cipher, is an algorithm that is used to encrypt or scramble text so that it is unreadable unless one knows how to descrypt it. A cipher converts plaintext into ciphertext and vice versa.
    :answer_d: substantial cipher
    :feedback_d: Don’t worry, it’s hard! Let’s go back and try it again...
    :correct: c

    A Caesar cipher is an example of a ______________________.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <br/>
    
.. fillintheblank:: mcsp-6-5-4
    :casei:

    .. raw:: html
    
    	<p>The following word was encrypted using a Caesar cipher with a shift of 2: <b>ecguct</b>. What word is it? Type your answer into the text box.</p>

    - :caesar: That's right! With a shift of 2, the letter 'c' becomes 'e'. The letter 'a' becomes 'c', and so on giving caesar as the secret word.
      :x: 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>
	<br/>
    <h3>Part II: Caesar Cipher App</h3>
    <p>To get started click on this link to <a href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit5/templates/CaesarApp/CaesarCipherTemplate.asc" target="_blank">open App Inventor and import the CaesarCipherTemplate</a>.   Use the <i>Save As</i> button to rename your project "CaesarCipherApp".</p>
    <p>You are provided with a template that sets up the environment for implementing Caesar <span class="hover vocab yui-wk-div" data-id='encryption'>encryption</span> and <span class="hover vocab yui-wk-div" data-id='decryption'>decryption</span>.  Your task will be to implement the <span class="hover vocab yui-wk-div" data-id='encryption'>encryption</span> <span class="hover vocab yui-wk-div" data-id='function'>function</span> following the tutorial and implement the  <span class="hover vocab yui-wk-div" data-id='decryption'>decryption</span> <span class="hover vocab yui-wk-div" data-id='function'>function</span> as an enhancement.</p>
    Programming constructs you will learn in building this app are
    <ul>
    <li>Defining and using <span class="hover vocab yui-wk-div" data-id='local variables'>local variables</span></li>
    <li>Defining and using procedures with returns (also called <span class="hover vocab yui-wk-div" data-id='function'>functions</span>)</li>
    <li>Using a for-range loop and an index to process a string of letters in a message</li>
    <li>Using built-in text <span class="hover vocab yui-wk-div" data-id='function'>functions</span> to process a string of letters in a message</li>
    </ul>
    
.. youtube:: ZKcv1IfrS7A
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <br/>
    <h3>Functions and Local Variables</h3>
    <p>This app makes use of <span class="hover vocab yui-wk-div" data-id='function'>functions</span> and <span class="hover vocab yui-wk-div" data-id='local variables'>local variables</span>. A <span class="hover vocab yui-wk-div" data-id='function'>function</span> is a procedure that returns a value.  A <span class="hover vocab yui-wk-div" data-id='local variables'>local variable</span>  (in contrast to a global variable) is one that has a limited <b>scope</b>, which means that it only exists and can only be used within a block of code, for example in a procedure or a <span class="hover vocab yui-wk-div" data-id='function'>function</span>. To help improve your understanding of these important programming concepts, there are several short (~ 1 minute) video tutorials <a href="http://mobile-csp.org/oneminutelessons/" target="_blank">available here</a>.</p>
    <p>In the AP exam, <span class="hover vocab yui-wk-div" data-id='function'>functions</span> are represented in the following pseudocode compared to procedures and to App Inventor blocks:</p>
    <table border="">
    <tbody>
    <tr><td width="10%"></td><td width="25%">AP Text Pseudocode</td><td width="30%">AP Block Pseudocode</td><td width="30%">App Inventor Block</td></tr>
    <tr><td>Procedure</td><td>
    <pre>PROCEDURE name(param1,...)
    {
     <em>instructions</em>
    }
    </pre>
    </td><td><div class="yui-wk-div" id="APblocks">
    <bl class="dark">PROCEDURE name <bl>param1,param2,...</bl><br/>
    <bl>instructions</bl>
    </bl></div></td>
    <td><img src="../_static/assets/img/procedurewparams.png" width="100%"/></td></tr>
    <tr><td>Function</td><td>
    <pre>PROCEDURE name(param1,...)
    {
     <em>instructions</em>
     RETURN (expression)
    }
    </pre>
    </td><td><div class="yui-wk-div" id="APblocks">
    <bl class="dark">PROCEDURE name <bl>param1,param2,...</bl><br/>
    <bl>instructions</bl><br/>
    <bl>RETURN <bl>expression</bl></bl>
    </bl></div></td>
    <td><img src="../_static/assets/img/procedurewresult.png" width="100%"/></td></tr>
    </tbody></table>
    <h3>Enhancements and Extensions</h3>
    <ol>
    <li style="margin-bottom: 5px;"><b>Decryption</b> Implement the <i>caesarDecrypt</i> <span class="hover vocab yui-wk-div" data-id='function'>function</span> and the handler for the decrypt button to enable the app to
        perform <span class="hover vocab yui-wk-div" data-id='decryption'>decryption</span>.  
		<ul>
		<li style="margin-bottom:5px;"><span class="hover vocab yui-wk-div" data-id='decryption'>Decryption</span> is the mirror image of <span class="hover vocab yui-wk-div" data-id='encryption'>encryption</span>.  Whereas for <span class="hover vocab yui-wk-div" data-id='encryption'>encryption</span> you replace every character in the <span class="hover vocab yui-wk-div" data-id='plaintext'>plaintext</span> with the corresponding letter from the CIPHER_ALPHABET, for <span class="hover vocab yui-wk-div" data-id='decryption'>decryption</span>, loop through the <span class="hover vocab yui-wk-div" data-id='ciphertext'>ciphertext</span> and replace every character with the corresponding letter from the PLAIN_ALPHABET.</li>
		<li style="margin-bottom:5px;">When you test the app, it will only work if you type lowercase letters into the <span class="hover vocab yui-wk-div" data-id='plaintext'>plaintext</span> textbox to encrypt, and type uppercase letters in the <span class="hover vocab yui-wk-div" data-id='ciphertext'>ciphertext</span> textbox to decrypt.</li>
		<li>To fix this, in the <i>ButtonDecrypt.Click</i>, you could use <img style="height:25px; width:70px" src="../_static/assets/img/upcaseBlock.jpg"/> before calling your decrypt <span class="hover vocab yui-wk-div" data-id='function'>function</span>.</li>
		</ul>
    <li style="margin-bottom: 5px;"><b>Extend the Alphabet </b> As it is currently implemented, the <span class="hover vocab yui-wk-div" data-id='plaintext'>plaintext</span> alphabet consists only of lowercase letters 'a' through 'z'.  This means that digits (0 through 9) and uppercase letters ('A' through 'Z') are not encrypted.  That's a security flaw that makes it easier for Eve, the eavesdropper, to break the <span class="hover vocab yui-wk-div" data-id='cipher'>cipher</span> and discover the secret message.  To fix this, extend the <span class="hover vocab yui-wk-div" data-id='plaintext'>plaintext</span> alphabet to include digits and UPPERCASE letters in any order. If you use the appropriate amount of abstraction, this should be a simple change to implement!</li>
    <li><b>Challenging (Optional) </b> Preserving the blank spaces between words makes it easier for Eve the eavesdropper to crack the encrypted message.  To make this more difficult, write a <span class="hover vocab yui-wk-div" data-id='function'>function</span> that will take a sentence and output the letters in four-letter blocks with all punctuation (i.e., all characters not in the <span class="hover vocab yui-wk-div" data-id='plaintext'>plaintext</span> alphabet) removed. For example, the <span class="hover vocab yui-wk-div" data-id='function'>function</span> would take  'this, is a test message!!' return '<b>this isat estm essa ge</b>'.</li>
    </ol>

Summary
--------

.. raw:: html

    <p>
    In this lesson, you learned how to:
      <div class="yui-wk-div" id="summarylist">
    </div>
    </p>
    
Still Curious?
---------------

.. raw:: html

    <p>
    <p>Read more about the historical context of Caesar's <span class="hover vocab yui-wk-div" data-id='Cipher'>Cipher</span> in <a href="http://www.bitsbook.com/wp-content/uploads/2008/12/chapter5.pdf" target="_blank">Chapter 5 of <i>Blown to Bits</i></a> (pg.165).</p>


Self-Check
-----------

.. raw:: html

    <p>
    
    Here is a table of some of the technical terms discussed in this
    lesson. Hover over the terms to review the definitions.
    
    <table align="center">
    <tbody>
    <tr>
    <td>
    <span class="hover vocab yui-wk-div" data-id="cipher">cipher</span>
    <br/><span class="hover vocab yui-wk-div" data-id="cryptography">cryptography</span>
    <br/><span class="hover vocab yui-wk-div" data-id="encryption">encryption</span>
    <br/><span class="hover vocab yui-wk-div" data-id="plaintext">plaintext</span>
    <br/><span class="hover vocab yui-wk-div" data-id="ciphertext">ciphertext</span>
    <br/><span class="hover vocab yui-wk-div" data-id="function">function</span>
    </td>
    <td>
    <span class="hover vocab yui-wk-div" data-id="decryption">decryption</span>
    <br/><span class="hover vocab yui-wk-div" data-id="encryption key">encryption key</span>
    <br/><span class="hover vocab yui-wk-div" data-id="encryption algorithm">encryption algorithm</span>
    <br/><span class="hover vocab yui-wk-div" data-id="substitution cipher">substitution cipher</span>
    <br/><span class="hover vocab yui-wk-div" data-id="local variables">local variables</span>
    </td>
    </tr>
    </tbody>
    </table>
    <p>Here are some Quizly exercises to practice coding functions. 
    
    
    
    
.. quizly:: mscp-6-5-5
    
    
    :quizname: quiz_hello_function
    
    
    
.. quizly:: mscp-6-5-6
    
    
    :quizname: quiz_double_function
    
    
    
.. quizly:: mscp-6-5-7
    
    
    :quizname: quiz_function_square
    
    </p>
    <br/>
    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1ItSlTR8YxgxmXgfs8JHSdPWu3Csrz98qjYUeE-xZKwI/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vScQGT-4IIld1UNjj-RvwEbkx5zUriWMBWHxbg7Seo6-KqCffcsfvPO0o04LSVxBx4C80qXj4rx_hXf/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--&lt;p&gt;Create a page named &lt;i&gt;&lt;b&gt;Caesar Cipher App&lt;/b&gt;&lt;/i&gt; in your portfolio and answer the following questions:&lt;/p&gt;
      &lt;ol&gt;
        &lt;li&gt;Post a screenshot of your code for the &lt;i&gt;caesarDecrypt&lt;/i&gt; function. 
        &lt;/li&gt;
        &lt;li&gt;Explain the difference between a function and a procedure. Give an example of a function.&lt;/li&gt;
        &lt;li&gt;
    Explain the difference between global and local variables. Why are local variables easier to debug than global variables?&lt;/li&gt;
      &lt;/ol&gt;-->
    </div>
    </div>